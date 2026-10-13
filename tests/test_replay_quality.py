import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from pipemind.storage import Store
from pipemind.twin.asset_forecast import replay_forecast
from pipemind.twin.telemetry import check_batch


class ReplayQualityTests(unittest.TestCase):
    def make_rows(self,n=45,step=60):
        t=datetime(2026,10,12,tzinfo=timezone.utc)
        return [{"asset_id":"tank-1","measured_at":(t+timedelta(seconds=i*step)).isoformat(),
                 "value":20+i*.01,"metric":"temperature_k","unit":"K","source":"operator-import"}
                 for i in range(n)]

    def test_no_spoofed_signed_gateway(self):
        sample=self.make_rows(1)[0].copy()
        sample["source"]="signed-gateway"
        result=check_batch([sample],now=datetime(2026,10,13,tzinfo=timezone.utc))
        self.assertEqual(result.counts["accepted"],0)
        self.assertIn("UNTRUSTED_SOURCE",result.rejected[0]["flags"])

    def test_replay_only_with_regular_cadence(self):
        rows=self.make_rows()
        result=replay_forecast(rows,"temperature_k")
        self.assertFalse(result["live_operational"])
        self.assertTrue(result["status"] in ("BASELINE_PREFERRED","RESEARCH_TREND_ONLY"))
        self.assertEqual(result["expected_sampling_interval_s"],60)

    def test_gap_and_mixed_provenance_abstain(self):
        rows=self.make_rows()
        rows[20]["measured_at"]=(datetime(2026,10,12,tzinfo=timezone.utc)+timedelta(hours=10)).isoformat()
        result=replay_forecast(rows,"temperature_k")
        self.assertEqual(result["status"],"NON_MONOTONIC_OR_DUPLICATE_TIMESTAMPS")
        rows=self.make_rows()
        rows[5]["source"]="simulated"
        self.assertEqual(replay_forecast(rows,"temperature_k")["status"],"MULTIPLE_DATA_PROVENANCES")

    def test_storage_retries_do_not_duplicate_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=Store(str(Path(tmp)/"test.sqlite"))
            rows=self.make_rows(2)
            self.assertEqual(store.append_observations("tenantA","engineer",rows),2)
            self.assertEqual(store.append_observations("tenantA","engineer",rows),0)
            self.assertEqual(len(store.read_observations("tenantA","tank-1","temperature_k")),2)
            self.assertEqual(store.append_observations("tenantB","engineer",rows),2)
            self.assertTrue(store.verify_audit_chain()["verified"])
            store.db.close()


if __name__=="__main__":
    unittest.main()
