"""Run independent, bounded agent-role checks on a model output.

These are *implemented deterministic validators*, not LLMs or trained neural
agents. They produce a review pack to be interpreted by a human or a separately
deployed secure APEX AI assistant (with no control permissions).
"""
from __future__ import annotations
from hashlib import sha256
from json import dumps
from typing import Any

from pipemind.evidence import retrieve_verified, evidence_checksum


def compose_review(kind: str, payload: dict[str, Any], question: str = "") -> dict:
    if kind not in ("tank","cable","cost","trend","comparison"):
        raise ValueError("unsupported model kind")
    if not isinstance(payload,dict) or len(dumps(payload,allow_nan=False)) > 750000:
        raise ValueError("invalid or oversized model payload")
    if len(question) > 300:
        raise ValueError("question too long")
    checks=[]
    def check(role: str, verdict: str, detail: str):
        checks.append({"role":role,"verdict":verdict,"detail":detail})
    status=payload.get("status","")
    if kind in ("tank","cable"):
        status_expected="SIMULATED_NOT_VALIDATED_FOR_OPERATIONS"
        if status!=status_expected:
            raise ValueError("model status absent or inconsistent")
        limitations=payload.get("limitations",[])
        if not limitations or not isinstance(limitations,list):
            raise ValueError("mandatory modelling limitations absent")
        check("cryogenic_engineer","SCREENING_ONLY","EOS and conservation screening present; independent reference comparison not established.")
        check("hydrogen_safety_reviewer","REQUIRES_REVIEW","No equipment limit, operating setpoint, quench assessment or release consequence rating.")
        check("digital_twin_engineer","NO_SENSOR_PROOF","Simulation is not an observation. Compare with licensed, quality-gated field measurements.")
        if kind=="cable":
            check("superconducting_specialist","NO_RATING","No MgB2 Ic(T,B) derating, joint, fault or protection validation.")
    elif kind in ("cost","comparison"):
        check("optimization_analyst","SCENARIO_ONLY","Missing full CAPEX, liquid hydrogen upstream supply/recovery energy and site-specific operating data.")
        check("hydrogen_safety_reviewer","NOT_SAFETY_EVALUATED","Cost result does not establish safe/feasible physical interventions.")
    else:
        check("digital_twin_engineer","UNCALIBRATED","Backtest vs persistence alone is not a calibrated plant predictor.")
        check("hydrogen_safety_reviewer","NOT_A_SAFETY_ALARM","Forecast cannot trigger or replace plant independent alarms.")
    evidence=retrieve_verified(question or kind,limit=6)
    check("research_verifier","SOURCE_LINKED_NOT_FIELD_VALIDATED",
          "Retrieved source-checked primary literature and standards, but no published test benchmark of this exact model.")
    digest=sha256(dumps(payload,sort_keys=True,allow_nan=False,separators=(",",":")).encode()).hexdigest()
    return {
        "kind":kind,"status":"ADVISORY_DRAFT_REQUIRES_HUMAN_REVIEW",
        "human_review_required":True,"industrial_actuation":False,
        "input_payload_sha256":digest,"evidence_manifest_sha256":evidence_checksum(),
        "checks":checks,"evidence":evidence,
        "open_questions":[
            "Is this the correct property and physical regime for the equipment?",
            "Which measured dataset independently tests these predictions?",
            "What are the operator-approved equipment and site constraints?",
            "Which omitted costs or failure modes could reverse the conclusion?"
        ],
        "next_step":"Independent cryogenic/process engineering review and a scoped synthetic or read-only customer pilot."
    }
