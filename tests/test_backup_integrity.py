"""Online backup is consistent and refuses silent mutation, overwrite or corruption."""
from __future__ import annotations

import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from pipemind.storage import Store
from pipemind.maintenance.backup import (
    BackupFailure, create_backup, verify_backup
)


class BackupTests(unittest.TestCase):
    def test_create_verify_and_detect_mutation(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/"active.sqlite"
            target=Path(tmp)/"snapshot.sqlite"
            store=Store(str(source))
            store.save_run("tenant-a","analyst","model",{"x":1})
            store.save_run("tenant-a","analyst","model",{"x":2})
            created=create_backup(source,target)
            self.assertTrue(created["verified"])
            self.assertEqual(created["audit_events"],2)
            self.assertEqual(store.list_runs("tenant-a")[0]["kind"],"model")
            self.assertTrue(verify_backup(target)["verified"])
            with self.assertRaises(BackupFailure):
                create_backup(source,target)
            with sqlite3.connect(target) as db:
                db.execute("UPDATE runs SET payload=? WHERE kind='model'",('{}',))
            with self.assertRaises(BackupFailure):
                verify_backup(target)
            store.db.close()

    def test_symlink_source_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/"active.sqlite"
            alias=Path(tmp)/"alias.sqlite"
            target=Path(tmp)/"snapshot.sqlite"
            store=Store(str(source))
            store.save_run("t","a","x",{"n":1})
            alias.symlink_to(source)
            # The actual implementation must reject the symlink before resolve.
            with self.assertRaises(BackupFailure):
                create_backup(alias,target)
            store.db.close()

    def test_database_permissions_local(self):
        if os.name!="posix":
            self.skipTest("POSIX local filesystem only")
        with tempfile.TemporaryDirectory() as tmp:
            store=Store(str(Path(tmp)/"secure.sqlite"))
            try:
                self.assertEqual((Path(tmp)/"secure.sqlite").stat().st_mode & 0o777,0o600)
            finally:
                store.db.close()


if __name__ == "__main__":
    unittest.main()
