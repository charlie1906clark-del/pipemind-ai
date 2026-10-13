"""Safe single-node SQLite offline backup/verification for the research pilot.

No implicit restore or overwrite. A separate encrypted/offsite backup policy,
restore drills, key custody and retention controls are required before hosting
industrial customer data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from pipemind.storage import Store


class BackupFailure(RuntimeError):
    pass


def _hash_file(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha.update(chunk)
    return sha.hexdigest()


def _integrity(path: Path) -> dict:
    if not path.is_file() or path.is_symlink():
        raise BackupFailure("expected an ordinary local SQLite backup file")
    # Always verify a disposable copy or a settled backup, never open production
    # data in write mode merely to check its integrity.
    database = sqlite3.connect(f"file:{path.resolve().as_posix()}?mode=ro", uri=True)
    try:
        query = database.execute("PRAGMA integrity_check").fetchone()
        if not query or query[0] != "ok":
            raise BackupFailure("SQLite integrity check failed")
        required = {"observations", "runs", "audit"}
        actual = {row[0] for row in database.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )}
        if not required.issubset(actual):
            raise BackupFailure("backup is missing expected pilot data tables")
        audit = database.execute(
            "SELECT seq, ts, tenant, actor, event, digest, prev_hash, hash "
            "FROM audit ORDER BY seq"
        ).fetchall()
        prev = "0" * 64
        for _, ts, tenant, actor, event, digest, expected_previous, claimed in audit:
            message = json.dumps(
                [ts, tenant, actor, event, digest, prev], separators=(",", ":")
            ).encode()
            actual_hash = hashlib.sha256(message).hexdigest()
            if expected_previous != prev or claimed != actual_hash:
                raise BackupFailure("audit chain mismatch; backup rejected")
            prev = claimed
        return {"audit_events": len(audit), "audit_head": prev}
    finally:
        database.close()


def verify_backup(path: str | Path) -> dict:
    """Verify SHA256 manifest, SQLite consistency and audit chain."""
    target = Path(path).resolve()
    manifest_path = Path(str(target) + ".sha256.json")
    if not manifest_path.is_file() or manifest_path.is_symlink():
        raise BackupFailure("backup manifest is missing or unsafe")
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if data.get("schema") != "pipemind-backup-v1":
        raise BackupFailure("unrecognised backup manifest schema")
    digest = _hash_file(target)
    if digest != data.get("sha256"):
        raise BackupFailure("backup file does not match signed-off digest")
    evidence = _integrity(target)
    if evidence["audit_head"] != data.get("audit_head"):
        raise BackupFailure("audit head disagrees with backup manifest")
    return {
        "verified": True, "path": str(target), "sha256": digest,
        "audit_events": evidence["audit_events"], "audit_head": evidence["audit_head"],
        "anchored_externally": False,
    }


def create_backup(source: str | Path, destination: str | Path) -> dict:
    """Create a consistent snapshot without overwriting an existing backup."""
    src = Path(source).resolve()
    dst = Path(destination).absolute()
    if not src.is_file() or src.is_symlink():
        raise BackupFailure("source must be an existing local database file")
    if src == dst or dst.exists() or Path(str(dst)+".sha256.json").exists():
        raise BackupFailure("refusing to overwrite database or existing backup")
    dst.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if dst.is_symlink():
        raise BackupFailure("backup destination must not be a symlink")

    partial = dst.with_name("." + dst.name + "." + secrets.token_hex(8) + ".partial")
    try:
        # SQLite's online backup API makes a consistent copy even when the
        # source uses WAL. Directly copying the .sqlite file would not.
        db = sqlite3.connect(f"file:{src.as_posix()}?mode=ro", uri=True)
        try:
            snapshot = sqlite3.connect(str(partial))
            try:
                db.backup(snapshot)
            finally:
                snapshot.close()
        finally:
            db.close()
        if os.name == "posix":
            os.chmod(partial, 0o600)
        integrity = _integrity(partial)
        digest = _hash_file(partial)
        payload = {
            "schema": "pipemind-backup-v1",
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "sha256": digest,
            "audit_events": integrity["audit_events"],
            "audit_head": integrity["audit_head"],
            "limitations": "local plain-text backup; no encryption or external anchoring",
        }
        # Atomic create-without-overwrite on the same filesystem.
        os.link(partial, dst)
        manifest = Path(str(dst) + ".sha256.json")
        try:
            with manifest.open("x", encoding="utf-8") as out:
                json.dump(payload, out, indent=2)
                out.write("\n")
            if os.name == "posix":
                os.chmod(manifest, 0o600)
        except Exception:
            dst.unlink(missing_ok=True)
            raise
        return verify_backup(dst)
    except sqlite3.DatabaseError as exc:
        raise BackupFailure("invalid or unreadable SQLite source") from exc
    finally:
        partial.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="PipeMind single-node backup integrity tool")
    parser.add_argument("action", choices=["create", "verify"])
    parser.add_argument("source", help="existing SQLite DB or settled backup file")
    parser.add_argument("destination", nargs="?", help="new backup filename for create")
    args = parser.parse_args()
    if args.action == "create":
        if not args.destination:
            parser.error("create requires a destination path")
        result = create_backup(args.source, args.destination)
    else:
        result = verify_backup(args.source)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
