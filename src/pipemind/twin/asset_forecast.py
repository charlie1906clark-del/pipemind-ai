"""Forecast historical *replay* only, with cadence and provenance gates.

Never use this as a live pressure, temperature or hydrogen safety alarm.
"""
from __future__ import annotations

from datetime import datetime, timezone
from math import isfinite
from statistics import median

from .forecast import forecast
from .telemetry import METRICS


def replay_forecast(
    observations: list[dict], metric: str, horizon_samples: int = 1
) -> dict:
    if metric not in METRICS:
        raise ValueError("unknown metric")
    if not 1 <= horizon_samples <= 24:
        raise ValueError("invalid horizon")
    if len(observations) < 12:
        return {"status":"INSUFFICIENT_DATA","record_count":len(observations),
                "reason":"At least 12 quality-gated regularly spaced samples needed",
                "live_operational":False}
    if len(observations) > 2000:
        raise ValueError("too many samples")

    expected_unit = METRICS[metric][0]
    times = []
    values = []
    sources = set()
    for row in observations:
        if row.get("unit") != expected_unit or row.get("source") not in ("simulated","operator-import"):
            return {"status":"UNTRUSTED_OR_MIXED_UNITS","live_operational":False}
        sources.add(row["source"])
        value = row.get("value")
        if type(value) not in (int,float) or not isfinite(value):
            return {"status":"INVALID_SAMPLE","live_operational":False}
        try:
            when = datetime.fromisoformat(row["measured_at"].replace("Z","+00:00"))
            if when.tzinfo is None:
                raise ValueError("timezone missing")
            times.append(when.astimezone(timezone.utc))
        except (KeyError, TypeError, ValueError, OverflowError):
            return {"status":"INVALID_TIMESTAMP","live_operational":False}
        values.append(float(value))
    if len(sources) != 1:
        return {"status":"MULTIPLE_DATA_PROVENANCES","live_operational":False}
    deltas = [(b-a).total_seconds() for a,b in zip(times,times[1:])]
    if not deltas or min(deltas)<=0:
        return {"status":"NON_MONOTONIC_OR_DUPLICATE_TIMESTAMPS","live_operational":False}
    cadence=median(deltas)
    if any(abs(d-cadence) > max(1.0,cadence*0.1) for d in deltas):
        return {"status":"IRREGULAR_SAMPLING","median_sample_interval_s":cadence,
                "live_operational":False,"reason":"Resample/quality-review source intervals before forecasting"}
    result=forecast(values,horizon_samples).to_dict()
    return {
        **result,
        "source":next(iter(sources)), "unit":expected_unit,
        "reference_time_utc":times[-1].isoformat(),
        "expected_sampling_interval_s":cadence,
        "prediction_time_utc":(times[-1].timestamp()+cadence*horizon_samples),
        "live_operational":False,
        "usage":"Historical offline replay for scientific validation only",
    }
