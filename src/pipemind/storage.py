"""Single-node append-only, tenant-scoped SQLite evidence store.

This is a pilot persistence layer, not a multi-node industrial historian.
Never store access tokens, secrets or unclassified personal records here.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path


class Store:
    def __init__(self, path: str) -> None:
        self.path = path
        self.lock = threading.RLock()
        if path != ":memory:":
            db_path = Path(path)
            if db_path.is_symlink():
                raise ValueError("SQLite database path must not be a symlink")
            db_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        # A single connection is guarded by lock; multi-process deployments not supported.
        self.db = sqlite3.connect(path, check_same_thread=False, timeout=10, isolation_level=None)
        if path != ":memory:" and os.name == "posix":
            # The pilot's stored observations and run inputs must not be
            # readable by other local users. OS access is still ultimately
            # controlled by volume/host permissions.
            os.chmod(path, 0o600)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA busy_timeout=10000")
        self.db.execute("PRAGMA foreign_keys=ON")
        with self.lock:
            self.db.executescript(
                "CREATE TABLE IF NOT EXISTS observations ("
                "id TEXT PRIMARY KEY, tenant TEXT NOT NULL, asset TEXT NOT NULL, "
                "ts TEXT NOT NULL, metric TEXT NOT NULL, value REAL NOT NULL, "
                "unit TEXT NOT NULL, source TEXT NOT NULL, lineage TEXT NOT NULL);"
                "CREATE INDEX IF NOT EXISTS observations_by_asset ON observations(tenant,asset,metric,ts);"
                "CREATE TABLE IF NOT EXISTS runs ("
                "id TEXT PRIMARY KEY, tenant TEXT NOT NULL, created TEXT NOT NULL, "
                "kind TEXT NOT NULL, payload TEXT NOT NULL);"
                "CREATE INDEX IF NOT EXISTS runs_by_tenant ON runs(tenant, created);"
                "CREATE TABLE IF NOT EXISTS audit ("
                "seq INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, tenant TEXT NOT NULL, "
                "actor TEXT NOT NULL, event TEXT NOT NULL, digest TEXT NOT NULL, prev_hash TEXT NOT NULL, hash TEXT NOT NULL);"
            )

    def _audit(self, cur, tenant: str, actor: str, event: str, digest: str) -> None:
        previous = cur.execute("SELECT hash FROM audit ORDER BY seq DESC LIMIT 1").fetchone()
        prev = previous[0] if previous else "0"*64
        ts = datetime.now(timezone.utc).isoformat()
        canonical = json.dumps([ts, tenant, actor, event, digest, prev], separators=(",",":"))
        hash_ = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        cur.execute("INSERT INTO audit(ts,tenant,actor,event,digest,prev_hash,hash) VALUES(?,?,?,?,?,?,?)",
                    (ts,tenant,actor,event,digest,prev,hash_))

    def append_observations(self, tenant: str, actor: str, points: list[dict]) -> int:
        with self.lock:
            cur = self.db.cursor()
            try:
                cur.execute("BEGIN IMMEDIATE")
                inserted: list[dict] = []
                for p in points:
                    # Idempotence across REST retries and batches: the same source +
                    # asset + metric + timestamp is one sample, regardless of value.
                    # A changed value needs an explicit correction process, never an
                    # invisible overwrite of historical measurements.
                    cur.execute(
                        "INSERT INTO observations(id,tenant,asset,ts,metric,value,unit,source,lineage) "
                        "SELECT ?,?,?,?,?,?,?,?,? WHERE NOT EXISTS ("
                        "SELECT 1 FROM observations WHERE tenant=? AND asset=? AND ts=? "
                        "AND metric=? AND source=?)",
                        (str(uuid.uuid4()),tenant,p["asset_id"],p["measured_at"],p["metric"],
                         p["value"],p["unit"],p["source"],p.get("lineage",""),
                         tenant,p["asset_id"],p["measured_at"],p["metric"],p["source"]),
                    )
                    if cur.rowcount:
                        inserted.append(p)
                if inserted:
                    digest = hashlib.sha256(json.dumps(inserted,sort_keys=True).encode()).hexdigest()
                    self._audit(cur,tenant,actor,"telemetry.append",digest)
                cur.execute("COMMIT")
            except Exception:
                cur.execute("ROLLBACK")
                raise
        return len(inserted)

    def read_observations(self, tenant: str, asset: str, metric: str, limit: int = 200) -> list[dict]:
        with self.lock:
            rows=self.db.execute(
                "SELECT ts,value,unit,source,lineage FROM observations "
                "WHERE tenant=? AND asset=? AND metric=? ORDER BY ts DESC LIMIT ?",
                (tenant,asset,metric,max(1,min(limit,2000)))
            ).fetchall()
        return [{"measured_at":r[0],"value":r[1],"unit":r[2],"source":r[3],"lineage":r[4]} for r in reversed(rows)]

    def save_run(self, tenant: str, actor: str, kind: str, value: dict) -> str:
        run_id=str(uuid.uuid4())
        raw=json.dumps(value,allow_nan=False,sort_keys=True)
        with self.lock:
            cur=self.db.cursor()
            try:
                cur.execute("BEGIN IMMEDIATE")
                cur.execute("INSERT INTO runs VALUES(?,?,?,?,?)",(run_id,tenant,datetime.now(timezone.utc).isoformat(),kind,raw))
                self._audit(cur,tenant,actor,"run."+kind,hashlib.sha256(raw.encode()).hexdigest())
                cur.execute("COMMIT")
            except Exception:
                cur.execute("ROLLBACK")
                raise
        return run_id

    def get_run(self, tenant: str, run_id: str) -> dict | None:
        with self.lock:
            row=self.db.execute("SELECT payload FROM runs WHERE tenant=? AND id=?",(tenant,run_id)).fetchone()
        return json.loads(row[0]) if row else None

    def get_run_record(self, tenant: str, run_id: str) -> dict | None:
        """Return original run kind and payload for safely scoped review."""
        with self.lock:
            row=self.db.execute(
                "SELECT kind,payload FROM runs WHERE tenant=? AND id=?",
                (tenant,run_id),
            ).fetchone()
        return {"kind":row[0],"payload":json.loads(row[1])} if row else None

    def list_runs(self, tenant: str, limit: int = 30) -> list[dict]:
        with self.lock:
            rows=self.db.execute("SELECT id,created,kind FROM runs WHERE tenant=? ORDER BY created DESC LIMIT ?",(tenant,max(1,min(limit,100)))).fetchall()
        return [{"id":x[0],"created_at":x[1],"kind":x[2]} for x in rows]

    def verify_audit_chain(self, tenant: str | None = None) -> dict:
        """Verify the whole physical hash chain without leaking other tenants' activity.

        An authenticated tenant sees only its event count and a per-tenant
        fingerprint, never global sequence numbers, cross-tenant event counts or
        the global chain head. An internal integrity service may call with None
        to obtain the complete chain head for offline anchoring.
        """
        with self.lock:
            rows = self.db.execute(
                "SELECT seq,ts,tenant,actor,event,digest,prev_hash,hash "
                "FROM audit ORDER BY seq"
            ).fetchall()

        prev = "0" * 64
        own_count = 0
        own_fingerprint = hashlib.sha256()
        for seq, ts, row_tenant, actor, event, digest, recorded_prev, hash_ in rows:
            canonical = json.dumps(
                [ts, row_tenant, actor, event, digest, prev],
                separators=(",", ":"),
            )
            computed = hashlib.sha256(canonical.encode()).hexdigest()
            if recorded_prev != prev or computed != hash_:
                if tenant is not None:
                    return {
                        "verified": False, "event_count": own_count,
                        "error": "shared audit integrity failed; engineering review required",
                    }
                return {
                    "verified": False, "failed_sequence": seq,
                    "event_count": len(rows),
                }
            if tenant is not None and row_tenant == tenant:
                own_count += 1
                own_fingerprint.update(hash_.encode("ascii"))
            prev = hash_

        if tenant is not None:
            return {
                "verified": True, "event_count": own_count,
                "tenant_evidence_fingerprint": own_fingerprint.hexdigest(),
                "scope": "tenant",
                "note": "Fingerprint is not an externally anchored audit certificate",
            }
        return {
            "verified": True, "event_count": len(rows),
            "chain_head": prev,
            "scope": "internal_global",
        }
