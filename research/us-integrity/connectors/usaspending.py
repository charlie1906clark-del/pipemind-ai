"""Bounded public USAspending samples; standard library only, no agent decisions."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import socket
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import uuid

ENDPOINT = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
CONTRACT_SOURCE = "https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_award.md"
FILTER_SOURCE = "https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/search_filters.md"
TIMEOUT_SECONDS = 20
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
MAX_ROWS = 25
BASE_FIELDS = [
    "Award ID", "Recipient Name", "Recipient UEI", "recipient_id",
    "generated_internal_id", "Award Amount", "Total Outlays",
    "Awarding Agency", "Awarding Agency Code", "Awarding Sub Agency",
    "Awarding Sub Agency Code", "Start Date", "End Date", "Description",
    "Place of Performance State Code",
]
COHORTS = {
    "medical-supplies": {
        "limit": 25,
        "award_type_codes": ["A", "B", "C", "D"],
        "psc_codes": ["6515"],
        "extra_fields": ["PSC"],
        "scope": "PSC 6515 contract sample across awarding agencies; no fraud inference.",
    },
    "defense-parts": {
        "limit": 20,
        "award_type_codes": ["A", "B", "C", "D"],
        "psc_codes": ["1680"],
        "agencies": [{"type": "awarding", "tier": "toptier", "name": "Department of Defense"}],
        "extra_fields": ["PSC"],
        "scope": "PSC 1680 contracts awarded by the API's Department of Defense label; no fraud inference.",
    },
    "nih-grants": {
        "limit": 20,
        "award_type_codes": ["02", "03", "04", "05"],
        "agencies": [{"type": "awarding", "tier": "subtier", "name": "National Institutes of Health", "toptier_name": "Department of Health and Human Services"}],
        "extra_fields": ["Assistance Listings"],
        "scope": "NIH grant-type award sample; research-focused proxy, not a verified research-only population.",
    },
}


class AcquisitionError(ValueError):
    """A bounded request or response failed validation."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def build_request(cohort: str) -> dict[str, Any]:
    if cohort not in COHORTS:
        raise AcquisitionError(f"Unknown cohort: {cohort}")
    settings = COHORTS[cohort]
    filters = {
        "award_type_codes": list(settings["award_type_codes"]),
        "time_period": [{"start_date": "2025-10-01", "end_date": "2026-09-30"}],
    }
    for key in ("psc_codes", "agencies"):
        if key in settings:
            filters[key] = settings[key]
    request = {
        "filters": filters, "fields": BASE_FIELDS + settings["extra_fields"],
        "limit": settings["limit"], "page": 1, "sort": "Award Amount",
        "order": "desc", "subawards": False,
    }
    validate_request(request)
    return request


def validate_request(payload: dict[str, Any]) -> None:
    """Reject expansions outside the finite first-page acquisition contract."""
    if type(payload.get("limit")) is not int or not 1 <= payload["limit"] <= MAX_ROWS:
        raise AcquisitionError("Limit must be an integer from 1 to 25")
    if payload.get("page") != 1 or payload.get("subawards") is not False:
        raise AcquisitionError("Only first-page prime-award samples are supported")
    if payload.get("sort") != "Award Amount" or payload.get("order") != "desc":
        raise AcquisitionError("Only descending award-amount sampling is supported")
    periods = payload.get("filters", {}).get("time_period")
    if periods != [{"start_date": "2025-10-01", "end_date": "2026-09-30"}]:
        raise AcquisitionError("Only the configured FY2026 date window is supported")
    if not payload.get("filters", {}).get("award_type_codes"):
        raise AcquisitionError("Explicit award types are required")
    permitted = set(BASE_FIELDS + ["PSC", "Assistance Listings"])
    if not payload.get("fields") or not set(payload["fields"]).issubset(permitted):
        raise AcquisitionError("Fields must use the public business-award allowlist")


def validate_response(payload: Any, request: dict[str, Any]) -> list[str]:
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise AcquisitionError("Response must contain an object with a results array")
    rows = payload["results"]
    if len(rows) > request["limit"]:
        raise AcquisitionError("Response exceeds requested row limit")
    metadata = payload.get("page_metadata")
    if not isinstance(metadata, dict) or metadata.get("page") != 1 or type(metadata.get("hasNext")) is not bool:
        raise AcquisitionError("Missing/invalid first-page pagination metadata")
    warnings = []
    pscs = request["filters"].get("psc_codes")
    agencies = request["filters"].get("agencies", [])
    for row in rows:
        if not isinstance(row, dict) or not row.get("generated_internal_id"):
            raise AcquisitionError("Every award needs a generated_internal_id")
        if pscs:
            psc = row.get("PSC")
            psc_code = psc.get("code") if isinstance(psc, dict) else str(psc or "").split(":")[0].strip()
            if psc_code not in pscs:
                raise AcquisitionError("Observed PSC does not match requested cohort")
        for agency in agencies:
            field = "Awarding Agency" if agency["tier"] == "toptier" else "Awarding Sub Agency"
            if row.get(field) != agency["name"]:
                raise AcquisitionError("Observed awarding agency does not match requested cohort")
        if not row.get("Recipient UEI"):
            warnings.append("At least one award has no Recipient UEI; do not resolve its recipient by name alone.")
    return sorted(set(warnings))


def acquire(cohort: str, output_dir: Path) -> dict[str, Any]:
    """One POST, no retry, no pagination; preserve exact response body and provenance."""
    request_payload = build_request(cohort)
    request_raw = json_bytes(request_payload)
    cohort_dir = output_dir / cohort
    cohort_dir.mkdir(parents=True, exist_ok=False)
    (cohort_dir / "request.json").write_bytes(request_raw)
    manifest = {
        "schema_version": "1.0", "cohort": cohort, "scope": COHORTS[cohort]["scope"],
        "endpoint": ENDPOINT, "method": "POST", "started_at": utc_now(),
        "request_file": "request.json", "request_sha256": sha256(request_raw),
        "source_contract": CONTRACT_SOURCE, "source_filters": FILTER_SOURCE,
        "api_contract_checked_on": "2026-10-29", "timeout_seconds": TIMEOUT_SECONDS,
        "max_response_bytes": MAX_RESPONSE_BYTES, "request_limit": request_payload["limit"],
        "pages_requested": [1], "auto_pagination": False, "automatic_retries": 0,
        "sampling": "largest_cumulative_award_amount_descending_first_page",
        "sample_is_random": False, "sample_is_complete_population": False,
        "truncated_sample": True, "is_fraud_rank": False,
        "amount_semantics": "Cumulative award-level amount, not spending within the FY filter, not contract ceiling, not a fraud loss or recoverable sum.",
        "time_filter_semantics": "FY2026 award-search date window; default date_type omitted. It is not an FY2026 transaction-spending aggregate.",
        "ownership_verified": False, "success": False,
    }
    request = Request(ENDPOINT, data=request_raw, method="POST", headers={
        "Content-Type": "application/json", "Accept": "application/json",
        "User-Agent": "PipeMind-USIntegrity-PublicResearch/0.1",
    })
    response_raw = None
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            manifest["http_status"] = response.status
            manifest["response_content_type"] = response.headers.get("Content-Type")
            manifest["response_date_header"] = response.headers.get("Date")
            response_raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(response_raw) > MAX_RESPONSE_BYTES:
            # This prefix is not a full raw response; label and hash it accordingly.
            (cohort_dir / "oversize-response-prefix.bin").write_bytes(response_raw)
            manifest["partial_response_sha256"] = sha256(response_raw)
            manifest["partial_response_file"] = "oversize-response-prefix.bin"
            raise AcquisitionError("Response exceeded bounded byte cap; capture is partial")
        (cohort_dir / "response.json").write_bytes(response_raw)
        manifest.update(response_file="response.json", response_sha256=sha256(response_raw), response_bytes=len(response_raw))
        decoded = json.loads(response_raw)
        manifest["warnings"] = validate_response(decoded, request_payload)
        manifest.update(success=True, records_returned=len(decoded["results"]), page_metadata=decoded["page_metadata"], api_messages=decoded.get("messages", []))
    except HTTPError as exc:
        manifest.update(http_status=exc.code, error_type="HTTPError", error="API rejected request; bounded response retained.")
        error_raw = exc.read(MAX_RESPONSE_BYTES + 1)
        error_complete = len(error_raw) <= MAX_RESPONSE_BYTES
        filename = "error-response.bin" if error_complete else "error-response-prefix.bin"
        (cohort_dir / filename).write_bytes(error_raw)
        manifest.update(error_response_file=filename, error_response_sha256=sha256(error_raw), error_response_complete=error_complete)
    except (URLError, socket.timeout, TimeoutError, OSError, ValueError, UnicodeDecodeError) as exc:
        manifest.update(error_type=type(exc).__name__, error=str(exc)[:500])
    finally:
        manifest["completed_at"] = utc_now()
        (cohort_dir / "manifest.json").write_bytes(json_bytes(manifest))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", choices=["all", *COHORTS], default="all")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "snapshots")
    args = parser.parse_args()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    run_dir = args.output / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    selected = list(COHORTS) if args.cohort == "all" else [args.cohort]
    with ThreadPoolExecutor(max_workers=3) as pool:
        manifests = list(pool.map(lambda c: acquire(c, run_dir), selected))
    summary = {"run_id": run_id, "cohorts": manifests, "all_successful": all(m["success"] for m in manifests)}
    (run_dir / "run-manifest.json").write_bytes(json_bytes(summary))
    print(json.dumps({"path": str(run_dir), "all_successful": summary["all_successful"], "cohorts": [{"cohort": m["cohort"], "success": m["success"], "records_returned": m.get("records_returned"), "error": m.get("error")} for m in manifests]}, indent=2))
    return 0 if summary["all_successful"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
