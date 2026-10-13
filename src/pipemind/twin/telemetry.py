"""Safety-neutral data quality checks; never infer a facility is safe.

All input records carry source, UTC timestamp and data-quality annotations.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone, timedelta
from math import isfinite
from statistics import median
from typing import Iterable

METRICS = {
    "pressure_pa": ("Pa", 0, 5_000_000),
    "temperature_k": ("K", 0, 500),
    "liquid_fill_fraction": ("fraction", 0, 1),
    "mass_flow_kg_s": ("kg/s", 0, 1000),
    "heat_ingress_w": ("W", 0, 5e6),
    "refrigeration_power_w": ("W", 0, 5e6),
}
QUALITY_FLAGS = {
    "ACCEPTED", "OUT_OF_RANGE", "STALE", "FUTURE_TIMESTAMP", "DUPLICATE",
    "INVALID_UNIT", "UNTRUSTED_SOURCE", "SPIKE", "INSUFFICIENT_CONTEXT",
}


@dataclass(frozen=True)
class Observation:
    asset_id: str
    measured_at: str
    metric: str
    value: float
    unit: str
    source: str = "simulated"
    quality: str = "ACCEPTED"
    lineage: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class QualityResult:
    accepted: tuple[Observation, ...]
    rejected: tuple[dict, ...]
    counts: dict

    def to_dict(self) -> dict:
        return {
            "accepted": [x.to_dict() for x in self.accepted],
            "rejected": list(self.rejected),
            "counts": self.counts,
        }


def check_batch(
    raw: Iterable[dict], *, now: datetime | None = None,
    trusted_sources: tuple[str, ...] = ("simulated", "operator-import", "signed-gateway"),
    history: dict[tuple[str, str], list[float]] | None = None,
) -> QualityResult:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    accepted: list[Observation] = []
    rejected: list[dict] = []
    seen: set[tuple] = set()
    prior = {k: list(v) for k, v in (history or {}).items()}
    raw_list = list(raw)
    if len(raw_list) > 500:
        raise ValueError("maximum 500 observations per batch")
    for idx, item in enumerate(raw_list):
        flags: list[str] = []
        metric = item.get("metric", "")
        value = item.get("value")
        asset = item.get("asset_id", "")
        source = item.get("source", "")
        unit = item.get("unit", "")
        ts = item.get("measured_at", "")
        if metric not in METRICS:
            flags.append("INVALID_METRIC")
        else:
            expected, lo, hi = METRICS[metric]
            if unit != expected:
                flags.append("INVALID_UNIT")
            if type(value) not in (int, float) or not isfinite(value) or not lo <= value <= hi:
                flags.append("OUT_OF_RANGE")
        if not isinstance(asset, str) or not asset or len(asset) > 64 or not all(c.isalnum() or c in "-_." for c in asset):
            flags.append("INVALID_ASSET")
        if source not in trusted_sources:
            flags.append("UNTRUSTED_SOURCE")
        try:
            when = datetime.fromisoformat(ts.replace("Z", "+00:00")) if isinstance(ts, str) else None
            if when is None or when.tzinfo is None:
                raise ValueError
            when = when.astimezone(timezone.utc)
            if when > now + timedelta(minutes=5):
                flags.append("FUTURE_TIMESTAMP")
            if when < now - timedelta(days=31):
                flags.append("STALE")
        except (ValueError, OverflowError):
            when = None
            flags.append("INVALID_TIMESTAMP")
        key = (asset, metric, when)
        if key in seen:
            flags.append("DUPLICATE")
        seen.add(key)
        if not flags:
            readings = prior.get((asset, metric), [])
            if len(readings) >= 5:
                center = median(readings[-25:])
                mad = median(abs(r-center) for r in readings[-25:])
                if mad > 1e-12 and abs(value - center) > max(8 * 1.4826 * mad, 0.05 * max(abs(center), 1)):
                    flags.append("SPIKE")
            if not flags:
                prior.setdefault((asset, metric), []).append(value)
                accepted.append(Observation(
                    asset_id=asset, measured_at=when.isoformat(),
                    metric=metric, value=float(value), unit=unit,
                    source=source, lineage=str(item.get("lineage", ""))[:200]
                ))
        if flags:
            rejected.append({"index": idx, "asset_id": asset, "metric": metric, "flags": sorted(set(flags))})
    return QualityResult(
        accepted=tuple(accepted), rejected=tuple(rejected),
        counts={"received": len(raw_list), "accepted": len(accepted), "rejected": len(rejected)}
    )
