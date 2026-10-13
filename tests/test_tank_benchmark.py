import unittest
from datetime import datetime, timedelta, timezone
from pipemind.twin.benchmark import benchmark_tank_pressure


class TankBenchmarkTests(unittest.TestCase):
    def model(self):
        return {"status":"SIMULATED_NOT_VALIDATED_FOR_OPERATIONS",
                "model":"unit-test-tank","eos_version":"test-only",
                "points":[{"hour":i,"pressure_pa":100000+100*i} for i in range(10)]}

    def measurements(self,diff=0,source="simulated"):
        t=datetime(2026,10,13,12,tzinfo=timezone.utc)
        return [{"measured_at":(t+timedelta(hours=i)).isoformat(),
                 "value":100000+100*i+diff,"unit":"Pa","source":source} for i in range(9)]

    def test_identical_trace_has_zero_error_but_not_certified(self):
        result=benchmark_tank_pressure(self.model(),self.measurements(),model_start_utc="2026-10-13T12:00:00Z")
        self.assertEqual(result["status"],"RESEARCH_BENCHMARK_NOT_CERTIFICATION")
        self.assertEqual(result["rmse_pa"],0)
        self.assertTrue(result["synthetic_validation_only"])
        self.assertTrue(result["human_review_required"])

    def test_known_bias_and_provenance(self):
        result=benchmark_tank_pressure(self.model(),self.measurements(50,"operator-import"),
                                       model_start_utc="2026-10-13T12:00:00Z")
        self.assertAlmostEqual(result["mae_pa"],50)
        self.assertAlmostEqual(result["bias_pa"],-50)
        self.assertFalse(result["synthetic_validation_only"])
        self.assertEqual(len(result["evidence_sha256"]),64)

    def test_abstain_with_no_overlap(self):
        result=benchmark_tank_pressure(self.model(),self.measurements(),
                                       model_start_utc="2026-11-13T12:00:00Z")
        self.assertEqual(result["status"],"ABSTAIN_INSUFFICIENT_OVERLAP")

    def test_mixed_source_or_unlabelled_input_rejected(self):
        rows=self.measurements()
        rows[3]["source"]="operator-import"
        with self.assertRaises(ValueError):
            benchmark_tank_pressure(self.model(),rows,model_start_utc="2026-10-13T12:00:00Z")
        with self.assertRaises(ValueError):
            benchmark_tank_pressure(self.model(),self.measurements(),
                                    model_start_utc="2026-10-13T12:00:00")

    def test_does_not_benchmark_unverified_model(self):
        model=self.model()
        model["status"]="CERTIFIED"
        with self.assertRaises(ValueError):
            benchmark_tank_pressure(model,self.measurements(),
                                    model_start_utc="2026-10-13T12:00:00Z")


if __name__=="__main__":
    unittest.main()
