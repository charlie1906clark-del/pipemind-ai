#!/usr/bin/env python3
"""Build a proposed, offline projection; never edit the approval registry.

The source URL for locally produced artifacts identifies the repository, not an
assertion that GitHub served the supplied bytes. Each actual artifact is pinned
by its local retained SHA256. Publication/review is a separate coordinator step.
"""
from collections import Counter
from copy import deepcopy
from decimal import Decimal
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PILOT = ROOT / "investigations/federal-price-pilot-2026-10-30"
AGENTS = ROOT / "price-agents"
SPEC = ROOT / "investigations/bolt-spec-followup-2026-10-30"
DAY = "2026-10-30"
REPO = "https://github.com/charlie1906clark-del/pipemind-ai"
COLLECTION = "PA-SYSTEM-20261030"


class Projection:
    def __init__(self):
        self.nodes, self.edges, self.inputs, self.by_id = [], [], {}, {}

    def pin(self, path, expected=None):
        path = Path(path).resolve()
        if not any(path.is_relative_to(base) for base in (ROOT / "investigations", AGENTS)):
            raise ValueError("Input is outside approved investigation/agent roots")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if expected is not None and digest != expected:
            raise ValueError("Frozen input changed: " + str(path))
        self.inputs[str(path.relative_to(ROOT))] = digest
        return digest

    def read(self, path):
        self.pin(path)
        return json.loads(Path(path).read_text())

    def node(self, ident, kind, title, sources=(), status="documented_fact", **properties):
        if not ident.startswith(("PA-", "FPP-")) or ident in self.by_id:
            raise ValueError("Invalid or duplicate extension identity: " + ident)
        record = dict(id=ident, type=kind, title=title, status=status,
                      source_ids=sorted(set(sources)), properties={"visibility": "public", **properties})
        self.nodes.append(record)
        self.by_id[ident] = record
        return ident

    def edge(self, relationship, subject, obj, sources=(), status="documented_fact", **properties):
        ident = "PA-E-" + hashlib.sha256(f"{relationship}|{subject}|{obj}".encode()).hexdigest()[:24]
        if any(x["id"] == ident for x in self.edges):
            raise ValueError("Duplicate projected relationship")
        self.edges.append(dict(id=ident, type=relationship, source=subject, target=obj,
            status=status, source_ids=sorted(set(sources)), properties={"visibility": "public", **properties}))

    def source(self, ident, title, url, path=None, expected=None, accessed_at=DAY, **props):
        properties = dict(url=url, accessed_at=accessed_at, source_bytes_archived=False, **props)
        if path:
            properties.update(source_bytes_archived=True, content_sha256=self.pin(path, expected),
                              snapshot_path=str(Path(path).resolve().relative_to(ROOT)))
        return self.node(ident, "source", title, status="source", **properties)

    def artifact(self, ident, path, title, **props):
        return self.source(ident, title, REPO, path, artifact_origin="locally_produced_repository_artifact",
            snapshot_scope="Exact retained repository artifact; not downloaded GitHub response bytes",
            public_repository_location=REPO, network_retrieval_inferred=False, **props)

    def money(self, ident, title, sources, amount, kind, period, basis):
        return self.node(ident, "money_measure", title, sources,
            money=dict(amount=str(amount), currency="USD", kind=kind, period=period,
                       qualifier="source_reported_as_of_2026-10-30", basis=basis),
            aggregation_permitted=False, paid_cash_verified=False,
            recoverable_loss=None, buyer_benefit=None)

    def plan(self):
        plan = self.read(AGENTS / "plans/current-wave.json")
        contracts = self.read(AGENTS / "plans/role-contracts.json")
        if len(plan["tasks"]) != 20 or len(contracts["roles"]) != 14:
            raise ValueError("Frozen current-wave/role scope changed")
        ps = self.artifact("PA-SRC-CURRENT-PLAN", AGENTS / "plans/current-wave.json", "Current bounded 20-task plan")
        rs = self.artifact("PA-SRC-ROLE-CONTRACTS", AGENTS / "plans/role-contracts.json", "Fourteen specialist role contracts")
        self.node(COLLECTION, "investigation_collection", "Public procurement price-agent system and bounded observations", [ps, rs],
            scope="Proposed extension containing plan definitions, bounded public observations and scoped local execution receipts",
            nationwide_coverage=False, new_fraud_established=False, automated_model_execution=False,
            background_schedule_created=False, provider_dispatch_verified=False,
            actual_financial_semantics="Cumulative obligations, awarded ordered values and paid cash remain distinct")
        self.node(plan["plan_id"], "research_plan", "Current wave: 20 bounded public-source research tasks", [ps], "planned",
            plan_id=plan["plan_id"], base_commit=plan["base_commit"], definition_status="planned",
            runtime_status_source="PA-SRC-LOCAL-RUN", model_count_inferred=False,
            evidence_mode=plan["evidence_mode"], plan_sha256=self.pin(AGENTS / "plans/current-wave.json"))
        self.edge("defines_plan", COLLECTION, plan["plan_id"], [ps], "planned")
        for role in contracts["roles"]:
            self.node(role["id"], "agent_role_contract", role["name"], [rs], "planned", contract=role,
                deployed_model_instance=False, common_contract=contracts["common_contract"])
            self.edge("defines_role", COLLECTION, role["id"], [rs], "planned")
        for task in plan["tasks"]:
            self.node(task["id"], "research_task_definition", task["title"], [ps, rs], "planned",
                definition=task, execution_state_in_definition=False)
            self.edge("includes_task", plan["plan_id"], task["id"], [ps], "planned")
            self.edge("assigned_role", task["id"], task["agent_role"], [ps, rs], "planned")
            for dep in task["depends_on"]:
                self.edge("requires_accepted_packet", task["id"], dep, [ps], "planned",
                    independent_price_eligibility_check_still_required=True)
        later = self.read(AGENTS / "plans/later-waves.json")
        ls = self.artifact("PA-SRC-LATER-WAVES", AGENTS / "plans/later-waves.json", "Eight gated future sector designs")
        for wave in later["waves"]:
            wid = "PA-" + wave["id"]
            self.node(wid, "gated_sector_design", wave["sector"], [ls], "planned", definition=wave,
                activation_rules=later["activation_rules"], runtime_imported=False, nationwide_work_executed=False)
            self.edge("proposes_gated_wave", COLLECTION, wid, [ls], "planned")
        cs = self.artifact("PA-SRC-CLAUDE-SUPPLEMENT", AGENTS / "plans/claude-supplemental-assignment.json",
                           "Prepared Claude supplemental assignment; not a dispatch receipt")
        self.node("PA-CLAUDE-SUPPLEMENT", "coordination_assignment", "Prepared bounded Claude bid and role assignments", [cs], "planned",
            provider_contact_or_execution_verified=False, original_assignment_baseline_preserved=True,
            definition=self.read(AGENTS / "plans/claude-supplemental-assignment.json"))
        self.edge("prepares_assignment", COLLECTION, "PA-CLAUDE-SUPPLEMENT", [cs], "planned")
        for name in ["record-contracts.json", "host-admissions.json", "source-observations.json", "research-log.json", "VALIDATION.json"]:
            self.pin(AGENTS / "plans" / name)
        self.pin(AGENTS / "ARCHITECTURE.md")
        self.pin(AGENTS / "SOURCE-MAP.md")
        for source in self.read(AGENTS / "plans/source-observations.json")["sources"]:
            extras = {k: v for k, v in source.items() if k not in ("id", "url", "retrieved_at", "content_sha256")}
            sid = self.source(source["id"], "Official source availability: " + source["id"].removeprefix("PA-SOURCE-"),
                source["url"], accessed_at=source["retrieved_at"], **extras)
            self.edge("documents_source_route", COLLECTION, sid, [sid])

    def pilot(self):
        observations = self.read(PILOT / "observations.json")
        lines = self.read(PILOT / "line_observations.json")
        graph = self.read(PILOT / "transaction_links.json")
        if len(observations["observations"]) != 30 or len(lines["observations"]) != 2 or len(graph["nodes"]) != 65 or len(graph["edges"]) != 42:
            raise ValueError("Reviewed pilot scope changed")
        sources = {}
        for row in self.read(PILOT / "sources.json")["sources"]:
            sid = "FPP-SRC-" + row["id"]
            sources[row["id"]] = sid
            snapshot = PILOT / row["snapshot_path"] if row.get("snapshot_path") else None
            props = {k: v for k, v in row.items() if k not in ("id", "url", "snapshot_path", "snapshot_sha256", "observed_at", "observed_date", "request_path")}
            self.source(sid, "Pilot source: " + row["id"], row["url"], snapshot, row.get("snapshot_sha256"),
                        accessed_at=row.get("observed_at", row.get("observed_date", DAY)), **props)
            if row.get("request_path"):
                self.pin(PILOT / row["request_path"])
        selected = self.read(PILOT / "selected_manifest.json")
        selected_refs = {}
        for row in selected["selected_artifacts"]:
            sid = "FPP-SRC-SELECTED-" + Path(row["path"]).name.replace(".", "-")
            selected_refs[row["path"]] = self.source(sid, "Selected primary contract artifact: " + Path(row["path"]).name,
                selected["source_url"], PILOT / row["path"], row["sha256"], snapshot_scope=row["scope"],
                original_pdf_sha256=selected["original_pdf_sha256"], original_pdf_archived=False)
        cohort_sources = [sources["usaspending-search-" + x] for x in ("dla-bolts", "va-medical", "hhs-medical")]
        self.node("FPP-COHORT-20261030", "dataset_cohort", "Thirty selected award summaries in three first-page strata", cohort_sources,
            date_filter={"start":"2026-07-03", "end":"2026-07-31", "date_type":"new_awards_only"},
            stratum_counts=dict(Counter(x["stratum"] for x in observations["observations"])),
            page=1, limit_per_stratum=10, sort="Award Amount descending", source_has_next=True,
            sample_type="incomplete_nonrandom_first_page", nationwide_coverage=False,
            date_basis="Base award transaction date; cumulative amounts are not July spending",
            selection_reason="Bounded declared agency/commodity strata and document availability; not fraud ranking")
        self.edge("includes_bounded_pilot", COLLECTION, "FPP-COHORT-20261030", cohort_sources)
        by_award = {"award:" + x["generated_award_id"]: x for x in observations["observations"]}
        by_line = {"line:" + x["observation_id"]: x for x in lines["observations"]}
        mapping = {}
        for row in graph["nodes"]:
            original = row["id"]
            if original.startswith("award:"):
                ident = "FPP-AWARD-" + original.split(":",1)[1]
            elif original.startswith("uei:"):
                ident = "FPP-UEI-" + original.split(":",1)[1]
            elif original.startswith("line:"):
                ident = "FPP-LINE-" + original.split(":",1)[1]
            elif original.startswith("nsn:"):
                ident = "FPP-NSN-" + original.split(":",1)[1]
            else:
                ident = "FPP-OFFICE-" + hashlib.sha256(original.encode()).hexdigest()[:16]
            mapping[original] = ident
            refs = [sources[x] for x in row["source_ids"]]
            props = dict(original_projection_id=original, public_record=True, no_adverse_inference=True)
            kind = {"award":"award_observation", "business_recipient":"reported_business_recipient",
                    "office":"government_office_observation", "line":"contract_line_observation", "nsn":"item_identifier"}.get(row["type"], row["type"])
            if original in by_award:
                props.update(observation=by_award[original], amount_interpretation=observations["amount_basis"])
            elif row["type"] == "award":
                kind = "reported_parent_award_reference"
                props.update(reference_scope="Parent identifier reported for a sampled award; not an additional sampled purchase",
                             priced_order_lines_acquired=False, actual_payment_verified=False)
            elif original in by_line:
                line = by_line[original]
                props.update(observation=line, actual_payment_verified=False, benchmark_qualified=False)
                refs.extend(selected_refs[x] for x in line.get("source_paths",[]) + line.get("additional_source_paths",[]))
                # Page 2 identifies intended manufacturer; pages 5/7/11 delimit terms/test.
                refs.extend(selected_refs[x] for x in selected_refs if x.endswith(("page2.txt", "page5-selected.txt", "page7-e08-selected.txt", "page11-first-article-selected.txt")))
            elif original.startswith("uei:"):
                props.update(uei=original.split(":",1)[1], beneficial_owner_verified=False, paid_recipient_verified=False)
            self.node(ident, kind, row["label"], refs, **props)
            if original in by_award:
                ob = by_award[original]
                self.edge("includes_award_observation", "FPP-COHORT-20261030", ident, refs)
                mid = self.money("FPP-OBLIGATION-" + ob["generated_award_id"], ob["piid"] + ": cumulative award obligation", refs,
                    ob["award_obligation_usd"], "cumulative_award_obligation", "as_of_2026-10-30",
                    "USAspending award-level cumulative obligation; neither selected-period expenditure, ordered unit price nor paid cash")
                self.edge("reports_cumulative_obligation", ident, mid, refs)
            if original in by_line:
                ob = by_line[original]
                mid = self.money("FPP-ORDERED-VALUE-" + ob["observation_id"], ob["observation_id"] + ": awarded extended line value", refs,
                    ob["extended_amount_usd"], "awarded_contract_line_ordered_value", "2026-07-09",
                    "Original award quantity × stated unit price; payment/delivery not acquired")
                self.edge("reports_ordered_line_value", ident, mid, refs)
        for row in graph["edges"]:
            self.edge(row["relation"], mapping[row["from"]], mapping[row["to"]], [sources[x] for x in row["source_ids"]],
                original_projection_properties={k:v for k,v in row.items() if k not in ("from","to","relation","source_ids")},
                actual_cash_transfer_inferred=False)
        total = sum(Decimal(x["extended_amount_usd"]) for x in lines["observations"])
        selected_award = next(x for x in observations["observations"] if x["piid"] == "SPE4A626PW775")
        if total != Decimal(selected_award["award_obligation_usd"]):
            raise ValueError("Selected CLINs no longer reconcile to reported award amount")
        rec_sources = [sources["usaspending-detail-SPE4A626PW775"], sources["dla-original-SPE4A626PW775"],
                       selected_refs["selected/dla-award-page4.txt"]]
        self.node("FPP-DLA-LINE-RECONCILIATION", "arithmetic_reconciliation", "Two separately typed ordered CLINs sum to the reported award obligation", rec_sources,
            ordered_production_value="612316.57", separately_ordered_test_value="3500.00", sum_usd=str(total),
            inference_limit="Arithmetic agreement establishes neither payment, price fairness, excessive markup nor loss",
            payment_verified=False, independently_qualified_benchmark_count=0)
        self.edge("reconciles_selected_award", "FPP-DLA-LINE-RECONCILIATION", mapping["award:"+selected_award["generated_award_id"]], rec_sources)
        rejected = self.read(PILOT / "rejected_comparators.json")
        for row in rejected["observations"]:
            sid = sources[row["id"]]
            ident = "FPP-REJECTED-" + row["id"]
            self.node(ident, "excluded_price_comparator", "Rejected HHS comparator: " + row["catalog_number"], [sid],
                observation=row, benchmark_status="excluded_wrong_product", aggregation_permitted=False,
                purchased_line=False, paid_price=False, historical_order_date_price_verified=False)
            self.edge("records_excluded_comparator", "FPP-COHORT-20261030", ident, [sid])
        for filename in ["bundle_manifest.json", "validation.json", "follow_up_tasks.json", "detail-selection.json"]:
            path = PILOT / filename
            if path.exists(): self.pin(path)
        for artifact in self.read(PILOT / "bundle_manifest.json")["artifacts"]:
            self.pin(PILOT / artifact["path"], artifact["sha256"])
        return mapping, sources

    def parties(self, pilot_mapping, pilot_sources):
        base = PILOT / "parties"
        graph = self.read(base / "graph.json")
        if len(graph["nodes"]) != 15 or len(graph["edges"]) != 9:
            raise ValueError("Reviewed party projection scope changed")
        mapping = {x["id"]:"FPP-" + x["id"] for x in graph["nodes"]}
        for row in graph["nodes"]:
            props = deepcopy(row["properties"])
            props.update(original_projection_id=row["id"], projection_scope="Reviewed 15-node/9-edge party subgraph")
            if row["type"] == "source":
                path = (base / props.pop("snapshot_path")).resolve()
                digest = props.pop("snapshot_sha256")
                url, accessed = props.pop("url"), props.pop("accessed_at")
                self.source(mapping[row["id"]], row["title"], url, path, digest, accessed_at=accessed,
                    snapshot_scope="Selected public professional or business fields; not complete original response/document", **props)
            else:
                self.node(mapping[row["id"]], row["type"], row["title"], [mapping[x] for x in row["source_ids"]], row["status"], **props)
        for row in graph["edges"]:
            self.edge(row["type"], mapping[row["source"]], mapping[row["target"]], [mapping[x] for x in row["source_ids"]], row["status"],
                original_projection_id=row["id"], **row["properties"])
        self.edge("same_exact_award_identifier", mapping["TP-AWARD-W775"],
            pilot_mapping["award:CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-"],
            [mapping["TP-S-AWARD"], pilot_sources["usaspending-detail-SPE4A626PW775"]], join_basis="Exact generated award ID and PIID")
        self.edge("same_reported_uei", mapping["TP-ORG-DON"], pilot_mapping["uei:XN9HKU6LUM59"],
            [mapping["TP-S-CAGE-DON"], mapping["TP-S-AWARD"]], join_basis="Exact UEI; no name-only person/entity merge")
        for name in ["sources.json", "manifest.json", "validation.json", "identity-decisions.json", "unresolved.json", "timeline.json", "finding.json", "research-budget.json"]:
            self.pin(base / name)

    def local_run(self):
        path = AGENTS / "runs/current-run/export-state.json"
        run = self.read(path)
        sid = self.artifact("PA-SRC-LOCAL-RUN", path, "Frozen local replay state: existing captures, not new network retrieval")
        tasks = run["status"]["tasks"]
        counts = dict(Counter(x["status"] for x in tasks))
        attempts = run["tables"]["attempts"]
        if counts != {"queued":11,"blocked":5,"accepted":4} or len(attempts)!=6:
            raise ValueError("Reviewed local runtime scope changed")
        if any(a["payload"]["method"] != "LOCAL_CAPTURE_REUSE" or a["payload"].get("new_network_requests") != 0 for a in attempts):
            raise ValueError("Local replay now includes a different acquisition scope")
        self.node("PA-RUN-LOCAL-20261030", "local_runtime_observation", "Local ledger: 4 accepted packets, 5 blocked tasks, 11 queued", [sid],
            counts=counts, local_capture_reuse_attempts=6, new_network_requests=0,
            graph_promotion="separate_publication_review", model_execution="not_provided_by_runtime",
            accepted_meaning="Independently accepted as worded; not qualified pricing, source truth, innocence or fraud",
            prior_acquisition_scope="Network acquisition occurred separately in producer source manifests; this replay did not reacquire it")
        self.edge("records_local_replay", COLLECTION, "PA-RUN-LOCAL-20261030", [sid])
        for task in tasks:
            ident="PA-RUNSTATE-" + task["task_id"]
            self.node(ident, "task_execution_observation", task["task_id"] + ": " + task["status"], [sid],
                ledger_observation=task, scoped_to_retained_local_run=True)
            self.edge("observes_task_state", ident, task["task_id"], [sid])
            self.edge("includes_task_state", "PA-RUN-LOCAL-20261030", ident, [sid])
        for result in run["tables"]["results"]:
            ident="PA-RUNRESULT-" + result["id"]
            self.node(ident, "accepted_research_packet", result["task_id"] + ": accepted scoped observation packet", [sid],
                result_sha256=result["sha256"], packet=result["payload"],
                external_truth_authentication=False, new_fraud_established=False)
            self.edge("records_result_packet", result["task_id"], ident, [sid])
        for attempt in attempts:
            cap=attempt["payload"]["original_capture"]
            self.pin(ROOT.parents[1] / cap["artifact_path"], cap["sha256"])
        for file in ["runtime/agent_runtime.py", "runtime/price_check.py", "runtime/README.md", "runtime/VALIDATION.json",
                     "runtime/demo-output.json", "runs/replay_pilot.py", "runs/README.md",
                     "review/cohort-receipts.json", "review/line-receipts.json"]:
            self.pin(AGENTS / file)

    def scoped_modules(self):
        obs = self.read(SPEC / "observations.json")
        if obs["actual_primary_characteristic_rows_acquired"] != 0 or obs["actual_primary_reference_rows_acquired"] != 0:
            raise ValueError("Specification follow-up changed; review new authoritative rows")
        sid = self.artifact("PA-SRC-SPEC-FOLLOWUP", SPEC / "observations.json", "Original bolt specification follow-up: no authoritative item rows acquired")
        refs=[sid]
        for row in self.read(SPEC / "sources.json")["sources"]:
            ident="PA-SPEC-SRC-" + row["id"]
            self.source(ident, "Specification route: " + row["id"], row["url"], accessed_at=row["observed_on"],
                retrieval_depth=row["retrieval_depth"], supported_facts=row["supported_facts"],
                item_row_acquired=False)
            refs.append(ident)
        self.node("PA-SPEC-FOLLOWUP-20261030", "source_access_observation", "Original bolt technical comparison remains unresolved", refs,
            observation=obs, authoritative_characteristics_rows=0, authoritative_reference_rows=0,
            parser_is_authentication=False, price_benchmark_qualified=False)
        self.edge("documents_specification_gap", "PA-W1-SPEC-BOLT", "PA-SPEC-FOLLOWUP-20261030", refs)
        for name in ["parse_publog_export.py", "export-packet.json", "query_log.json", "prior-inputs.json", "VALIDATION.json"]:
            self.pin(SPEC / name)
        for artifact in self.read(SPEC / "prior-inputs.json")["inputs"]:
            self.pin(SPEC / artifact["path"], artifact["sha256"])
        live = self.read(AGENTS / "tracing/runs/live-public-source-proof-final.json")
        coverage = live["coverage"]
        if coverage["http_requests_sent_confirmed"] != 0 or coverage["acquired_documents"] != 0:
            raise ValueError("Tracer live scope changed")
        ts=self.artifact("PA-SRC-TRACER-LIVE", AGENTS / "tracing/runs/live-public-source-proof-final.json", "Direct tracer live proof: DNS failure before HTTP")
        self.node("PA-TRACER-LIVE-20261030", "local_execution_observation", "Direct tracer: 3 logical attempts, 0 HTTP requests and 0 acquired documents", [ts],
            coverage=coverage, scope=live["scope"], attempts=live["attempts"],
            runtime_reservation_bridge_implemented=False, other_research_tools_inferred_unavailable=False)
        self.edge("records_tracer_scope", COLLECTION, "PA-TRACER-LIVE-20261030", [ts])
        for name in ["trace_links.py", "README.md", "validation.json", "examples/live-public-source-plan.json"]:
            self.pin(AGENTS / "tracing" / name)
        actual = self.read(AGENTS / "analysis/examples/actual-blocked-result.json")
        synthetic = self.read(AGENTS / "analysis/examples/synthetic-result.json")
        if actual["groups"][0]["eligible_lines"] != 0 or actual["groups"][0]["weighted_premium_percent_display"] is not None:
            raise ValueError("Actual recurrence screen scope changed")
        ass=self.artifact("PA-SRC-RECURRENCE-ACTUAL", AGENTS / "analysis/examples/actual-blocked-result.json", "Actual single-line recurrence attempt remains blocked")
        syn=self.artifact("PA-SRC-RECURRENCE-SYNTHETIC", AGENTS / "analysis/examples/synthetic-result.json", "Invented four-line recurrence calibration")
        self.node("PA-RECURRENCE-ACTUAL-BLOCKED", "arithmetic_screen_observation", "No real repeated premium established: actual comparison is blocked", [ass],
            result=actual, actual_repeated_premium=None, real_loss=None, real_buyer_benefit=None,
            purchasing_office_label_is_only_piid_prefix=True)
        self.node("PA-RECURRENCE-SYNTHETIC", "synthetic_calibration_observation", "Synthetic four-line 12% example exercises the recurrence calculator", [syn],
            data_origin="illustrative", evidence_kind="synthetic_calibration", real_transactions=0,
            invented_line_count=4, calibration_percent="12", real_financial_totals_included=False,
            source_result_path="price-agents/analysis/examples/synthetic-result.json",
            inference_limit="Calculator behavior only; not an actual purchase, misconduct finding or measured loss")
        self.edge("records_blocked_actual_screen", COLLECTION, "PA-RECURRENCE-ACTUAL-BLOCKED", [ass])
        self.edge("records_synthetic_calibration_only", COLLECTION, "PA-RECURRENCE-SYNTHETIC", [syn])
        for name in ["recurrence.py", "README.md", "examples/actual-blocked-input.json", "examples/actual-blocked-plan.json",
                     "examples/actual-blocked-metadata.json", "examples/synthetic-input.json", "examples/exploratory-plan.json",
                     "examples/synthetic-metadata.json"]:
            self.pin(AGENTS / "analysis" / name)

    def finish(self, review_paths):
        omitted_review_dependencies=[]
        for path in review_paths:
            self.pin(ROOT / path)
            if Path(path).suffix == ".json":
                review=json.loads((ROOT / path).read_text())
                for artifact in review.get("reviewed_input_artifacts", []):
                    candidate=(ROOT.parents[1] / artifact["path"]).resolve()
                    if any(candidate.is_relative_to(base) for base in (ROOT / "investigations", AGENTS)):
                        self.pin(candidate, artifact["sha256"])
                    else:
                        omitted_review_dependencies.append(dict(path=artifact["path"],
                            reason="Outside approved investigation/agent input roots; review receipt retains its declared hash"))
        self.pin(Path(__file__))
        graph=dict(version="1.0", as_of=DAY,
            projection_status="candidate_requires_separate_registry_approval",
            pin_scope="Explicit relevant immutable inputs; no automatic directory ingestion or graph promotion",
            omitted_review_dependencies=omitted_review_dependencies,
            input_artifacts=[dict(path=p,sha256=d) for p,d in sorted(self.inputs.items())],
            nodes=self.nodes, edges=self.edges)
        spec=importlib.util.spec_from_file_location("price_agent_graph_integrity", ROOT / "engine/integrity.py")
        engine=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(engine)
        counts=engine.validate_graph(graph,public=True)
        prior=json.loads((ROOT / "data/graph.json").read_text())
        old_ids={x["id"] for x in prior["nodes"]+prior["edges"]}
        new_ids={x["id"] for x in self.nodes+self.edges}
        collisions=old_ids & new_ids
        # A re-run after approval is permitted only if the existing record equals
        # this projection exactly; never silently replace a changed graph ID.
        old_by_id={x["id"]:x for x in prior["nodes"]+prior["edges"]}
        new_by_id={x["id"]:x for x in self.nodes+self.edges}
        if any(old_by_id[i] != new_by_id[i] for i in collisions):
            raise ValueError("Canonical graph ID collision with unequal content")
        target=HERE / "graph-extension.json"
        target.write_text(json.dumps(graph,indent=2,ensure_ascii=False)+"\n")
        print(json.dumps({"path":str(target.relative_to(ROOT)),"sha256":hashlib.sha256(target.read_bytes()).hexdigest(),
            **counts,"input_artifacts":len(self.inputs),"existing_identical_records":len(collisions),
            "final_review_pins":review_paths,"canonical_registry_modified":False}))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-pin",action="append",default=[],help="Explicit frozen review path relative to us-integrity")
    args=parser.parse_args()
    projection=Projection()
    projection.plan()
    mapping,sources=projection.pilot()
    projection.parties(mapping,sources)
    projection.local_run()
    projection.scoped_modules()
    projection.finish(args.review_pin)


if __name__ == "__main__":
    main()
