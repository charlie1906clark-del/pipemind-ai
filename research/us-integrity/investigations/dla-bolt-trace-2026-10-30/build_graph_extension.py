#!/usr/bin/env python3
"""Build a bounded, public graph projection of the single-NSN bolt trace.

This offline generator preserves the prior observations, links exact identifiers
with dated source evidence, and separates obligations, ordered line values and
cash. It writes a candidate; approval is a separate digest-pinned manifest edit.
"""
from collections import Counter
from decimal import Decimal
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DAY = "2026-10-30"
COLLECTION = "BOLT-TRACE-20261030"
PRIOR = ROOT / "investigations/discovery-policy-2026-10-30"
PRIOR_PDF_SOURCE = "DISC-PRICE-SRC-DLA-SPE4A626U3619"
NSN_NODE = "DISC-NSN-5306016864912"


class Projection:
    def __init__(self):
        self.nodes, self.edges, self.by_id, self.inputs = [], [], {}, {}

    def pin_path(self, path, expected=None):
        path = Path(path).resolve()
        if not path.is_relative_to(ROOT / "investigations"):
            raise ValueError("Trace evidence must remain inside investigations")
        if path.is_relative_to(HERE / "current/document-attempts") and path.suffix.lower() == ".pdf":
            raise ValueError("Current original documents are not public graph dependencies; use reviewed selected artifacts")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if expected is not None and digest != expected:
            raise ValueError("Reviewed source/input digest mismatch: " + str(path))
        self.inputs[str(path.relative_to(ROOT))] = digest
        return digest

    def pin(self, relative, expected=None):
        return self.pin_path(HERE / relative, expected)

    def read(self, relative):
        self.pin(relative)
        return json.loads((HERE / relative).read_text())

    def node(self, ident, node_type, title, sources=(), status="documented_fact", **props):
        if not ident.startswith("BOLT-") or ident in self.by_id:
            raise ValueError("Invalid or duplicate bolt-trace ID: " + ident)
        record = dict(id=ident, type=node_type, title=title, status=status,
            source_ids=sorted(set(sources)), properties={"visibility": "public", **props})
        self.nodes.append(record)
        self.by_id[ident] = record
        return ident

    def edge(self, relationship, subject, obj, sources=(), status="documented_fact", **props):
        ident = "BOLT-E-" + hashlib.sha256(f"{relationship}|{subject}|{obj}".encode()).hexdigest()[:20]
        if any(row["id"] == ident for row in self.edges):
            raise ValueError("Duplicate trace relationship")
        self.edges.append(dict(id=ident, type=relationship, source=subject, target=obj,
            status=status, source_ids=sorted(set(sources)), properties={"visibility": "public", **props}))

    def source(self, ident, title, url, snapshot=None, expected_hash=None, accessed_at=DAY, **props):
        properties = dict(url=url, accessed_at=accessed_at, source_bytes_archived=False, **props)
        if snapshot:
            digest = self.pin(snapshot, expected_hash)
            properties.update(source_bytes_archived=True, content_sha256=digest,
                snapshot_path=str((HERE / snapshot).relative_to(ROOT)))
        return self.node(ident, "source", title, status="source", **properties)

    def finding(self, ident, title, sources, node_type="finding", status="documented_fact", **props):
        self.node(ident, node_type, title, sources, status, **props)
        self.edge("records_finding", COLLECTION, ident, sources, status)
        return ident

    def money(self, ident, title, sources, amount, amount_kind, period, qualifier="as_reported", **props):
        return self.node(ident, "money_measure", title, sources,
            money=dict(amount=str(amount), currency="USD", kind=amount_kind, period=period,
                qualifier=qualifier, basis=props.pop("basis", "Explicit source-reported measure")),
            aggregation_permitted=False, independently_verified_collection=False, **props)

    def awards(self):
        previous_path = PRIOR / "pricing/snapshots/selected_evidence.json"
        self.pin_path(previous_path)
        history = json.loads(previous_path.read_text())["observations"]
        history_by_key = {row["contract_number"]: (i, row) for i, row in enumerate(history, 1)}
        coverage = self.read("awards/capture-success/coverage.json")
        manifest = self.read("awards/capture-success/manifest.json")
        if coverage["missing_keys"] or set(coverage["requested_keys"]) != set(history_by_key):
            raise ValueError("Award coverage must match the seven declared historical keys")
        if not coverage["terminal_page_empty"]:
            raise ValueError("Award search completion evidence missing")
        refs = {}
        for row in manifest:
            if row["http_status"] != 200:
                raise ValueError("Successful award manifest contains a failed response")
            if row.get("request_file"):
                self.pin("awards/capture-success/" + row["request_file"], row["request_sha256"])
            refs[row["id"]] = self.source("BOLT-SRC-" + row["id"], "USAspending exact contract capture: " + row["id"],
                row["url"], snapshot="awards/capture-success/" + row["snapshot"],
                expected_hash=row["snapshot_sha256"], accessed_at=row["retrieved_at_utc"],
                snapshot_scope=row["snapshot_scope"], original_wire_archived=row["wire_bytes_archived"],
                original_wire_sha256=row["wire_sha256"], request_sha256=row.get("request_sha256"),
                method=row["method"], manifest_path="awards/capture-success/manifest.json")
        coverage_sources = [refs["exact-award-search"], refs["exact-award-terminal"], PRIOR_PDF_SOURCE]
        self.finding("BOLT-AWARD-COVERAGE", "All seven declared historical PIIDs resolved in the bounded official search",
            coverage_sources, node_type="dataset_cohort", coverage=coverage,
            total_observation_count=7, nationwide_coverage=False, no_fraud_ranking=True)
        summaries = {}
        for key, (i, historical) in history_by_key.items():
            detail = self.read("awards/capture-success/award-" + key + ".json")
            if detail["piid"] != key:
                raise ValueError("Award response PIID mismatch")
            recipient = detail["recipient"]
            transaction = detail["latest_transaction_contract_data"]
            refs_for_award = [refs["award-" + key]]
            observation = dict(piid=key, generated_award_id=detail["generated_unique_award_id"],
                date_signed=detail["date_signed"], instrument=detail["type_description"],
                description=detail["description"], recipient_uei=recipient["recipient_uei"],
                recipient_name_as_reported=recipient["recipient_name"],
                source_reports_offers=transaction["number_of_offers_received"],
                source_reports_competition=transaction["extent_competed_description"],
                source_reports_pricing=transaction["type_of_contract_pricing_description"],
                solicitation_identifier=transaction["solicitation_identifier"],
                total_outlay=detail["total_outlay"], historical_clin_acquired=False, cash_payment_verified=False)
            aid = self.node("BOLT-AWARD-" + key, "award_observation", key + ": official award observation", refs_for_award,
                observation=observation, no_adverse_inference=True,
                source_scope="Award summary and latest contract transaction, not priced line item or invoice")
            self.edge("includes_award_observation", "BOLT-AWARD-COVERAGE", aid, refs_for_award)
            mid = self.money("BOLT-OBLIGATION-" + key, key + ": cumulative obligation", refs_for_award,
                detail["total_obligation"], "cumulative_award_obligation", detail["date_signed"],
                qualifier="reported_as_of_2026-10-30", no_cash_or_loss_inference=True)
            self.edge("reports_obligation", aid, mid, refs_for_award)
            product = Decimal(historical["quantity_as_printed"]) * Decimal(historical["unit_cost_as_printed"])
            obligation = Decimal(str(detail["total_obligation"]))
            if product != obligation or historical["award_date"] != detail["date_signed"]:
                raise ValueError("Historical date or amount reconciliation changed; requires review")
            reconciliation = self.finding("BOLT-RECONCILIATION-" + key, key + ": printed quantity × cost equals reported obligation",
                refs_for_award + [PRIOR_PDF_SOURCE],
                exact_contract_key=key, history_quantity=historical["quantity_as_printed"],
                history_unit_cost=historical["unit_cost_as_printed"], product=str(product),
                obligation_usd=str(obligation), dates_match=True,
                inference_limit="Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement")
            self.edge("checks_award", reconciliation, aid, refs_for_award + [PRIOR_PDF_SOURCE])
            self.edge("checks_prior_history_row", reconciliation, f"DISC-PRICE-HISTORY-{i:02d}", refs_for_award + [PRIOR_PDF_SOURCE],
                join_basis="Exact printed PIID; no supplier-name inference")
            self.edge("history_reports_cage", aid, "DISC-CAGE-" + historical["cage"], [PRIOR_PDF_SOURCE],
                join_basis="Exact PIID in original RFQ history; award summary alone does not independently verify CAGE registration")
            summaries[key] = observation
        return refs, summaries

    def identities(self, awards):
        records = self.read("identity/entity_records.json")
        relationships = self.read("identity/relationships.json")["relationships"]
        registry = self.read("identity/sources.json")["sources"]
        refs = {"BI-S-HISTORY": PRIOR_PDF_SOURCE}
        for row in registry:
            self.pin_path(HERE / "identity" / row["snapshot_path"], row["snapshot_sha256"])
            if row["id"] == "BI-S-HISTORY":
                continue
            if row["id"].startswith("BI-S-AWARD-"):
                refs[row["id"]] = "BOLT-SRC-award-" + row["id"].removeprefix("BI-S-AWARD-")
                continue
            refs[row["id"]] = self.source("BOLT-SRC-" + row["id"], row["title"], row["url"],
                snapshot="identity/" + row["snapshot_path"], expected_hash=row["snapshot_sha256"],
                accessed_at=row["accessed_on"], snapshot_scope=row["snapshot_scope"],
                original_wire_archived=row["original_wire_bytes_archived"])
        if len(records["entities"]) != 5 or len(relationships) != 29:
            raise ValueError("The reviewed five-supplier identity scope changed")
        for entry in records["input_artifacts"]:
            self.pin_path(HERE / "identity" / entry["path"], entry["sha256"])
        supplier_sources = []
        for row in records["entities"]:
            cage, uei = row["cage"], row["uei"]
            sources = [refs[s] for s in row["source_ids"]]
            supplier_sources.extend(sources)
            eid = self.node("BOLT-SUPPLIER-" + cage, "supplier_identity_record", row["legal_business_name"], sources,
                exact_cage=cage, exact_uei=uei, recipient_record_type=row["recipient_record_type"],
                business_structure_types=row["business_structure_types"], public_record=True,
                profile_location=row["profile_location"], identity_as_of=row["current_registry_as_of"],
                beneficial_owners=None, historical_registration_status=None,
                sam_active_registration_verified=False, no_adverse_inference=True)
            uid = self.node("BOLT-UEI-" + uei, "identifier", "UEI " + uei,
                [refs["BI-S-CAGE-" + cage]], identifier_scheme="UEI", identifier_value=uei)
            self.edge("includes_supplier_observation", COLLECTION, eid, sources)
            self.edge("source_reports_uei", eid, uid, [refs["BI-S-CAGE-" + cage]], observed_on=DAY)
            self.edge("current_registry_crosswalk", "DISC-CAGE-" + cage, uid, [refs["BI-S-CAGE-" + cage]],
                observed_on=DAY, historical_validity_inferred=False)
            for link in row["historical_award_links"]:
                key = link["contract_number"]
                if awards[key]["recipient_uei"] != uei or awards[key]["date_signed"] != link["award_date"]:
                    raise ValueError("Exact historical supplier/award join changed")
                self.edge("source_reports_award_recipient", "BOLT-AWARD-" + key, eid,
                    [refs[s] for s in link["source_ids"]], effective_date=link["award_date"],
                    join_basis=link["method"], ownership_inferred=False)
            parent = row["reporting_parent"]
            if parent["uei"] != uei or not parent["same_uei_as_child"]:
                raise ValueError("Reporting hierarchy changed; review before adding parent identities")
            self.edge("source_reports_parent", eid, uid, [refs[s] for s in parent["source_ids"]],
                observed_on=DAY, same_uei_as_child=True, source_reported_name=parent["name"],
                meaning=parent["meaning"], beneficial_ownership_inferred=False)
            for i, alias in enumerate(row["reported_aliases"], 1):
                aid = self.node(f"BOLT-ALIAS-{cage}-{i:02d}", "reported_alias", alias,
                    [refs["BI-S-PROFILE-" + cage]], observed_on=DAY, effective_date=None,
                    independent_legal_name_history_verified=False, separate_legal_entity_inferred=False)
                self.edge("source_reports_alternate_name", eid, aid, [refs["BI-S-PROFILE-" + cage]], observed_on=DAY)
        self.finding("BOLT-IDENTITY-COVERAGE", "Five current CAGE–UEI crosswalks corroborate the seven historical award joins",
            supplier_sources, node_type="dataset_cohort",
            summary={k: v for k, v in records["summary"].items() if k != "recipient_query_profiles"},
            inference_limits="Current registry matches do not prove historical registration eligibility, active SAM status, beneficial ownership or misconduct")
        self.finding("BOLT-OWNERSHIP-LIMIT", "All five reporting-parent fields are self-UEI records; beneficial ownership remains unresolved",
            [refs["BI-S-PROFILE-" + row["cage"]] for row in records["entities"]],
            identified_beneficial_owners=0, unknown_beneficial_ownership_records=5,
            no_ownership_edge_created=True, source_parent_is_not_beneficial_owner=True)

    def current(self):
        observation = self.read("current/observations.json")
        registry = self.read("current/sources.json")["sources"]
        manifest = self.read("current/selected_manifest.json")
        selected = {row["source_id"]: row for row in manifest["records"]}
        for row in registry:
            props = {k: v for k, v in row.items() if k not in ("id", "title", "url", "accessed_at")}
            if row["id"] in selected:
                evidence = selected[row["id"]]
                if evidence["original_pdf_archived_in_public_repo"]:
                    raise ValueError("Full current award documents must not enter the public trace")
                artifacts = []
                for capture in evidence["selected_artifacts"]:
                    self.pin("current/" + capture["path"], capture["sha256"])
                    artifacts.append({**capture, "path": "investigations/dla-bolt-trace-2026-10-30/current/" + capture["path"]})
                primary = evidence["selected_artifacts"][0]
                self.source(row["id"], row["title"], row["url"], "current/" + primary["path"], primary["sha256"],
                    snapshot_scope=primary["hash_scope"], additional_selected_artifacts=artifacts,
                    derivation=manifest["derivation"], original_wire_archived=False, **props)
            else:
                self.source(row["id"], row["title"], row["url"], **props)
        parent, child = observation["parent"], observation["child_order"]
        psrc, csrc = parent["source_id"], child["source_id"]
        if Decimal(parent["unit_price"]) != Decimal(child["unit_price"]):
            raise ValueError("Parent and order unit prices differ; review required")
        if Decimal(child["quantity"]) * Decimal(child["unit_price"]) != Decimal(child["order_line_total"]):
            raise ValueError("Ordered line arithmetic changed")
        pid = self.node("BOLT-PARENT-SPE4A626D61WS", "contract_observation", "SPE4A626D61WS: parent contract terms", [psrc],
            observation=parent, money_aggregation_permitted=False,
            archived_scope="Selected neutral pages 2 and 5; full PDF is not in the public repository")
        oid = self.node("BOLT-ORDER-SPE4A627F0588", "order_observation", "SPE4A627F0588: 906 EA ordered at USD 0.91 each", [psrc, csrc],
            observation=child, money_aggregation_permitted=False,
            archived_scope="Selected neutral page 2; full PDF is not in the public repository")
        self.edge("includes_current_contract", COLLECTION, pid, [psrc])
        self.edge("issued_under", oid, pid, [psrc, csrc], join_basis="Exact parent PIID and basic CLIN reference on order page 2")
        for node, source in [(pid, psrc), (oid, csrc)]:
            self.edge("orders_item", node, NSN_NODE, [source])
            self.edge("source_reports_contractor", node, "BOLT-SUPPLIER-8A1E8", [source],
                join_basis="Exact CAGE in original award/order; source page 1 inspected but not archived publicly")
        price = self.money("BOLT-CURRENT-UNIT-PRICE", "Executed parent and order price: USD 0.91 per EA", [psrc, csrc],
            child["unit_price"], "contract_unit_price", parent["award_date"] + " to " + child["order_date"],
            unit_of_issue="EA", no_historical_unit_inference=True)
        ceiling = self.money("BOLT-PARENT-CEILING", "Parent ceiling: USD 350,000; not an order or payment", [psrc],
            parent["contract_ceiling"], "contract_ceiling", parent["award_date"], no_payment_or_loss_inference=True)
        ordered = self.money("BOLT-ORDERED-LINE-VALUE", "Order CLIN 0001: USD 824.46 ordered value", [csrc, psrc],
            child["order_line_total"], "ordered_line_value", child["order_date"], no_payment_or_loss_inference=True)
        self.edge("reports_unit_price", pid, price, [psrc])
        self.edge("reports_unit_price", oid, price, [csrc, psrc])
        self.edge("reports_ceiling", pid, ceiling, [psrc])
        self.edge("reports_ordered_value", oid, ordered, [csrc])
        self.finding("BOLT-CURRENT-LINE-RECONCILIATION", "The current ordered line reconciles: 906 EA × USD 0.91 = USD 824.46",
            [psrc, csrc], arithmetic=child["arithmetic"], parent_child_price_consistent=True,
            delivery_verified=False, receipt_or_acceptance_verified=False, payment_verified=False,
            all_orders_under_parent_acquired=False)
        self.finding("BOLT-RFQ-TERM-CHANGES", "Minimum order quantity and delivery days changed between RFQ and parent award",
            [PRIOR_PDF_SOURCE, psrc], observation=observation["term_changes_from_rfq"],
            inference_limit="RFQ terms cannot automatically substitute for executed terms; no misconduct inference")
        query_sources = []
        for query in observation["public_database_observation"]["success_queries"] + observation["public_database_observation"]["failed_503_queries"]:
            capture = self.read("current/" + query + "-manifest.json")
            self.pin("current/" + query + "-request.json", capture["request_sha256"])
            successful = capture.get("status") == 200
            sid = "BOLT-SRC-CURRENT-QUERY-" + query
            if successful:
                response = self.read("current/" + query + "-response.json")
                if response.get("results") != []:
                    raise ValueError("Current query result changed; false-absence review required")
                self.source(sid, "Current public API query: " + query, capture["url"],
                    "current/" + query + "-response.json", capture["response_sha256"], capture["accessed_at"],
                    request_sha256=capture["request_sha256"], snapshot_scope="Original empty API response bytes",
                    request_path="investigations/dla-bolt-trace-2026-10-30/current/" + query + "-request.json")
            else:
                self.source(sid, "Failed current public API query: " + query, capture["url"],
                    accessed_at=capture["accessed_at"], error=capture["error"],
                    request_sha256=capture["request_sha256"], retrieval_successful=False,
                    failed_response_is_not_empty_result=True)
            query_sources.append(sid)
        self.finding("BOLT-PUBLICATION-LAG-LIMIT", "Three empty public queries and two HTTP 503 failures do not show award absence or concealment",
            query_sources + ["BOLT-CUR-S03", "BOLT-CUR-S04", psrc, csrc],
            observation=observation["public_database_observation"], inference_status="Plausible normal lag; exact cause unverified")
        self.finding("BOLT-CURRENT-COMPARISON-LIMIT", "Current USD 0.91/EA is verified in priced documents; historical like-for-like comparison remains unresolved",
            [psrc, csrc, PRIOR_PDF_SOURCE], observation=observation["comparison_status"],
            historical_priced_clins_acquired=0, historical_units_not_inherited=True,
            fraud_established=False, loss_calculated=False, reward_assessed=False)

    def review(self):
        review = self.read("review/review.json")
        if review["status"] != "completed" or review["public_neutral_graph_decision"] != "accept_with_recorded_limits":
            raise ValueError("A completed neutral-graph review is required")
        for row in review["input_artifacts"]:
            self.pin(row["path"], row["sha256"])
        refs = {"BR-S01": PRIOR_PDF_SOURCE, "BR-S06": "BOLT-CUR-S01", "BR-S07": "BOLT-CUR-S02",
            "BI-S-HISTORY": PRIOR_PDF_SOURCE, "BOLT-AWD-SEARCH": "BOLT-SRC-exact-award-search"}
        for node in self.nodes:
            if node["type"] != "source":
                continue
            refs[node["id"]] = node["id"]
            if node["id"].startswith("BOLT-SRC-award-"):
                refs["BOLT-AWD-" + node["id"].removeprefix("BOLT-SRC-award-")] = node["id"]
            if node["id"].startswith("BOLT-SRC-BI-S-"):
                refs[node["id"].removeprefix("BOLT-SRC-")] = node["id"]
        for row in self.read("review/sources.json")["sources"]:
            if row["id"] in refs:
                if row.get("bytes_archived"):
                    self.pin_path(HERE / "review" / row["path"], row["sha256"])
                continue
            props = {k: v for k, v in row.items() if k not in ("id", "title", "url", "accessed_at", "web_ref", "bytes_archived")}
            refs[row["id"]] = self.source("BOLT-SRC-" + row["id"], row["title"], row["url"],
                accessed_at=row["accessed_at"], **props)
        # The review's source-path receipts are not substitutes for the underlying
        # official responses. Preserve the ten bounded recipient-query captures.
        identity_query_sources = []
        for row in self.read("identity/capture_manifest.json")["requests"]:
            if "-recipient-page-" not in row["id"]:
                continue
            if row["http_status"] != 200:
                raise ValueError("Reviewed identity capture changed")
            self.pin("identity/" + row["request_path"], row["request_sha256"])
            sid = self.source("BOLT-SRC-IDENTITY-QUERY-" + row["id"], "Bounded recipient query: " + row["id"], row["url"],
                "identity/" + row["snapshot_path"], row["snapshot_sha256"], row["accessed_at"],
                snapshot_scope=row["selection"], original_wire_archived=row["original_wire_bytes_archived"],
                original_wire_sha256=row["wire_response_sha256"], request_sha256=row["request_sha256"])
            identity_query_sources.append(sid)
        spotcheck_sources = []
        for row in self.read("review/spotchecks/manifest.json"):
            if not row["producer_selected_fields_match"] or row["http_status"] != 200:
                raise ValueError("Independent spotcheck failed")
            spotcheck_sources.append(self.source("BOLT-SRC-SPOTCHECK-" + row["contract_number"],
                "Independent exact-award spotcheck: " + row["contract_number"], row["url"],
                "review/spotchecks/" + row["snapshot"], row["snapshot_sha256"], row["retrieved_at_utc"],
                snapshot_scope=row["snapshot_scope"], original_wire_archived=row["wire_bytes_archived"],
                original_wire_sha256=row["wire_sha256"]))
        award_sources = [node["id"] for node in self.nodes if node["id"].startswith("BOLT-SRC-award-")]
        identity_sources = [node["id"] for node in self.nodes if node["id"].startswith("BOLT-SRC-BI-S-")]
        all_review_sources = sorted(set(refs.values()) | set(award_sources + identity_sources + identity_query_sources + spotcheck_sources))
        rid = self.finding("BOLT-INDEPENDENT-REVIEW", "Independent single-NSN review completed with recorded limits",
            all_review_sources, node_type="review_record", reviewer_task=review["reviewer"],
            method=review["method"], summary=review["summary"], tests=review["tests"],
            review_decision=review["public_neutral_graph_decision"],
            evidence_receipt_path="investigations/dla-bolt-trace-2026-10-30/review/review.json",
            scope_limit=review["scope_limit"])
        targets = {
            "BREV-F01": "DISC-RFQ-SPE4A626U3619", "BREV-F02": "BOLT-AWARD-COVERAGE",
            "BREV-F03": "BOLT-CURRENT-LINE-RECONCILIATION", "BREV-F04": "BOLT-CURRENT-UNIT-PRICE",
            "BREV-F05": "BOLT-PARENT-SPE4A626D61WS", "BREV-F06": "BOLT-RFQ-TERM-CHANGES",
            "BREV-F07": "BOLT-IDENTITY-COVERAGE", "BREV-F08": "BOLT-CURRENT-COMPARISON-LIMIT",
            "BREV-F09": "BOLT-PUBLICATION-LAG-LIMIT", "BREV-F10": "BOLT-AWARD-COVERAGE"}
        if set(targets) != {row["id"] for row in review["findings"]}:
            raise ValueError("Reviewed finding set changed; explicit mapping needs review")
        for row in review["findings"]:
            if row["new_named_adverse_allegation"]:
                raise ValueError("Novel adverse allegations are outside this neutral trace")
            sources = [refs[s] for s in row["source_ids"]]
            if row["id"] in ("BREV-F02", "BREV-F10"):
                sources += award_sources + spotcheck_sources
            if row["id"] == "BREV-F07":
                sources += identity_sources + identity_query_sources + award_sources
            for path in row["source_paths"]:
                self.pin(path)
            fid = self.finding("BOLT-" + row["id"], row["title"], sources, node_type="review_assessment",
                statement=row["statement"], review_decision=row["decision"], locator=row["locator"],
                evidence_limits=row["evidence_limits"], review_input_paths=row["source_paths"],
                new_named_adverse_allegation=False)
            self.edge("records_review_assessment", rid, fid, sources)
            self.edge("assesses_evidence", fid, targets[row["id"]], sources,
                review_decision=row["decision"])
        next_step = self.finding("BOLT-NEXT-DISCRIMINATING-EVIDENCE", "Historical CLINs and governing terms remain the next discriminating evidence",
            [PRIOR_PDF_SOURCE, "BOLT-CUR-S01", "BOLT-CUR-S02"], node_type="research_question", status="planned",
            questions=review["next_discriminating_evidence"], executed=False,
            no_background_monitoring_or_external_model_execution_claimed=True)
        self.edge("identifies_remaining_evidence", rid, next_step,
            [PRIOR_PDF_SOURCE, "BOLT-CUR-S01", "BOLT-CUR-S02"], status="planned")

    def price_challenge(self):
        methods = self.read("price-challenge/method_sources.json")
        mechanism = self.read("price-challenge/mechanism_sources.json")
        requirements = self.read("price-challenge/evidence_requirements.json")
        refs = {}
        for row in methods["sources"] + mechanism["sources"]:
            props = {k: v for k, v in row.items() if k not in ("id", "title", "url", "accessed_at", "web_ref")}
            refs[row["id"]] = self.source("BOLT-" + row["id"], row["title"], row["url"],
                accessed_at=row["accessed_at"], original_wire_archived=False,
                capture_scope="Web text reviewed; only research summaries retained, not original webpage bytes", **props)
        method_sources = [refs[row["id"]] for row in methods["sources"]]
        known_sources = [refs[row["id"]] for row in mechanism["sources"]]
        framework = self.finding("BOLT-PRICE-FAIRNESS-AUDIT", "Price fairness and buyer independence require separate evidence beyond document arithmetic",
            method_sources + known_sources + ["BOLT-CUR-S01", "BOLT-CUR-S02"], node_type="audit_framework",
            scope=requirements["scope"], framework_origin="Research design informed by the cited official methodology and known-case mechanisms",
            actual_cohort_price_fairness="unknown", actual_cohort_buyer_independence="unknown",
            benchmark_relative_difference=None, buyer_benefit=None, fraud_finding=False,
            normalization_rules=requirements["normalization_rules"])
        fairness = self.finding("BOLT-PRICE-FAIRNESS-UNKNOWN", "The verified USD 0.91 document price does not establish market fairness",
            method_sources[:2] + ["BOLT-CUR-S01", "BOLT-CUR-S02"], node_type="research_question", status="unknown",
            document_arithmetic_verified=True, independent_like_for_like_benchmark_verified=False,
            reasonable_price_determination_examined=False, excess_price=None, recoverable_loss=None)
        independence = self.finding("BOLT-BUYER-INDEPENDENCE-UNKNOWN", "Buyer decision roles, bid independence and benefit relationships remain unverified",
            method_sources + known_sources, node_type="research_question", status="unknown",
            individual_decision_roles_established=False, actual_bid_files_examined=False,
            improper_benefit_evidence_for_this_cohort=False, named_buyer_accused=False,
            inference_limit="Registry consistency, reported offer counts and correct arithmetic do not establish independent procurement decisions")
        for question in [fairness, independence]:
            self.edge("separately_tests", framework, question, method_sources)
        for row in requirements["finding_classes"]:
            ident = self.node("BOLT-PRICE-CLASS-" + row["id"], "audit_classification_definition",
                row["id"].replace("_", " ").capitalize(), method_sources + known_sources, status="planned",
                definition=row, applied_to_current_cohort=False, framework_origin="Research classification, not an official finding")
            self.edge("defines_finding_class", framework, ident, method_sources + known_sources, status="planned")
        for row in requirements["tests"]:
            ident = self.node("BOLT-" + row["id"], "audit_protocol", row["name"], method_sources + known_sources,
                status="planned", protocol=row, execution_status="Protocol defined; complete real-data test not established",
                legal_fraud_threshold=False, named_adverse_inference=False)
            self.edge("specifies_test", framework, ident, method_sources + known_sources, status="planned")
        for row in requirements["record_acquisition_queue"]:
            ident = self.node("BOLT-" + row["id"], "research_question", row["record"], method_sources,
                status="planned", acquisition_requirement=row, requested_or_obtained_by_this_node=False)
            self.edge("requires_evidence", framework, ident, method_sources, status="planned")
        self.finding("BOLT-PRICE-EVIDENCE-CONTRACT", "Required evidence fields separate price, decision roles and actual benefits",
            method_sources, node_type="evidence_schema", status="planned", field_groups=requirements["record_fields"],
            schema_not_populated_personal_data=True)
        for row in mechanism["cases"]:
            ident = self.node("BOLT-" + row["id"], "mechanism_calibration", row["label"],
                [refs[s] for s in row["source_ids"]],
                classification=row["classification"], legal_status_as_reported=row["legal_status"],
                mechanism=row["source_reported_mechanism"],
                source_reported_evidence=row["source_reported_evidence_and_investigative_steps"],
                amount_interpretation=row["amount_interpretation"],
                researcher_inferences=row["researcher_inferences_for_dla_screen"],
                transfer_limitations=row["transfer_limitations"],
                linked_to_studied_dla_participants=False, price_comparator=False, new_case_claimed=False)
            self.edge("calibrates_control_questions", framework, ident, [refs[s] for s in row["source_ids"]])
        hypothesis = self.finding("BOLT-REPEATED-PREMIUM-HYPOTHESIS", "A repeated unexplained premium is a testable hypothesis, not evidence of a buyer kickback",
            method_sources + known_sources, node_type="research_hypothesis", status="hypothesis",
            proposed_rate="0.12", rate_origin="User-proposed illustrative screening hypothesis",
            repeated_real_cohort_premium_established=False, benchmark_eligibility_required=True,
            complete_declared_universe_required=True, independent_solicitations_required=True,
            buyer_benefit=None, actual_loss=None, named_adverse_entities=[],
            ordinary_alternatives="Margin, quantity, technical requirements, freight, delivery, risk and composition changes need review")
        self.edge("tests_hypothesis", framework, hypothesis, method_sources + known_sources, status="planned")
        return refs

    def market(self):
        matrix = self.read("market/benchmark_matrix.json")
        registry = self.read("market/sources.json")
        captures = {r["path"]: r for r in self.read("market/capture_manifest.json")["captures"]}
        refs = {}
        for row in registry["sources"]:
            props = {k: v for k, v in row.items() if k not in ("id", "url", "web_ref", "capture")}
            if row.get("capture"):
                capture = captures[row["capture"]]
                refs[row["id"]] = self.source("BOLT-" + row["id"],
                    row["id"] + " — " + row["source_type"].replace("_", " "), row["url"],
                    "market/" + capture["path"], capture["sha256"], registry["observed_date"],
                    snapshot_scope=capture["hash_scope"], original_website_bytes_archived=False,
                    original_wire_archived=False, **props)
            else:
                refs[row["id"]] = self.source("BOLT-" + row["id"],
                    row["id"] + " — " + row["source_type"].replace("_", " "), row["url"],
                    accessed_at=registry["observed_date"], original_website_bytes_archived=False, **props)
        qualified = matrix["qualified_comparison"]
        if qualified["eligible"] or qualified["eligible_comparator_count"] != 0 or any(
                qualified[k] is not None for k in ("price_premium", "overcharge_amount", "kickback_amount", "loss_amount")):
            raise ValueError("Qualified market comparison changed; obtain a fresh independent review")
        sources = list(refs.values()) + ["BOLT-CUR-S01", "BOLT-CUR-S02", "BOLT-PC-METHOD-S01", "BOLT-PC-METHOD-S02"]
        mid = self.finding("BOLT-MARKET-BENCHMARK-MATRIX", "Three provisional catalog candidates; zero qualified DLA price comparators",
            sources, node_type="benchmark_review", qualified_comparison=qualified,
            candidate_count=len(matrix["candidates"]), candidate_spec_origin=matrix["candidate_spec_origin"],
            conclusion=matrix["conclusion"], price_fairness_established=False,
            no_new_named_adverse_inference=True, independent_market_price_verified=False)
        for row in matrix["candidates"]:
            candidate_sources = [refs[row["source_id"]]] + [refs[s] for s in row.get("terms_source_ids", [])]
            if row["qualification_status"] not in {"excluded_from_transactable_quote_set", "provisional_product_comparator"}:
                raise ValueError("Market candidate became qualified without explicit projection review")
            ident = self.node("BOLT-" + row["id"], "market_product_observation", row["seller"] + ": " + row["sku"], candidate_sources,
                observation={k: v for k, v in row.items() if k not in ("id", "source_id", "terms_source_ids")},
                observation_kind="Posted catalog data, not an accepted government-compliant quote",
                exact_nsn_equivalence_verified=False, eligible_for_price_premium=False,
                no_suspect_classification=True, no_money_export=True)
            self.edge("screens_candidate", mid, ident, candidate_sources)
            self.edge("screened_as_possible_comparator_for", ident, NSN_NODE, candidate_sources + ["BOLT-CUR-S01"],
                exact_identity_asserted=False, eligibility="blocked", no_equivalence_merge=True)
            self.finding("BOLT-MARKET-GATE-" + row["id"], row["seller"] + ": comparison gate remains blocked",
                candidate_sources + ["BOLT-CUR-S01", "BOLT-CUR-S02"], node_type="comparison_gate",
                candidate_id=ident, qualification_status=row["qualification_status"],
                reasons=row["limitations"], qualified_comparator=False,
                price_premium=None, government_loss=None, buyer_benefit=None)
        self.finding("BOLT-MARKET-COMPARABILITY-REQUIREMENTS", "Market comparisons require item, quantity and accepted supply-term reconciliation",
            sources, node_type="audit_gate_set", status="planned", required_gates=matrix["required_gates"],
            execution_scope="Requirements for this research workflow; legal applicability must be checked separately")
        self.finding("BOLT-MARKET-UPSTREAM-INDEPENDENCE", "Two provisional sellers share a reported part reference; upstream independence is unverified",
            [refs["MKT-SRC-FSS"], refs["MKT-SRC-MF"]], reported_shared_reference="3812CH8O",
            common_ownership_inferred=False, collusion_inferred=False, independent_benchmarks_established=False,
            limit="A shared supplier reference does not establish common ownership, coordinated pricing or misconduct")
        spec = self.read("market/spec-crosswalk.json")
        spec_sources = ["BOLT-CUR-S01", "BOLT-SRC-BR-S02"]
        for row in spec["sources"]:
            if row["id"] == "SPEC-P01":
                self.pin(row["local_path_relative_to_investigation"], row["sha256_selected_text"])
                continue
            spec_sources.append(self.source("BOLT-" + row["id"], "Official catalog route: " + row["id"], row["url"],
                retrieval_status=row["open_status"], evidence_scope=row["type"],
                search_index_lead=row.get("search_index_lead"), exact_nsn_record_acquired=False,
                failed_access_does_not_establish_absence=True))
        gap = self.finding("BOLT-NSN-SPEC-CROSSWALK-GAP", "An exact primary NSN-to-commercial-specification bridge has not been acquired",
            spec_sources, node_type="research_question", status="unknown", primary_verified=spec["primary_verified"],
            candidate_part_reference=spec["unverified_candidate_association"]["part_reference"],
            candidate_part_reference_primary_confirmation=False, decision=spec["decision"],
            bounded_search=spec["bounds"], next_required_evidence=spec["next_required_evidence"])
        self.edge("requires_resolved_crosswalk", mid, gap, spec_sources, status="planned")
        self.edge("keeps_fairness_question_open", mid, "BOLT-PRICE-FAIRNESS-UNKNOWN", sources)
        return refs

    def specification(self):
        observation = self.read("specification/specification_record.json")
        registry = self.read("specification/sources.json")["sources"]
        directory = self.read("specification/archive-directory.json")
        metadata = self.read("specification/archive-metadata-access.json")
        members = self.read("specification/member-format-inspection.json")["members"]
        self.pin("specification/reading-room-access.json")
        if directory["entry_count"] != len(directory["entries"]) or metadata["status"] != 200:
            raise ValueError("Public catalog archive metadata changed")
        if observation["verified_item_characteristics"] is not None or observation["exact_nsn_to_retail_specification_match"] is not None:
            raise ValueError("Primary specification gate changed; review the actual extracted record before promotion")
        refs = []
        for row in registry:
            props = {k: v for k, v in row.items() if k not in ("id", "url", "retrieved_on", "web_ref")}
            if row["id"] == "BOLT-SPEC-DLA-ARCHIVE":
                refs.append(self.source(row["id"], "DLA public PUB LOG archive: partial metadata capture", row["url"],
                    "specification/archive-directory.json", accessed_at=directory["accessed_at"],
                    snapshot_scope="Structured ZIP directory metadata extracted from HTTP ranges; not original archive or raw range bytes",
                    original_wire_archived=False, range_reads=directory["range_reads"], **props))
            else:
                refs.append(self.source(row["id"], row["id"] + ": official catalog route", row["url"],
                    accessed_at=row["retrieved_on"], original_wire_archived=False, **props))
        for member in members:
            if not member.get("selected_file"):
                continue
            refs.append(self.source("BOLT-SPEC-TOOLS-README", "PUB LOG tools: selected DECOMP extraction instructions", directory["url"],
                "specification/" + member["selected_file"], member["selected_sha256"],
                snapshot_scope=member["selected_scope"], member_name=member["name"],
                original_member_sha256=member["original_member_sha256"],
                original_member_archived_in_repo=member["original_member_archived_in_repo"],
                original_wire_archived=False, archive_complete=False, executable_run=False))
        self.finding("BOLT-SPEC-PUBLIC-ROUTE", "The public catalog archive is accessible; its member inventory and reader instructions were inspected",
            refs, node_type="acquisition_observation", archive_bytes=directory["archive_bytes"],
            archive_entry_count=directory["entry_count"], metadata_bytes_received=sum(r["bytes"] for r in directory["range_reads"]),
            full_archive_downloaded=False, exact_niin_record_extracted=False,
            member_inspection=[{"name": r["name"], "complete_member": r["complete_member"],
                "compressed_bytes_read": r["compressed_bytes_read"], "uncompressed_bytes_read": r["uncompressed_bytes_read"]} for r in members],
            executable_run=False, restriction_or_absence_inferred=False)
        gap = self.finding("BOLT-SPEC-EXACT-ROW-GAP", "The exact NIIN record remains unextracted; commercial equivalence is still unresolved",
            refs + ["BOLT-CUR-S01"], node_type="research_question", status="unknown", observation=observation,
            technical_evidence_gap=True, data_privacy_or_unavailability_inferred=False,
            source_scope="Public archive route and member format, not an authenticated item characteristic row")
        self.edge("investigates_specification_for", gap, NSN_NODE, refs + ["BOLT-CUR-S01"])
        self.edge("continues_crosswalk_research", gap, "BOLT-NSN-SPEC-CROSSWALK-GAP", refs)
        self.edge("blocks_qualified_comparison", gap, "BOLT-MARKET-BENCHMARK-MATRIX", refs, status="planned")

    def price_controls(self):
        code_hash = self.pin("price-controls/premium_audit.py")
        tests_hash = self.pin("price-controls/test_premium_audit.py")
        method_sources = ["BOLT-PC-METHOD-S01", "BOLT-PC-METHOD-S02"]
        engine = self.finding("BOLT-PRICE-PREMIUM-ENGINE", "Offline price-comparison calculator preserves eligibility gates and amount bases",
            method_sources, node_type="analytical_method", implementation_sha256=code_hash,
            test_artifact_sha256=tests_hash,
            implementation_path="investigations/dla-bolt-trace-2026-10-30/price-controls/premium_audit.py",
            method_origin="Custom research code; cited official sources supply methodological context, not software certification",
            automatic_source_authentication=False, automatic_reviewer_authentication=False,
            official_fraud_detector=False, real_cohort_loss_established=False,
            source_role="Methodological background; execution evidence is in the pinned local inputs, outputs and independent review")
        outputs = {}
        for name in ("uniform-12-percent", "weighted-mix", "dla-current-no-qualified-benchmark"):
            payload = self.read("price-controls/scenarios/" + name + ".json")
            result = self.read("price-controls/outputs/" + name + ".json")
            expected = result["input_snapshot"]["sha256"]
            self.pin("price-controls/scenarios/" + name + ".json", expected)
            if result["data_origin"] != payload["data_origin"]:
                raise ValueError("Calculator output changed its declared data origin")
            outputs[name] = result
        for name, expected_percent in (("uniform-12-percent", Decimal("12")), ("weighted-mix", Decimal("2"))):
            result = outputs[name]
            if result["data_origin"] != "illustrative" or result["evidence_kind"] != "synthetic_calibration":
                raise ValueError("Synthetic calibration must stay explicitly illustrative")
            aggregate, = result["aggregates"]
            calculated = Decimal(aggregate["difference_exact"]) / Decimal(aggregate["reference_basis_exact"]) * 100
            if calculated != expected_percent or Decimal(aggregate["weighted_premium_against_reference_percent"]) != expected_percent:
                raise ValueError("Synthetic value-weighted arithmetic changed")
            ident = self.node("BOLT-SYNTHETIC-" + name, "synthetic_calibration", "Synthetic calculator example: " + name,
                status="hypothesis", data_origin=result["data_origin"], synthetic=True,
                evidence_kind=result["evidence_kind"], dataset_scope=result["dataset_scope"],
                declared_input_only=True, government_transaction=False, monetary_finding=False,
                aggregates=result["aggregates"],
                line_rates=[{"line_id": r["line_id"], "quantity": r["quantity"],
                    "reference_basis_exact": r["reference_basis_exact"],
                    "difference_exact": r["difference_exact"],
                    "premium_percent": r["premium_against_reference_percent"]} for r in result["lines"]],
                input_sha256=result["input_snapshot"]["sha256"],
                output_path="investigations/dla-bolt-trace-2026-10-30/price-controls/outputs/" + name + ".json",
                authentication_limit=result["authentication_limit"], no_money_export=True)
            self.edge("has_synthetic_calibration", engine, ident, method_sources,
                calibration_data_is_invented=True, source_role="Methodological context; numerical provenance is the pinned synthetic artifact")
        annual = self.read("price-controls/outputs/annual-12-percent-illustration.json")
        if annual["data_origin"] != "illustrative_user_scenario" or annual["currency"] != "unspecified":
            raise ValueError("Annual illustration must not be promoted to a real currency/loss finding")
        annual_id = self.node("BOLT-SYNTHETIC-ANNUAL-ILLUSTRATION", "synthetic_calibration", "Synthetic annual algebra: 12% markup and a 100,000 total increment",
            status="hypothesis", synthetic=True, declared_input_only=True, government_transaction=False,
            illustration=annual, amount_is_buyer_benefit=False, no_money_export=True,
            interpretation="Assumes 100,000 is total price increment; it does not establish personal benefit or government loss")
        self.edge("has_synthetic_calibration", engine, annual_id, method_sources,
            calibration_data_is_invented=True, source_role="Methodological context only")
        real = outputs["dla-current-no-qualified-benchmark"]
        if real["data_origin"] != "public_observation" or real["eligible_lines"] != 0 or real["aggregates"]:
            raise ValueError("Actual DLA result must remain blocked pending a qualified benchmark")
        for row in real["lines"]:
            if row["status"] != "blocked" or any(row[k] is not None for k in (
                    "adjusted_reference_unit_price", "premium_against_reference_percent", "difference_exact")):
                raise ValueError("Real benchmark/premium must remain null without comparable evidence")
        blocked = self.finding("BOLT-PRICE-ACTUAL-BLOCKED", "Actual DLA price calculation is blocked; no benchmark premium or loss is emitted",
            ["BOLT-CUR-S01", "BOLT-CUR-S02"] + method_sources, node_type="analytical_result",
            data_origin="public_observation", evidence_kind=real["evidence_kind"], dataset_scope=real["dataset_scope"],
            result=real, qualified_benchmark=None, price_premium=None, buyer_benefit=None,
            recoverable_loss=None, source_authentication_by_calculator=False,
            gate_behavior="Fail-fast validation; the first missing field is not an exhaustive gap list")
        self.edge("records_actual_gate_result", engine, blocked, ["BOLT-CUR-S01", "BOLT-CUR-S02"])
        self.edge("evaluates_ordered_line", blocked, "BOLT-ORDER-SPE4A627F0588", ["BOLT-CUR-S02"])
        self.edge("keeps_fairness_question_open", blocked, "BOLT-PRICE-FAIRNESS-UNKNOWN", method_sources + ["BOLT-CUR-S02"])

    def price_review(self):
        receipt = self.read("price-challenge/market_review.json")
        if receipt["status"] != "frozen_independent_review":
            raise ValueError("Expanded price investigation requires its frozen independent review")
        for row in receipt["input_artifacts"]:
            self.pin_path(ROOT.parents[1] / row["path"], row["sha256"])
        observations = self.read("price-challenge/independent_market_observations.json")
        independent_sources = []
        for row in observations["sources"]:
            independent_sources.append(self.source("BOLT-" + row["source_id"],
                "Independent market observation: " + row["source_id"], row["url"],
                "price-challenge/independent_market_observations.json",
                snapshot_scope="Selected factual observations in a shared JSON collection; hash covers the entire collection, not original webpages",
                selected_observation_id=row["source_id"], locator=row["locator"],
                original_webpage_bytes_archived=False, original_wire_archived=False,
                observed_facts=row["observed"], reviewer_decision=row["decision"]))
        conclusions = receipt["conclusions"]
        if conclusions["qualified_comparator_count"] != 0 or conclusions["new_fraud_finding_established"] or any(
                conclusions[k] is not None for k in ("premium_amount", "paid_amount", "loss_amount", "kickback_amount")):
            raise ValueError("Expanded reviewer conclusion changed; explicit re-review required")
        method_sources = ["BOLT-PC-METHOD-S01", "BOLT-PC-METHOD-S02", "BOLT-PC-METHOD-S03"]
        market_sources = ["BOLT-MKT-SRC-COX", "BOLT-MKT-SRC-FSS", "BOLT-MKT-SRC-MF"]
        current_sources = ["BOLT-CUR-S01", "BOLT-CUR-S02"]
        mechanism_sources = ["BOLT-PC-MECH-S01", "BOLT-PC-MECH-S02"]
        award_sources = [n["id"] for n in self.nodes if n["id"].startswith("BOLT-SRC-award-")]
        all_sources = method_sources + market_sources + current_sources + mechanism_sources + independent_sources + award_sources
        review = self.finding("BOLT-PRICE-CHALLENGE-REVIEW", "Independent market and buyer-independence review leaves fairness and benefit questions open",
            all_sources, node_type="review_record", reviewer_task=receipt["reviewer"],
            conclusions=conclusions, verification=receipt["verification"],
            next_discriminating_records=receipt["next_discriminating_records"],
            review_receipt_path="investigations/dla-bolt-trace-2026-10-30/price-challenge/market_review.json",
            prior_document_review_unchanged=True)
        targets = {
            "PCR-F01": "BOLT-PRICE-FAIRNESS-UNKNOWN", "PCR-F02": "BOLT-MKT-COX-HB8F38-34",
            "PCR-F03": "BOLT-MKT-FSS-191377", "PCR-F04": "BOLT-MKT-MF-HH38FX3-4G8ZY",
            "PCR-F05": "BOLT-NSN-SPEC-CROSSWALK-GAP", "PCR-F06": "BOLT-PRICE-ACTUAL-BLOCKED",
            "PCR-F07": "BOLT-BUYER-INDEPENDENCE-UNKNOWN", "PCR-F08": "BOLT-PRICE-PREMIUM-ENGINE",
            "PCR-F09": "BOLT-SYNTHETIC-ANNUAL-ILLUSTRATION", "PCR-F10": "BOLT-PC-MECH-C01",
            "PCR-F11": "BOLT-PRICE-FAIRNESS-AUDIT", "PCR-F12": "BOLT-MARKET-COMPARABILITY-REQUIREMENTS"}
        backing = {
            "PCR-F01": current_sources + method_sources, "PCR-F02": ["BOLT-CUR-S02", "BOLT-MKT-SRC-COX"],
            "PCR-F03": ["BOLT-CUR-S02", "BOLT-MKT-SRC-FSS-FAQ", "BOLT-MKT-SRC-FSS-TERMS"],
            "PCR-F04": ["BOLT-CUR-S02"], "PCR-F05": ["BOLT-CUR-S01", "BOLT-SPEC-R01", "BOLT-SPEC-R02"],
            "PCR-F06": market_sources + current_sources + method_sources,
            "PCR-F07": award_sources, "PCR-F08": current_sources + method_sources,
            "PCR-F09": ["BOLT-PC-METHOD-S02"], "PCR-F10": mechanism_sources,
            "PCR-F11": market_sources, "PCR-F12": ["BOLT-PC-METHOD-S02"]}
        if set(targets) != {r["id"] for r in receipt["findings"]}:
            raise ValueError("Expanded review finding set changed")
        for row in receipt["findings"]:
            sources = ["BOLT-" + s for s in row["source_ids"]] + backing[row["id"]]
            for path in row["evidence_paths"]:
                self.pin_path(ROOT.parents[1] / path)
            finding = self.finding("BOLT-" + row["id"], row["claim"], sources, node_type="review_assessment",
                review_decision=row["decision"], limits=row["limits"], evidence_paths=row["evidence_paths"],
                synthetic_numeric_claim=row["id"] == "PCR-F09",
                provenance_note="External source links provide source facts or methodology; code execution and synthetic arithmetic are supported by the separately pinned local artifacts",
                new_named_adverse_inference=False)
            self.edge("records_review_assessment", review, finding, sources)
            self.edge("assesses_evidence", finding, targets[row["id"]], sources, review_decision=row["decision"])

    def build(self):
        self.pin_path(Path(__file__))
        self.node(COLLECTION, "research_collection", "Single-NSN DLA bolt award and supplier trace — 2026-10-30",
            status="planned", nsn="5306016864912", no_new_fraud_case_established=True,
            scope="Seven historical contract keys, five supplier CAGEs, current parent/order, provisional market comparisons and separate price-fairness/buyer-independence controls",
            market_fairness_established=False, buyer_independence_established=False, audit_closed=False,
            report_path="investigations/dla-bolt-trace-2026-10-30/REPORT.md")
        refs, awards = self.awards()
        self.identities(awards)
        self.current()
        self.review()
        self.price_challenge()
        self.market()
        self.specification()
        self.price_controls()
        self.price_review()
        self.by_id[COLLECTION]["status"] = "documented_fact"
        self.by_id[COLLECTION]["source_ids"] = sorted(set([PRIOR_PDF_SOURCE] +
            [node["id"] for node in self.nodes if node["type"] == "source"]))
        self.edge("traces_exact_item", COLLECTION, NSN_NODE, [PRIOR_PDF_SOURCE])
        self.edge("continues_source_trace", COLLECTION, "DISC-RFQ-SPE4A626U3619", [PRIOR_PDF_SOURCE])
        return dict(version="1.0", as_of=DAY,
            input_artifacts=[dict(path=path, sha256=self.inputs[path]) for path in sorted(self.inputs)],
            nodes=sorted(self.nodes, key=lambda row: row["id"]), edges=sorted(self.edges, key=lambda row: row["id"]))


def main():
    graph = Projection().build()
    target = HERE / "graph-extension.json"
    target.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(dict(nodes=len(graph["nodes"]), edges=len(graph["edges"]),
        types=dict(Counter(n["type"] for n in graph["nodes"])), pinned_inputs=len(graph["input_artifacts"]),
        sha256=hashlib.sha256(target.read_bytes()).hexdigest()), indent=2))


if __name__ == "__main__":
    main()
