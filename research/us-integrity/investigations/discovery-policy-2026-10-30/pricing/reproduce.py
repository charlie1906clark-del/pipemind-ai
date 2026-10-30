#!/usr/bin/env python3
"""Reacquire one public DLA RFQ through its normal notice and consent form.

No authentication, API key, proxy, restricted drawings, or access-control bypass.
Requires Python 3 and pdftotext (Poppler). Output directory must not exist.
Use --pdf with the archived PDF for a completely offline extraction check.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import http.cookiejar
import json
from pathlib import Path
import re
import subprocess
import urllib.parse
import urllib.request

URL = "https://dibbs2.bsm.dla.mil/Downloads/RFQ/9/SPE4A626U3619.PDF"
EXPECTED_SHA256 = "4a3996d9aca0fac0b32ea1cebfe8833fdbb144de33dc0af2739d0269b037ac51"


class NoticeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.action = None
        self.fields = {}
        self.agree_button_found = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "form" and a.get("method", "").lower() == "post":
            self.action = a.get("action")
        if tag == "input" and a.get("name"):
            self.fields[a["name"]] = a.get("value", "")
            if a["name"] == "butAgree" and a.get("value") == "OK":
                self.agree_button_found = True


def acquire():
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
    )
    steps = []
    with opener.open(URL, timeout=20) as response:
        data = response.read(5_000_001)
        steps.append({"method": "GET", "status": response.status,
                      "content_type": response.headers.get("Content-Type")})
    if not data.startswith(b"%PDF-"):
        html = data.decode("utf-8")
        parser = NoticeParser()
        parser.feed(html)
        if not parser.action or not parser.agree_button_found:
            raise RuntimeError("Expected public DoD notice was not found; stop for review")
        action = urllib.parse.urljoin(URL, parser.action)
        parsed = urllib.parse.urlsplit(action)
        if parsed.scheme != "https" or parsed.netloc != "dibbs2.bsm.dla.mil" or parsed.path.lower() != "/dodwarning.aspx":
            raise RuntimeError("Unexpected notice action; stop for review")
        parser.fields["butAgree"] = "OK"
        request = urllib.request.Request(
            action, data=urllib.parse.urlencode(parser.fields).encode()
        )
        with opener.open(request, timeout=20) as response:
            data = response.read(5_000_001)
            steps.append({"method": "POST public notice consent", "status": response.status,
                          "content_type": response.headers.get("Content-Type")})
    if len(data) > 5_000_000 or not data.startswith(b"%PDF-"):
        raise RuntimeError("Response is not a bounded PDF; no retry or bypass attempted")
    return data, steps


def extract(text):
    pages = text.split("\f")
    observations = []
    pattern = re.compile(r"^([A-Z0-9]{5})\s+(SPE[A-Z0-9]+)\s+([\d.]+)\s+([\d.]+)\s+(\d{8})\s+([NY])\s*$", re.M)
    for page_no, page in enumerate(pages, 1):
        if "Procurement History for NSN/FSC:016864912/5306" not in page:
            continue
        for cage, contract, quantity, unit_cost, award_date, surplus in pattern.findall(page):
            observations.append({
                "source_page": page_no, "cage": cage, "contract_number": contract,
                "nsn": "5306016864912", "quantity_as_printed": quantity,
                "unit_cost_as_printed": unit_cost,
                "award_date": f"{award_date[:4]}-{award_date[4:6]}-{award_date[6:]}",
                "surplus_material_flag": surplus,
                "historical_unit_of_issue": None,
                "historical_pack_quantity": None,
                "historical_revision": None,
                "historical_delivery_terms": None,
                "historical_nonrecurring_costs": None,
                "currency_explicit_in_history_table": None,
                "evidence_kind": "solicitation_disclosed_procurement_history",
                "invoice_or_payment_verified": False,
                "comparable_price_verified": False
            })
    if len(observations) != 7:
        raise ValueError(f"Expected seven observed history rows, got {len(observations)}; review changed source")
    return {
        "source_id": "DLA-SPE4A626U3619", "source_url": URL,
        "solicitation": "SPE4A6-26-U-3619", "issue_date": "2026-09-03",
        "product_family": "machine bolt", "nsn": "5306016864912",
        "observations": observations,
        "current_solicitation_terms": {
            "source_pages": [2, 8, 9, 10], "instrument": "potential unilateral indefinite delivery contract",
            "estimated_annual_quantity": 2221, "estimated_quantity_is_firm": False,
            "guaranteed_minimum_quantity_after_binding": 222, "minimum_order_quantity": 555,
            "unit_of_issue": "EA", "quantity_per_unit_pack": 1,
            "maximum_contract_value_usd": 350000,
            "unit_price_field": None, "total_price_field": None,
            "delivery_days": 78, "fob": "ORIGIN", "inspection": "DESTINATION",
            "acceptance": "DESTINATION", "packaging_standard": "ASTM D3951 subject to incorporated DLA requirements",
            "drawing_or_technical_revision_printed": "TDP Rev A Gen 1; ASMEB18.24 dated 2023-10-16"
        },
        "analysis": {
            "finding_class": "public_data_feasibility_demonstration",
            "novel_fraud_finding": False,
            "comparable_price_pairs": 0,
            "blocked_reason": "Historical item revisions, units, packs, delivery and other price-affecting terms not verified; current price blank",
            "prohibited_calculation": "350000 / 2221 is not a per-bolt price",
            "potential_savings_usd": None,
            "inference": "Published historical cost entries alone do not establish overpricing, payment, misrepresentation or fraud"
        }
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, help="Use existing PDF; no network")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    if args.pdf:
        data, steps = args.pdf.read_bytes(), [{"mode": "offline", "path": str(args.pdf)}]
    else:
        data, steps = acquire()
    digest = hashlib.sha256(data).hexdigest()
    pdf = args.output / "SPE4A626U3619.pdf"
    pdf.write_bytes(data)
    if digest != EXPECTED_SHA256:
        raise RuntimeError("Source hash changed; raw PDF saved, but selection requires a new manual review")
    text_path = args.output / "SPE4A626U3619.txt"
    subprocess.run(["pdftotext", "-layout", str(pdf), str(text_path)], check=True)
    selected = extract(text_path.read_text())
    (args.output / "selected_evidence.json").write_text(json.dumps(selected, indent=2) + "\n")
    manifest = {"executed_at_utc": datetime.now(timezone.utc).isoformat(), "source_url": URL,
                "bytes": len(data), "sha256": digest, "matches_initial_capture": digest == EXPECTED_SHA256,
                "steps": steps, "hidden_form_values_retained": False,
                "historical_rows": len(selected["observations"]), "review_required_if_hash_changes": True}
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "rows": len(selected["observations"]), "matches_initial_capture": digest == EXPECTED_SHA256}))


if __name__ == "__main__":
    main()
