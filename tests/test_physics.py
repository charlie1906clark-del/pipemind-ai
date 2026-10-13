import math
import unittest
from dataclasses import replace

from pipemind.physics import (
    HydrogenProperties, PropertyDomainError, TankInput, CableInput,
    simulate_tank, simulate_cable
)

try:
    import CoolProp  # noqa
    COOLPROP = True
except ImportError:
    COOLPROP = False


@unittest.skipUnless(COOLPROP, "CoolProp must be installed for EOS tests")
class PropertyTests(unittest.TestCase):
    def test_saturation_positive_latent_heat(self):
        s = HydrogenProperties("para").saturation(101325)
        self.assertGreater(s.rho_liquid_kg_m3, s.rho_vapour_kg_m3)
        self.assertGreater(s.latent_heat_j_kg, 300000)
        self.assertLess(s.latent_heat_j_kg, 600000)
        self.assertTrue(19 < s.temperature_k < 22)

    def test_invalid_domain_fails(self):
        eos = HydrogenProperties()
        for p in (0, -100, 2e6, float("nan"), True):
            with self.subTest(p=p), self.assertRaises(PropertyDomainError):
                eos.saturation(p)

    def test_spin_variants_have_different_properties(self):
        p = HydrogenProperties("para").saturation(101325).temperature_k
        n = HydrogenProperties("normal").saturation(101325).temperature_k
        self.assertNotAlmostEqual(p, n, places=4)


@unittest.skipUnless(COOLPROP, "CoolProp must be installed for EOS tests")
class TankTests(unittest.TestCase):
    def test_zero_heat_pressure_and_mass_conserved(self):
        r = simulate_tank(TankInput(heat_ingress_w=0, cooling_duty_w=0, steps=4))
        self.assertEqual(len(r.points), 5)
        self.assertLess(abs(r.points[-1]["pressure_pa"] - r.points[0]["pressure_pa"]), 2)
        for pt in r.points:
            self.assertAlmostEqual(pt["liquid_mass_kg"] + pt["vapour_mass_kg"], r.initial_mass_kg, places=4)

    def test_positive_heat_increases_pressure(self):
        r = simulate_tank(TankInput(heat_ingress_w=300, duration_hours=3, steps=6))
        self.assertGreater(r.points[-1]["pressure_pa"], r.points[0]["pressure_pa"])
        self.assertAlmostEqual(
            r.points[-1]["total_internal_energy_j"] - r.points[0]["total_internal_energy_j"],
            r.net_heat_j, delta=max(1, r.net_heat_j * 1e-6)
        )

    def test_cooling_offsets_heat(self):
        b = simulate_tank(TankInput(heat_ingress_w=250, duration_hours=2, steps=4))
        c = simulate_tank(TankInput(heat_ingress_w=250, cooling_duty_w=250, duration_hours=2, steps=4))
        self.assertLess(c.points[-1]["pressure_pa"], b.points[-1]["pressure_pa"])
        self.assertAlmostEqual(c.points[-1]["pressure_pa"], c.points[0]["pressure_pa"], delta=2)
        self.assertGreater(c.refrigeration_electricity_kwh, 0)

    def test_rejects_unphysical_inputs(self):
        with self.assertRaises(PropertyDomainError):
            simulate_tank(TankInput(fill_liquid_volume_fraction=1.0))
        with self.assertRaises(PropertyDomainError):
            simulate_tank(TankInput(steps=20000))


@unittest.skipUnless(COOLPROP, "CoolProp must be installed for EOS tests")
class CableTests(unittest.TestCase):
    def test_cable_heat_increases_temp_and_friction_reduces_pressure(self):
        r = simulate_cable(CableInput(length_m=60, inlet_temperature_k=18, inlet_pressure_pa=250000, steps=6))
        self.assertGreater(r.outlet_temperature_k, r.points[0]["temperature_k"])
        self.assertLess(r.outlet_pressure_pa, r.points[0]["pressure_pa"])
        self.assertGreater(r.minimum_saturation_margin_k, 0)
        self.assertTrue(all(math.isfinite(p["pressure_pa"]) for p in r.points))

    def test_invalid_and_phase_boundary_rejected(self):
        with self.assertRaises(PropertyDomainError):
            simulate_cable(CableInput(steps=10000))
        with self.assertRaises(PropertyDomainError):
            simulate_cable(CableInput(inlet_temperature_k=28, inlet_pressure_pa=100000))


if __name__ == "__main__":
    unittest.main()
