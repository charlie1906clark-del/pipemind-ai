"""Curated research evidence bridge to an independent APEX webhook.

No automatic execution, no Wong private memory and no operational telemetry.
Caller must supply a separate PIPEMIND_PUBLIC_RESEARCH signing secret and configure
an APEX pipeline/marking; NEVER reuse Wong's BRAIN_SYNC key or JWKS signing keys.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import re
import time
from dataclasses import asdict
from urllib.parse import urlsplit

import httpx

from pipemind.evidence import load_evidence, evidence_checksum


class ApexBridgeError(ValueError):
    """Cannot send due to missing permission, configuration or trust."""


def curated_snapshot(ids: list[str], reviewed_by: str, *, allow_publish: bool = False) -> dict:
    """Export only checked public bibliographic facts; manual opt-in required."""
    if not allow_publish:
        raise ApexBridgeError("publication requires explicit human approval")
    if not isinstance(reviewed_by, str) or not re.fullmatch(r"[A-Za-z0-9_.@-]{3,80}", reviewed_by):
        raise ApexBridgeError("reviewer ID missing or invalid")
    if not ids or len(ids)>40 or len(set(ids))!=len(ids):
        raise ApexBridgeError("1..40 unique claim IDs required")
    catalog={c.id:c for c in load_evidence()}
    records=[]
    for claim_id in ids:
        claim=catalog.get(claim_id)
        if claim is None or claim.status!="source_checked" or claim.evidence_tier.startswith(("assumption","hypothesis")):
            raise ApexBridgeError("claim is not source-checked and exportable")
        records.append({
            "uid":claim.id,"title":claim.title,
            "claim":claim.claim,"source_url":claim.source_url,"doi":claim.doi,
            "evidence_tier":claim.evidence_tier,"limitations":claim.limitations,
            "source_checked":True,"markings":["PIPEMIND_REVIEWED_PUBLIC"],
        })
    return {
        "schema":"pipemind-apex-evidence-v1",
        "source":"pipemind-ai",
        "approved_by":reviewed_by,
        "evidence_manifest_sha256":evidence_checksum(),
        "records":records,
        "warning":"Bibliographic verification only; no safety, engineering or plant certification",
    }


def signed_headers(secret: str, body: bytes, delivery_id: str, timestamp: int | None = None) -> dict[str,str]:
    if not isinstance(secret,str) or len(secret)<32:
        raise ApexBridgeError("distinct high-entropy APEX webhook key required (>=32 chars)")
    if not isinstance(delivery_id,str) or not re.fullmatch(r"[a-zA-Z0-9_.:-]{8,120}",delivery_id):
        raise ApexBridgeError("invalid delivery identifier")
    stamp=str(int(time.time()) if timestamp is None else timestamp)
    signature=hmac.new(secret.encode(),stamp.encode()+b"."+body,hashlib.sha256).hexdigest()
    return {
        "Content-Type":"application/json",
        "X-Apex-Timestamp":stamp,
        "X-Apex-Signature":"v1="+signature,
        "X-Apex-Delivery-Id":delivery_id,
    }


async def deliver_curated_snapshot(
    *, apex_origin: str, pipeline: str, secret: str,
    snapshot: dict, delivery_id: str, transport: httpx.AsyncBaseTransport | None = None
) -> dict:
    """Opt-in signed delivery; requires a PIPEMIND-only ingestion pipeline at APEX."""
    parsed=urlsplit(apex_origin)
    if parsed.scheme!="https" or not parsed.hostname or parsed.username or parsed.password:
        raise ApexBridgeError("APEX requires secure HTTPS origin")
    if parsed.path not in ("","/") or parsed.query or parsed.fragment:
        raise ApexBridgeError("APEX URL must be an origin, not an arbitrary target")
    if pipeline!="pipemind.reviewed-public-evidence":
        raise ApexBridgeError("only dedicated PipeMind reviewed research pipeline is allowed")
    if snapshot.get("schema")!="pipemind-apex-evidence-v1":
        raise ApexBridgeError("unexpected snapshot schema")
    records=snapshot.get("records")
    if not isinstance(records,list) or not 1<=len(records)<=40:
        raise ApexBridgeError("snapshot contains no approved records")
    approved_ids={card.id for card in load_evidence() if card.status=="source_checked"}
    for record in records:
        if not isinstance(record,dict) or set(record)-{
            "uid","title","claim","source_url","doi","evidence_tier",
            "limitations","source_checked","markings"
        } or record.get("uid") not in approved_ids or record.get("markings")!=["PIPEMIND_REVIEWED_PUBLIC"]:
            raise ApexBridgeError("unapproved research card or unexpected field")
    body=json.dumps(snapshot,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    if len(body)>100000:
        raise ApexBridgeError("research packet exceeds size limit")
    headers=signed_headers(secret,body,delivery_id)
    async with httpx.AsyncClient(
        base_url=apex_origin.rstrip("/"),timeout=8,transport=transport,
        follow_redirects=False,trust_env=False
    ) as client:
        try:
            response=await client.post(
                "/api/v1/ingest/webhooks/pipemind.reviewed-public-evidence",
                content=body,headers=headers
            )
        except httpx.HTTPError as exc:
            raise ApexBridgeError("APEX delivery failed: transport error") from exc
    if response.status_code!=202:
        raise ApexBridgeError(f"APEX did not accept snapshot (HTTP {response.status_code})")
    result=response.json()
    return {"accepted":True,"delivery_id":delivery_id,"apex_run":str(result.get("run_id","")),
            "warning":"HTTP 202 only queues ingestion; verify APEX worker, records and permissions separately"}
