"""Two-phase, well-mixed, rigid LH2 tank control-volume screening model.

Heat input changes internal energy; venting is NEVER assumed to be lossless or
automatically commanded. The model holds a fixed geometric volume and solves
for saturation pressure and quality from conserved mass and internal energy.
It neglects stratification, ortho/para conversion heat, wall thermal inertia,
heat leaks through penetrations, liquid withdrawal, vent valves and relief design.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite

from .properties import HydrogenProperties, PropertyDomainError, SaturationState, MIN_PRESSURE_PA, MAX_PRESSURE_PA


@dataclass(frozen=True)
class TankInput:
    volume_m3: float = 100.0
    fill_liquid_volume_fraction: float = 0.84
    initial_pressure_pa: float = 101325.0
    heat_ingress_w: float = 700.0
    cooling_duty_w: float = 0.0
    cooling_cop: float = 0.04
    duration_hours: float = 12.0
    steps: int = 24
    spin: str = "para"


@dataclass(frozen=True)
class TankPoint:
    hour: float
    pressure_pa: float
    temperature_k: float
    vapour_quality_mass_fraction: float
    liquid_mass_kg: float
    vapour_mass_kg: float
    total_internal_energy_j: float
    saturation_margin_k: float = 0.0  # two-phase equilibrium, NOT a safety margin


@dataclass(frozen=True)
class TankRun:
    model: str
    status: str
    input: dict
    eos_version: str
    provenance: str
    initial_mass_kg: float
    net_heat_j: float
    refrigeration_electricity_kwh: float
    points: list[dict]
    limitations: list[str]


def _bounded(name: str, x: float, lower: float, upper: float) -> None:
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x) or not lower <= x <= upper:
        raise PropertyDomainError(f"{name} must lie within [{lower}, {upper}]")


def _quality(mass_kg: float, volume_m3: float, s: SaturationState) -> float:
    specific_volume = volume_m3 / mass_kg
    return (specific_volume - 1.0 / s.rho_liquid_kg_m3) / (
        1.0 / s.rho_vapour_kg_m3 - 1.0 / s.rho_liquid_kg_m3
    )


def _state_at_pressure(
    p: float, mass_kg: float, internal_energy_j: float, volume_m3: float, eos: HydrogenProperties
):
    s = eos.saturation(p)
    x = _quality(mass_kg, volume_m3, s)
    if not 0 <= x <= 1:
        return None
    u_pred = mass_kg * (s.u_liquid_j_kg * (1 - x) + s.u_vapour_j_kg * x)
    return u_pred - internal_energy_j, x, s


def _equilibrium(
    mass_kg: float, total_u_j: float, volume_m3: float, eos: HydrogenProperties
) -> tuple[SaturationState, float]:
    """Bracket and bisect the energy residual inside the two-phase region."""
    previous = None
    # More samples near the lower pressure, where saturated properties change faster.
    for i in range(49):
        p = MIN_PRESSURE_PA * (MAX_PRESSURE_PA / MIN_PRESSURE_PA) ** (i / 48)
        point = _state_at_pressure(p, mass_kg, total_u_j, volume_m3, eos)
        if point is None:
            continue
        residual, x, s = point
        if abs(residual) < max(1.0, abs(total_u_j) * 1e-9):
            return s, x
        if previous is not None and (residual > 0) != (previous[1] > 0):
            lo, hi = previous[0], p
            vlo = previous[1]
            for _ in range(45):
                mid = (lo + hi) * 0.5
                candidate = _state_at_pressure(mid, mass_kg, total_u_j, volume_m3, eos)
                if candidate is None:
                    raise PropertyDomainError("two-phase bracket left admissible state")
                v, x, s = candidate
                if abs(v) < max(1.0, abs(total_u_j) * 1e-10):
                    return s, x
                if (v > 0) == (vlo > 0):
                    lo, vlo = mid, v
                else:
                    hi = mid
            return s, x
        previous = (p, residual)
    raise PropertyDomainError(
        "No well-mixed two-phase equilibrium found in the bounded EOS region; "
        "phase transition, pressure limit or assumptions may be invalid"
    )


def simulate_tank(spec: TankInput) -> TankRun:
    _bounded("volume_m3", spec.volume_m3, 0.01, 100_000)
    _bounded("fill_liquid_volume_fraction", spec.fill_liquid_volume_fraction, 0.03, 0.97)
    _bounded("initial_pressure_pa", spec.initial_pressure_pa, MIN_PRESSURE_PA, 500_000)
    _bounded("heat_ingress_w", spec.heat_ingress_w, 0, 250_000)
    _bounded("cooling_duty_w", spec.cooling_duty_w, 0, 250_000)
    _bounded("cooling_cop", spec.cooling_cop, 0.001, 0.25)
    _bounded("duration_hours", spec.duration_hours, 0.01, 72)
    if isinstance(spec.steps, bool) or not isinstance(spec.steps, int) or not 1 <= spec.steps <= 144:
        raise PropertyDomainError("steps must be an integer from 1 to 144")
    eos = HydrogenProperties(spec.spin)
    init = eos.saturation(spec.initial_pressure_pa)
    f = spec.fill_liquid_volume_fraction
    lm = f * spec.volume_m3 * init.rho_liquid_kg_m3
    vm = (1 - f) * spec.volume_m3 * init.rho_vapour_kg_m3
    mass = lm + vm
    initial_u = lm * init.u_liquid_j_kg + vm * init.u_vapour_j_kg
    net_w = spec.heat_ingress_w - min(spec.cooling_duty_w, spec.heat_ingress_w)
    points = [TankPoint(
        hour=0, pressure_pa=spec.initial_pressure_pa,
        temperature_k=init.temperature_k, vapour_quality_mass_fraction=vm / mass,
        liquid_mass_kg=lm, vapour_mass_kg=vm,
        total_internal_energy_j=initial_u
    )]
    u = initial_u
    dt_s = spec.duration_hours * 3600 / spec.steps
    for i in range(1, spec.steps + 1):
        u += net_w * dt_s
        state, quality = _equilibrium(mass, u, spec.volume_m3, eos)
        points.append(TankPoint(
            hour=spec.duration_hours * i / spec.steps,
            pressure_pa=state.pressure_pa, temperature_k=state.temperature_k,
            vapour_quality_mass_fraction=quality,
            liquid_mass_kg=mass * (1 - quality),
            vapour_mass_kg=mass * quality,
            total_internal_energy_j=u,
        ))
    actual_cooling_w = min(spec.cooling_duty_w, spec.heat_ingress_w)
    return TankRun(
        model="rigid-tank-well-mixed-two-phase-v0.2",
        status="SIMULATED_NOT_VALIDATED_FOR_OPERATIONS",
        input=asdict(spec),
        eos_version=eos.version,
        provenance="Leachman 2009 DOI:10.1063/1.3160306 / CoolProp " + eos.version,
        initial_mass_kg=mass,
        net_heat_j=net_w * spec.duration_hours * 3600,
        refrigeration_electricity_kwh=actual_cooling_w * spec.duration_hours / (spec.cooling_cop * 1000),
        points=[asdict(p) for p in points],
        limitations=[
            "Closed rigid tank only; no relief/vent, filling, liquid withdrawal or pressure control",
            "Ideal well-mixed phase equilibrium; no stratification, wall inertia or ortho/para conversion",
            "Pressure is a simulated state, not an allowable operating pressure",
            "Must be benchmarked against measured experiments before engineering decisions",
            "No industrial equipment may be controlled from these outputs",
        ],
    )
