"""Transparent trend forecasts with backtest and abstention (not certified alarms)."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from math import isfinite, sqrt
from statistics import mean
from typing import Sequence


@dataclass(frozen=True)
class Forecast:
    status: str
    next_value: float | None
    interval_low: float | None
    interval_high: float | None
    horizon_samples: int
    backtest_mae: float | None
    persistence_mae: float | None
    beats_baseline: bool
    sample_count: int
    limitations: tuple[str, ...]

    def to_dict(self) -> dict:
        return asdict(self)


def _line_fit(values: Sequence[float]) -> tuple[float, float]:
    n = len(values)
    xmean = (n - 1) / 2
    ymean = mean(values)
    denom = sum((i-xmean)**2 for i in range(n))
    slope = sum((i-xmean)*(y-ymean) for i, y in enumerate(values)) / denom if denom else 0
    return ymean - slope*xmean, slope


def forecast(values: Sequence[float], horizon_samples: int = 1) -> Forecast:
    if not 1 <= horizon_samples <= 24:
        raise ValueError("horizon_samples must be in 1..24")
    if len(values) > 2000:
        raise ValueError("maximum 2000 data points")
    if any(type(v) not in (int, float) or not isfinite(v) for v in values):
        raise ValueError("values must be finite numbers")
    n = len(values)
    missing = ("No forecast or recommendation when fewer than 12 validated observations exist",)
    if n < 12:
        return Forecast("INSUFFICIENT_DATA", None, None, None, horizon_samples, None, None, False, n, missing)
    # Rolling-origin evaluation without training on held-out target points.
    window = min(24, max(6, n // 3))
    errors: list[float] = []
    baseline_errors: list[float] = []
    for i in range(window, n - horizon_samples + 1):
        history = values[max(0, i-window):i]
        a, slope = _line_fit(history)
        estimated = a + slope*(len(history)-1+horizon_samples)
        actual = values[i+horizon_samples-1]
        errors.append(abs(actual-estimated))
        baseline_errors.append(abs(actual-history[-1]))
    if len(errors) < 3:
        return Forecast("INSUFFICIENT_BACKTEST", None, None, None, horizon_samples, None, None, False, n, ("Need at least 3 holdout windows",))
    trend_mae = mean(errors)
    persistence_mae = mean(baseline_errors)
    a, slope = _line_fit(values[-window:])
    estimate = a + slope*(window-1+horizon_samples)
    # Intervals are descriptive holdout-error bands, NOT statistically calibrated confidence bounds.
    band = max(sorted(errors)[round((len(errors)-1)*0.9)], 0.00001)
    passes = trend_mae < persistence_mae * 0.98
    return Forecast(
        status="RESEARCH_TREND_ONLY" if passes else "BASELINE_PREFERRED",
        next_value=estimate if passes else float(values[-1]),
        interval_low=(estimate if passes else values[-1])-band,
        interval_high=(estimate if passes else values[-1])+band,
        horizon_samples=horizon_samples,
        backtest_mae=trend_mae, persistence_mae=persistence_mae,
        beats_baseline=passes, sample_count=n,
        limitations=(
            "Only regular-interval, unit-consistent, quality-checked observations",
            "Simple linear trend compared to persistence on rolling holdout; no trained neural model",
            "Historical error band is descriptive, not a calibrated prediction interval",
            "Not a safety alert, pressure relief design or equipment instruction",
        ),
    )
