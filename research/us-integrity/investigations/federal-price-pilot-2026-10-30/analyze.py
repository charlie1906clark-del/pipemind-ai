#!/usr/bin/env python3
"""Offline derivation from selected public captures; no price from award division."""
import hashlib
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path
from acquire import STRATA, validate_search, encoded

HERE = Path(__file__).resolve().parent
BASE_COMMIT = "d535e545adf362c17e43337e1147a0b2f6c7c18a"


def money(value):
    if value is None:
        return None
    amount = Decimal(str(value))
    if not amount.is_finite():
        raise ValueError("Nonfinite monetary value")
    return format(amount, ".2f")


def load(relative):
    return json.loads((HERE / relative).read_text())


def write(relative, value):
    (HERE / relative).write_bytes(encoded(value))


def validate_lines(lines, obligation):
    seen = set()
    total = Decimal("0")
    for line in lines:
        if line["clin"] in seen:
            raise ValueError("Duplicate CLIN")
        seen.add(line["clin"])
        quantity, price, extended = (Decimal(line[k]) for k in ("quantity", "unit_price_usd", "extended_amount_usd"))
        if not all(x.is_finite() for x in (quantity, price, extended)):
            raise ValueError("Nonfinite line value")
        if quantity <= 0 or price < 0 or extended < 0:
            raise ValueError("Positive original-award line expected; adjustments require a separate typed basis")
        if quantity * price != extended:
            raise ValueError("Line arithmetic does not reconcile")
        if line["price_basis"] != "awarded_contract_line":
            raise ValueError("Not an awarded contract line")
        if line["line_type"] == "first_article_test_requirement" and line["item_id"] is not None:
            raise ValueError("Test requirement must not be counted as a production item")
        total += extended
    if total != Decimal(str(obligation)):
        raise ValueError("Award does not reconcile to selected lines")
    return total


def verify_manifest(folder):
    for item in load(folder + "/manifest.json"):
        if not item["success"]:
            raise ValueError("Acquisition failure in successful cohort")
        for field in ("snapshot", "request"):
            if field + "_path" in item:
                raw = (HERE / folder / item[field + "_path"]).read_bytes()
                if hashlib.sha256(raw).hexdigest() != item[field + "_sha256"]:
                    raise ValueError("Capture hash mismatch")


def build():
    for folder in ("capture", "detail-capture", "parent-capture"):
        verify_manifest(folder)
    for artifact in load("selected_manifest.json")["selected_artifacts"]:
        if hashlib.sha256((HERE / artifact["path"]).read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("Selected document artifact hash mismatch")
    details = {r["piid"]: load("detail-capture/detail-" + r["piid"] + ".json") for r in load("detail-selection.json")}
    lines = load("line_observations.json")["observations"]
    validate_lines(lines, details["SPE4A626PW775"]["total_obligation"])
    observations, edges, strata = [], [], []
    for stratum in STRATA:
        capture = validate_search(load("capture/" + stratum + ".json"), stratum)
        total = Decimal("0")
        for rank, row in enumerate(capture["results"], 1):
            identifier, piid = row["generated_internal_id"], row["Award ID"]
            detail = details.get(piid)
            if detail and detail["generated_unique_award_id"] != identifier:
                raise ValueError("Detail join ID mismatch")
            if detail and money(detail["total_obligation"]) != money(row["Award Amount"]):
                raise ValueError("Search/detail amount mismatch; investigate timing")
            transaction = detail.get("latest_transaction_contract_data", {}) if detail else {}
            parent = detail.get("parent_award") if detail else None
            award_url = "https://www.usaspending.gov/award/" + identifier
            detail_url = "https://api.usaspending.gov/api/v2/awards/" + identifier + "/"
            sources = ["usaspending-search-" + stratum]
            if detail:
                sources.append("usaspending-detail-" + piid)
            has_line = piid == "SPE4A626PW775"
            is_express = "EXPRESS" in (row.get("Description") or "").upper()
            item = {
                "observation_id": "award-" + piid,
                "stratum": stratum,
                "sample_page_rank": rank,
                "generated_award_id": identifier,
                "piid": piid,
                "recipient_name": row["Recipient Name"],
                "recipient_uei": row["Recipient UEI"],
                "awarding_toptier": row["Awarding Agency"],
                "awarding_subtier": row["Awarding Sub Agency"],
                "awarding_office": detail["awarding_agency"].get("office_agency_name") if detail else None,
                "funding_toptier": row["Funding Agency"],
                "funding_subtier": row["Funding Sub Agency"],
                "funding_office": detail["funding_agency"].get("office_agency_name") if detail else None,
                "base_obligation_date": row["Base Obligation Date"],
                "date_signed": detail.get("date_signed") if detail else None,
                "performance_start": row["Start Date"],
                "performance_end": row["End Date"],
                "award_obligation_usd": money(row["Award Amount"]),
                "amount_basis": "cumulative_award_obligation_not_unit_price_or_cash_payment",
                "total_outlays_usd": money(row.get("Total Outlays")),
                "psc": row["PSC"]["code"],
                "naics": row["NAICS"]["code"],
                "description": row["Description"],
                "performance_state": row.get("Place of Performance State Code"),
                "express_report_in_description": is_express,
                "parent_piid": parent.get("piid") if parent else None,
                "parent_generated_award_id": parent.get("generated_unique_award_id") if parent else None,
                "solicitation_id": transaction.get("solicitation_identifier"),
                "reported_number_offers": transaction.get("number_of_offers_received"),
                "pricing_type": transaction.get("type_of_contract_pricing_description"),
                "professional_officer_role_excerpt": "selected/dla-award-page1-role-selected.txt" if has_line else None,
                "line_observation_ids": [x["observation_id"] for x in lines] if has_line else [],
                "unit_price_usd": None,
                "unit_price_note": "Use separately typed CLIN records; heterogeneous award has no single unit price.",
                "estimated_loss_usd": None,
                "undiscovered_status": "not_established",
                "award_url": award_url,
                "api_detail_url": detail_url,
                "source_ids": sources,
                "missingness": {
                    "original_order_lines": "acquired_two_clins" if has_line else "not_acquired",
                    "exact_production_item_and_unit": "observed_on_original_award" if has_line else "not_acquired",
                    "awarding_office": "observed" if detail else "detail_not_requested",
                    "date_signed": "observed" if detail else "detail_not_requested",
                    "parent_award": ("observed" if parent else "null_in_detail_response") if detail else "detail_not_requested",
                    "solicitation": ("observed" if transaction.get("solicitation_identifier") else "null_in_detail_response") if detail else "detail_not_requested",
                    "cash_payment_or_invoice": "not_acquired",
                    "delivery_acceptance": "not_acquired",
                    "independent_like_for_like_price": "not_acquired",
                    "supplier_cost_or_markup": "not_acquired",
                    "buyer_benefit_or_kickback": "not_acquired",
                    "individual_price_selection_decision_maker": "not_established_by_professional_officer_role" if has_line else "not_identified"
                }
            }
            observations.append(item)
            total += Decimal(item["award_obligation_usd"])
            edges.append({"from": "award:" + identifier, "to": "uei:" + item["recipient_uei"], "relation": "reported_award_recipient", "source_ids": sources, "cash_transfer_proven": False})
            if parent:
                edges.append({"from": "award:" + identifier, "to": "award:" + parent["generated_unique_award_id"], "relation": "reported_parent_award", "source_ids": ["usaspending-detail-" + piid]})
            if detail:
                for kind in ("awarding", "funding"):
                    office = item[kind + "_office"]
                    edges.append({"from": "award:" + identifier, "to": "office:" + office, "relation": kind + "_office", "source_ids": ["usaspending-detail-" + piid], "individual_buyer_identified": False})
        strata.append({"stratum": stratum, "sample_rows": len(capture["results"]), "has_next_page": capture["page_metadata"]["hasNext"], "sum_cumulative_sample_award_obligations_usd": money(total), "not_period_spending": True, "not_population_total": True})
    if len({x["generated_award_id"] for x in observations}) != len(observations):
        raise ValueError("Cross-stratum duplicate exact award ID")
    parent = load("parent-capture/parent-36C79123A0003.json")
    edges.append({"from": "award:" + parent["generated_unique_award_id"], "to": "award:" + parent["parent_award"]["generated_unique_award_id"], "relation": "reported_parent_award", "source_ids": ["usaspending-parent-36C79123A0003"]})
    for line in lines:
        edges.append({"from": "award:CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-", "to": "line:" + line["observation_id"], "relation": "awarded_clin", "source_ids": ["dla-original-SPE4A626PW775"], "cash_payment_proven": False})
    edges.append({"from": "line:SPE4A626PW775-0001", "to": "nsn:5306004457358", "relation": "contracted_production_item", "source_ids": ["dla-original-SPE4A626PW775"]})
    nodes = {}
    for row in observations:
        nodes["award:" + row["generated_award_id"]] = {"id": "award:" + row["generated_award_id"], "type": "award", "label": row["piid"], "source_ids": row["source_ids"]}
        nodes["uei:" + row["recipient_uei"]] = {"id": "uei:" + row["recipient_uei"], "type": "business_recipient", "label": row["recipient_name"], "source_ids": row["source_ids"]}
    for edge in edges:
        for endpoint in (edge["from"], edge["to"]):
            nodes.setdefault(endpoint, {"id": endpoint, "type": endpoint.split(":", 1)[0], "label": endpoint.split(":", 1)[1], "source_ids": edge["source_ids"]})
    missingness = {field: dict(Counter(row["missingness"][field] for row in observations)) for field in observations[0]["missingness"]}
    return {
        "observations.json": {"schema_version": "1.0", "base_commit": BASE_COMMIT, "observed_date": "2026-10-30", "amount_basis": "award_obligations_are_not_unit_prices", "observations": observations},
        "transaction_links.json": {"schema_version": "1.0", "scope": "reported award/recipient/office/parent and contracted-line relationships; not a payment ledger", "nodes": list(nodes.values()), "edges": edges},
        "coverage.json": {"strata": strata, "sample_size": len(observations), "deep_trace_awards": len(details), "original_order_awards_acquired": 1, "priced_original_clins": len(lines), "production_clins": 1, "first_article_test_clins": 1, "independent_matched_price_comparators": 0, "cash_payments_verified": 0, "express_reports": sum(r["express_report_in_description"] for r in observations), "fraud_established": False, "loss_established": False, "novelty_verified": False, "population_complete": False},
        "missingness.json": {"scope": "missing from this captured evidence, not necessarily absent from government records", "by_field": missingness, "per_award_path": "observations.json"}
    }


if __name__ == "__main__":
    outputs = build()
    for filename, data in outputs.items():
        write(filename, data)
    print(json.dumps({"outputs": list(outputs), "coverage": outputs["coverage.json"]}, indent=2))
