"""Load only digest-pinned, explicitly reviewed investigation graph extensions.

An extension may link to existing graph nodes but cannot replace any existing ID.
Approval is a separate reviewed manifest edit, never a directory scan or a side
effect of running an investigation's generator.
"""
import hashlib
import importlib.util
import json
from pathlib import Path


def load_approved_extensions(root, nodes, edges, as_of):
    root = Path(root).resolve()
    manifest = root / "data/approved-investigations.json"
    if not manifest.exists():
        return []
    approval = json.loads(manifest.read_text())
    if approval.get("version") != "1.0" or not isinstance(approval.get("extensions"), list):
        raise ValueError("Invalid investigation approval manifest")
    incoming_nodes, incoming_edges, loaded = [], [], []
    identities = {record["id"] for record in nodes + edges}
    seen_paths = set()
    for entry in approval["extensions"]:
        if entry.get("review_status") != "accepted_for_public_graph":
            raise ValueError("Investigation is not accepted for public graph")
        if not isinstance(entry.get("review_note"), str) or not entry["review_note"].strip():
            raise ValueError("Investigation requires an explicit review note")
        if Path(entry["path"]).is_absolute():
            raise ValueError("Investigation paths must be repository-relative")
        path = (root / entry["path"]).resolve()
        if not path.is_relative_to(root / "investigations") or path in seen_paths:
            raise ValueError("Invalid or repeated investigation extension path")
        seen_paths.add(path)
        body = path.read_bytes()
        if hashlib.sha256(body).hexdigest() != entry.get("sha256"):
            raise ValueError("Investigation extension digest mismatch: " + str(path))
        extension = json.loads(body)
        if extension.get("version") != "1.0" or extension.get("as_of") != as_of:
            raise ValueError("Investigation version/date must match assembly")
        for dependency in extension.get("input_artifacts", []):
            source_path = (root / dependency["path"]).resolve()
            if not source_path.is_relative_to(root / "investigations"):
                raise ValueError("Investigation input escapes investigations directory")
            if hashlib.sha256(source_path.read_bytes()).hexdigest() != dependency["sha256"]:
                raise ValueError("Investigation reviewed input changed: " + str(source_path))
        for record in extension["nodes"] + extension["edges"]:
            if record["id"] in identities:
                raise ValueError("Investigation cannot replace existing ID: " + record["id"])
            identities.add(record["id"])
        for record in extension["nodes"]:
            props = record.get("properties", {})
            if record.get("type") == "source" and props.get("source_bytes_archived"):
                snapshot = (root / props["snapshot_path"]).resolve()
                if not snapshot.is_relative_to(root):
                    raise ValueError("Archived source escapes research directory")
                if hashlib.sha256(snapshot.read_bytes()).hexdigest() != props.get("content_sha256"):
                    raise ValueError("Archived investigation source digest mismatch")
        incoming_nodes.extend(extension["nodes"])
        incoming_edges.extend(extension["edges"])
        loaded.append({"path": entry["path"], "sha256": entry["sha256"],
                       "nodes": len(extension["nodes"]), "edges": len(extension["edges"])})
    # Use the same public provenance, legal status, monetary and privacy contract
    # as final exports. No partial append occurs if any extension is invalid.
    spec = importlib.util.spec_from_file_location("investigation_integrity", root / "engine/integrity.py")
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    engine.validate_graph({"version": "1.0", "as_of": as_of,
        "nodes": nodes + incoming_nodes, "edges": edges + incoming_edges}, public=True)
    nodes.extend(incoming_nodes)
    edges.extend(incoming_edges)
    return loaded
