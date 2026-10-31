"""Independently reconcile exact RFQ-history keys to saved USAspending records.

No producer modules are imported. Matching arithmetic is a consistency check,
never proof of an awarded unit, a paid invoice, delivery or fair pricing.
"""
import hashlib
import json
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAPTURE = HERE.parent / "awards" / "capture-success"
PRIOR = HERE.parents[1] / "discovery-policy-2026-10-30" / "pricing"


def read(path):
    return json.loads(path.read_text(), parse_float=Decimal)


def verify():
    manifest = read(CAPTURE / "manifest.json")
    checked = []
    for item in manifest:
        if item.get("snapshot"):
            path = CAPTURE / item["snapshot"]
            if hashlib.sha256(path.read_bytes()).hexdigest() != item["snapshot_sha256"]:
                raise ValueError("Snapshot digest mismatch: " + str(path))
            if len(path.read_bytes()) != item["snapshot_bytes"]:
                raise ValueError("Snapshot size mismatch: " + str(path))
            if item["wire_bytes_archived"]:
                if item["snapshot_sha256"] != item["wire_sha256"] or item["snapshot_scope"] != "original_response_bytes":
                    raise ValueError("Original-byte declaration inconsistent")
            elif item["snapshot_scope"] != "selected_fields_reformatted":
                raise ValueError("Selected snapshot scope missing")
            checked.append(item["snapshot"])
        if item.get("request_file"):
            if hashlib.sha256((CAPTURE / item["request_file"]).read_bytes()).hexdigest() != item["request_sha256"]:
                raise ValueError("Request digest mismatch")
    history = read(PRIOR / "snapshots/selected_evidence.json")["observations"]
    expected = {r["contract_number"] for r in history}
    request = read(CAPTURE / "exact-award-search.request.json")
    if set(request["filters"]["award_ids"]) != expected or request["page"] != 1:
        raise ValueError("Query cohort differs from seven source keys")
    terminal_request = read(CAPTURE / "exact-award-terminal.request.json")
    if {k: v for k, v in terminal_request.items() if k != "page"} != {k: v for k, v in request.items() if k != "page"} or terminal_request["page"] != 2:
        raise ValueError("Terminal request not the next page of the same query")
    search = read(CAPTURE / "exact-award-search.json")
    results = search["results"]
    if len(results) != 7 or {r["Award ID"] for r in results} != expected:
        raise ValueError("Unexpected returned award keys or duplicates")
    terminal = read(CAPTURE / "exact-award-terminal.json")
    if terminal["results"] or terminal["page_metadata"]["hasNext"]:
        raise ValueError("Terminal page is not empty")
    by_key = {r["Award ID"]: r for r in results}
    findings = []
    for h in history:
        key = h["contract_number"]
        d = read(CAPTURE / ("award-" + key + ".json"))
        s = by_key[key]
        if d["piid"] != key or d["generated_unique_award_id"] != s["generated_internal_id"]:
            raise ValueError("Award identity mismatch: " + key)
        if d["date_signed"] != h["award_date"]:
            raise ValueError("Award date mismatch: " + key)
        if d["recipient"]["recipient_uei"] != s["Recipient UEI"]:
            raise ValueError("Recipient identifier mismatch: " + key)
        obligation = Decimal(str(d["total_obligation"]))
        if obligation != Decimal(str(s["Award Amount"])):
            raise ValueError("Search/detail monetary mismatch: " + key)
        product = Decimal(h["quantity_as_printed"]) * Decimal(h["unit_cost_as_printed"])
        x = d["latest_transaction_contract_data"]
        findings.append({
            "contract_number": key, "history_cage": h["cage"],
            "recipient_uei": d["recipient"]["recipient_uei"],
            "award_date_matches": True, "source_amount_kind": "total_obligation",
            "total_obligation_usd": str(obligation),
            "history_quantity_times_printed_cost": str(product),
            "arithmetic_matches": obligation == product,
            "source_reports_offers": x["number_of_offers_received"],
            "source_reports_competition": x["extent_competed_description"],
            "source_reports_pricing": x["type_of_contract_pricing_description"],
            "solicitation_identifier": x["solicitation_identifier"],
            "total_outlay_field": d["total_outlay"],
            "cash_payment_verified": False, "priced_clin_verified": False,
            "historical_cage_join_basis": "Same exact contract key in the retained RFQ history and API award; no direct CAGE registry proof from this API selection",
        })
    return {
        "as_of": "2026-10-30", "passed": True,
        "method": "Independent request, byte-digest, exact-key, date, UEI and Decimal reconciliation; no producer modules",
        "capture_manifest_sha256": hashlib.sha256((CAPTURE / "manifest.json").read_bytes()).hexdigest(),
        "checked_snapshots": checked, "exact_keys_resolved": 7,
        "findings": findings, "all_arithmetic_matches": all(x["arithmetic_matches"] for x in findings),
        "new_fraud_established": False,
        "limits": "Data consistency, source-reported competition and obligations are not underlying bid verification, legal supplier eligibility, priced-CLIN verification, delivery or payment proof.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
