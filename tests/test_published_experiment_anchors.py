"""The metadata may be accurate while the model remains *unvalidated*."""
from __future__ import annotations
import unittest

from pipemind.validation.references import load_reference_cases, prepare_screening_input


class ExperimentAnchorTests(unittest.TestCase):
    def test_five_published_scenarios_exactly(self):
        manifest=load_reference_cases()
        self.assertEqual({c["id"] for c in manifest["cases"]},
                         {"K(i)","K(ii)","M(i)","M(ii)","M(iii)"})
        self.assertEqual(manifest["experimental_pressure_time_series"],"NOT_INCLUDED")
        self.assertEqual(manifest["validation_status"],"NO_INDEPENDENT_PRESSURE_TRACE_BENCHMARKED")

    def test_selected_boundary_conditions(self):
        scenarios={c["id"]:c for c in load_reference_cases()["cases"]}
        self.assertAlmostEqual(scenarios["K(i)"]["total_heat_w"],49)
        self.assertAlmostEqual(scenarios["K(ii)"]["total_heat_w"],28)
        self.assertAlmostEqual(scenarios["M(iii)"]["fill_fraction"],.9)
        self.assertAlmostEqual(scenarios["M(ii)"]["initial_pressure_pa"],111600)

    def test_prepared_case_abstains_from_validation_claim(self):
        cfg=prepare_screening_input("M(ii)")
        self.assertAlmostEqual(cfg["tank_input"]["volume_m3"],18.27)
        self.assertFalse(cfg["validated"])
        self.assertFalse(cfg["experimental_time_series_available"])
        self.assertTrue(cfg["assumptions"])
        with self.assertRaises(ValueError):
            prepare_screening_input("made-up")


if __name__=="__main__":
    unittest.main()
