"""Shared audit-chain integrity must not reveal other customer activity."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipemind.storage import Store


class AuditTenantIsolationTests(unittest.TestCase):
    def test_tenant_has_no_global_count_or_head(self):
        with tempfile.TemporaryDirectory() as folder:
            store = Store(str(Path(folder) / "audit.sqlite"))
            try:
                store.save_run("tenant-a", "alice", "cost", {"amount": 10})
                store.save_run("tenant-a", "alice", "tank", {"mass": 1})
                store.save_run("tenant-b", "bob", "tank", {"mass": 2})
                a = store.verify_audit_chain("tenant-a")
                b = store.verify_audit_chain("tenant-b")
                global_check = store.verify_audit_chain()
                self.assertTrue(a["verified"])
                self.assertEqual(a["event_count"], 2)
                self.assertEqual(b["event_count"], 1)
                self.assertEqual(global_check["event_count"], 3)
                self.assertNotIn("chain_head", a)
                self.assertNotIn("failed_sequence", a)
                self.assertNotEqual(
                    a["tenant_evidence_fingerprint"],
                    b["tenant_evidence_fingerprint"]
                )
                self.assertEqual(a["scope"], "tenant")
            finally:
                store.db.close()

    def test_shared_corruption_has_no_cross_tenant_sequence_disclosure(self):
        with tempfile.TemporaryDirectory() as folder:
            store = Store(str(Path(folder) / "audit.sqlite"))
            try:
                store.save_run("tenant-b", "bob", "tank", {"mass": 2})
                store.save_run("tenant-a", "alice", "cost", {"cost": 5})
                store.db.execute(
                    "UPDATE audit SET digest='tampered' WHERE seq=1"
                )
                result = store.verify_audit_chain("tenant-a")
                self.assertFalse(result["verified"])
                self.assertNotIn("failed_sequence", result)
                self.assertNotIn("chain_head", result)
                self.assertNotIn("tenant", str(result))
            finally:
                store.db.close()
