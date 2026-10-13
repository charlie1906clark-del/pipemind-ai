"""Source-constrained experimental input registry for cross-lab validation.

A reference case is not a validated numerical benchmark until measured pressure
or temperature time series, calibration metadata and pre-agreed acceptance
tolerances are supplied and compared independently.
"""
from __future__ import annotations

import json
from pathlib import Path


def load_reference_cases() -> dict:
    path = Path(__file__).with_name("nasa_cases.json")
    registry = json.loads(path.read_text(encoding="utf-8"))
    if registry.get("schema")!="pipemind-experimental-anchors-v1" or not registry.get("source_url"):
        raise ValueError("invalid experiment registry")
    tanks={t["id"]:t for t in registry["tanks"]}
    if len(tanks)!=2 or len(registry["cases"])!=5:
        raise ValueError("reference-case registry inconsistent")
    unique=set()
    for case in registry["cases"]:
        if case["id"] in unique or case["tank_id"] not in tanks:
            raise ValueError("duplicate case or unknown reference tank")
        unique.add(case["id"])
        for field in ("fill_fraction","initial_pressure_pa","total_heat_w","duration_hours"):
            if type(case[field]) not in (float,int) or case[field] <= 0:
                raise ValueError("invalid experiment numeric input")
        if case["fill_fraction"]>=1:
            raise ValueError("invalid reported tank filling")
    return registry


def prepare_screening_input(case_id: str, *, spin: str="para") -> dict:
    """Prepare *approximate* research inputs, not an experimental replication."""
    registry=load_reference_cases()
    chosen=next((c for c in registry["cases"] if c["id"]==case_id),None)
    if not chosen:
        raise ValueError("unknown NASA reference case")
    tank=next(t for t in registry["tanks"] if t["id"]==chosen["tank_id"])
    return {
        "status":"PUBLISHED_BOUNDARIES_REQUIRING_EXPERIMENTAL_VALIDATION",
        "case_id":chosen["id"],
        "source_url":registry["source_url"],
        "tank_input":{
            "volume_m3":tank["volume_m3"],
            "fill_liquid_volume_fraction":chosen["fill_fraction"],
            "initial_pressure_pa":chosen["initial_pressure_pa"],
            "heat_ingress_w":chosen["total_heat_w"],
            "cooling_duty_w":0.0,
            "duration_hours":chosen["duration_hours"],
            "spin":spin,
        },
        "assumptions":[
            "Liquid hydrogen model takes all published heat as constant homogeneous internal heat",
            "Tank and vapour initially at saturation, not the measured stratified K-Site temperature field",
            "Reference publication does not establish exact ortho/para composition of this PipeMind calculation",
            "Published measured pressure time series not incorporated or benchmarked",
            "Two-phase equilibrium approximation is NOT the referenced CFD model",
        ],
        "experimental_time_series_available":False,
        "validated":False,
    }
