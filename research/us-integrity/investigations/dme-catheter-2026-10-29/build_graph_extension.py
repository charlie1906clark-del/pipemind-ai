#!/usr/bin/env python3
"""Generate the DME public evidence extension from explicitly selected reports.

Offline and deterministic. This writes a candidate extension; it does NOT grant
approval. A reviewer separately pins its digest in approved-investigations.json.
No individual outlier ranking or ownership inference enters the graph.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DAY = "2026-10-29"
nodes, edges, by_id, sources_by_url, inputs = [], [], {}, {}, {}
INV = "DME-INV-20261029"


def read(relative):
    path = HERE / relative
    inputs[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return json.loads(path.read_text())


def pin(relative):
    path = HERE / relative
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    inputs[str(path.relative_to(ROOT))] = digest
    return digest


def n(ident, typ, title, status="documented_fact", sources=(), **properties):
    if ident in by_id:
        raise ValueError("Duplicate extension node: " + ident)
    record = dict(id=ident, type=typ, title=title, status=status,
                  source_ids=sorted(set(sources)), properties={"visibility": "public", **properties})
    nodes.append(record)
    by_id[ident] = record
    return ident


def e(kind, subject, obj, sources=(), status="documented_fact", **properties):
    ident = "DME-E-" + hashlib.sha256(f"{kind}|{subject}|{obj}".encode()).hexdigest()[:20]
    if any(edge["id"] == ident for edge in edges):
        raise ValueError("Duplicate extension relationship")
    edges.append(dict(id=ident, type=kind, source=subject, target=obj, status=status,
        source_ids=sorted(set(sources)), properties={"visibility": "public", **properties}))


def source(ident, title, url, **properties):
    if url in sources_by_url:
        existing = sources_by_url[url]
        by_id[existing]["properties"].setdefault("registry_aliases", []).append(ident)
        return existing
    sources_by_url[url] = ident
    return n(ident, "source", title, "source", url=url, accessed_at=DAY,
             source_bytes_archived=False, **properties)


def capture_source(ident, title, url, relative_snapshot, **properties):
    result = source(ident, title, url, **properties)
    path = HERE / relative_snapshot
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    inputs[str(path.relative_to(ROOT))] = digest
    by_id[result]["properties"].update(source_bytes_archived=True,
        snapshot_path=str(path.relative_to(ROOT)), content_sha256=digest,
        hash_scope="Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response")
    return result


def finding(ident, title, sources, status="documented_fact", **properties):
    result = n(ident, "finding", title, status, sources, **properties)
    e("records_finding", INV, result, sources, status=status)
    return result


def money(parent, suffix, title, amount, kind, sources, period="not_specified",
          qualifier="as_reported", status="documented_fact", **properties):
    result = n(parent + "-money-" + suffix, "money_measure", title, status, sources,
        money=dict(amount=str(amount), currency="USD", kind=kind, period=period,
                   qualifier=qualifier, basis=properties.pop("basis", "Attributed source or stated reconstruction")),
        aggregation_permitted=False, independently_verified_collection=False,
        **properties)
    e("reports_amount", parent, result, sources, status=status)
    return result


def add_data():
    analysis = read("data-audit/analysis.json")
    manifest = read("data-audit/acquisition_manifest.json")
    manifests = manifest["cohorts"]
    cohort_sources = {}
    for capture in manifests:
        year, code = capture["year"], capture["code"]
        sid = capture_source(f"DME-SRC-PUF-{year}-{code}", f"CMS supplier detail: {year} {code}",
            capture["pages"][0]["url"], "data-audit/" + capture["snapshot"],
            dataset_uuid=capture["dataset_uuid"], period=str(year),
            completion=capture["completion"], selected_columns=capture["columns"],
            request_manifest="investigations/dme-catheter-2026-10-29/data-audit/acquisition_manifest.json")
        if by_id[sid]["properties"]["content_sha256"] != capture["snapshot_sha256"]:
            raise ValueError("Supplier snapshot differs from acquisition manifest")
        cohort_sources[(year, code)] = sid
    for row in analysis["summaries"]:
        year, code = row["year"], row["code"]
        sid = cohort_sources[(year, code)]
        cid = n(f"DME-COHORT-{year}-{code}", "dataset_cohort", f"{year} {code}: published supplier rows",
            sources=[sid], scope=analysis["cohort_scope"], metrics=row,
            no_fraud_determination=True, cash_reconciliation="not_performed",
            national_unique_beneficiaries="not_calculable_from_supplier_sums",
            complete_public_filtered_rows=True, complete_underlying_claims=False)
        e("examines_cohort", INV, cid, [sid])
        for kind, amount in row["amounts_usd_reconstructed"].items():
            money(cid, kind, f"{year} {code}: reconstructed supplier-detail {kind}", amount,
                "reconstructed_puf_" + kind, [sid], period=str(year), qualifier="approximate_reconstructed",
                basis="Sum of each row's services multiplied by its published per-service average",
                claim_of_fraud_loss=False, cash_disbursement_reconciliation=False)
    for row in analysis["comparisons"]:
        before, after, code = row["before_year"], row["after_year"], row["code"]
        sources = [cohort_sources[(before, code)], cohort_sources[(after, code)]]
        fid = finding(f"DME-CHANGE-{before}-{after}-{code}", f"{code}: {before}–{after} exact-row decomposition",
            sources, calculation=row, inference_limit=analysis["amount_method"],
            source_record="data-audit/analysis.json#/comparisons")
        for year in [before, after]:
            e("compares_cohort", fid, f"DME-COHORT-{year}-{code}", sources)
    for row in analysis.get("cross_code_entry_controls", []):
        before, after = row["before_year"], row["after_year"]
        sources = [cohort_sources[(before, code)] for code in ["A4351", "A4352", "A4353"]]
        sources.append(cohort_sources[(after, "A4353")])
        finding(f"DME-ENTRY-CONTROL-{before}-{after}", f"A4353 code entry compared with other catheter codes, {before}–{after}",
            sources, calculation=row, no_business_formation_inference=True)
    nat_manifest = read("data-audit/national_acquisition_manifest.json")
    reconciliation = read("data-audit/national_reconciliation.json")
    for row in reconciliation:
        year, code = row["year"], row["code"]
        request = next(r for r in nat_manifest["requests"] if r["year"] == year and r["code"] == code)
        sid = capture_source(f"DME-SRC-NATIONAL-{year}-{code}", f"CMS national geography aggregate: {year} {code}",
            request["url"], "data-audit/snapshots/national_2022_2024.json",
            capture_scope="Combined nine national responses; select matching year and HCPCS before interpreting",
            dataset_uuid=request["dataset_uuid"], selected_year=year, selected_hcpcs=code)
        sources = [sid, cohort_sources[(year, code)]]
        fid = finding(f"DME-NATIONAL-CHECK-{year}-{code}", f"{year} {code}: supplier detail versus national aggregate",
            sources, reconciliation=row, not_additive_with_supplier_detail=True)
        money(fid, "national-puf-payment", f"{year} {code}: national reconstructed payment measure",
            row["national_amounts_usd_reconstructed"]["puf_payment"], "reconstructed_national_puf_payment", [sid],
            period=str(year), qualifier="approximate_reconstructed",
            basis="National geography/service published average multiplied by services",
            not_additive_with_supplier_detail=True, claim_of_fraud_loss=False)
    return cohort_sources


def add_falsification(cohort_sources):
    evidence = read("falsification/evidence_records.json")
    review = read("falsification/data_review.json")
    if not review.get("passed"):
        raise ValueError("Independent arithmetic review has not passed")
    for relative, key in [
        ("data-audit/analysis.json", "analysis_sha256"),
        ("data-audit/audit_catheters.py", "script_reviewed_sha256"),
        ("data-audit/snapshots/national_2022_2024.json", "national_snapshot_sha256"),
        ("data-audit/national_reconciliation.json", "national_reconciliation_sha256")]:
        if pin(relative) != review[key]:
            raise ValueError("Independent review refers to a different input: " + relative)
    for relative, digest in review["snapshot_sha256"].items():
        if pin(relative) != digest:
            raise ValueError("Independent review refers to a different supplier snapshot")
    refs = {}
    for key, row in evidence["sources"].items():
        refs[key] = source("DME-SRC-FALS-" + key, row["title"], row["url"],
            publication_date=row["date"], publication_date_basis=row["date_basis"],
            retrieval_method="specialist_web_review", source_record="falsification/evidence_records.json")
    for row in evidence["evidence_records"]:
        if row["source_id"] == "local-data-audit":
            sources = sorted(cohort_sources.values())
        else:
            sources = [refs[row["source_id"]]]
        status = "allegation" if row["legal_status"] == "allegation" else "documented_fact"
        fid = finding(row["id"], row["claim"], sources, status, locator=row["locator"],
            inference_limit=row["inference_limit"], finding_type=row["finding_type"],
            underlying_record_status=row["legal_status"], source_record="falsification/evidence_records.json")
        if "money" in row:
            amount = row["money"]
            measures = [("attributed", amount["amount_usd"])] if "amount_usd" in amount else [
                ("total", amount["total_usd"]), ("pharmacy-category", amount["pharmacy_category_usd"])]
            for label, value in measures:
                money(fid, label, row["claim"] + " — " + label, value, amount["basis"], sources,
                    period=amount.get("period", "source_period_not_stated_here"), qualifier=amount.get("qualifier", "as_reported"),
                    status=status, source_amount_details=amount, subtotal_overlap_not_additive=True)


def add_case_trace():
    evidence = read("case-trace/evidence_records.json")
    refs = {}
    for row in evidence["sources"]:
        props = {key: value for key, value in row.items() if key not in {
            "id", "title", "url", "accessed_at", "browse_ref", "sha256"}}
        if "sha256" in row:
            props["retrieved_original_sha256"] = row["sha256"]
            props["digest_scope"] = "Downloaded source bytes kept outside this public repository; not an archived-source assertion"
        refs[row["id"]] = source("DME-SRC-" + row["id"], row["title"], row["url"], **props)
    for row in evidence["direct_findings"]:
        props = {key: value for key, value in row.items() if key not in {
            "id", "statement", "status", "source_ids", "visibility", "amounts"}}
        sources = [refs[s] for s in row["source_ids"]]
        fid = finding("DME-" + row["id"], row["statement"], sources, row["status"],
            public_record=True, novel_lead=False, source_record="case-trace/evidence_records.json", **props)
        for i, amount in enumerate(row.get("amounts", []), 1):
            period = amount["period"]
            if period == "same":
                period = row["amounts"][0]["period"]
            amount_status = "allegation" if amount["measure"].startswith("alleged_") else row["status"]
            money(fid, str(i), row["statement"] + " — " + amount["measure"], amount["amount"],
                amount["measure"], sources, period=period, qualifier=amount["qualifier"], status=amount_status,
                payer=amount.get("payer"), overlap_group=amount["overlap_group"],
                source_amount_details=amount, cash_recovery_not_established=True)
    cases = {
        "EDNY Nakhmatullaev et al.": ("EDNY", "indicted", "published_case", "indicted; individual current dispositions not exhaustively verified"),
        "Kakha Bendeliani": ("Bendeliani", "indicted", "published_case", "indicted"),
        "Goga Danelia": ("Danelia", "complaint", "published_case", "charged_by_complaint"),
        "Erekle Gugava": ("Gugava", "indicted", "published_case", "indicted"),
        "Renat Abramov": ("Abramov", "sentenced", "conviction", "sentenced"),
        "Elnar Zarbailov": ("Zarbailov", "sentenced", "conviction", "sentenced"),
        "Eldar Zarbavel": ("Zarbavel", "guilty_plea", "conviction", "pleaded_guilty; sentencing scheduled2026-12-16")}
    for row in evidence["legal_status_if_case"]:
        slug, legal, status, expected_detail = cases[row["case"]]
        if row["status"] != expected_detail:
            raise ValueError("Case disposition changed and requires a new explicit graph review")
        sources = [refs[s] for s in row["source_ids"]]
        cid = n("DME-CASE-" + slug, "case", row["case"], status, sources,
            legal_status=legal, legal_status_detail=row["status"], source_status_date=row["as_of_source"],
            public_record=True, novel_lead=False,
            docket_scope="Latest disposition in reviewed sources; not a complete live-docket certification")
        e("examines_published_case", INV, cid, sources)
    # Explicitly connect only the public filings that identify these businesses.
    for ids, company in [
        (["CT-F005", "CT-F006", "CT-F007", "CT-F008", "CT-F009", "CT-F010", "CT-F011"],
         "identity-org-centennial-med-supply"),
        (["CT-F012", "CT-F013", "CT-F014"], "identity-org-nd-medical-solutions")]:
        for ident in ids:
            record = by_id["DME-" + ident]
            e("concerns_published_organization", record["id"], company,
              record["source_ids"], status=record["status"], no_inherited_liability=True)
    for slug, pid in [("Bendeliani", "identity-person-bendeliani"),
                      ("Danelia", "identity-person-danelia"), ("Gugava", "identity-person-gugava")]:
        cid = "DME-CASE-" + slug
        e("names_defendant", cid, pid, by_id[cid]["source_ids"])
    roles = next(row for row in evidence["direct_findings"] if row["id"] == "CT-F002")["roles"]
    for name, role in roles.items():
        pid = "DME-EDNY-PERSON-" + name.replace(" ", "-")
        n(pid, "person", name, sources=[refs["CT-S003"]], public_record=True,
          identity_scope="Exact label in published indictment; no names-only merge to other sources",
          latest_disposition="Not exhaustively verified beyond reviewed indictment")
        e("alleged_role_in", pid, "DME-CASE-EDNY", [refs["CT-S003"]], status="allegation", role=role)
    for slug, fid, name in [("Abramov", "CT-F018", "Renat Abramov"),
                            ("Zarbailov", "CT-F019", "Elnar Zarbailov"),
                            ("Zarbavel", "CT-F020", "Eldar Zarbavel")]:
        sources = by_id["DME-" + fid]["source_ids"]
        pid = n("DME-PERSON-" + slug, "person", name, sources=sources,
            public_record=True, identity_scope="Named person in the cited case event")
        e("names_defendant", "DME-CASE-" + slug, pid, sources)
        e("reports_disposition", "DME-" + fid, "DME-CASE-" + slug, sources, status="conviction")
    royce_sources = [refs["CT-S018"]]
    n("DME-ORG-ROYCE", "organization", "Royce Medical Supply LLC", sources=royce_sources,
      public_record=True, identity_scope="Published DOJ label; exact NPI and state registry not resolved here",
      geographic_scope="Florida business in release; no beneficial owner inference")
    e("mentions_company", "DME-CT-F020", "DME-ORG-ROYCE", royce_sources,
      status="documented_fact", scope="Named in guilty-plea release; record does not confer liability on unrelated parties")
    sources = [refs["CT-S009"]]
    for ordinal in ["second", "third"]:
        n("DME-UNNAMED-" + ordinal.upper(), "published_unidentified_entity",
            f"{ordinal.title()} unnamed DME counterparty in Danelia affidavit", "allegation", sources,
            identity="not_disclosed_in_source", source_locator="affidavit paragraph 47",
            no_deanonymization_attempted=True, transfer_purpose="expressly still under investigation")
    e("reported_transfer_from", "DME-CT-F009-money-1", "DME-UNNAMED-SECOND", sources, status="allegation")
    e("reported_transfer_to", "DME-CT-F009-money-1", "identity-org-centennial-med-supply", sources, status="allegation")
    e("reported_transfer_from", "DME-CT-F009-money-2", "identity-org-centennial-med-supply", sources, status="allegation")
    e("reported_transfer_to", "DME-CT-F009-money-2", "DME-UNNAMED-THIRD", sources, status="allegation")
    finding("DME-UNNAMED-TRANSFER-QUESTION", "What explains the two unnamed intercompany transfer relationships?",
        sources, "unknown", source_locator="Danelia affidavit paragraph 47",
        missing_evidence="Publicly disclosed counterparty identities, transaction purpose and invoices or contracts; none established in this packet",
        alternatives=["Legitimate intercompany payment", "Refund or supplier settlement", "Transfer of proceeds as alleged in broader case"],
        no_new_fraud_conclusion=True, already_known_to_investigators=True)
    timeline = read("case-trace/timeline.json")
    for event in timeline["events"]:
        sources = [refs[s] for s in event["source_ids"]]
        eid = n("DME-" + event["id"], "case_timeline_event", event["event"], event["status"], sources,
            event_date=event["date"], date_precision=event["date_precision"],
            source_record="case-trace/timeline.json", event_scope="Date/event as characterized in cited source; allegation and official action remain distinct")
        e("records_event", INV, eid, sources, status=event["status"])


def add_identity():
    evidence = read("identity/evidence_records.json")
    refs = {}
    for row in evidence["sources"]:
        props = row["properties"].copy()
        url = props.pop("url")
        props.pop("accessed_at", None)
        if props.get("snapshot_file"):
            sid = capture_source(row["id"], row["title"], url, "identity/" + props["snapshot_file"],
                capture_scope="Sanitized selected official records only; no complete upstream NPPES/LEIE archive", **props)
        else:
            sid = source(row["id"], row["title"], url, **props)
        refs[row["id"]] = sid
    for row in read("identity/entities.json"):
        typ = "person" if row["type"] == "public_case_person" else row["type"]
        sources = [refs[s] for s in row["source_ids"]]
        n(row["id"], typ, row["title"], row["status"], sources,
          public_record=True, **row["properties"])
        e("includes_identity_record", INV, row["id"], sources, status=row["status"])
    for row in read("identity/relationships.json"):
        e(row["type"], row["source"], row["target"], [refs[s] for s in row["source_ids"]],
          status=row["status"], original_record_id=row["id"], **row["properties"])
    for row in evidence["records"]:
        props = {key: value for key, value in row.items() if key not in {"id", "status", "source_ids", "finding"}}
        title = row.get("finding", "Centennial acquisition milestones are distinct dated allegations")
        finding(row["id"], title, [refs[s] for s in row["source_ids"]], row["status"],
            source_record="identity/evidence_records.json", **props)


def add_enrollment(cohort_sources):
    manifest = read("enrollment/acquisition_manifest.json")
    crosscheck = read("enrollment/crosscheck.json")
    known = read("enrollment/snapshots/known_case_matches.json")
    refs = []
    for ident, url, snapshot, title in [
        ("DME-SRC-REVOCATIONS-Q3-2026", manifest["immutable_data_root"] + "/data",
         "enrollment/snapshots/revoked_selected.json", "CMS Q3 2026 revoked enrollments: selected public fields"),
        ("DME-SRC-REVOCATIONS-ADDITIONAL-NPIS", manifest["additional_request"]["url"],
         "enrollment/snapshots/additional_npis.json", "CMS Q3 2026 revoked enrollments: additional NPIs")]:
        refs.append(capture_source(ident, title, url, snapshot,
            catalog_modified=manifest["modified"], temporal_coverage=manifest["temporal"],
            capture_scope="All public rows, selected noncontact fields; snapshot rather than live enrollment status",
            request_manifest="enrollment/acquisition_manifest.json"))
    for row in read("enrollment/supporting_sources.json"):
        sid = source("DME-SRC-ENROLLMENT-" + row["id"].replace("_", "-"), row["id"].replace("_", " "), row["url"],
            retrieval_metadata=row)
        if row["id"] == "cms_methodology":
            refs.append(sid)
    overview = {key: value for key, value in crosscheck.items() if key not in {"cohorts", "known_case_puf_presence", "cohort_input_sha256"}}
    all_sources = refs + sorted(cohort_sources.values())
    finding("DME-REVOCATION-COHORT-OVERVIEW", "64 of 1,976 cohort NPIs match the current revocation snapshot",
        all_sources, calculation=overview,
        inference_limit="An exact NPI intersection is neither a fraud rate nor proof the corresponding annual claims were paid after revocation.")
    for row in crosscheck["cohorts"]:
        year, code = row["year"], row["code"]
        data_sources = [cohort_sources[(year, code)]] if code != "ALL_THREE_CODES" else [
            cohort_sources[(year, c)] for c in ["A4351", "A4352", "A4353"]]
        finding(f"DME-REVOCATION-CROSSCHECK-{year}-{code}", f"{year} {code}: current revocation intersection",
            refs + data_sources, calculation=row, inference_limits=crosscheck["interpretation"],
            named_new_suspicions_published=False)
    companies = {"nd_medical": "identity-org-nd-medical-solutions", "centennial": "identity-org-centennial-med-supply"}
    for key, company in companies.items():
        sid = capture_source("DME-SRC-REVOKED-" + key.replace("_", "-"),
            f"CMS exact enrollment revocation lookup: {known[key][0]['ORG_NAME']}",
            manifest["known_case_requests"][key]["url"], "enrollment/snapshots/known_case_matches.json",
            capture_scope="Combined two known-case responses; select matching NPI before interpreting",
            selected_npi=known[key][0]["NPI"], catalog_modified=manifest["modified"])
        for row in known[key]:
            rid = n("DME-REVOCATION-" + row["ENRLMT_ID"], "administrative_revocation_record",
                f"{row['ORG_NAME']}: revocation effective {row['REVOCATION_EFCTV_DT']}",
                sources=[sid], record=row, criminal_adjudication=False,
                interpretation="Specific revoked enrollment and current bar record; NPI activity, OIG exclusion and preclusion are separate states")
            e("has_revoked_enrollment", company, rid, [sid], exact_npi_match=True)
        presence = crosscheck["known_case_puf_presence"][key]
        result = finding("DME-PUF-PRESENCE-" + key.replace("_", "-"),
            f"{known[key][0]['ORG_NAME']}: exact NPI presence in the 2022–2024 catheter cohorts",
            [sid] + sorted(cohort_sources.values()), observation=presence,
            inference_limit="Annual 2024 data cannot establish any 2025 owner or defendant's conduct, post-revocation payment or released cash; missing rows are not zero billing.")
        e("reports_cohort_presence_for", result, company, [sid] + sorted(cohort_sources.values()))
    evidence = read("enrollment/evidence_records.json")
    # The complete reviewer packet is input-pinned. Distinct dated registry records
    # and aggregate joins above are the intentionally bounded graph projection.
    by_id["DME-REVOCATION-COHORT-OVERVIEW"]["properties"]["review_packet"] = "enrollment/evidence_records.json"
    followup = read("enrollment/candidate_followup_summary.json")
    followup_sources = []
    for row in followup["source_main_versions"]:
        followup_sources.append(source("DME-SRC-PPEF-" + row["label"].replace("_", "-"),
            "CMS approved enrollment snapshot " + row["label"], row["data_url"],
            catalog_modified=row["modified"], retrieval_scope="Bounded exact candidate queries; identifying query parameters and responses omitted from public packet",
            public_reproducibility="Methods and anonymous outcomes only; national dataset is public"))
    followup_sources.append(source("DME-SRC-PPEF-ADDITIONAL", "CMS approved enrollments additional NPI table",
        followup["additional_npi_source"], retrieval_scope="Two bounded exact matches reviewed; identifiers not published"))
    followup_sources.append(source("DME-SRC-PPEF-METHOD", "CMS approved provider enrollment guidance",
        followup["source_methodology"]))
    for row in followup["candidates"]:
        finding("DME-ANONYMOUS-ENROLLMENT-" + row["label"].split()[-1],
            row["label"] + ": unresolved enrollment-scope follow-up", followup_sources + refs, "unknown",
            bounded_observation=row, unknowns=followup["unknowns"], source_record="enrollment/candidate_followup_summary.json",
            public_reproducibility="Identifying query parameters and responses intentionally omitted; no named allegation is published",
            fraud_finding=False, scope=followup["scope"])


def main():
    n(INV, "investigation", "Urinary-catheter public evidence investigation — 2026-10-29", "planned",
        scope="Published cases, selected public CMS cohorts and exact registry cross-checks",
        report_path="investigations/dme-catheter-2026-10-29/REPORT.md",
        novel_fraud_cases_established=0, agents_running_unattended=False)
    cohort_sources = add_data()
    add_falsification(cohort_sources)
    add_case_trace()
    add_identity()
    add_enrollment(cohort_sources)
    by_id[INV].update(status="documented_fact", source_ids=sorted(cohort_sources.values()))
    e("deepens_sector_research", INV, "sector-healthcare-dme", sorted(cohort_sources.values()))
    umbrella_sources = by_id["DME-CT-F001"]["source_ids"]
    e("examines_existing_published_case", INV, "HC-C02", umbrella_sources,
      scope="Foundation umbrella case; no case total is added to component figures")
    by_id[INV]["properties"].update(
        research_pass_status="completed_bounded_public_research",
        completed_specialist_roles=["claims data audit", "case trace", "identity resolution",
            "enrollment cross-check", "independent falsification", "graph integration"],
        interpretation="Completed bounded public checks within an ongoing research project; no new fraud case established")
    graph = dict(version="1.0", as_of=DAY,
        input_artifacts=[dict(path=p, sha256=inputs[p]) for p in sorted(inputs)],
        nodes=sorted(nodes, key=lambda node: node["id"]),
        edges=sorted(edges, key=lambda edge: edge["id"]))
    (HERE / "graph-extension.json").write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(dict(nodes=len(nodes), edges=len(edges), types=dict(Counter(n["type"] for n in nodes))), indent=2))


if __name__ == "__main__":
    main()
