"""Syntactic price-comparison gate, not evidence authentication or a fraud score.

Authenticity, equivalence, adjustments and provenance must be independently reviewed;
passing arbitrary strings or reviewed=True cannot establish those real-world facts.
"""
import json
import math
from itertools import combinations
from pathlib import Path

REQUIRED = (
    "nsn", "unit_of_issue", "pack_quantity", "item_revision", "condition",
    "delivery_terms", "inspection_acceptance", "warranty_basis",
    "nonrecurring_cost_treatment", "currency", "quantity", "unit_price",
    "price_date", "source_sha256", "source_page", "unit_conversion_evidence",
)
ALLOWED_PRICE_KINDS = {"verified_award_clin", "verified_invoice_line"}
ECONOMIC_FIELDS = (
    "quantity", "price_date", "delivery_terms", "inspection_acceptance",
    "warranty_basis", "nonrecurring_cost_treatment", "condition", "item_revision",
    "unit_of_issue", "pack_quantity", "currency",
)


def eligible_pair(left, right, adjustment=None):
    reasons = []
    for label, row in (("left", left), ("right", right)):
        missing = [field for field in REQUIRED if row.get(field) is None or row.get(field) == ""]
        if missing:
            reasons.append(f"{label}: missing " + ", ".join(missing))
        if row.get("price_kind") not in ALLOWED_PRICE_KINDS:
            reasons.append(f"{label}: amount is not a verified award CLIN or invoice line price")
        for field in ("quantity", "unit_price", "pack_quantity"):
            value = row.get(field)
            if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0):
                reasons.append(f"{label}: invalid positive numeric {field}")
    if left.get("nsn") != right.get("nsn"):
        reasons.append("different NSNs: independent item-equivalence review required")
    differences = [field for field in ECONOMIC_FIELDS if left.get(field) != right.get(field)]
    if differences:
        approved = adjustment and adjustment.get("reviewed") is True and adjustment.get("source_refs") and all(
            field in adjustment.get("covered_fields", []) for field in differences
        )
        if not approved:
            reasons.append("unresolved economic differences: " + ", ".join(differences))
    return {"eligible": not reasons, "reasons": reasons,
            "input_authenticity_independently_verified_by_this_code": False,
            "fraud_inference_permitted": False, "automatic_savings_inference_permitted": False}


def pilot_result(directory):
    data = json.loads((directory / "snapshots/selected_evidence.json").read_text())
    manifest = json.loads((directory / "acquisition_manifest.json").read_text())
    rows = []
    for observation in data["observations"]:
        rows.append({
            "nsn": observation["nsn"], "quantity": float(observation["quantity_as_printed"]),
            "unit_price": float(observation["unit_cost_as_printed"]),
            "price_date": observation["award_date"], "source_page": observation["source_page"],
            "source_sha256": manifest["original_sha256"],
            "price_kind": observation["evidence_kind"],
            "unit_of_issue": observation["historical_unit_of_issue"],
            "pack_quantity": observation["historical_pack_quantity"],
            "item_revision": observation["historical_revision"],
            "currency": observation["currency_explicit_in_history_table"]
        })
    results = [eligible_pair(left, right) for left, right in combinations(rows, 2)]
    return {
        "observations": len(rows), "possible_pairs": len(results),
        "eligible_pairs": sum(result["eligible"] for result in results),
        "blocked_pairs": sum(not result["eligible"] for result in results),
        "representative_block_reasons": results[0]["reasons"],
        "scope": "One purposively selected public solicitation; not a representative procurement cohort",
        "suspect_scores_generated": 0, "potential_savings_usd": None,
        "new_fraud_case_claimed": False
    }


if __name__ == "__main__":
    print(json.dumps(pilot_result(Path(__file__).resolve().parent), indent=2))
