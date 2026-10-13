"""Single-phase, steady 1-D liquid-hydrogen line screening.

Does not rate MgB2 conductor, assess HV insulation, or predict a quench.
The fluid must remain subcooled at every integration step. Reject otherwise.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite, log10, pi

from .properties import HydrogenProperties, PropertyDomainError


@dataclass(frozen=True)
class CableInput:
    length_m: float = 1000.0
    inner_diameter_m: float = 0.12
    absolute_roughness_m: float = 0.00001
    mass_flow_kg_s: float = 0.8
    inlet_temperature_k: float = 19.0
    inlet_pressure_pa: float = 240000.0
    heat_ingress_w_per_m: float = 1.0
    residual_electrical_heat_w_per_m: float = 0.0
    elevation_gain_m: float = 0.0
    steps: int = 40
    spin: str = "para"


@dataclass(frozen=True)
class CableRun:
    model: str
    status: str
    input: dict
    eos_version: str
    outlet_temperature_k: float
    outlet_pressure_pa: float
    minimum_saturation_margin_k: float
    heat_load_w: float
    points: list[dict]
    limitations: list[str]


def _within(name: str, x: float, low: float, high: float) -> None:
    if isinstance(x, bool) or not isinstance(x, (float, int)) or not isfinite(x) or not low <= x <= high:
        raise PropertyDomainError(f"{name} must lie within [{low}, {high}]")


def simulate_cable(spec: CableInput) -> CableRun:
    for name, low, high in (
        ("length_m", 1, 50_000), ("inner_diameter_m", 0.01, 2),
        ("mass_flow_kg_s", 0.01, 100), ("inlet_temperature_k", 15, 28),
        ("inlet_pressure_pa", 50_000, 600_000),
        ("heat_ingress_w_per_m", 0, 50),
        ("residual_electrical_heat_w_per_m", 0, 100),
        ("absolute_roughness_m", 0, 0.01),
        ("elevation_gain_m", -1000, 1000),
    ):
        _within(name, getattr(spec, name), low, high)
    if spec.absolute_roughness_m >= spec.inner_diameter_m / 10:
        raise PropertyDomainError("unrealistic roughness relative to inner diameter")
    if type(spec.steps) is not int or not 2 <= spec.steps <= 240:
        raise PropertyDomainError("steps must be an integer between 2 and 240")
    eos = HydrogenProperties(spec.spin)
    p = spec.inlet_pressure_pa
    t = spec.inlet_temperature_k
    ds = spec.length_m / spec.steps
    area = pi * spec.inner_diameter_m ** 2 / 4
    total_heat_w = (spec.heat_ingress_w_per_m + spec.residual_electrical_heat_w_per_m) * spec.length_m
    points = []
    min_margin = float("inf")
    for i in range(spec.steps + 1):
        fluid = eos.state_liquid(t, p)
        margin = fluid["saturation_margin_k"]
        if margin <= 0.1:
            raise PropertyDomainError("subcooling margin <= 0.1 K; stop model before phase boundary")
        min_margin = min(margin, min_margin)
        points.append({
            "metres": round(i * ds, 6), "temperature_k": t,
            "pressure_pa": p, "saturation_margin_k": margin,
        })
        if i == spec.steps:
            break
        rho = fluid["density_kg_m3"]
        viscosity = fluid["viscosity_pa_s"]
        v = spec.mass_flow_kg_s / (rho * area)
        re = rho * v * spec.inner_diameter_m / viscosity
        if re <= 0:
            raise PropertyDomainError("nonphysical Reynolds number")
        friction = 64 / re if re < 2300 else 0.25 / (
            log10(spec.absolute_roughness_m / (3.7 * spec.inner_diameter_m)
                  + 5.74 / re ** 0.9) ** 2
        )
        dp_friction = friction * (ds / spec.inner_diameter_m) * rho * v * v / 2
        dp_gravity = rho * 9.80665 * spec.elevation_gain_m / spec.steps
        p_next = p - dp_friction - dp_gravity
        h_next = fluid["enthalpy_j_kg"] + (
            spec.heat_ingress_w_per_m + spec.residual_electrical_heat_w_per_m
        ) * ds / spec.mass_flow_kg_s
        if p_next < 30_000 or p_next > 650_000:
            raise PropertyDomainError("predicted pressure exits bounded fluid domain")
        try:
            from CoolProp.CoolProp import PropsSI
            t_next = PropsSI("T", "P", p_next, "Hmass", h_next, eos.fluid)
        except (ValueError, OverflowError) as exc:
            raise PropertyDomainError("cannot resolve next liquid enthalpy state") from exc
        if not isfinite(t_next):
            raise PropertyDomainError("non-finite fluid temperature")
        p, t = p_next, t_next
    return CableRun(
        model="steady-1d-single-phase-LH2-screening-v0.1",
        status="SIMULATED_NOT_VALIDATED_FOR_OPERATIONS",
        input=asdict(spec), eos_version=eos.version,
        outlet_temperature_k=t, outlet_pressure_pa=p,
        minimum_saturation_margin_k=min_margin,
        heat_load_w=total_heat_w, points=points,
        limitations=[
            "Single-phase steady flow only; fails closed near saturation",
            "No two-phase flow, quench, AC electromagnetic loss model or fault analysis",
            "MgB2 current capacity and insulation ratings NOT calculated",
            "Darcy friction with approximate turbulent correlation; not validated for a real cryostat",
            "Elevation distributed uniformly; joints, stations and fittings not included",
        ],
    )
