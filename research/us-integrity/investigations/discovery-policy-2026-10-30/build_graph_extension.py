#!/usr/bin/env python3
"""Project reviewed policy and neutral procurement observations into the graph.

Offline, deterministic, and deliberately separate from manifest approval. The
generator preserves source dates, legislative states, raw names and missing price
terms. It does not infer ownership, discover fraud, or run external models.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DAY = "2026-10-30"
COLLECTION = "DISC-20261030"


class Projection:
    def __init__(self):
        self.nodes, self.edges, self.by_id, self.inputs = [], [], {}, {}

    def pin(self, relative, expected=None):
        path = HERE / relative
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if expected is not None and digest != expected:
            raise ValueError("Reviewed input hash mismatch: " + relative)
        self.inputs[str(path.relative_to(ROOT))] = digest
        return digest

    def read(self, relative):
        self.pin(relative)
        return json.loads((HERE / relative).read_text())

    def node(self, ident, node_type, title, source_ids=(), status="documented_fact", **props):
        if not ident.startswith("DISC-") or ident in self.by_id:
            raise ValueError("Invalid or duplicate discovery ID: " + ident)
        row = dict(id=ident, type=node_type, title=title, status=status,
            source_ids=sorted(set(source_ids)), properties={"visibility": "public", **props})
        self.nodes.append(row)
        self.by_id[ident] = row
        return ident

    def edge(self, kind, subject, obj, sources=(), status="documented_fact", **props):
        ident = "DISC-E-" + hashlib.sha256(f"{kind}|{subject}|{obj}".encode()).hexdigest()[:20]
        if any(row["id"] == ident for row in self.edges):
            raise ValueError("Duplicate discovery edge")
        self.edges.append(dict(id=ident, type=kind, source=subject, target=obj, status=status,
            source_ids=sorted(set(sources)), properties={"visibility": "public", **props}))

    def source(self, ident, title, url, snapshot=None, expected_hash=None, **props):
        properties = dict(url=url, accessed_at=DAY, source_bytes_archived=False, **props)
        if snapshot is not None:
            digest = self.pin(snapshot, expected_hash)
            properties.update(source_bytes_archived=True, content_sha256=digest,
                snapshot_path=str((HERE / snapshot).relative_to(ROOT)))
        return self.node(ident, "source", title, status="source", **properties)

    def finding(self, ident, title, sources, kind="finding", status="documented_fact", **props):
        self.node(ident, kind, title, sources, status, **props)
        self.edge("records_observation", COLLECTION, ident, sources, status=status)
        return ident

    def executive(self):
        registry = self.read("executive/sources.json")
        statements = self.read("executive/statements.json")
        refs = {}
        for row in registry["sources"]:
            props = {k: v for k, v in row.items() if k not in {
                "id", "title", "url", "accessed_on", "web_reference_ids", "raw_bytes_archived"}}
            refs[row["id"]] = self.source("DISC-" + row["id"], row["title"], row["url"],
                registry_path="executive/sources.json", **props)
        for row in statements["statements"]:
            props = {k: v for k, v in row.items() if k not in {"id", "claim_or_paraphrase", "source_ids"}}
            is_speech = row["authoritative_type"] == "attributed_speech"
            props.update(entitlement_established=False,
                factual_scope="Attribution to the cited source; no independent verification of every underlying assertion",
                independently_verified_audio=False if is_speech else None,
                source_record="executive/statements.json")
            self.finding("DISC-" + row["id"], row["claim_or_paraphrase"], [refs[s] for s in row["source_ids"]],
                kind="attributed_statement" if is_speech else "policy_observation", **props)
        for left, right, issue in [
            ("EX-ST02", "EX-ST11", "Speech percentage versus published discretionary dollar range"),
            ("EX-ST03", "EX-ST11", "Speech recovery condition versus charge-stage written pilot"),
            ("EX-ST05", "EX-ST12", "Speech arbitration description versus written DOJ decision process"),
            ("EX-ST06", "EX-ST13", "Speech scope beyond criminal cases versus written criminal-charge eligibility")]:
            sources = self.by_id["DISC-" + left]["source_ids"] + self.by_id["DISC-" + right]["source_ids"]
            self.edge("has_policy_wording_difference", "DISC-" + left, "DISC-" + right, sources,
                issue=issue, resolution="Unresolved; do not replace published terms with speech or calculate a guaranteed award")
        return refs

    def congress(self):
        registry = self.read("congress/sources.json")
        captures = self.read("congress/capture_manifest.json")
        captured = {row["url"]: row for row in captures if row.get("file") and row.get("sha256")}
        refs = {}
        for row in registry["sources"]:
            props = {k: v for k, v in row.items() if k not in {
                "id", "title", "url", "accessed_at", "web_ref", "capture", "sha256"}}
            capture = captured.get(row["url"])
            refs[row["id"]] = self.source("DISC-CONG-" + row["id"], row["title"], row["url"],
                snapshot="congress/" + capture["file"] if capture else None,
                expected_hash=capture["sha256"] if capture else None,
                hash_scope="Exact captured official-source bytes" if capture else "No raw bytes archived for this source",
                registry_path="congress/sources.json", **props)
        for row in self.read("congress/statements.json")["statements"]:
            props = {k: v for k, v in row.items() if k not in {"id", "source_ids", "summary"}}
            title = row.get("summary", row.get("quote", row["speaker"]))
            self.finding("DISC-" + row["id"], title, [refs[s] for s in row["source_ids"]],
                kind="congressional_statement", enacts_law=False, source_record="congress/statements.json", **props)
        accepted_states = {
            "not_established_by_bounded_search", "enacted_statutory_authority", "existing_sector_program",
            "enacted_amendment", "member_announcement_bill_number_unresolved", "not_enacted_in_captured_status_record"}
        for row in self.read("congress/authority_matrix.json")["authorities"]:
            if row["status"] not in accepted_states:
                raise ValueError("New authority status requires explicit review: " + row["status"])
            props = {k: v for k, v in row.items() if k not in {"id", "topic", "source_ids", "status"}}
            self.finding("DISC-" + row["id"], row["topic"], [refs[s] for s in row["source_ids"]],
                kind="legal_authority_observation", authority_status=row["status"],
                status="unknown" if row["status"] == "not_established_by_bounded_search" else "documented_fact",
                source_record="congress/authority_matrix.json", **props)
        self.edge("identifies_statutory_basis", "DISC-EX-ST10", "DISC-CA02", [refs["C01"], "DISC-EX-S05"],
            scope="Statutory discretion and ordinary cap are separate from the narrower written pilot range")
        self.edge("checks_proposal_status", "DISC-EX-ST08", "DISC-CA09", [refs["C16"], refs["C17"], "DISC-EX-S03"],
            scope="Speech and member draft do not establish enactment")
        return refs

    def names(self):
        capture_base = "names/capture-2026-10-30/"
        manifest = self.read(capture_base + "manifest.json")
        analysis = self.read("names/analysis.json")
        review = self.read("review/name_data_review.json")
        if not manifest.get("success") or not review.get("passed"):
            raise ValueError("Name capture and independent review must pass")
        for relative, expected in review["input_sha256"].items():
            self.pin(relative, expected)
        sources = {}
        for row in manifest["requests"]:
            if row["http_status"] != 200:
                raise ValueError("Unsuccessful capture cannot enter reviewed discovery graph")
            if row.get("request_path"):
                self.pin(capture_base + row["request_path"], row["request_sha256"])
            label = row["label"]
            sid = self.source("DISC-NAME-SRC-" + label, "USAspending captured request: " + label, row["url"],
                snapshot=capture_base + row["snapshot_path"], expected_hash=row["snapshot_sha256"],
                method=row["method"], retrieved_at=row["retrieved_at"],
                request_path=str((HERE / (capture_base + row["request_path"])).relative_to(ROOT)) if row.get("request_path") else None,
                request_sha256=row.get("request_sha256"), original_wire_sha256=row["wire_response_sha256"],
                original_wire_archived=False, hash_scope=manifest["hash_scope"],
                selection=row["selection"], selection_note=row.get("selection_note"),
                request_manifest="names/capture-2026-10-30/manifest.json")
            sources[label] = sid
        for label, query in manifest["queries"].items():
            relevant = [sid for name, sid in sources.items() if name.startswith(label + "-") and
                (label == "amazon-dot" or not name.startswith("amazon-dot-"))]
            self.finding("DISC-NAME-COHORT-" + label, f"Literal keyword {query['keyword']}: bounded contract-query cohort", relevant,
                kind="dataset_cohort", query=query, scope=manifest["scope"],
                all_nationwide_recipients=False, complete_for_bounded_query=query["complete_for_bounded_query"],
                amount_semantics="Recipient trailing-twelve-month and award cumulative amounts have different scopes; no monetary sums made",
                fraud_rank=False)
        all_sources = sorted(sources.values())
        self.finding("DISC-NAME-ANALYSIS", "Neutral recipient-name and punctuation comparison", all_sources,
            calculation=analysis, no_fraud_determination=True, source_record="names/analysis.json")
        self.finding("DISC-NAME-INDEPENDENT-REVIEW", "Independent reconstruction confirms bounded name-query results", all_sources,
            verification=review["summary"], verification_scope=review["limits"],
            method=review["method"], source_record="review/name_data_review.json")
        for i, group in enumerate(analysis["recipient_groups"], 1):
            self.finding(f"DISC-NAME-GROUP-{i}", "Comparison key: " + group["comparison_key"], all_sources,
                kind="name_comparison_group", comparison=group, automatic_merge=False,
                inference_limit="Formatting and source profile levels are comparison aids, not separate-company, ownership or wrongdoing conclusions")
        profiles = self.read(capture_base + "profiles.json")
        grouped = {}
        for i, row in enumerate(profiles, 1):
            grouped.setdefault(row["uei"], []).append((i, row))
        for uei, rows in grouped.items():
            refs = [sources[f"profile-{i:02d}"] for i, _ in rows]
            self.node("DISC-UEI-" + uei, "organization_identifier_reference", rows[0][1]["name"], refs,
                uei=uei, raw_names=sorted({r["name"] for _, r in rows}),
                identity_scope="Exact reported USAspending UEI only; no name-based merge with other UEIs or historical graph entities",
                business_registration_verified=False, beneficial_ownership_verified=False, fraud_assessment="none")
        parent_sources = [sources[f"profile-{i:02d}"] for i, row in enumerate(profiles, 1) if row["recipient_level"] == "C"]
        parent_rows = [row for row in profiles if row["recipient_level"] == "C"]
        for parent_uei in sorted({row["parent_uei"] for row in parent_rows}):
            match = next(row for row in parent_rows if row["parent_uei"] == parent_uei)
            self.node("DISC-PARENT-UEI-" + parent_uei, "source_reported_parent_reference", match["parent_name"], parent_sources,
                reported_parent_uei=parent_uei, direct_parent_profile_fetched=False,
                ultimate_beneficial_ownership_verified=False, source_scope="Top-level parent fields of three child profiles")
        for i, row in enumerate(profiles, 1):
            refs = [sources[f"profile-{i:02d}"]]
            pid = self.node(f"DISC-NAME-PROFILE-{i:02d}", "recipient_profile", row["name"] + " — " + row["recipient_level"] + " profile", refs,
                record=row, profile_is_not_separate_company=True, observed_at=DAY,
                parent_field_is_not_ultimate_ownership=True, no_fraud_determination=True)
            self.edge("reports_recipient_uei", pid, "DISC-UEI-" + row["uei"], refs)
            target = "DISC-PARENT-UEI-" + row["parent_uei"] if row["recipient_level"] == "C" else "DISC-UEI-" + row["uei"]
            self.edge("reports_parent_profile_reference", pid, target, refs,
                recipient_level=row["recipient_level"], self_reference=row["parent_uei"] == row["uei"],
                ownership_adjudication=False)
            self.edge("includes_profile", "DISC-NAME-ANALYSIS", pid, refs)
        named_refs = {}
        requests_by_snapshot = {row["snapshot_path"]: sources[row["label"]] for row in manifest["requests"]}
        for row in self.read("names/sources.json"):
            if row.get("snapshot_path"):
                snapshot = row["snapshot_path"].removeprefix("capture-2026-10-30/")
                named_refs[row["id"]] = [requests_by_snapshot[snapshot]]
                # Aggregate findings must retain all pages, not cite only page one.
                cohort_prefix = {"NAMES-D01": "amazon-awards-", "NAMES-D02": "amazon-dot-awards-",
                                 "NAMES-D03": "amazon-recipients-", "NAMES-D04": "amazon-dot-recipients-"}.get(row["id"])
                if cohort_prefix:
                    named_refs[row["id"]] = [sid for label, sid in sources.items() if label.startswith(cohort_prefix)]
            else:
                props = {k: v for k, v in row.items() if k not in {"id", "title", "url", "accessed_at", "source_bytes_archived"}}
                named_refs[row["id"]] = [self.source("DISC-" + row["id"], row["title"], row["url"], **props)]
        for row in self.read("names/evidence_records.json")["findings"]:
            props = {k: v for k, v in row.items() if k not in {"id", "statement", "status", "source_ids"}}
            refs = [ref for sid in row["source_ids"] for ref in named_refs[sid]]
            self.finding("DISC-" + row["id"], row["statement"], refs, status=row["status"],
                source_record="names/evidence_records.json", **props)
        return all_sources

    def pricing(self):
        manifest = self.read("pricing/acquisition_manifest.json")
        selected = self.read("pricing/snapshots/selected_evidence.json")
        self.pin("pricing/" + manifest["selected_path"], manifest["selected_sha256"])
        refs = {}
        for row in self.read("pricing/sources.json")["sources"]:
            props = {k: v for k, v in row.items() if k not in {"id", "title", "url", "accessed_on", "archive_path"}}
            refs[row["id"]] = self.source("DISC-PRICE-SRC-" + row["id"], row["title"], row["url"],
                snapshot="pricing/" + row["archive_path"] if row.get("archive_path") else None,
                expected_hash=manifest["original_sha256"] if row.get("archive_path") else None,
                hash_scope="Exact acquired primary PDF bytes" if row.get("archive_path") else "No raw source bytes archived",
                **props)
        sid = refs[selected["source_id"]]
        item = self.node("DISC-NSN-" + selected["nsn"], "catalog_item_reference",
            "Machine bolt NSN " + selected["nsn"], [sid], nsn=selected["nsn"],
            identity_scope="Identifier printed in one current solicitation and its history table; historical revision equivalence remains unverified")
        solicitation = self.finding("DISC-RFQ-SPE4A626U3619", selected["solicitation"] + ": current solicitation terms", [sid],
            kind="solicitation_observation", issue_date=selected["issue_date"],
            current_terms=selected["current_solicitation_terms"],
            evidence_scope="Unpriced RFQ; not an awarded or paid invoice", source_record="pricing/snapshots/selected_evidence.json")
        self.edge("describes_item", solicitation, item, [sid])
        for cage in sorted({row["cage"] for row in selected["observations"]}):
            self.node("DISC-CAGE-" + cage, "supplier_identifier_reference", "History-table CAGE " + cage, [sid],
                cage=cage, resolved_company_name=None, legal_entity_verified=False, ownership_verified=False,
                investigation_status="neutral published identifier; no suspicion or fraud ranking")
        for i, row in enumerate(selected["observations"], 1):
            ident = self.finding(f"DISC-PRICE-HISTORY-{i:02d}", row["contract_number"] + ": printed history unit cost " + row["unit_cost_as_printed"], [sid],
                kind="historical_price_observation", record=row,
                missing_terms_are_unknown=True, current_terms_not_backfilled=True,
                source_record="pricing/snapshots/selected_evidence.json", no_overpricing_verdict=True)
            self.edge("references_item", ident, item, [sid])
            self.edge("reports_supplier_identifier", ident, "DISC-CAGE-" + row["cage"], [sid])
        terms = selected["current_solicitation_terms"]
        ceiling = self.node("DISC-PRICE-CURRENT-CEILING", "money_measure", "Current RFQ maximum contract value", [sid],
            money=dict(amount=str(terms["maximum_contract_value_usd"]), currency="USD", kind="solicitation_maximum_contract_value",
                qualifier="ceiling_not_paid_amount", period=selected["issue_date"], basis="Current RFQ maximum; no current quoted price"),
            aggregation_permitted=False, independently_verified_collection=False,
            unit_price_inference_forbidden=True, source_pages=terms["source_pages"])
        self.edge("states_maximum_value", solicitation, ceiling, [sid])
        self.finding("DISC-PRICE-COMPARABILITY", "No verified comparable historical price pairs", [sid, refs["FAR-15-404-1"]],
            analysis=selected["analysis"], possible_row_pairs=21,
            historical_unit_and_currency_not_verified=True, no_savings_calculation=True)
        for row in self.read("pricing/source_access_matrix.json")["sources"]:
            source_id = row["source_id"]
            if source_id in refs:
                references = [refs[source_id]]
            elif row.get("parent_source_id"):
                references = [refs[row["parent_source_id"]]]
            elif row.get("url"):
                references = [self.source("DISC-PRICE-SRC-" + source_id, source_id.replace("-", " "), row["url"],
                    retrieval_status="Route identified; prior award documents not acquired")]
            else:
                raise ValueError("Access matrix row lacks source provenance")
            self.finding("DISC-ACCESS-" + source_id, row["data_kind"] + ": " + row["actual_status"], references,
                kind="source_access_observation", access_observation=row,
                no_access_implied_beyond_observed_status=True)
        contract = self.read("pricing/agent_contract.json")
        self.node("DISC-WP-DLA-BOLTS-001", "research_task", "Next bounded cohort: 30 public DLA bolt RFQs", status="planned",
            definition=contract, execution_status="not_executed", claude_executed=False, grok_executed=False,
            completed_seed_rfqs=1)
        self.edge("defines_followup", COLLECTION, "DISC-WP-DLA-BOLTS-001", status="planned")
        for row in contract["roles"]:
            rid = self.node("DISC-ROLE-" + row["id"].replace("_", "-"), "agent_specification", row["id"].replace("_", " "),
                status="planned", definition=row, runtime_active=False, execution_evidence="No execution of this future 30-RFQ role claimed")
            self.edge("assigns_planned_role", "DISC-WP-DLA-BOLTS-001", rid, status="planned")
        return list(refs.values())

    def review(self, name_sources, price_sources):
        review = self.read("review/review.json")
        price_review = self.read("review/price_data_review.json")
        if not price_review.get("passed") or not review["validation"]["independent_price_transcription_passed"]:
            raise ValueError("Independent pricing review has not passed")
        for relative, expected in price_review["input_sha256"].items():
            self.pin(relative, expected)
        # Pin the independent calculations and executable checks. Root summaries
        # and human-readable reports remain separately editable, not graph inputs.
        for relative, expected in review["artifact_sha256"].items():
            if not relative.endswith(".md"):
                self.pin(relative, expected)
        existing_sources = {n["properties"]["url"]: n["id"] for n in self.nodes if n["type"] == "source"}
        refs = {}
        for row in review["sources"]:
            if row["url"] in existing_sources:
                ident = existing_sources[row["url"]]
                self.by_id[ident]["properties"].setdefault("independent_review_locators", []).append(row["locator"])
                refs[row["id"]] = [ident]
            else:
                refs[row["id"]] = [self.source("DISC-" + row["id"], row["title"], row["url"],
                    source_locator=row["locator"], source_record="review/review.json")]
        refs["names/analysis.json"] = name_sources
        refs["review/name_data_review.json"] = name_sources
        refs["review/price_data_review.json"] = ["DISC-PRICE-SRC-DLA-SPE4A626U3619", "DISC-PRICE-SRC-FAR-15-404-1"]
        for row in review["findings"]:
            sources = [ident for source_id in row["sources"] for ident in refs[source_id]]
            self.finding("DISC-" + row["id"], row["conclusion"], sources,
                finding_kind=row["kind"], verification_scope=review["independence"],
                source_record="review/review.json", no_fraud_or_reward_determination=True)
        self.finding("DISC-PRICE-INDEPENDENT-REVIEW", "Independent price transcription confirms seven history observations and zero comparable pairs",
            refs["review/price_data_review.json"], verification=price_review["summary"],
            verification_scope=price_review["limits"], method=price_review["method"],
            source_record="review/price_data_review.json")
        eligibility = self.read("pricing/eligibility_result.json")
        self.finding("DISC-PRICE-ELIGIBILITY-GATE", "All 21 candidate history-row pairs fail the comparison gate",
            refs["review/price_data_review.json"], gate_result=eligibility,
            source_record="pricing/eligibility_result.json",
            gate_limit="Software checks completeness and declared evidence flags; it cannot independently authenticate arbitrary provenance or prove fraud")
        self.edge("supports_followup_design", "DISC-RV-F06", "DISC-WP-DLA-BOLTS-001",
            self.by_id["DISC-RV-F06"]["source_ids"], scope="Research-design judgment; future cohort remains unexecuted")
        self.by_id[COLLECTION]["properties"].update(
            review_decision=review["decision"], independent_review_scope=review["independence"],
            unresolved=review["unresolved"], claude_executed=False, grok_executed=False,
            unattended_agents_running=False)

    def build(self):
        self.node(COLLECTION, "research_collection", "Policy verification and neutral procurement discovery — 2026-10-30",
            status="planned", scope="Bounded statement, authority, recipient-name and price-source review",
            new_fraud_cases_established=0, report_path="investigations/discovery-policy-2026-10-30/REPORT.md")
        self.executive()
        self.congress()
        names = self.names()
        prices = self.pricing()
        self.review(names, prices)
        self.by_id[COLLECTION]["status"] = "documented_fact"
        self.by_id[COLLECTION]["source_ids"] = sorted(n["id"] for n in self.nodes if n["type"] == "source")
        self.edge("extends_policy_bibliography", COLLECTION, "bibliography-reward", status="planned")
        self.edge("informs_bounded_procurement_research", COLLECTION, "sector-defense-spares", status="planned")
        graph = dict(version="1.0", as_of=DAY,
            input_artifacts=[dict(path=p, sha256=self.inputs[p]) for p in sorted(self.inputs)],
            nodes=sorted(self.nodes, key=lambda r: r["id"]), edges=sorted(self.edges, key=lambda r: r["id"]))
        return graph


def main():
    graph = Projection().build()
    output = HERE / "graph-extension.json"
    output.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(dict(nodes=len(graph["nodes"]), edges=len(graph["edges"]),
        types=dict(Counter(n["type"] for n in graph["nodes"])),
        input_artifacts=len(graph["input_artifacts"]), sha256=hashlib.sha256(output.read_bytes()).hexdigest()), indent=2))


if __name__ == "__main__":
    main()
