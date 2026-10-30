#!/usr/bin/env python3
"""Offline, standard-library evidence graph and leased research work queue.

This program records supplied evidence. It does not discover or establish fraud.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import os
from pathlib import Path
import re
import secrets
import sqlite3
import sys
import tempfile
import time
from urllib.parse import urlparse

STATUSES = frozenset({"source", "documented_fact", "published_case", "allegation",
    "settlement", "conviction", "audit_finding", "hypothesis", "planned", "unknown",
    "verified", "disputed", "closed", "disproved"})
UNSOURCED = frozenset({"hypothesis", "planned", "unknown"})
LEGAL_STATUSES = frozenset({"allegation", "charged", "indicted", "complaint",
    "pending", "settlement", "settled", "conviction", "convicted", "guilty_plea",
    "sentenced", "acquitted", "dismissed", "audit_finding", "audit", "unknown",
    "civil_settlement", "administrative_action", "mixed", "judgment", "published_case"})
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]{0,159}$")
PRIVATE_FIELDS = frozenset({"ssn", "social_security_number", "date_of_birth", "dob",
    "home_address", "personal_email", "personal_phone", "bank_account",
    "medical_record", "patient_id", "passport_number", "private_address"})
GENERATOR = "<!-- generated-by: us-integrity-engine-v1 -->"


class IntegrityError(ValueError):
    pass


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IntegrityError(f"Cannot read JSON {path}: {exc}") from exc


def safe_id(value, context):
    if not isinstance(value, str) or not ID_RE.fullmatch(value) or ".." in value:
        raise IntegrityError(f"{context}: unsafe identifier {value!r}")


def _date(value, context):
    if not isinstance(value, str):
        raise IntegrityError(f"{context}: date must be an ISO string")
    try:
        # Both date and timezone-qualified datetime are accepted.
        if "T" in value:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("timezone required")
        else:
            date.fromisoformat(value)
    except ValueError as exc:
        raise IntegrityError(f"{context}: invalid ISO date {value!r}") from exc


def _privacy_properties(properties, context):
    for key, value in properties.items():
        if key.lower() in PRIVATE_FIELDS and value not in (None, "", [], {}):
            raise IntegrityError(f"{context}: sensitive field {key!r} cannot be exported")
        if isinstance(value, dict):
            _privacy_properties(value, context)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    _privacy_properties(item, context)


def validate_graph(graph, public=False):
    """Validate provenance and references; public=True additionally refuses restricted data."""
    if not isinstance(graph, dict) or graph.get("version") != "1.0":
        raise IntegrityError("graph version must be '1.0'")
    if public:
        _privacy_properties(graph, "graph")
        if graph.get("visibility", "public") != "public":
            raise IntegrityError("restricted graph cannot be publicly exported")
    _date(graph.get("as_of"), "as_of")
    nodes, edges = graph.get("nodes"), graph.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise IntegrityError("nodes and edges must be arrays")
    identities = set()
    for item in nodes + edges:
        if not isinstance(item, dict):
            raise IntegrityError("each graph record must be an object")
        ident = item.get("id")
        safe_id(ident, "record")
        if ident in identities:
            raise IntegrityError(f"duplicate record id {ident}")
        identities.add(ident)
        if not isinstance(item.get("type"), str) or not item["type"].strip():
            raise IntegrityError(f"{ident}: nonempty type required")
        if item.get("status") not in STATUSES:
            raise IntegrityError(f"{ident}: unknown status {item.get('status')!r}")
        if not isinstance(item.get("source_ids"), list) or any(
                not isinstance(ref, str) for ref in item["source_ids"]):
            raise IntegrityError(f"{ident}: source_ids must be an array of ids")
        if len(set(item["source_ids"])) != len(item["source_ids"]):
            raise IntegrityError(f"{ident}: duplicate source references")
        props = item.get("properties")
        if not isinstance(props, dict):
            raise IntegrityError(f"{ident}: properties must be an object")
        if "content_sha256" in props and not re.fullmatch(r"[0-9a-f]{64}", str(props["content_sha256"])):
            raise IntegrityError(f"{ident}: content_sha256 must hash the acquired source bytes")
        money = props.get("money")
        if money is not None:
            if not isinstance(money, dict) or not all(k in money for k in ("amount", "currency", "kind")):
                raise IntegrityError(f"{ident}: money requires amount, currency and kind")
            try:
                amount = Decimal(str(money["amount"]))
                if not amount.is_finite():
                    raise InvalidOperation()
            except (InvalidOperation, ValueError):
                raise IntegrityError(f"{ident}: invalid money amount")
            if not re.fullmatch(r"[A-Z]{3}", str(money["currency"])) or not str(money["kind"]).strip():
                raise IntegrityError(f"{ident}: money currency/kind required")
        if public:
            if item.get("visibility", "public") != "public" or props.get("visibility", "public") != "public":
                raise IntegrityError(f"{ident}: restricted visibility cannot be publicly exported")
            _privacy_properties(props, ident)
            if props.get("sensitive_person_data") or props.get("contains_private_information"):
                raise IntegrityError(f"{ident}: private information cannot be exported")
            if props.get("novel_lead") and not props.get("public_record"):
                raise IntegrityError(f"{ident}: novel nonpublic lead requires restricted storage")
            if item["type"] in ("lead", "person") and not props.get("public_record"):
                raise IntegrityError(f"{ident}: public_record=true is required for a public {item['type']}")
    by_id = {node["id"]: node for node in nodes}
    for node in nodes:
        ident, props = node["id"], node["properties"]
        if not isinstance(node.get("title"), str) or not node["title"].strip():
            raise IntegrityError(f"{ident}: nonempty title required")
        if node["type"] == "source":
            url = props.get("url")
            parsed = urlparse(url) if isinstance(url, str) else None
            if not parsed or parsed.scheme not in ("http", "https") or not parsed.netloc or parsed.username:
                raise IntegrityError(f"{ident}: source requires a public http(s) URL")
            _date(props.get("accessed_at"), f"{ident}.accessed_at")
        elif node["status"] not in UNSOURCED and not node["source_ids"]:
            raise IntegrityError(f"{ident}: documented record requires provenance")
        if node["type"] == "case":
            legal_status = props.get("legal_status")
            if legal_status not in LEGAL_STATUSES:
                raise IntegrityError(f"{ident}: explicit supported legal_status required")
            if public and not props.get("public_record"):
                raise IntegrityError(f"{ident}: case requires public_record=true for public export")
            if node["status"] == "conviction" and legal_status not in {"conviction", "convicted", "guilty_plea", "sentenced", "mixed"}:
                raise IntegrityError(f"{ident}: conviction label conflicts with legal_status")
    for edge in edges:
        ident = edge["id"]
        if edge.get("source") not in by_id or edge.get("target") not in by_id:
            raise IntegrityError(f"{ident}: dangling edge endpoint")
        if edge["status"] not in UNSOURCED and not edge["source_ids"]:
            raise IntegrityError(f"{ident}: documented edge requires provenance")
    for item in nodes + edges:
        for ref in item["source_ids"]:
            if ref not in by_id or by_id[ref]["type"] != "source":
                raise IntegrityError(f"{item['id']}: missing/non-source provenance {ref}")
    return {"nodes": len(nodes), "edges": len(edges),
            "sources": sum(n["type"] == "source" for n in nodes)}


def connect_db(path):
    reject_symlinks(Path(path))
    db = sqlite3.connect(path, timeout=20, isolation_level=None)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.execute("PRAGMA busy_timeout=20000")
    db.executescript("""
      CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS nodes(id TEXT PRIMARY KEY, type TEXT NOT NULL,
        title TEXT NOT NULL, status TEXT NOT NULL, source_ids TEXT NOT NULL, properties TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS edges(id TEXT PRIMARY KEY, type TEXT NOT NULL,
        source TEXT NOT NULL REFERENCES nodes(id), target TEXT NOT NULL REFERENCES nodes(id),
        status TEXT NOT NULL, source_ids TEXT NOT NULL, properties TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS tasks(id TEXT PRIMARY KEY, title TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('queued','claimed','completed','blocked')),
        owner TEXT, lease_until REAL, result TEXT, depends_on TEXT NOT NULL,
        definition TEXT NOT NULL, lease_token TEXT);
      CREATE TABLE IF NOT EXISTS task_events(sequence INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id TEXT NOT NULL, action TEXT NOT NULL, owner TEXT NOT NULL,
        at REAL NOT NULL, detail TEXT NOT NULL);
    """)
    columns = {row["name"] for row in db.execute("PRAGMA table_info(tasks)")}
    if "lease_token" not in columns:
        # Existing queues retain state; pre-fencing active leases must be reclaimed.
        db.execute("ALTER TABLE tasks ADD COLUMN lease_token TEXT")
    return db


def validate_tasks(tasks):
    if isinstance(tasks, dict):
        tasks = tasks.get("tasks")
    if not isinstance(tasks, list):
        raise IntegrityError("tasks must be an array or object containing tasks array")
    ids = set()
    for task in tasks:
        if not isinstance(task, dict):
            raise IntegrityError("task must be an object")
        safe_id(task.get("id"), "task")
        if task["id"] in ids:
            raise IntegrityError(f"duplicate task {task['id']}")
        ids.add(task["id"])
        if not isinstance(task.get("title"), str) or not task["title"].strip():
            raise IntegrityError("task title required")
        if task.get("status", "queued") not in {"queued", "blocked"}:
            raise IntegrityError("new task definitions must be queued or blocked")
        if not isinstance(task.get("depends_on", []), list):
            raise IntegrityError("task depends_on must be array")
        if task.get("visibility", "public") != "public":
            raise IntegrityError("restricted tasks must not be imported into public database")
    deps = {task["id"]: task.get("depends_on", []) for task in tasks}
    for task_id, references in deps.items():
        if any(ref not in ids or ref == task_id for ref in references):
            raise IntegrityError(f"{task_id}: missing/self task dependency")
    visited, active = set(), set()
    def visit(task_id):
        if task_id in active:
            raise IntegrityError("cyclic task dependencies")
        if task_id in visited:
            return
        active.add(task_id)
        for ref in deps[task_id]:
            visit(ref)
        active.remove(task_id)
        visited.add(task_id)
    for task_id in deps:
        visit(task_id)
    return tasks


def import_tasks(db, tasks, manage_transaction=True):
    tasks = validate_tasks(tasks)
    if manage_transaction:
        db.execute("BEGIN IMMEDIATE")
    try:
        for task in tasks:
            existing = db.execute("SELECT definition FROM tasks WHERE id=?", (task["id"],)).fetchone()
            definition = canonical(task)
            if existing:
                if existing["definition"] != definition:
                    raise IntegrityError(f"{task['id']}: task definition changed; use a new versioned task id")
            else:
                db.execute("INSERT INTO tasks(id,title,status,owner,lease_until,result,depends_on,definition,lease_token) VALUES(?,?,?,?,?,?,?,?,?)", (
                    task["id"], task["title"], task.get("status", "queued"), None, None,
                    None, canonical(task.get("depends_on", [])), definition, None))
        if manage_transaction:
            db.execute("COMMIT")
    except Exception:
        if manage_transaction and db.in_transaction:
            db.execute("ROLLBACK")
        raise


def reject_symlinks(path):
    """Never write a generated artifact or database through a symbolic link."""
    for current in (path, *path.parents):
        if current.is_symlink():
            raise IntegrityError(f"symlink output path refused: {current}")


def _atomic_text(path, content):
    reject_symlinks(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        name = stream.name
        stream.write(content)
    try:
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def csv_value(value):
    if value is None:
        return ""
    text = value if isinstance(value, str) else canonical(value)
    if text.startswith(("=", "+", "-", "@", "\t", "\r")):
        return "'" + text
    return text


def export_csv(path, fields, records, numeric_fields=()):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow({key: str(record[key]) if key in numeric_fields and key in record
                         else csv_value(record.get(key)) for key in fields})
    _atomic_text(path, stream.getvalue())


def build_graph(graph, output, tasks=None):
    stats = validate_graph(graph, public=True)
    if tasks is not None:
        tasks = validate_tasks(tasks)
    output = Path(output)
    reject_symlinks(output)
    for child in ("graph.sqlite", "exports", "obsidian", "manifest.json"):
        reject_symlinks(output / child)
    output.mkdir(parents=True, exist_ok=True)
    ordered = dict(graph)
    ordered["nodes"] = sorted(graph["nodes"], key=lambda n: n["id"])
    ordered["edges"] = sorted(graph["edges"], key=lambda e: e["id"])
    graph_digest = hashlib.sha256(canonical(ordered).encode()).hexdigest()
    db = connect_db(output / "graph.sqlite")
    try:
        db.execute("BEGIN IMMEDIATE")
        db.execute("DELETE FROM edges")
        db.execute("DELETE FROM nodes")
        for node in ordered["nodes"]:
            db.execute("INSERT INTO nodes VALUES(?,?,?,?,?,?)", (node["id"], node["type"], node["title"], node["status"], canonical(node["source_ids"]), canonical(node["properties"])))
        for edge in ordered["edges"]:
            db.execute("INSERT INTO edges VALUES(?,?,?,?,?,?,?)", (edge["id"], edge["type"], edge["source"], edge["target"], edge["status"], canonical(edge["source_ids"]), canonical(edge["properties"])))
        for key, value in {"as_of": graph["as_of"], "version": "1.0", "graph_sha256": graph_digest}.items():
            db.execute("INSERT OR REPLACE INTO metadata VALUES(?,?)", (key, value))
        try:
            db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS node_search USING fts5(id UNINDEXED,title,properties)")
            db.execute("DELETE FROM node_search")
            for node in ordered["nodes"]:
                db.execute("INSERT INTO node_search VALUES(?,?,?)", (node["id"], node["title"], canonical(node["properties"])))
            db.execute("INSERT OR REPLACE INTO metadata VALUES('search_backend','fts5')")
        except sqlite3.OperationalError as exc:
            if "no such module" not in str(exc).lower():
                raise
            db.execute("INSERT OR REPLACE INTO metadata VALUES('search_backend','like')")
        if tasks is not None:
            import_tasks(db, tasks, manage_transaction=False)
        db.execute("COMMIT")
    except Exception:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
    finally:
        db.close()
    exports = output / "exports"
    _atomic_text(exports / "graph.json", json.dumps(ordered, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    export_csv(exports / "nodes.csv", ["id", "type", "title", "status", "source_ids", "properties"], ordered["nodes"])
    export_csv(exports / "edges.csv", ["id", "type", "source", "target", "status", "source_ids", "properties"], ordered["edges"])
    money_records = []
    for item in ordered["nodes"] + ordered["edges"]:
        money = item["properties"].get("money")
        if money:
            money_records.append({"id": item["id"], **money})
    export_csv(exports / "money.csv", ["id", "amount", "currency", "kind", "qualifier", "period", "basis", "condition"], money_records, numeric_fields=("amount",))
    notes = output / "obsidian"
    outgoing, incoming = {}, {}
    for edge in ordered["edges"]:
        outgoing.setdefault(edge["source"], []).append(edge)
        incoming.setdefault(edge["target"], []).append(edge)
    current_paths = set()
    for node in ordered["nodes"]:
        ident = node["id"]
        path = notes / f"{ident}.md"
        current_paths.add(path.name)
        lines = ["---", f"id: {json.dumps(ident)}", f"type: {json.dumps(node['type'])}",
            f"title: {json.dumps(node['title'], ensure_ascii=False)}", f"status: {json.dumps(node['status'])}",
            "visibility: public", f"as_of: {json.dumps(graph['as_of'])}", "---", GENERATOR,
            "", f"# {node['title']}", "", f"Evidence status: **{node['status']}**.",
            "This note records supplied sources; it does not independently establish fraud.", "", "## Properties", "", "```json",
            json.dumps(node["properties"], ensure_ascii=False, sort_keys=True, indent=2), "```", "", "## Sources", ""]
        lines += [f"- [[{source_id}]]" for source_id in node["source_ids"]] or ["No supporting source attached; treat as an unverified planning record."]
        lines += ["", "## Outgoing relationships", ""]
        lines += [f"- {e['type']}: [[{e['target']}]] — {e['status']} ({e['id']}); sources: " + ", ".join(f"[[{s}]]" for s in e["source_ids"]) for e in outgoing.get(ident, [])] or ["None recorded."]
        lines += ["", "## Backlinks", ""]
        lines += [f"- [[{e['source']}]]: {e['type']} — {e['status']} ({e['id']})" for e in incoming.get(ident, [])] or ["None recorded."]
        _atomic_text(path, "\n".join(lines) + "\n")
    if notes.exists():
        for stale in notes.glob("*.md"):
            if stale.name not in current_paths and GENERATOR in stale.read_text(encoding="utf-8"):
                stale.unlink()
    manifest = {**stats, "version": "1.0", "as_of": graph["as_of"], "graph_sha256": graph_digest,
        "hash_scope": "canonical supplied JSON, not downloaded source content",
        "public_export": True, "obsidian_notes": len(ordered["nodes"]),
        "tasks_imported": len(tasks) if tasks is not None else 0}
    _atomic_text(output / "manifest.json", json.dumps(manifest, sort_keys=True, indent=2) + "\n")
    return manifest


def search_nodes(db, query, limit=20):
    if not isinstance(query, str) or not query.strip() or len(query) > 2000:
        raise IntegrityError("query must contain 1–2000 characters")
    limit = max(1, min(int(limit), 100))
    backend = db.execute("SELECT value FROM metadata WHERE key='search_backend'").fetchone()
    if backend and backend["value"] == "fts5":
        try:
            return [dict(row) for row in db.execute("SELECT n.id,n.type,n.title,n.status FROM node_search f JOIN nodes n ON n.id=f.id WHERE node_search MATCH ? ORDER BY rank,n.id LIMIT ?", (query, limit))]
        except sqlite3.OperationalError:
            # Literal fallback for malformed FTS syntax; SQL remains parameterized.
            pass
    escaped = query.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    term = f"%{escaped}%"
    return [dict(row) for row in db.execute("SELECT id,type,title,status FROM nodes WHERE title LIKE ? ESCAPE '\\' OR properties LIKE ? ESCAPE '\\' ORDER BY id LIMIT ?", (term, term, limit))]


def _identity(task_id, owner):
    safe_id(task_id, "task")
    if not isinstance(owner, str) or not 1 <= len(owner.strip()) <= 120 or any(ord(c) < 32 for c in owner):
        raise IntegrityError("owner must contain 1–120 printable characters")


def claim_task(db, task_id, owner, lease_seconds=1800, now=None):
    _identity(task_id, owner)
    if not isinstance(lease_seconds, int) or not 30 <= lease_seconds <= 86400:
        raise IntegrityError("lease_seconds must be between 30 and 86400")
    now = time.time() if now is None else now
    db.execute("BEGIN IMMEDIATE")
    try:
        task = db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if not task:
            raise IntegrityError("unknown task")
        if task["status"] in ("completed", "blocked"):
            raise IntegrityError(f"task is {task['status']}")
        if task["status"] == "claimed" and task["lease_until"] > now:
            if task["owner"] != owner:
                raise IntegrityError(f"task already leased by {task['owner']}")
            db.execute("COMMIT")
            if task["lease_token"] is None:
                raise IntegrityError("legacy lease has no fencing token; wait for expiry then reclaim")
            return {"id": task_id, "status": "claimed", "owner": owner, "lease_until": task["lease_until"], "lease_token": task["lease_token"], "idempotent": True}
        dependencies = json.loads(task["depends_on"])
        for dependency in dependencies:
            dep = db.execute("SELECT status FROM tasks WHERE id=?", (dependency,)).fetchone()
            if not dep or dep["status"] != "completed":
                raise IntegrityError(f"dependency incomplete: {dependency}")
        until = now + lease_seconds
        token = secrets.token_urlsafe(24)
        db.execute("UPDATE tasks SET status='claimed',owner=?,lease_until=?,lease_token=? WHERE id=?", (owner, until, token, task_id))
        db.execute("INSERT INTO task_events(task_id,action,owner,at,detail) VALUES(?,?,?,?,?)", (task_id, "claimed", owner, now, canonical({"lease_until": until})))
        db.execute("COMMIT")
        return {"id": task_id, "status": "claimed", "owner": owner, "lease_until": until, "lease_token": token, "idempotent": False}
    except Exception:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise


def complete_task(db, task_id, owner, result, lease_token, now=None):
    _identity(task_id, owner)
    if not isinstance(result, str) or not result.strip() or len(result) > 20000:
        raise IntegrityError("result must contain 1–20000 characters")
    if not isinstance(lease_token, str) or not lease_token:
        raise IntegrityError("lease_token from the successful claim is required")
    now = time.time() if now is None else now
    db.execute("BEGIN IMMEDIATE")
    try:
        task = db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if not task:
            raise IntegrityError("unknown task")
        if not task["lease_token"] or not secrets.compare_digest(task["lease_token"], lease_token):
            raise IntegrityError("stale or incorrect lease token")
        if task["status"] == "completed" and task["owner"] == owner and task["result"] == result:
            db.execute("COMMIT")
            return {"id": task_id, "status": "completed", "idempotent": True}
        if task["status"] != "claimed" or task["owner"] != owner:
            raise IntegrityError("only the current task owner can complete a claimed task")
        if task["lease_until"] <= now:
            raise IntegrityError("task lease expired; claim it again before completing")
        db.execute("UPDATE tasks SET status='completed',lease_until=NULL,result=? WHERE id=?", (result, task_id))
        db.execute("INSERT INTO task_events(task_id,action,owner,at,detail) VALUES(?,?,?,?,?)", (task_id, "completed", owner, now, canonical({"result": result})))
        db.execute("COMMIT")
        return {"id": task_id, "status": "completed", "idempotent": False}
    except Exception:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("data")
    validate.add_argument("--public", action="store_true")
    build = sub.add_parser("build")
    build.add_argument("data")
    build.add_argument("--output", required=True)
    build.add_argument("--tasks")
    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--db", required=True)
    search.add_argument("--limit", type=int, default=20)
    for command in ("claim-task", "complete-task"):
        task = sub.add_parser(command)
        task.add_argument("--db", required=True)
        task.add_argument("--task", required=True)
        task.add_argument("--owner", required=True)
        if command == "claim-task":
            task.add_argument("--lease-seconds", type=int, default=1800)
        else:
            task.add_argument("--result", required=True)
            task.add_argument("--lease-token", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_graph(load_json(args.data), public=args.public)
        elif args.command == "build":
            result = build_graph(load_json(args.data), args.output, load_json(args.tasks) if args.tasks else None)
        else:
            if not Path(args.db).is_file():
                raise IntegrityError("database does not exist; build it first")
            db = connect_db(args.db)
            try:
                if args.command == "search":
                    result = search_nodes(db, args.query, args.limit)
                elif args.command == "claim-task":
                    result = claim_task(db, args.task, args.owner, args.lease_seconds)
                else:
                    result = complete_task(db, args.task, args.owner, args.result, args.lease_token)
            finally:
                db.close()
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (IntegrityError, sqlite3.Error, OSError) as exc:
        print(f"integrity error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
