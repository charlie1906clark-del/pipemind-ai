"""Run an openly documented example: PYTHONPATH=src python -m pipemind.cli."""
import json

from .cryogenics import TankScenario, compare_scenarios


def main() -> None:
    shared = dict(
        inventory_kg=10_000,
        heat_ingress_w=1000,
        duration_h=24,
        hydrogen_value_gbp_per_kg=5,
        electricity_gbp_per_kwh=0.15,
    )
    baseline = TankScenario(**shared)
    candidate = TankScenario(
        **shared, cooling_duty_w=500, cooling_cop=0.04, vapor_recovery_fraction=0.5
    )
    print(json.dumps(compare_scenarios(baseline, candidate), indent=2))


if __name__ == "__main__":
    main()
