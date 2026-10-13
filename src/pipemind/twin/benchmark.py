"""Traceable, offline measured-vs-simulated tank pressure validation.

This is the bridge toward rigorous research experiments, *not* a claim of
pressure vessel operating safety or a certified cryogenic property model.
"""
from __future__ import annotations

from bisect import bisect_left
from datetime import datetime, timezone
from hashlib import sha256
from json import dumps
from math import isfinite, sqrt
from statistics import mean


def _timestamp(s: str) -> datetime:
    if not isinstance(s,str):
        raise ValueError("timestamp must be a string")
    try:
        t=datetime.fromisoformat(s.replace("Z","+00:00"))
    except (ValueError,OverflowError) as exc:
        raise ValueError("invalid ISO timestamp") from exc
    if t.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return t.astimezone(timezone.utc)


def _validate_simulation(run: dict) -> list[tuple[float,float]]:
    if run.get("status")!="SIMULATED_NOT_VALIDATED_FOR_OPERATIONS":
        raise ValueError("only traceable tank screening model runs are supported")
    points=run.get("points")
    if not isinstance(points,list) or not 2<=len(points)<=1000:
        raise ValueError("tank run needs ordered pressure points")
    sorted_points=[]
    for point in points:
        hour=point.get("hour")
        pressure=point.get("pressure_pa")
        if type(hour) not in (int,float) or type(pressure) not in (int,float):
            raise ValueError("invalid tank model point")
        if not isfinite(hour) or not isfinite(pressure) or hour<0 or pressure<=0:
            raise ValueError("nonphysical tank model point")
        if sorted_points and hour<=sorted_points[-1][0]:
            raise ValueError("simulator timestamps are not monotonic")
        sorted_points.append((float(hour),float(pressure)))
    return sorted_points


def _interpolate(points: list[tuple[float,float]], hour: float) -> float:
    hours=[p[0] for p in points]
    at=bisect_left(hours,hour)
    if at<len(points) and abs(hours[at]-hour)<1e-10:
        return points[at][1]
    if at==0 or at==len(points):
        raise ValueError("interpolation outside modelled period")
    x0,y0=points[at-1]
    x1,y1=points[at]
    return y0+(hour-x0)*(y1-y0)/(x1-x0)


def benchmark_tank_pressure(
    run: dict, observations: list[dict], *, model_start_utc: str
) -> dict:
    """Compute error only when ≥5 overlapping, single-source Pa samples exist."""
    points=_validate_simulation(run)
    model_start=_timestamp(model_start_utc)
    if len(observations)>2000:
        raise ValueError("too many observations")
    matches=[]
    skipped=0
    sources=set()
    for row in observations:
        if row.get("unit")!="Pa":
            raise ValueError("pressure observations must be in Pa")
        val=row.get("value")
        if type(val) not in (int,float) or not isfinite(val) or val<=0:
            raise ValueError("observed pressure must be finite and positive")
        source=row.get("source")
        if source not in ("simulated","operator-import"):
            raise ValueError("untrusted observation provenance")
        sources.add(source)
        hour=(_timestamp(row["measured_at"])-model_start).total_seconds()/3600
        if hour<points[0][0] or hour>points[-1][0]:
            skipped+=1
            continue
        matches.append((hour,float(val),_interpolate(points,hour)))
    if len(sources)!=1:
        raise ValueError("only one observation provenance per comparison")
    if len(matches)<5:
        return {
            "status":"ABSTAIN_INSUFFICIENT_OVERLAP","matched_samples":len(matches),
            "skipped_samples":skipped,"human_review_required":True,
            "reason":"Need at least five source-consistent pressure observations inside modelled time",
        }
    matches.sort(key=lambda x:x[0])
    if len({x[0] for x in matches})!=len(matches):
        raise ValueError("duplicate pressure observation timestamps")
    errors=[prediction-observed for _t,observed,prediction in matches]
    abs_errors=[abs(e) for e in errors]
    mae=mean(abs_errors)
    rmse=sqrt(mean(e*e for e in errors))
    bias=mean(errors)
    mean_obs=mean(x[1] for x in matches)
    mape=100*mean(abs((prediction-observed)/observed) for _t,observed,prediction in matches)
    source=next(iter(sources))
    digest=sha256(dumps({
        "start":model_start.isoformat(),"samples":matches,"kind":source,
        "model":run.get("model"),"eos":run.get("eos_version")
    },sort_keys=True,allow_nan=False).encode()).hexdigest()
    return {
        "status":"RESEARCH_BENCHMARK_NOT_CERTIFICATION",
        "model":run.get("model"),"eos_version":run.get("eos_version"),
        "source":source,"synthetic_validation_only":source=="simulated",
        "matched_samples":len(matches),"skipped_samples":skipped,
        "modelled_duration_hours":points[-1][0]-points[0][0],
        "comparison_span_hours":matches[-1][0]-matches[0][0],
        "mae_pa":mae,"rmse_pa":rmse,"bias_pa":bias,"mape_percent":mape,
        "mean_observed_pa":mean_obs,"evidence_sha256":digest,
        "human_review_required":True,
        "limits":[
            "No independent experimental validation implied by a synthetic trace",
            "No universal pass/fail tolerance: predefine acceptable error with independent cryogenics engineer",
            "Sensor calibration, tank construction, heat ingress and wall dynamics not validated by this error metric",
            "Do not use this benchmark to approve equipment operating limits or safety protection",
        ],
    }
