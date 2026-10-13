import tempfile
import unittest
from dataclasses import replace
from datetime import datetime, timezone, timedelta
from pathlib import Path

from pipemind.twin.telemetry import check_batch
from pipemind.twin.forecast import forecast
from pipemind.finance import CostInputs, evaluate_cost, compare_options
from pipemind.storage import Store

class TwinTests(unittest.TestCase):
    def test_quality_rejects_bad_units_and_untrusted(self):
        now=datetime.now(timezone.utc)
        ts=now.isoformat()
        points=[
            dict(asset_id="tank-1",metric="temperature_k",value=20.0,unit="K",source="simulated",measured_at=ts),
            dict(asset_id="tank-1",metric="temperature_k",value=20.0,unit="C",source="simulated",measured_at=ts),
            dict(asset_id="tank-1",metric="pressure_pa",value=100,unit="Pa",source="evil",measured_at=ts),
        ]
        result=check_batch(points,now=now)
        self.assertEqual(result.counts["accepted"],1)
        self.assertEqual(result.counts["rejected"],2)

    def test_future_and_nonfinite_fails_closed(self):
        now=datetime.now(timezone.utc)
        r=check_batch([dict(asset_id="a",metric="pressure_pa",value=float("nan"),unit="Pa",source="simulated",
                            measured_at=(now+timedelta(days=2)).isoformat())],now=now)
        self.assertEqual(r.counts["accepted"],0)

    def test_forecast_abstains_and_benchmarks(self):
        self.assertEqual(forecast([1,2,3]).status,"INSUFFICIENT_DATA")
        result=forecast([float(i) for i in range(45)])
        self.assertTrue(result.beats_baseline)
        self.assertLess(result.backtest_mae, result.persistence_mae)
        self.assertGreater(result.next_value,40)

    def test_cost_comparison_separates_boiloff(self):
        base=CostInputs(duration_hours=24,heat_load_w=1000)
        r=evaluate_cost(base)
        self.assertGreater(r["gross_vapour_equivalent_kg"],100)
        variants=compare_options(base,[replace(base,cooling_fraction=0.5)])
        self.assertEqual(len(variants),1)
        self.assertIn("saving_vs_baseline_gbp",variants[0])

    def test_cost_input_bools_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_cost(CostInputs(cooling_fraction=True))

    def test_storage_enforces_tenant_and_audit(self):
        with tempfile.TemporaryDirectory() as d:
            store=Store(str(Path(d)/"data.sqlite"))
            points=[dict(asset_id="tank-a",metric="temperature_k",value=20,unit="K",
                         source="simulated",lineage="test",measured_at=datetime.now(timezone.utc).isoformat())]
            self.assertEqual(store.append_observations("tenant-a","analyst",points),1)
            self.assertEqual(store.read_observations("tenant-b","tank-a","temperature_k"),[])
            run=store.save_run("tenant-a","analyst","simulation",{"pressure":101325})
            self.assertIsNone(store.get_run("tenant-b",run))
            self.assertTrue(store.verify_audit_chain()["verified"])

if __name__ == "__main__":
    unittest.main()
