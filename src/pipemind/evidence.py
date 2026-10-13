"""Curated evidence claims distinct from raw Obsidian notes and model assumptions."""
from __future__ import annotations
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

_DATA = Path(__file__).with_name("evidence_claims.json")
_VALID = {"primary_published_model", "primary_project_plan", "primary_government_guidance", "primary_intergovernmental_report",
          "technical_software_documentation", "vendor_claim", "assumption", "hypothesis"}


@dataclass(frozen=True)
class Evidence:
    id: str
    module: str
    title: str
    claim: str
    source_url: str
    evidence_tier: str
    status: str
    limitations: str
    doi: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def load_evidence(path: Path | None = None) -> list[Evidence]:
    source = path or _DATA
    loaded = json.loads(source.read_text(encoding="utf-8"))
    if loaded.get("schema") != "pipemind-evidence-v1" or not isinstance(loaded.get("claims"), list):
        raise ValueError("unsupported evidence manifest")
    cards: list[Evidence] = []
    ids: set[str] = set()
    for raw in loaded["claims"]:
        card = Evidence(**raw)
        if card.id in ids or card.evidence_tier not in _VALID or not card.source_url.startswith("https://"):
            raise ValueError("duplicate or invalid evidence card")
        if card.status not in {"source_checked", "unverified", "superseded"}:
            raise ValueError("invalid evidence status")
        ids.add(card.id)
        cards.append(card)
    return cards


def retrieve_verified(question: str, *, limit: int = 6) -> list[dict]:
    if not 1 <= limit <= 50:
        raise ValueError("limit out of range")
    terms = set(re.findall(r"[a-z0-9]{3,}", question.lower()))
    candidates = []
    for card in load_evidence():
        if card.status!="source_checked":
            continue
        haystack = " ".join((card.title,card.claim,card.module,card.id,card.limitations)).lower()
        score = sum(1 for word in terms if word in haystack)
        if score:
            candidates.append((score,card.id,card))
    candidates.sort(key=lambda x:(-x[0],x[1]))
    return [card.to_dict() for _,_,card in candidates[:limit]]


def evidence_checksum() -> str:
    return hashlib.sha256(_DATA.read_bytes()).hexdigest()
