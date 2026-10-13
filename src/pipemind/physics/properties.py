"""Traceable CoolProp-backed hydrogen properties; SI units throughout.

Data basis: J.W. Leachman et al. (2009), DOI 10.1063/1.3160306,
as implemented by CoolProp (version returned with each run).
Different molecular hydrogen spin-state EOS are NOT interchangeable.
The finite domain below is a platform *screening* domain, not a design code.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import isfinite

try:
    import CoolProp
    from CoolProp.CoolProp import PropsSI, PhaseSI
except ImportError:  # fail closed if the optional numerical backend is unavailable
    CoolProp = None
    PropsSI = None
    PhaseSI = None

EOS_DOI = "10.1063/1.3160306"
MIN_PRESSURE_PA = 30_000.0
MAX_PRESSURE_PA = 650_000.0
FLUIDS = {"para": "ParaHydrogen", "normal": "Hydrogen", "ortho": "OrthoHydrogen"}


class PropertyDomainError(ValueError):
    """The available EOS or model cannot support a requested condition."""


@dataclass(frozen=True)
class SaturationState:
    pressure_pa: float
    temperature_k: float
    rho_liquid_kg_m3: float
    rho_vapour_kg_m3: float
    u_liquid_j_kg: float
    u_vapour_j_kg: float
    h_liquid_j_kg: float
    h_vapour_j_kg: float
    eos: str
    eos_version: str
    doi: str = EOS_DOI

    @property
    def latent_heat_j_kg(self) -> float:
        return self.h_vapour_j_kg - self.h_liquid_j_kg


def _positive(name: str, value: float, low: float, high: float) -> None:
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not isfinite(value):
        raise PropertyDomainError(f"{name} must be a finite number")
    if not low <= value <= high:
        raise PropertyDomainError(f"{name} outside bounded model domain [{low}, {high}]")


class HydrogenProperties:
    """Standalone EOS interface, no global mutation of reference states."""

    def __init__(self, spin: str = "para") -> None:
        if spin not in FLUIDS:
            raise PropertyDomainError("spin must be 'para', 'normal' or 'ortho'")
        if CoolProp is None:
            raise PropertyDomainError("CoolProp is required; install the simulation extra")
        self.spin = spin
        self.fluid = FLUIDS[spin]
        self.version = CoolProp.__version__

    def saturation(self, pressure_pa: float) -> SaturationState:
        _positive("pressure_pa", pressure_pa, MIN_PRESSURE_PA, MAX_PRESSURE_PA)
        return _saturation(self.fluid, self.version, round(pressure_pa, 4))

    def state_liquid(self, temperature_k: float, pressure_pa: float) -> dict:
        _positive("pressure_pa", pressure_pa, MIN_PRESSURE_PA, MAX_PRESSURE_PA)
        _positive("temperature_k", temperature_k, 15.0, 32.0)
        try:
            sat = self.saturation(pressure_pa)
            if temperature_k >= sat.temperature_k:
                raise PropertyDomainError("inlet is not safely within the subcooled liquid domain")
            phase = str(PhaseSI("T", temperature_k, "P", pressure_pa, self.fluid)).lower()
            if "liquid" not in phase and "supercritical" not in phase:
                raise PropertyDomainError(f"unsupported phase: {phase}")
            result = {
                "density_kg_m3": PropsSI("Dmass", "T", temperature_k, "P", pressure_pa, self.fluid),
                "enthalpy_j_kg": PropsSI("Hmass", "T", temperature_k, "P", pressure_pa, self.fluid),
                "viscosity_pa_s": PropsSI("V", "T", temperature_k, "P", pressure_pa, self.fluid),
                "temperature_k": temperature_k,
                "pressure_pa": pressure_pa,
                "saturation_margin_k": sat.temperature_k - temperature_k,
                "eos": self.fluid,
                "eos_version": self.version,
            }
            if not all(isfinite(result[k]) and result[k] > 0 for k in ("density_kg_m3", "viscosity_pa_s")):
                raise PropertyDomainError("EOS returned invalid liquid properties")
            return result
        except PropertyDomainError:
            raise
        except (ValueError, OverflowError) as exc:
            raise PropertyDomainError("EOS cannot resolve requested liquid state") from exc


@lru_cache(maxsize=8192)
def _saturation(fluid: str, version: str, pressure_pa: float) -> SaturationState:
    try:
        def prop(code: str, quality: int) -> float:
            value = float(PropsSI(code, "P", pressure_pa, "Q", quality, fluid))
            if not isfinite(value):
                raise PropertyDomainError("non-finite CoolProp result")
            return value

        return SaturationState(
            pressure_pa=pressure_pa, temperature_k=prop("T", 0),
            rho_liquid_kg_m3=prop("Dmass", 0), rho_vapour_kg_m3=prop("Dmass", 1),
            u_liquid_j_kg=prop("Umass", 0), u_vapour_j_kg=prop("Umass", 1),
            h_liquid_j_kg=prop("Hmass", 0), h_vapour_j_kg=prop("Hmass", 1),
            eos=fluid, eos_version=version,
        )
    except PropertyDomainError:
        raise
    except (ValueError, OverflowError) as exc:
        raise PropertyDomainError("CoolProp saturation calculation failed") from exc
