"""Advisory optimisation ranking only, with uncertainty over missing costs.

Critical: no cost-saving recommendations from free assumed equipment.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from math import isfinite

from .finance import CostInputs, evaluate_cost


@dataclass(frozen=True)
class OptimisationStudy:
    baseline: CostInputs
    cooling_capital_annual_gbp: float | None = None
    recovery_capital_annual_gbp: float | None = None
    recovery_aux_electricity_kwh_per_kg: float | None = None
    cooling_options: tuple[float, ...] = (0,.25,.5,.75,1)
    recovery_options: tuple[float, ...] = (0,.25,.5,.75)


def optimise(study: OptimisationStudy) -> dict:
    base=evaluate_cost(study.baseline)
    missing=[]
    for name in ("cooling_capital_annual_gbp","recovery_capital_annual_gbp","recovery_aux_electricity_kwh_per_kg"):
        value=getattr(study,name)
        if value is None:
            missing.append(name)
        elif type(value) not in (int,float) or not isfinite(value) or value < 0:
            raise ValueError(name+" must be finite nonnegative")
    if missing:
        return {"status":"ABSTAIN_COST_DATA_MISSING","missing":missing,"baseline":base,
                "candidates":[],"advisory_only":True,"human_review_required":True}
    if len(study.cooling_options)*len(study.recovery_options)>100:
        raise ValueError("scenario search space too large")
    out=[]
    for cf in study.cooling_options:
        for rf in study.recovery_options:
            if not 0 <= cf <= 1 or not 0 <= rf <= 1:
                raise ValueError("fractions outside 0..1")
            b=study.baseline
            values=asdict(b)
            values["cooling_fraction"]=cf
            values["recovered_vapour_fraction"]=rf
            values["annualised_equipment_cost_gbp"]= (
                b.annualised_equipment_cost_gbp +
                (study.cooling_capital_annual_gbp if cf else 0) +
                (study.recovery_capital_annual_gbp if rf else 0)
            )
            v=evaluate_cost(CostInputs(**values))
            aux_kwh=(v["gross_vapour_equivalent_kg"]*rf*study.recovery_aux_electricity_kwh_per_kg)
            total=v["total_modelled_cost_gbp"]+aux_kwh*b.electricity_gbp_kwh
            out.append({
                "cooling_fraction":cf,"recovery_fraction":rf,"modelled_total_gbp":total,
                "savings_vs_baseline_gbp":base["total_modelled_cost_gbp"]-total,
                "cooling_electricity_kwh":v["cooling_electricity_kwh"],
                "recovery_aux_electricity_kwh":aux_kwh,
                "assumptions":"Provisional engineering-economic research; cannot actuate or override safety",
            })
    out.sort(key=lambda c:(c["modelled_total_gbp"],c["cooling_fraction"],c["recovery_fraction"]))
    return {"status":"RESEARCH_RANKING_NOT_OPERATING_ADVICE","candidates":out,
            "baseline":base,"uncertainty":"Capital annualisation, turn-down efficiency, phase control, recovery losses and availability are unvalidated",
            "human_review_required":True,"advisory_only":True}
