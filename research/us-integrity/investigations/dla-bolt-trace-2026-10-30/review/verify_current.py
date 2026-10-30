"""Cross-check visually transcribed current parent/child order against PDF text.

Do not infer payment or actual delivery from a signed order. Inspect the raw
documents separately if their hashes change. No producer module is imported.
"""
import hashlib
import json
import re
import subprocess
import argparse
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
CURRENT = HERE.parent / "current"
DOCUMENTS = {
    "parent": ("SPE4A626D61WS.pdf", "0a3a9251aefd31299321b89aba0afe7ebbfe0afc544af4af23585bba54f050e0"),
    "child": ("SPE4A626D61WSSPE4A627F0588.pdf", "3360e103d973fd70d38d2baebc1aa47644cd3806822bc8393fb5db99bcbbc4ef"),
}


def verify(source_dir=None, current_dir=CURRENT):
    manifest = json.loads((current_dir / "selected_manifest.json").read_text())
    originals = {r["file"]: r for r in manifest["records"]}
    for name, expected in DOCUMENTS.values():
        record = originals[name]
        if record["original_pdf_sha256"] != expected or record["original_pdf_archived_in_public_repo"]:
            raise ValueError("Original hash/publication scope differs from reviewed record")
        for artifact in record["selected_artifacts"]:
            path = current_dir / artifact["path"]
            if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
                raise ValueError("Selected artifact digest mismatch: " + str(path))
    pages = {"parent": [""] * 6, "child": [""] * 2}
    pages["parent"][1] = (current_dir / "snapshots/parent-page2.txt").read_text()
    pages["parent"][4] = (current_dir / "snapshots/parent-page5.txt").read_text()
    pages["child"][1] = (current_dir / "snapshots/order-page2.txt").read_text()
    if source_dir is not None:
        for role, (name, expected) in DOCUMENTS.items():
            path = source_dir / name
            if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError("Current document hash changed: " + name)
            text = subprocess.run(["pdftotext", "-layout", str(path), "-"], check=True, capture_output=True, text=True).stdout
            original_pages = text.split("\f")
            for number in ([2, 5] if role == "parent" else [2]):
                if original_pages[number - 1].strip() != pages[role][number - 1].strip():
                    raise ValueError("Selected page differs from original PDF")
            pages[role] = original_pages
    parent_line = re.search(r"^0001\s+1000241595\s+0001\s+EA\s+0\.000\s+0\.91000\s+USD\s+350000\.00\s*$", pages["parent"][4], re.M)
    child_line = re.search(r"^0001\s+0001\s+906\.000\s+EA\s+0\.9100\s+824\.46\s+2027 JAN 04\s*$", pages["child"][1], re.M)
    if not parent_line or not child_line:
        raise ValueError("Current price line differs from independent visual transcription")
    if "5306016864912" not in pages["parent"][4] or "5306016864912" not in pages["child"][1]:
        raise ValueError("Exact item identifier not corroborated")
    if "SPE4A6-26-D-61WS-SPE4A6-27-F-0588" not in pages["child"][1]:
        raise ValueError("Parent/child cross-reference changed")
    minimum = re.search(r"Minimum Delivery Order Quantity\s*:\s*1 EA", pages["parent"][1])
    if not minimum or "DELIVERY (IN DAYS):076" not in pages["parent"][4]:
        raise ValueError("Current award terms changed")
    if Decimal("906") * Decimal("0.9100") != Decimal("824.46"):
        raise ValueError("Ordered-line arithmetic mismatch")
    observations = json.loads((current_dir / "observations.json").read_text())
    parent = observations["parent"]
    child = observations["child_order"]
    expected_parent = {"contract": "SPE4A626D61WS", "unit_of_issue": "EA", "currency": "USD", "clin": "0001",
                       "minimum_delivery_order_quantity": "1", "delivery_days": "76", "quantity_per_unit_pack": "001",
                       "base_line_quantity_is_purchased_quantity": False, "estimate_is_order": False, "payment_verified": False}
    expected_child = {"contract": "SPE4A627F0588", "parent_contract": "SPE4A626D61WS", "unit_of_issue": "EA", "currency": "USD",
                      "clin": "0001", "basic_reference_clin": "0001", "delivery_date": "2027-01-04",
                      "inspection": "DESTINATION", "acceptance": "DESTINATION", "fob": "ORIGIN", "fob_payment_method": "GOVERNMENT",
                      "delivery_verified": False, "receipt_or_acceptance_verified": False, "payment_verified": False,
                      "all_orders_under_parent_acquired": False, "measure": "ordered_line_value_not_verified_payment"}
    for record, expected in ((parent, expected_parent), (child, expected_child)):
        for key, value in expected.items():
            if record.get(key) != value:
                raise ValueError("Structured observation differs from source or exceeds evidence: " + key)
    for record, expected in ((parent, {"unit_price": "0.91", "contract_ceiling": "350000", "estimated_annual_quantity": "2221", "base_line_quantity_as_printed": "0"}),
                             (child, {"quantity": "906", "unit_price": "0.91", "order_line_total": "824.46"})):
        for key, value in expected.items():
            number = Decimal(record[key])
            if not number.is_finite() or number != Decimal(value):
                raise ValueError("Structured monetary/quantity field differs from source: " + key)
    if Decimal(child["quantity"]) * Decimal(child["unit_price"]) != Decimal(child["order_line_total"]):
        raise ValueError("Structured ordered-line arithmetic mismatch")
    status = observations["comparison_status"]
    if status["ceiling_divided_by_estimate_is_unit_price"] or status["fraud_established"] or status["loss_calculated"] or status["historical_like_for_like_comparison_verified"]:
        raise ValueError("Structured comparison status exceeds evidence")
    return {
        "as_of": "2026-10-30", "passed": True,
        "method": "Selected-public-artifact digest and text/Decimal replay of independent visual transcription; no producer modules",
        "original_pdfs_replayed_this_run": source_dir is not None,
        "original_pdf_bytes_archived_in_public_repository": False,
        "selected_manifest_sha256": hashlib.sha256((current_dir / "selected_manifest.json").read_bytes()).hexdigest(),
        "observations_sha256": hashlib.sha256((current_dir / "observations.json").read_bytes()).hexdigest(),
        "structured_observations_checked_against_source": True,
        "documents": {role: {"filename": name, "sha256": digest} for role, (name, digest) in DOCUMENTS.items()},
        "visual_pages": {"parent": [2, 5], "child": [1, 2]},
        "additional_text_pages": {"parent": [1, 6]},
        "parent_contract": "SPE4A626D61WS", "child_order": "SPE4A627F0588",
        "nsn": "5306016864912", "parent_clin": "0001", "order_clin": "0001",
        "unit": "EA", "currency": "USD", "awarded_unit_price": "0.91000",
        "ordered_quantity": "906.000", "ordered_unit_price": "0.9100", "ordered_line_amount_usd": "824.46",
        "order_arithmetic_matches": True, "order_date": "2026-10-19", "required_delivery_date": "2027-01-04",
        "parent_ceiling_usd": "350000.00", "estimated_annual_quantity": "2221.000",
        "current_order_minimum_ea": "1", "rfq_order_minimum_ea": "555",
        "current_parent_delivery_days": "76", "rfq_delivery_days": "78",
        "current_line_price_verified": True,
        "secondary_displayed_unit_price_valid": False,
        "inspection_receipt_acceptance_payment_blocks_on_order_form": "blank in inspected original",
        "actual_delivery_verified": False, "cash_payment_verified": False,
        "contract_document_completeness_all_modifications": "not_established",
        "historical_like_for_like_comparison_approved": False,
        "new_fraud_established": False,
        "limits": "Confirms actual document price and quantity fields, not whether later modifications, shipment, acceptance or payment occurred.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, help="Optional directory containing both original PDFs; otherwise use public selected snapshots only")
    args = parser.parse_args()
    print(json.dumps(verify(args.source_dir), indent=2))
