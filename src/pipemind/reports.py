"""Traceable plain-text engineering *draft* report, never an audit certification."""
from __future__ import annotations
from datetime import datetime, timezone
from hashlib import sha256
from json import dumps
from typing import Any

def draft_report(run_id: str, kind: str, model: dict[str,Any], review: dict[str,Any]) -> str:
    digest=sha256(dumps(model,sort_keys=True,allow_nan=False).encode()).hexdigest()
    evidence=review.get("evidence",[])
    limitations=model.get("limitations",model.get("excluded_costs",[]))
    out=[
        "# PipeMind AI — Research Simulation Report",
        "",
        f"- Run ID: `{run_id}`",
        f"- Generated UTC: {datetime.now(timezone.utc).isoformat()}",
        f"- Model: {kind}",
        "- Status: **RESEARCH DRAFT — NOT APPROVED FOR OPERATIONAL USE**",
        f"- Input/output SHA256: `{digest}`",
        "",
        "## Results",
        "",
        "```json",
        dumps(model,indent=2,sort_keys=True,allow_nan=False),
        "```",
        "",
        "## Engineering restrictions",
        "",
        *[f"- {item}" for item in limitations],
        "- Not a regulatory compliance certificate, safety determination, control instruction or as-built design.",
        "",
        "## Review findings",
        "",
        *[f"- **{x['role']}** / {x['verdict']}: {x['detail']}" for x in review.get("checks",[])],
        "",
        "## Bibliography (source-checked; not model validation)",
        "",
        *[f"- {e['id']}: {e['title']}. {e['source_url']}; {e['limitations']}" for e in evidence],
        "",
        "## Sign-off",
        "",
        "- Reviewer: NOT SIGNED",
        "- Calibration / field validation: NOT PROVIDED",
        "- Engineering approval: NOT GRANTED",
    ]
    return "\n".join(out)+"\n"
