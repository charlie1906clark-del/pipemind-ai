"""Transparent *screening* calculation for LH2 tank heat ingress.

No pressure equation, phase envelope, ortho/para conversion, level calibration,
dynamic stratification, pipe flow or failure consequences are represented.
DO NOT USE for engineering sign-off, safety design or equipment actuation.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite


@dataclass(frozen=True)
class TankScenario:
    """All powers are W, energy J, time h, mass kg, electricity GBP/kWh.

    vapor_recovery_fraction is fraction of boiled-off mass captured elsewhere;
    it does NOT change in-tank inventory. Cold-side refrigeration duty is a
    measured/assumed cooling load, not electrical wall-plug consumption.
    """

    inventory_kg: float
    heat_ingress_w: float
    duration_h: float = 24.0
    latent_heat_j_per_kg: float = 445_000.0  # illustrative; not a design property table
    cooling_duty_w: float = 0.0
    cooling_cop: float | None = None  # Q_cold / P_electric; not Carnot efficiency
    vapor_recovery_fraction: float = 0.0
    hydrogen_value_gbp_per_kg: float = 0.0
    electricity_gbp_per_kwh: float = 0.0


@dataclass(frozen=True)
class ScreeningResult:
    heat_input_j: float
    cold_side_heat_removed_j: float
    net_heat_j: float
    boiloff_equivalent_kg: float
    vaporised_kg: float
    recovered_vapor_kg: float
    unrecovered_vapor_kg: float
    remaining_tank_mass_kg: float
    wall_electricity_kwh: float
    unrecovered_hydrogen_cost_gbp: float
    refrigeration_electricity_cost_gbp: float
    total_variable_cost_gbp: float
    model_status: str = "ILLUSTRATIVE_SCREENING_ONLY"

    def to_dict(self) -> dict:
        return asdict(self)


def _finite_nonnegative(name: str, value: float) -> None:
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise ValueError(f"{name} must be a finite nonnegative number")
    if not isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")


def evaluate(scenario: TankScenario) -> ScreeningResult:
    for name in (
        "inventory_kg", "heat_ingress_w", "duration_h",
        "cooling_duty_w", "hydrogen_value_gbp_per_kg", "electricity_gbp_per_kwh"
    ):
        _finite_nonnegative(name, getattr(scenario, name))
    if not isinstance(scenario.latent_heat_j_per_kg, (int, float)) or (
        not isfinite(scenario.latent_heat_j_per_kg) or scenario.latent_heat_j_per_kg <= 0
    ):
        raise ValueError("latent_heat_j_per_kg must be finite and > 0")
    fraction = scenario.vapor_recovery_fraction
    if isinstance(fraction, bool) or not isinstance(fraction, (int, float)) or not isfinite(fraction) or not 0 <= fraction <= 1:
        raise ValueError("vapor_recovery_fraction must be in [0,1]")
    if scenario.cooling_duty_w > 0:
        cop = scenario.cooling_cop
        if isinstance(cop, bool) or not isinstance(cop, (int, float)) or not isfinite(cop) or not 0 < cop <= 1:
            raise ValueError("cooling_cop must be supplied in (0,1] for powered cooling")
    elif scenario.cooling_cop is not None:
        if isinstance(scenario.cooling_cop, bool) or not isinstance(scenario.cooling_cop, (int, float)) or not isfinite(scenario.cooling_cop) or not 0 < scenario.cooling_cop <= 1:
            raise ValueError("cooling_cop must be in (0,1]")

    duration_s = scenario.duration_h * 3600
    heat_in = scenario.heat_ingress_w * duration_s
    # No cooling credit beyond heat ingress. Unused cooling capacity not run.
    actual_cooling_w = min(scenario.heat_ingress_w, scenario.cooling_duty_w)
    removed = actual_cooling_w * duration_s
    net = heat_in - removed
    equivalent = net / scenario.latent_heat_j_per_kg
    vaporised = min(scenario.inventory_kg, equivalent)
    recovered = vaporised * scenario.vapor_recovery_fraction
    lost = vaporised - recovered
    remaining = scenario.inventory_kg - vaporised
    electric_kwh = (actual_cooling_w / scenario.cooling_cop * scenario.duration_h / 1000) if actual_cooling_w else 0.0
    hydrogen_cost = lost * scenario.hydrogen_value_gbp_per_kg
    electric_cost = electric_kwh * scenario.electricity_gbp_per_kwh
    return ScreeningResult(
        heat_input_j=heat_in,
        cold_side_heat_removed_j=removed,
        net_heat_j=net,
        boiloff_equivalent_kg=equivalent,
        vaporised_kg=vaporised,
        recovered_vapor_kg=recovered,
        unrecovered_vapor_kg=lost,
        remaining_tank_mass_kg=remaining,
        wall_electricity_kwh=electric_kwh,
        unrecovered_hydrogen_cost_gbp=hydrogen_cost,
        refrigeration_electricity_cost_gbp=electric_cost,
        total_variable_cost_gbp=hydrogen_cost + electric_cost,
    )


def compare_scenarios(baseline: TankScenario, candidate: TankScenario) -> dict:
    """Cost comparison for equal inventory/duration/heat ingress/market prices only."""
    fields = ("inventory_kg", "heat_ingress_w", "duration_h",
              "latent_heat_j_per_kg", "hydrogen_value_gbp_per_kg",
              "electricity_gbp_per_kwh")
    for field in fields:
        if getattr(baseline, field) != getattr(candidate, field):
            raise ValueError(f"Comparison requires identical {field}")
    b = evaluate(baseline)
    c = evaluate(candidate)
    return {
        "baseline": b.to_dict(),
        "candidate": c.to_dict(),
        "modeled_variable_saving_gbp": b.total_variable_cost_gbp - c.total_variable_cost_gbp,
        "limitations": [
            "Not a phase-equilibrium or pressure/stratification model",
            "Illustrative latent heat, not authoritative temperature-pressure property data",
            "Excludes CAPEX, maintenance, pumping, startup and recovery equipment energy",
            "No safety claim or actuator decision",
        ],
    }
