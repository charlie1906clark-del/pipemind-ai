#!/usr/bin/env python3
"""Independently check the selected DLA history against the archived PDF.

Does not import the acquisition/extraction or price-gate modules. The expected
rows were transcribed by this reviewer from rendered pages 7 and 8. This verifies
transcription and limits, not price reasonableness or fraud.
"""
import hashlib
import json
from decimal import Decimal
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
PRICING = HERE.parent / "pricing"
EXPECTED = [
    (7, "6ZF42", "SPE4A626V138W", "1212.000", "0.93000", "20260526", "N"),
    (7, "0NFB8", "SPE4A626P5931", "706.000", "1.00000", "20251114", "N"),
    (8, "7W108", "SPE4A625V346U", "448.000", "1.05000", "20250616", "N"),
    (8, "8A1E8", "SPE4A625V252D", "665.000", "1.10000", "20250516", "N"),
    (8, "6ZF42", "SPE4A625V208Q", "472.000", "1.17000", "20250430", "N"),
    (8, "51Y73", "SPE4A625PK654", "240.000", "1.44000", "20250324", "N"),
    (8, "8A1E8", "SPE4A625V4508", "536.000", "1.92000", "20241204", "N"),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def review():
    pdf = PRICING / "snapshots/SPE4A626U3619.pdf"
    selected_path = PRICING / "snapshots/selected_evidence.json"
    selected = json.loads(selected_path.read_text())
    manifest = json.loads((PRICING / "acquisition_manifest.json").read_text())
    assert pdf.stat().st_size == manifest["original_bytes"] == 423468
    assert digest(pdf) == manifest["original_sha256"] == "4a3996d9aca0fac0b32ea1cebfe8833fdbb144de33dc0af2739d0269b037ac51"
    assert digest(selected_path) == manifest["selected_sha256"]
    result = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                            check=True, capture_output=True, text=True)
    pages = result.stdout.split("\f")
    extracted = []
    for number in (7, 8):
        assert "Procurement History for NSN/FSC:016864912/5306" in pages[number - 1]
        for line in pages[number - 1].splitlines():
            cells = line.split()
            if len(cells) == 6 and cells[1].startswith("SPE4A6"):
                extracted.append((number, *cells))
    assert extracted == EXPECTED
    transcribed = [
        (row["source_page"], row["cage"], row["contract_number"],
         row["quantity_as_printed"], row["unit_cost_as_printed"],
         row["award_date"].replace("-", ""), row["surplus_material_flag"])
        for row in selected["observations"]
    ]
    assert transcribed == EXPECTED
    assert len(set(row[2] for row in EXPECTED)) == 7
    for row in selected["observations"]:
        for field in ("historical_unit_of_issue", "historical_pack_quantity",
                      "historical_revision", "historical_delivery_terms",
                      "historical_nonrecurring_costs", "currency_explicit_in_history_table"):
            assert row[field] is None
        assert row["invoice_or_payment_verified"] is False
        assert row["comparable_price_verified"] is False
    current = selected["current_solicitation_terms"]
    assert current["source_pages"] == [2, 8, 9, 10]
    assert current["maximum_contract_value_usd"] == 350000
    assert current["estimated_annual_quantity"] == 2221
    assert current["estimated_quantity_is_firm"] is False
    assert current["unit_price_field"] is None and current["total_price_field"] is None
    assert "Contract Maximum Value:   $350000.00" in pages[1]
    assert "Estimated Annual Quantity:    2221.000 EA" in pages[1]
    assert "PKGING DATA-QUP:001" in pages[9]
    assert selected["analysis"]["comparable_price_pairs"] == 0
    assert selected["analysis"]["potential_savings_usd"] is None
    assert selected["analysis"]["novel_fraud_finding"] is False
    prices = [Decimal(row[4]) for row in EXPECTED]
    paths = [pdf, selected_path, PRICING / "acquisition_manifest.json",
             PRICING / "eligibility.py", PRICING / "reproduce.py",
             PRICING / "test_eligibility.py"]
    return {
        "reviewed_at": "2026-10-30", "passed": True,
        "method": "Independent rendered-page transcription and separate pdftotext check; producer modules not imported",
        "visual_pages_reviewed": [7, 8],
        "current_terms_text_pages_reviewed": [2, 9, 10],
        "summary": {"history_rows": 7, "distinct_contract_keys": 7,
                    "unit_cost_as_printed_min": str(min(prices)),
                    "unit_cost_as_printed_max": str(max(prices)),
                    "all_historical_units_unknown": True,
                    "current_quote_blank": True, "comparable_price_pairs": 0,
                    "savings_usd": None, "fraud_finding": False},
        "input_sha256": {str(path.relative_to(HERE.parent)): digest(path) for path in paths},
        "limits": "Solicitation history is not a paid invoice. No independent historical award, term or payment verification. No estimate of overpricing, loss or recovery."
    }


if __name__ == "__main__":
    output = review()
    (HERE / "price_data_review.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({key: value for key, value in output.items() if key != "input_sha256"}, indent=2))
