"""Independent visual-transcription cross-check of the retained official RFQ.

Uses no producer modules. This checks the retained document and descriptive
arithmetic; it does not verify an award, comparable unit price, payment or fraud.
"""
import hashlib
import json
import re
import subprocess
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parents[1] / "discovery-policy-2026-10-30" / "pricing"
PDF = PRIOR / "snapshots" / "SPE4A626U3619.pdf"
EXPECTED_HASH = "4a3996d9aca0fac0b32ea1cebfe8833fdbb144de33dc0af2739d0269b037ac51"
# Independently transcribed from rendered pages 7 and 8.
EXPECTED = [
    ("6ZF42", "SPE4A626V138W", "1212.000", "0.93000", "20260526", "N", 7),
    ("0NFB8", "SPE4A626P5931", "706.000", "1.00000", "20251114", "N", 7),
    ("7W108", "SPE4A625V346U", "448.000", "1.05000", "20250616", "N", 8),
    ("8A1E8", "SPE4A625V252D", "665.000", "1.10000", "20250516", "N", 8),
    ("6ZF42", "SPE4A625V208Q", "472.000", "1.17000", "20250430", "N", 8),
    ("51Y73", "SPE4A625PK654", "240.000", "1.44000", "20250324", "N", 8),
    ("8A1E8", "SPE4A625V4508", "536.000", "1.92000", "20241204", "N", 8),
]


def verify():
    digest = hashlib.sha256(PDF.read_bytes()).hexdigest()
    if digest != EXPECTED_HASH:
        raise ValueError("Changed original PDF: fresh review required")
    proc = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                          check=True, capture_output=True, text=True)
    pages = proc.stdout.split("\f")
    rows = []
    pattern = re.compile(r"^([A-Z0-9]{5})\s+(SPE[A-Z0-9]+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d{8})\s+([YN])\s*$", re.M)
    for page in (7, 8):
        rows.extend(tuple(m.groups()) + (page,) for m in pattern.finditer(pages[page - 1]))
    if rows != EXPECTED:
        raise ValueError("Extracted history differs from independent visual transcription")
    selected = json.loads((PRIOR / "snapshots/selected_evidence.json").read_text())
    derived = [(r["cage"], r["contract_number"], r["quantity_as_printed"],
                r["unit_cost_as_printed"], r["award_date"].replace("-", ""),
                r["surplus_material_flag"], r["source_page"])
               for r in selected["observations"]]
    if derived != rows:
        raise ValueError("Producer selection differs from original document")
    historical_unknowns = ["historical_unit_of_issue", "historical_pack_quantity",
                          "historical_revision", "historical_delivery_terms",
                          "historical_nonrecurring_costs", "currency_explicit_in_history_table"]
    if any(r.get(k) is not None for r in selected["observations"] for k in historical_unknowns):
        raise ValueError("Historical terms supplied without original history-table basis")
    quote_line = re.search(r"^0001\s+1000241595\s+0001\s+EA\s+2,221\.000\s*$", pages[8], re.M)
    if not quote_line:
        raise ValueError("Current quote line no longer matches independently observed blank prices")
    if "IAW BASIC NON GOVT STD ASMEB18.24" not in pages[8]:
        raise ValueError("Standard classification text changed")
    chronological = list(reversed(rows))
    descending = all(Decimal(a[3]) > Decimal(b[3]) for a, b in zip(chronological, chronological[1:]))
    same_cage = []
    for cage in sorted({r[0] for r in rows}):
        group = sorted([r for r in rows if r[0] == cage], key=lambda r: r[4])
        if len(group) == 2:
            before, after = group
            same_cage.append({
                "cage": cage, "earlier_contract": before[1], "later_contract": after[1],
                "quantity_change_percent": str(((Decimal(after[2]) / Decimal(before[2]) - 1) * 100).quantize(Decimal("0.01"))),
                "printed_cost_change_percent": str(((Decimal(after[3]) / Decimal(before[3]) - 1) * 100).quantize(Decimal("0.01"))),
                "meaning": "Unadjusted descriptive change only; neither supplier identity at award nor economic comparability is authenticated by this calculation",
            })
    return {
        "as_of": "2026-10-30", "passed": True, "source_sha256": digest,
        "source_id": "BR-S01", "visual_pages_reviewed": [7, 8, 9, 10],
        "separate_text_pages_reviewed": [2, 7, 8, 9, 10],
        "history_rows_verified": len(rows), "current_quote_prices_blank": True,
        "historical_unknown_fields": historical_unknowns,
        "all_seven_printed_costs_decline_in_chronological_order": descending,
        "same_cage_descriptive_changes": same_cage,
        "secondary_display_arithmetic": {
            "formula": "350000 / 2221", "rounded_to_four_decimals": str((Decimal("350000") / Decimal("2221")).quantize(Decimal("0.0001"))),
            "interpretation": "Matches secondary displayed 157.5867; invalid as purchased unit price because source values are ceiling and non-firm estimated quantity",
            "secondary_site_internal_calculation_verified": False,
        },
        "historical_terms_verified": False, "paid_price_verified": False,
        "new_fraud_finding": False, "savings_calculated": False,
        "parser_warning": proc.stderr.strip() or None,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
