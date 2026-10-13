"""Cost comparison with explicit scope; returns hypotheses, not realised savings."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite

@dataclass(frozen=True)
class CostInputs:
    duration_hours: float = 24.0
    heat_load_w: float = 1000.0
    recovered_vapour_fraction: float = 0.0
    cooling_fraction: float = 0.0
    cooling_cop: float = 0.04
    effective_latent_heat_j_kg: float = 445000.0
    electricity_gbp_kwh: float = 0.20
    unrecovered_hydrogen_gbp_kg: float = 5.0
    annualised_equipment_cost_gbp: float = 0.0

def evaluate_cost(inputs: CostInputs) -> dict:
    for name, value in asdict(inputs).items():
        if type(value) not in (int,float) or not isfinite(value) or value < 0:
            raise ValueError(f"{name} must be finite and nonnegative")
    if inputs.cooling_fraction > 1 or inputs.recovered_vapour_fraction > 1:
        raise ValueError("fractions must not exceed one")
    if not 0 < inputs.cooling_cop <= 0.25:
        raise ValueError("cooling_cop must be in (0, 0.25]")
    if inputs.effective_latent_heat_j_kg <= 0:
        raise ValueError("latent heat must be positive")
    total_heat_j = inputs.heat_load_w * inputs.duration_hours * 3600
    removed_j = total_heat_j * inputs.cooling_fraction
    boiled_equivalent_kg = (total_heat_j - removed_j) / inputs.effective_latent_heat_j_kg
    unrecovered_kg = boiled_equivalent_kg * (1-inputs.recovered_vapour_fraction)
    cooling_electricity_kwh = removed_j / 3.6e6 / inputs.cooling_cop
    annualisation = inputs.duration_hours / (365*24)
    total_cost = (
        unrecovered_kg*inputs.unrecovered_hydrogen_gbp_kg
        + cooling_electricity_kwh*inputs.electricity_gbp_kwh
        + inputs.annualised_equipment_cost_gbp*annualisation
    )
    return {
        "model": "idealised-fixed-pressure-boiloff-cost-v0.1",
        "status": "HYPOTHETICAL_COST_SCREENING",
        "inputs": asdict(inputs), "total_heat_j": total_heat_j,
        "cooling_electricity_kwh": cooling_electricity_kwh,
        "gross_vapour_equivalent_kg": boiled_equivalent_kg,
        "unrecovered_equivalent_kg": unrecovered_kg,
        "total_modelled_cost_gbp": total_cost,
        "excluded_costs": [
            "Liquefaction, pumping, equipment installation, staffing and servicing",
            "Gas recovery compression/recondensation cost and losses",
            "Tank pressure, wall inertia, liquid withdrawal and equipment efficiency curves",
        ],
    }


def compare_options(base: CostInputs, candidates: list[CostInputs]) -> list[dict]:
    if len(candidates) > 20:
        raise ValueError("at most 20 candidates")
    baseline = evaluate_cost(base)
    fixed_fields = (
        "duration_hours", "heat_load_w", "effective_latent_heat_j_kg",
        "electricity_gbp_kwh", "unrecovered_hydrogen_gbp_kg"
    )
    results = []
    for cand in candidates:
        if any(getattr(base,f) != getattr(cand,f) for f in fixed_fields):
            raise ValueError("comparison requires consistent baseline and commodity assumptions")
        cost = evaluate_cost(cand)
        cost["saving_vs_baseline_gbp"] = baseline["total_modelled_cost_gbp"] - cost["total_modelled_cost_gbp"]
        results.append(cost)
    return sorted(results, key=lambda x: x["total_modelled_cost_gbp"])
