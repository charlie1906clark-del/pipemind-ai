#!/usr/bin/env python3
"""Build a small proposed single-case projection without approving or publishing it.

National estimates, advertised commercial prices and hypothetical residuals never
become actual money measures here. Source hashes state whether they bind selected
original text or a locally authored receipt. No acquisition occurs in this script.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREFIX = "SC-20261030-"
DAY = "2026-10-30"
REPO = "https://github.com/charlie1906clark-del/pipemind-ai"
BASE = "9238fe6743be83e731cfb40f6481a096bc7208ca"


class Projection:
    def __init__(self):
        self.nodes, self.edges, self.inputs = [], [], {}
        self.old = json.loads((ROOT / "data/graph.json").read_text())
        self.old_nodes = {n["id"]: n for n in self.old["nodes"]}

    def pin(self, path, expected=None):
        path = Path(path).resolve()
        if not any(path.is_relative_to(p) for p in (ROOT / "investigations", ROOT / "price-agents")):
            raise ValueError("Input escapes approved evidence roots")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if expected and expected != digest:
            raise ValueError("Reviewed bytes changed: " + str(path))
        self.inputs[str(path.relative_to(ROOT))] = digest
        return digest

    def read(self, path):
        self.pin(path)
        return json.loads(Path(path).read_text())

    def node(self, suffix, kind, title, sources=(), status="documented_fact", **properties):
        ident = PREFIX + suffix
        if any(n["id"] == ident for n in self.nodes):
            raise ValueError("Duplicate node: " + ident)
        self.nodes.append(dict(id=ident, type=kind, title=title, status=status,
            source_ids=sorted(set(sources)), properties={"visibility": "public", **properties}))
        return ident

    def edge(self, relation, source, target, sources=(), **properties):
        ident = PREFIX + "E-" + hashlib.sha256(f"{relation}|{source}|{target}".encode()).hexdigest()[:20]
        if any(e["id"] == ident for e in self.edges):
            raise ValueError("Duplicate edge")
        self.edges.append(dict(id=ident, type=relation, source=source, target=target,
            status="documented_fact", source_ids=sorted(set(sources)),
            properties={"visibility": "public", **properties}))

    def source(self, suffix, title, url, path=None, expected=None, observed=DAY, **properties):
        props = dict(url=url, accessed_at=observed, source_bytes_archived=False, **properties)
        if path:
            props.update(source_bytes_archived=True,
                snapshot_path=str(Path(path).resolve().relative_to(ROOT)),
                content_sha256=self.pin(path, expected))
        return self.node("SRC-" + suffix, "source", title, status="source", **props)

    def artifact(self, suffix, title, path):
        return self.source(suffix, title, REPO, path,
            artifact_origin="locally_authored_repository_artifact",
            snapshot_scope="Exact retained local selected facts or receipt; not original webpage bytes",
            network_retrieval_inferred=False)

    def attach(self, ident, sources=()):
        self.edge("includes_observation", self.case, ident, sources)

    def retained_input_pins(self):
        # Explicit producer manifests, not an automatic directory ingestion.
        for folder, manifest_name in [("spec", "VALIDATION.json"),
                                      ("market-terms", "manifest.json"),
                                      ("bids", "bundle-manifest.json")]:
            manifest = self.read(HERE / folder / manifest_name)
            for a in manifest["artifacts"]:
                self.pin(HERE / folder / a["path"], a["sha256"])
        manifest = self.read(HERE / "selection/VALIDATION.json")
        for name, digest in manifest["artifact_hashes"].items():
            self.pin(HERE / "selection" / name, digest)
        self.pin(HERE / "history/acquire_history.py")
        self.pin(HERE / "history/REPORT.md")
        self.pin(HERE / "history/additional-route-checks.json")

    def selection(self):
        decision = self.read(HERE / "selection/decision.json")
        assert decision["base_commit"] == BASE
        ds = self.artifact("SELECTION", "Frozen selection by evidence availability", HERE / "selection/decision.json")
        self.case = self.node("CASE", "research_collection", "One common-bolt price and decision follow-up", [ds],
            nsn="5306016864912", parent_piid="SPE4A626D61WS", order_piid="SPE4A627F0588",
            base_commit=BASE, selection_basis="Investigability within the retained corpus",
            fraud_probability=None, new_fraud_established=False, nationwide_ranking=False,
            paid_cash_verified=False, buyer_benefit=None, external_model_execution=False,
            prior_runtime_state_mutated=False)
        sel = self.node("SELECTION", "selection_assessment", "Single-case choice does not estimate guilt", [ds],
            chosen_question="Can the documented price be compared with an actual equivalent supply offer and decision record?",
            known_case_not_selected="Centennial is an existing publicly investigated matter",
            specialty_item_not_selected="Different NSN and no acquired priced equivalent",
            other_pilot_awards_without_original_priced_lines=29,
            earlier_selection_market_unknowns_may_be_updated_by_later_observations=True)
        self.attach(sel, [ds])
        source_rows = {s["id"]: s for s in self.read(HERE / "selection/sources.json")["sources"]}
        national = [
            ("SC-SEL-SBA-OCT2026", "SBA-POTENTIAL", "SBA's $200 billion refers to potential pandemic PPP/EIDL fraud",
             {"reported_estimate_usd": "more than 200 billion", "program_scope": "Pandemic PPP/EIDL assistance",
              "measure_status": "Agency-reiterated potential-fraud estimate, not adjudicated loss or current missing cash",
              "other_reported_figures": "Referrals and suspensions are suspected/administrative measures with unreconciled overlap",
              "amounts_additive": False}),
            ("SC-SEL-GAO-IP", "GAO-IMPROPER", "FY2025 estimated improper payments are a distinct measure",
             {"reported_estimate_usd": "about 186 billion", "period": "FY2025", "reporting_agencies": 15,
              "reported_programs": 64, "not_all_fraud": True, "complete_government_coverage": False}),
            ("SC-SEL-GAO-FRAUD", "GAO-FRAUD-RANGE", "GAO's annual fraud-loss range uses FY2018–2022 data",
             {"modeled_annual_range_usd": "233–521 billion", "underlying_period": "FY2018–2022",
              "predictive_of_2026": False, "agency_program_allocation_permitted": False,
              "comparable_to_improper_payment_estimate": False})]
        for source_id, suffix, title, props in national:
            s = source_rows[source_id]
            sid = self.source(suffix, s["title"], s["url"], observed=s["observed_at"],
                source_class=s["source_class"], published_at=s["published_at"],
                retrieval_scope=s["access_outcome"], original_webpage_bytes_archived=False)
            n = self.node(suffix, "aggregate_estimate_observation", title, [sid],
                **props, actual_case_money_measure=False, allocation_to_selected_purchase=False)
            self.attach(n, [sid])
        for old_id, relation in [("BOLT-TRACE-20261030", "follows_existing_case"),
                                 ("BOLT-ORDER-SPE4A627F0588", "examines_documented_order")]:
            if old_id not in self.old_nodes:
                raise ValueError("Existing case node is missing: " + old_id)
            self.edge(relation, self.case, old_id, [ds], old_node_not_modified=True)

    def bids(self):
        sources = {}
        for s in self.read(HERE / "bids/selected-manifest.json")["records"]:
            sid = self.source(s["id"], "Selected original procurement record: " + s["id"], s["source_url"],
                HERE / "bids" / s["artifact_path"], s["sha256"],
                observed=s.get("observed_at", DAY), locator=s["locator"],
                snapshot_scope=s["hash_scope"], original_source_archived=False,
                original_source_sha256=s.get("original_pdf_sha256", s.get("original_body_sha256")),
                source_origin=s.get("source_origin", "New public original HTML; selected facts retained"),
                event_date=s.get("event_date"))
            sources[s["id"]] = sid
        rfq = self.read(HERE / "bids/selected/current-rfq-record.json")
        award = self.read(HERE / "bids/selected/current-award-record.json")
        assert rfq["solicitation"] == "SPE4A626U3619" and rfq["nsn"] == "5306016864912"
        assert award["award_basic_number"] == "SPE4A626D61WS"
        self.rfq = self.node("RFQ-RECORD", "solicitation_record_observation", "Original RFQ links exact NSN, PR, award and technical route", [sources["SCB-S02"]],
            solicitation=rfq["solicitation"], nsn=rfq["nsn"], purchase_request=rfq["purchase_request"],
            issue_date=rfq["issue_date"], return_by_date=rfq["return_by_date"],
            awardee_cage=rfq["awardee_cage"], parent_contract=rfq["contract"],
            displayed_rfq_quantity=rfq["rfq_quantity_as_displayed"], quantity_is_ordered_or_paid=False,
            attachments_label=rfq["rfq_attachment_label"], separate_technical_documents_link=True,
            actual_competing_quote_prices_acquired=0)
        self.award = self.node("AWARD-RECORD", "award_record_observation", "Original parent award page exposes office codes and document link", [sources["SCB-S04"]],
            parent_contract=award["award_basic_number"], award_date=award["award_date"],
            posted_date=award["posted_date"], issued_by_office=award["issued_by_office_code"],
            administered_by_office=award["admin_by_office_code"], payment_office=award["payment_office_code"],
            payment_verified=False, awardee_cage=award["awardee_cage"],
            displayed_modifications=award["modifications_label"], modifications_scope=award["modifications_scope"],
            displayed_amount_interpretation="Previously verified parent ceiling; not ordered or paid value")
        self.h06 = self.node("H06", "contract_term_observation", "H06 separates annual-demand evaluation from order-quantity pricing", [sources["SCB-S01"]],
            evaluation_quantity_basis="Quoted estimated annual demand",
            individual_order_price_basis="Price range covering total quantity on the individual order",
            award_standard="Conforming responsible offeror, price and other factors",
            actual_bids_or_evaluation_compliance_established=False,
            estimated_annual_demand_is_order=False, documented_child_order_is_separate=True)
        for n, refs in [(self.rfq, [sources["SCB-S02"]]), (self.award, [sources["SCB-S04"]]), (self.h06, [sources["SCB-S01"]])]:
            self.attach(n, refs)
        self.edge("links_award_record", self.rfq, self.award, [sources["SCB-S02"], sources["SCB-S04"]])
        self.edge("has_selected_contract_term", self.award, self.h06, [sources["SCB-S01"], sources["SCB-S04"]])
        self.bid_sources = sources

    def specification(self):
        rows = self.read(HERE / "spec/archive-static-inspection.json")
        refs = []
        for i, row in enumerate(rows, 1):
            refs.append(self.source("PUBLOG-" + str(i), "Selected PUB LOG member: " + row["member"], row["url"],
                HERE / "spec" / row["selected_artifact"], row["selected_sha256"], observed=row["observed_at"],
                locator=row["member"], snapshot_scope=row["selected_scope"], original_member_archived=False,
                original_member_sha256=row["member_sha256"], original_range_sha256=row["range_sha256"],
                requested_range=row["requested_range"], crc_matches_retained_directory=row["crc_matches_prior_directory"]))
        changes = self.read(HERE / "spec/archive-change-inspection.json")
        ch = self.artifact("PUBLOG-CHANGE-RECEIPT", "Static change-archive inspection receipt; no base item row", HERE / "spec/archive-change-inspection.json")
        self.archive = self.node("NATIVE-ARCHIVE", "source_access_observation", "Native archive schema acquired; exact NIIN rows remain absent", refs + [ch],
            http_206_range_requests=len(rows) + 1, received_range_bytes=sum(r["range_bytes"] for r in rows) + changes["range_bytes"],
            native_tables=["V_FLIS_PART", "V_CHARACTERISTICS"],
            native_part_number_field_length=60, native_characteristic_reply_length=3144,
            older_csv_layout_interchangeability=False, exact_niin_rows_acquired=0,
            base_tables_acquired=False, executable_extracted_or_run=False,
            change_scan_limit="Add/delete byte scans and nested directory only; large change member not decompressed",
            base_catalog_absence_inferred=False)
        release = self.node("RELEASE-LABEL", "source_label_observation", "November 2026 archive label observed on 30 October 2026", [refs[2]],
            printed_release_label="November 2026", observed_at=rows[2]["observed_at"],
            publication_timestamp_verified=False, september_contract_applicability_verified=False,
            exact_item_record=False)
        sources = {s["id"]: s for s in self.read(HERE / "spec/sources.json")}
        standard_refs = []
        for name in ["SC-SPEC-ASME-PRODUCT", "SC-SPEC-ASME-PREVIEW"]:
            s = sources[name]
            standard_refs.append(self.source(name, "ASME primary reference: " + name, s["url"],
                retrieval_scope=s["depth"], locator=s["locator"], original_bytes_archived=False))
        asme = self.node("ASME-BOUNDARY", "standards_reference_observation", "ASME PIN system and edition do not supply the exact NSN crosswalk", standard_refs,
            reference_issue_date="2023-10-16", full_code_tables_acquired=False,
            proposed_pin="AEB02F375750WA6DG1", proposed_pin_to_nsn_primary_link_verified=False)
        access = self.read(HERE / "spec/tdmt-access.json")
        td = self.source("TDMT-SHELL", "Exact TDMT link returned only an application shell", access["source_url"],
            observed=access["observed_at"], http_status=access["http_status"],
            original_body_sha256=access["original_sha256"], original_body_archived=False,
            received_bytes=access["received_bytes"], receipt_path="investigations/single-case-followup-2026-10-30/spec/tdmt-access.json",
            receipt_sha256=self.pin(HERE / "spec/tdmt-access.json"), snapshot_scope="Retained metadata only; no application HTML or target TDP",
            technical_record_acquired=False)
        policy = sources["SC-SPEC-TDMT-ACCESS"]
        tp = self.source("TDMT-POLICY", "Official TDMT access guidance observed through search index", policy["url"],
            retrieval_scope=policy["depth"], claim_scope=policy["claim"], direct_page_open_succeeded=False,
            policy_evidence_kind="official_indexed_text", live_login_screen_observed=False)
        self.tdmt = self.node("TDMT-GATE", "source_access_observation", "RFQ technical route is known; no technical package was acquired", [td, tp, self.bid_sources["SCB-S02"]],
            exact_startitem=access["exact_startitem_observed"], http_success_is_document_success=False,
            result_type=access["result_type"], technical_record_acquired=False,
            authentication_attempted=False, source_distribution_classification_verified=False,
            required_access_policy="Indexed official guidance describes AMPS and Okta MFA for external users")
        for n, src in [(self.archive, refs + [ch]), (release, [refs[2]]), (asme, standard_refs), (self.tdmt, [td, tp])]:
            self.attach(n, src)
        self.edge("links_technical_document_route", self.rfq, self.tdmt, [self.bid_sources["SCB-S02"], td])
        self.edge("retains_unresolved_specification", self.archive, "BOLT-SPEC-EXACT-ROW-GAP", refs + [ch])
        self.spec_sources = refs + [ch, td, tp] + standard_refs

    def market(self):
        data = self.read(HERE / "market-terms/observations.json")
        assert data["qualified_comparators"] == 0
        sources = {s["id"]: s for s in self.read(HERE / "market-terms/sources.json")["sources"]}
        sm = {}
        for key in ["SCM-S01", "SCM-S02", "SCM-S03", "SCM-S05", "SCM-S06"]:
            s = sources[key]
            sm[key] = self.source(key, "Public seller/distributor observation: " + key, s["url"],
                observed=s["observed_date"], source_class=s["type"], locator=s["locator"],
                snapshot_scope=s["hash_scope"], original_webpage_bytes_archived=False,
                selection_registry="investigations/single-case-followup-2026-10-30/market-terms/sources.json")
        mf = self.node("MF-PACK", "market_product_observation", "MF Supply's advertised box size is now explicitly 1,100", [sm["SCM-S01"], sm["SCM-S02"]],
            seller="MF Supply", sku="HH38FX3/4G8ZY", advertised_pack_quantity=1100,
            advertised_box_price="328.91", currency_interpretation="USD from US merchant context; page prints dollar symbol",
            displayed_boxes=7, nominal_displayed_pieces=7700, actual_stock_reservation_verified=False,
            quote_accepted=False, applicable_at_award_date_verified=False, government_equivalence=False,
            supersedes_only_prior_pack_unknown=True)
        nw = self.node("NATIONWIDE-OFFER", "market_product_observation", "Nationwide advertises a 1,100-piece carton at $190.49", [sm["SCM-S03"]],
            seller="Nationwide Industrial Supply", advertised_part="3812CH8O", advertised_carton_quantity=1100,
            advertised_case_price_1_to_4="190.49", advertised_case_price_5_plus="173.18",
            currency_interpretation="USD from US merchant context; page prints dollar symbol",
            displayed_stock_label="in_stock", available_cartons=None, delivery_or_acceptance_verified=False,
            price_observation_date=DAY, government_award_date_price_verified=False,
            actual_government_supplier_invoice=False, upstream_independence_verified=False,
            government_equivalence=False, price_excess=None, buyer_benefit=None, recoverable_loss=None)
        lot = self.node("UPSTREAM-LOT-GAP", "supply_chain_observation", "Shared reference and generic certification claims leave lot identity unresolved", [sm["SCM-S05"], sm["SCM-S06"]],
            common_catalog_reference="3812CH8O", published_catalog_origin="Canada",
            disclosed_distributor_role="master_distributor", actual_manufacturer_identified=False,
            country_restriction_violation_established=False,
            delivered_lot_origin_verified=False, exact_lot_certificate_acquired=False,
            free_generic_certifications_and_lot_control_advertised=True,
            certifications_automatically_assumed_costly=False, qup001_service_quote_acquired=False,
            number_of_seller_pages_proves_upstream_independence=False)
        for n, refs in [(mf, [sm["SCM-S01"], sm["SCM-S02"]]), (nw, [sm["SCM-S03"]]), (lot, [sm["SCM-S05"], sm["SCM-S06"]])]:
            self.attach(n, refs)
        self.edge("updates_pack_evidence_only", mf, "BOLT-MARKET-BENCHMARK-MATRIX", [sm["SCM-S01"], sm["SCM-S02"]],
            prior_dated_unknown_not_deleted=True, no_automatic_comparison_qualification=True)
        self.edge("requires_exact_specification", nw, self.archive, [sm["SCM-S03"]] + self.spec_sources[:3])
        self.market_sources = list(sm.values())

    def history_and_boundary(self):
        history = self.read(HERE / "history/acquisition.json")
        src = self.artifact("HISTORY-RECEIPT", "Bounded attempts at historical document locations", HERE / "history/acquisition.json")
        alternate = self.read(HERE / "history/additional-route-checks.json")
        alt = self.artifact("HISTORY-ALT-RECEIPT", "Two alternate public award-record routes also failed", HERE / "history/additional-route-checks.json")
        records = history["records"]
        assert len(records) == 2 and all(r["result"] == "failed_no_retry" for r in records)
        assert len(alternate["operations"]) == 2 and not any(r["document_acquired"] for r in alternate["operations"])
        hid = self.node("HISTORICAL-ROUTES", "acquisition_observation", "Historical document routes failed; award existence remains established separately", [src, alt, self.bid_sources["SCB-S03"]],
            history_lane_attempted_piids=[r["piid"] for r in records],
            history_lane_results=[dict(piid=r["piid"], result=r["result"], error_type=r["error_type"],
                url_lineage=r["url_lineage"]) for r in records],
            latest_other_attempt="SPE4A626V138W date-derived PDF route returned file-not-found text",
            history_lane_opener_operations=4, automatic_redirect_hops_separately_counted=False,
            alternate_public_award_record_opens=2, alternate_route_documents_acquired=0,
            alternate_route_lineage=alternate["scope"],
            new_historical_original_pdfs=0, awards_missing_or_concealed_inferred=False,
            actual_losing_bids_or_evaluation_records_acquired=0)
        self.attach(hid, [src, alt, self.bid_sources["SCB-S03"]])
        boundary = self.node("COMPARISON-BOUNDARY", "research_question", "Exact benchmark, actual decision and benefit evidence remain open", self.spec_sources + self.market_sources + list(self.bid_sources.values()),
            status="unknown", exact_primary_niin_characteristic_rows=0, exact_primary_niin_reference_rows=0,
            qualified_benchmarks=0, actual_competing_quote_prices=0, bid_abstracts=0, decision_memoranda=0,
            price_excess=None, supplier_cost_or_profit=None, buyer_benefit=None, paid_cash=None,
            recoverable_loss=None, new_fraud_established=False, fair_pricing_established=False,
            hypothetical_residuals_exported_as_money=False,
            next_record="Appropriately releasable exact NIIN characteristics/reference or technical package, then feasible dated equivalent offer and actual evaluation record")
        self.attach(boundary, self.spec_sources + self.market_sources)
        self.edge("keeps_price_question_open", boundary, "BOLT-PRICE-FAIRNESS-UNKNOWN", self.market_sources)
        self.edge("keeps_benefit_question_open", boundary, "BOLT-BUYER-INDEPENDENCE-UNKNOWN", list(self.bid_sources.values()))

    def finish(self, review_pins):
        omissions = []
        for name in review_pins:
            path = (ROOT / name).resolve()
            review = self.read(path)
            if review.get("decision", review.get("status")) in {"rejected", "blocked"}:
                raise ValueError("Cannot pin a rejected review as acceptance")
            rs = self.artifact("REVIEW", "Independent review of scoped source observations", path)
            rn = self.node("REVIEW", "review_assessment", "Independent challenge of this bounded follow-up", [rs],
                review_path=str(path.relative_to(ROOT)), review_claim_scope="Only the scope and exact bytes recorded in the review",
                fraud_or_price_fairness_certification=False)
            self.attach(rn, [rs])
            for a in review.get("reviewed_input_artifacts", review.get("reviewed_artifacts", [])):
                raw = a["path"]
                candidate = (ROOT.parents[1] / raw) if raw.startswith("research/") else (ROOT / raw)
                if candidate.resolve() in {HERE / "graph-extension.json", HERE / "REPORT.md", HERE / "VALIDATION.json"}:
                    omissions.append(dict(path=raw, reason="Avoid graph/review or root-summary validation cycle"))
                    continue
                if any(candidate.resolve().is_relative_to(p) for p in (ROOT / "investigations", ROOT / "price-agents")):
                    self.pin(candidate, a["sha256"])
                else:
                    omissions.append(dict(path=raw, reason="Outside approved evidence roots; retained in review receipt"))
        self.pin(__file__)
        all_new = self.nodes + self.edges
        assert len({n["id"] for n in all_new}) == len(all_new)
        assert 20 <= len(self.nodes) <= 45
        assert not any(n["type"] == "money_measure" or "money" in n["properties"] for n in self.nodes)
        existing = {r["id"]: r for r in self.old["nodes"] + self.old["edges"]}
        for item in all_new:
            if item["id"] in existing and item != existing[item["id"]]:
                raise ValueError("Prior record collision: " + item["id"])
        old_nodes = [n for n in self.old["nodes"] if n["id"] not in {a["id"] for a in self.nodes}]
        old_edges = [e for e in self.old["edges"] if e["id"] not in {a["id"] for a in self.edges}]
        spec = importlib.util.spec_from_file_location("single_case_engine", ROOT / "engine/integrity.py")
        engine = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(engine)
        engine.validate_graph(dict(version="1.0", as_of=DAY, nodes=old_nodes+self.nodes, edges=old_edges+self.edges), public=True)
        graph = dict(version="1.0", as_of=DAY,
            projection_status="proposed_requires_separate_digest_pinned_registry_approval",
            base_commit=BASE, no_actual_money_measures=True,
            input_artifacts=[dict(path=p, sha256=d) for p, d in sorted(self.inputs.items())],
            omitted_review_dependencies=omissions, nodes=self.nodes, edges=self.edges)
        path = HERE / "graph-extension.json"
        path.write_text(json.dumps(graph, indent=2, ensure_ascii=False)+"\n")
        print(json.dumps(dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            nodes=len(self.nodes), edges=len(self.edges), sources=sum(n["type"] == "source" for n in self.nodes),
            input_pins=len(self.inputs), review_pins=review_pins, canonical_registry_modified=False)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-pin", action="append", default=[])
    args = parser.parse_args()
    if len(args.review_pin) > 1:
        parser.error("This lean projection accepts one final independent producer review receipt")
    p = Projection()
    p.retained_input_pins()
    p.selection()
    p.bids()
    p.specification()
    p.market()
    p.history_and_boundary()
    p.finish(args.review_pin)


if __name__ == "__main__":
    main()
