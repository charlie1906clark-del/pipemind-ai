import math
import unittest
from dataclasses import replace

from pipemind.cryogenics import TankScenario, compare_scenarios, evaluate


class TankScreeningTests(unittest.TestCase):
    def test_reference_heat_balance(self):
        result = evaluate(TankScenario(inventory_kg=1000, heat_ingress_w=1000, duration_h=24))
        self.assertAlmostEqual(result.heat_input_j, 86_400_000)
        self.assertAlmostEqual(result.boiloff_equivalent_kg, 86_400_000 / 445_000)
        self.assertAlmostEqual(result.remaining_tank_mass_kg + result.vaporised_kg, 1000)

    def test_zero_heat_no_boiloff(self):
        result = evaluate(TankScenario(inventory_kg=100, heat_ingress_w=0))
        self.assertEqual(result.vaporised_kg, 0)
        self.assertEqual(result.wall_electricity_kwh, 0)

    def test_cooling_never_creates_hydrogen(self):
        result = evaluate(TankScenario(inventory_kg=100, heat_ingress_w=100, cooling_duty_w=500, cooling_cop=0.05))
        self.assertEqual(result.vaporised_kg, 0)
        self.assertEqual(result.remaining_tank_mass_kg, 100)
        self.assertAlmostEqual(result.wall_electricity_kwh, 48)

    def test_vapor_recovery_not_added_back_to_tank(self):
        result = evaluate(TankScenario(inventory_kg=100, heat_ingress_w=1000, vapor_recovery_fraction=1))
        self.assertAlmostEqual(result.unrecovered_vapor_kg, 0)
        self.assertGreater(result.recovered_vapor_kg, 0)
        self.assertLess(result.remaining_tank_mass_kg, 100)

    def test_inventory_caps_vaporised_mass(self):
        result = evaluate(TankScenario(inventory_kg=1, heat_ingress_w=1000))
        self.assertEqual(result.vaporised_kg, 1)
        self.assertEqual(result.remaining_tank_mass_kg, 0)
        self.assertGreater(result.boiloff_equivalent_kg, 1)

    def test_invalid_inputs_rejected(self):
        base = TankScenario(inventory_kg=100, heat_ingress_w=100)
        for s in [
            replace(base, inventory_kg=-1),
            replace(base, duration_h=float("nan")),
            replace(base, latent_heat_j_per_kg=0),
            replace(base, vapor_recovery_fraction=1.1),
            replace(base, cooling_duty_w=20),
            replace(base, cooling_duty_w=20, cooling_cop=0),
            replace(base, cooling_cop=float("inf")),
        ]:
            with self.subTest(s=s), self.assertRaises(ValueError):
                evaluate(s)

    def test_comparison_rejects_different_baselines(self):
        b = TankScenario(inventory_kg=100, heat_ingress_w=100)
        with self.assertRaises(ValueError):
            compare_scenarios(b, replace(b, heat_ingress_w=200))

    def test_cost_reconciles(self):
        r = evaluate(TankScenario(inventory_kg=100, heat_ingress_w=1000,
                                  hydrogen_value_gbp_per_kg=5,
                                  cooling_duty_w=200, cooling_cop=0.04,
                                  electricity_gbp_per_kwh=0.20))
        self.assertTrue(math.isfinite(r.total_variable_cost_gbp))
        self.assertAlmostEqual(r.total_variable_cost_gbp,
            r.unrecovered_hydrogen_cost_gbp + r.refrigeration_electricity_cost_gbp)


if __name__ == "__main__":
    unittest.main()
