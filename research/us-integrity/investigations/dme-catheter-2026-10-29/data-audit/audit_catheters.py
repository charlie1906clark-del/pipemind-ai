#!/usr/bin/env python3
"""Reproduce a bounded, public CMS DME supplier/service cohort audit.

stdlib only. Fetches selected non-contact columns, verifies filtered API counts,
records exact response hashes, then computes aggregates using Decimal. No names,
street addresses, patients, or novel named suspicion are exported.
"""
from __future__ import annotations
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import statistics
import time
import urllib.parse
import urllib.request
from decimal import Decimal as D

BASE = Path(__file__).resolve().parent
API = "https://data.cms.gov/data-api/v1/dataset/"
DATASETS = {
    2022: "dad703df-2e52-4ac6-a26f-51ecbf463d77",
    2023: "44235fd3-6cf9-487f-928d-12998cd84071",
    2024: "1746a83e-bb65-4300-8e02-21edbab77c6b",
}
CODES = ("A4351", "A4352", "A4353")
GEO_DATASETS = {2022: "a9d1461a-9c63-49e1-8d91-696082e20e47",
                2023: "87dc62d2-5671-4eb0-9b1a-dfe267a1fa1d",
                2024: "27c150fd-8578-43b1-bba5-6388987e32af"}
FIELDS = ["Suplr_NPI", "Suplr_Prvdr_Ent_Cd", "Suplr_Prvdr_State_Abrvtn",
          "Suplr_Prvdr_Spclty_Cd", "Suplr_Prvdr_Spclty_Desc", "HCPCS_Cd",
          "HCPCS_Desc", "Suplr_Rentl_Ind", "Tot_Suplr_Benes", "Tot_Suplr_Clms",
          "Tot_Suplr_Srvcs", "Avg_Suplr_Sbmtd_Chrg", "Avg_Suplr_Mdcr_Alowd_Amt",
          "Avg_Suplr_Mdcr_Pymt_Amt", "Avg_Suplr_Mdcr_Stdzd_Amt"]
MEASURES = {"submitted": "Avg_Suplr_Sbmtd_Chrg", "allowed": "Avg_Suplr_Mdcr_Alowd_Amt",
            "puf_payment": "Avg_Suplr_Mdcr_Pymt_Amt", "standardized_payment": "Avg_Suplr_Mdcr_Stdzd_Amt"}
PAGE_SIZE = 5000

def sha(b): return hashlib.sha256(b).hexdigest()
def canonical(obj): return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def save(path, obj): path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

def request(url):
    attempts = []
    for n in range(3):
        started = now()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Pipemind-public-data-audit/1.0"})
            with urllib.request.urlopen(req, timeout=20) as response:
                payload = response.read()
                record = {"url": url, "retrieved_at": started, "status": response.status,
                          "bytes": len(payload), "wire_response_sha256": sha(payload),
                          "content_type": response.headers.get("Content-Type"),
                          "last_modified": response.headers.get("Last-Modified"),
                          "etag": response.headers.get("ETag"), "prior_attempts": attempts}
            return json.loads(payload), record
        except Exception as exc:
            attempts.append({"at": started, "error": str(exc), "type": type(exc).__name__})
            if n == 2: raise RuntimeError(json.dumps({"url": url, "attempts": attempts})) from exc
            time.sleep(1 + n)

def fetch_cohort(year, code):
    root = API + DATASETS[year]
    count_query = urllib.parse.urlencode({"filter[HCPCS_Cd]": code})
    count, count_record = request(root + "/data/stats?" + count_query)
    expected = int(count["found_rows"])
    rows, pages, offset = [], [], 0
    while True:
        query = urllib.parse.urlencode({"filter[HCPCS_Cd]": code, "column": ",".join(FIELDS),
                                       "sort": "Suplr_NPI", "size": PAGE_SIZE, "offset": offset})
        page, rec = request(root + "/data?" + query)
        if not isinstance(page, list): raise ValueError("Data endpoint did not return list")
        rec.update({"offset": offset, "returned_rows": len(page), "requested_size": PAGE_SIZE})
        pages.append(rec)
        if not page: break
        rows.extend(page)
        offset += len(page)  # Explicit terminal empty page even for short pages.
    if len(rows) != expected: raise ValueError(f"Count mismatch {year} {code}: {len(rows)} != {expected}")
    keys = [(r["Suplr_NPI"], year, r["HCPCS_Cd"], r["Suplr_Rentl_Ind"]) for r in rows]
    if len(set(keys)) != len(keys): raise ValueError("Duplicate NPI/year/HCPCS/rental key")
    if any(set(r) != set(FIELDS) or r["HCPCS_Cd"] != code for r in rows): raise ValueError("Schema/filter drift")
    if any(not r["Suplr_NPI"].isdigit() or len(r["Suplr_NPI"]) != 10 for r in rows): raise ValueError("Invalid NPI")
    for r in rows:
        for field in ["Tot_Suplr_Clms", "Tot_Suplr_Srvcs", *MEASURES.values()]:
            if r[field] == "" or D(r[field]) < 0: raise ValueError(f"Missing/negative {field}")
    # Response data already selected on CMS server. Canonical ordering is a transformation.
    rows.sort(key=lambda r: (r["Suplr_NPI"], r["HCPCS_Cd"], r["Suplr_Rentl_Ind"]))
    path = BASE / "snapshots" / f"suppliers_{year}_{code}.json"
    save(path, rows)
    return {"year": year, "code": code, "dataset_uuid": DATASETS[year], "stats": count,
            "stats_request": count_record, "pages": pages, "rows": len(rows),
            "unique_exact_keys": len(set(keys)), "schema_sha256": sha(canonical(sorted(FIELDS))),
            "columns": FIELDS, "snapshot": str(path.relative_to(BASE)),
            "snapshot_sha256": sha(path.read_bytes()),
            "canonical_rows_sha256": sha(canonical(rows)),
            "hash_scope": "Wire hashes cover server-side column-selected responses, not full CMS source. Snapshot hash covers prettified, key-sorted selected rows; canonical hash covers compact sorted-key JSON.",
            "completion": "Filtered stats count matched; next offset returned an empty page."}

def num(r, field): return D(r[field])
def amount(r, measure="puf_payment"): return num(r, "Tot_Suplr_Srvcs") * num(r, MEASURES[measure])
def rounded(x): return str(x.quantize(D("0.01")))
def pct(n, d): return rounded(D(100) * D(n) / D(d)) if d else None
def key(r): return (r["Suplr_NPI"], r["HCPCS_Cd"], r["Suplr_Rentl_Ind"])

def metric(year, code, rows):
    amounts = [amount(r) for r in rows]
    total = sum(amounts, D(0))
    by_npi = {}
    for r in rows: by_npi[r["Suplr_NPI"]] = by_npi.get(r["Suplr_NPI"], D(0)) + amount(r)
    ranked = sorted(by_npi.values(), reverse=True)
    known_benes = [r for r in rows if r["Tot_Suplr_Benes"]]
    units_per_bene = [num(r, "Tot_Suplr_Srvcs") / num(r, "Tot_Suplr_Benes") for r in known_benes]
    services = sum(num(r, "Tot_Suplr_Srvcs") for r in rows)
    return {"year": year, "code": code, "description": sorted({r["HCPCS_Desc"] for r in rows}),
        "rows": len(rows), "suppliers": len(by_npi),
        "rental_indicators": sorted({r["Suplr_Rentl_Ind"] for r in rows}),
        "claims": str(sum(num(r, "Tot_Suplr_Clms") for r in rows)), "services": str(services),
        "amounts_usd_reconstructed": {m: rounded(sum(amount(r, m) for r in rows)) for m in MEASURES},
        "supplier_payment_median_usd": rounded(D(statistics.median(ranked))),
        "supplier_payment_p90_usd": rounded(sorted(ranked)[int((len(ranked)-1)*.9)]),
        "payment_share_top1_pct": pct(sum(ranked[:1]), total),
        "payment_share_top5_pct": pct(sum(ranked[:5]), total),
        "payment_share_top10_pct": pct(sum(ranked[:10]), total),
        "payment_hhi_0_to_10000": rounded(sum((a / total * 100)**2 for a in ranked)) if total else None,
        "weighted_payment_per_service": rounded(total/services),
        "supplier_median_payment_per_service": rounded(D(statistics.median(num(r, MEASURES["puf_payment"]) for r in rows))),
        "supplier_median_services_per_known_beneficiary": rounded(D(statistics.median(units_per_bene))),
        "known_supplier_beneficiary_sum_not_unique_people": str(sum(num(r, "Tot_Suplr_Benes") for r in known_benes)),
        "rows_with_suppressed_beneficiaries": len(rows)-len(known_benes),
        "payment_share_rows_with_suppressed_beneficiaries_pct": pct(sum(amount(r) for r in rows if not r["Tot_Suplr_Benes"]),total),
        "minimum_claim_count": str(min(num(r,"Tot_Suplr_Clms") for r in rows)),
        "missing_fields": {f: sum(r[f] == "" for r in rows) for f in FIELDS}}

def compare(before_year, after_year, code, before, after):
    a, b = {key(r): r for r in before}, {key(r): r for r in after}
    matched, entered, exited = set(a)&set(b), set(b)-set(a), set(a)-set(b)
    before_sum = sum(amount(r) for r in a.values())
    after_sum = sum(amount(r) for r in b.values())
    delta = after_sum - before_sum
    matched_delta = sum(amount(b[k])-amount(a[k]) for k in matched)
    entrants = sum(amount(b[k]) for k in entered)
    exits = sum(amount(a[k]) for k in exited)
    assert matched_delta + entrants - exits == delta
    large_base = [k for k in matched if amount(a[k]) >= 100000]
    changes = sorted((amount(b[k])-amount(a[k]) for k in matched), reverse=True)
    return {"before_year": before_year, "after_year": after_year, "code": code,
        "payment_change_usd": rounded(delta), "payment_change_pct": pct(delta,before_sum),
        "service_change_pct": pct(sum(num(r,"Tot_Suplr_Srvcs") for r in after)-sum(num(r,"Tot_Suplr_Srvcs") for r in before),sum(num(r,"Tot_Suplr_Srvcs") for r in before)),
        "matched_exact_npi_code_rental_rows": len(matched), "newly_observed_rows": len(entered), "no_longer_observed_rows": len(exited),
        "matched_payment_delta_usd": rounded(matched_delta), "newly_observed_payment_usd": rounded(entrants),
        "no_longer_observed_prior_payment_usd": rounded(exits),
        "top5_matched_positive_deltas_usd": rounded(sum(max(v,D(0)) for v in changes[:5])),
        "matched_prior_payment_at_least_100k_rows": len(large_base),
        "matched_prior_100k_median_payment_growth_pct": rounded(D(statistics.median((amount(b[k])/amount(a[k])-1)*100 for k in large_base))) if large_base else None,
        "matched_prior_100k_more_than_doubled_rows": sum(amount(b[k])>2*amount(a[k]) for k in large_base),
        "interpretation": "Newly/no-longer observed describes PUF visibility, not actual business opening/closure. No rank is a finding of fraud."}

def analyze():
    cohorts = {(y,c): json.loads((BASE/"snapshots"/f"suppliers_{y}_{c}.json").read_text()) for y in DATASETS for c in CODES}
    summaries = [metric(y,c,cohorts[y,c]) for y in DATASETS for c in CODES]
    comparisons = [compare(a,b,c,cohorts[a,c],cohorts[b,c]) for a,b in ((2022,2023),(2023,2024)) for c in CODES]
    cross_code=[]
    for before,after in ((2022,2023),(2023,2024)):
        previous_ids={r["Suplr_NPI"] for r in cohorts[before,"A4353"]}
        other_ids={r["Suplr_NPI"] for code in ("A4351","A4352") for r in cohorts[before,code]}
        entrants=[r for r in cohorts[after,"A4353"] if r["Suplr_NPI"] not in previous_ids]
        previous_other=[r for r in entrants if r["Suplr_NPI"] in other_ids]
        cross_code.append({"before_year":before,"after_year":after,"code":"A4353",
           "newly_observed_npis":len(entrants),"previously_visible_in_A4351_or_A4352":len(previous_other),
           "current_payment_for_previous_other_code_npis_usd":rounded(sum(amount(r) for r in previous_other)),
           "current_payment_for_npis_not_visible_in_any_of_three_prior_code_cohorts_usd":rounded(sum(amount(r) for r in entrants if r["Suplr_NPI"] not in other_ids)),
           "interpretation":"Code-entry is not business-entry; suppression and earlier activity outside these three codes remain unknown."})
    result = {"status": "descriptive_public_claims_audit_not_fraud_determination", "created_at": now(),
       "amount_method": "Decimal services multiplied by published per-service average; rounding only at output. Not an independent cash/recovery ledger.",
       "cohort_scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
       "national_unique_beneficiary_count": "Not calculable by summing supplier counts; suppression and overlap apply.",
       "summaries": summaries, "comparisons": comparisons,"cross_code_entry_controls":cross_code}
    save(BASE/"analysis.json",result)
    print(json.dumps(result,indent=2))

def fetch_national():
    """Fetch national aggregates separately; these include suppressed detail."""
    records, snapshots = [], []
    for year, uuid in GEO_DATASETS.items():
        for code in CODES:
            query=urllib.parse.urlencode({"filter[HCPCS_Cd]":code,"filter[Rfrg_Prvdr_Geo_Lvl]":"National","size":5000})
            rows,rec=request(API+uuid+"/data?"+query)
            if not rows or any(r["HCPCS_Cd"]!=code or r["Rfrg_Prvdr_Geo_Lvl"]!="National" for r in rows):raise ValueError("National filter mismatch")
            if len({r["Suplr_Rentl_Ind"] for r in rows})!=len(rows):raise ValueError("Duplicate national key")
            rec.update({"year":year,"code":code,"rows":len(rows),"dataset_uuid":uuid})
            records.append(rec)
            snapshots.extend({"year":year,**r} for r in rows)
    p=BASE/"snapshots"/"national_2022_2024.json";save(p,snapshots)
    save(BASE/"national_acquisition_manifest.json",{"requests":records,"snapshot":str(p.relative_to(BASE)),"snapshot_sha256":sha(p.read_bytes()),"hash_scope":"Original API response hash; snapshot additionally has year field. National all-code rows, no supplier or patient identities."})

def reconcile_national():
    path=BASE/"snapshots"/"national_2022_2024.json"
    if not path.exists():return
    rows=json.loads(path.read_text())
    output=[]
    for year in DATASETS:
        for code in CODES:
            detail=json.loads((BASE/"snapshots"/f"suppliers_{year}_{code}.json").read_text())
            national=[r for r in rows if r["year"]==year and r["HCPCS_Cd"]==code]
            detail_units=sum(num(r,"Tot_Suplr_Srvcs") for r in detail)
            national_units=sum(num(r,"Tot_Suplr_Srvcs") for r in national)
            detail_amount=sum(amount(r) for r in detail)
            national_amount=sum(amount(r) for r in national)
            output.append({"year":year,"code":code,"national_suppliers_sum_across_rental":sum(int(r["Tot_Suplrs"]) for r in national),
               "national_beneficiaries_sum_across_rental":sum(int(r["Tot_Suplr_Benes"]) for r in national),
               "national_claims":sum(int(r["Tot_Suplr_Clms"]) for r in national),
               "national_services":str(national_units),"detail_service_coverage_pct":pct(detail_units,national_units),
               "national_amounts_usd_reconstructed":{m:rounded(sum(amount(r,m) for r in national)) for m in MEASURES},
               "detail_payment_coverage_pct":pct(detail_amount,national_amount),
               "national_less_detail_payment_usd":rounded(national_amount-detail_amount),
               "note":"National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them."})
    save(BASE/"national_reconciliation.json",output)

def fetch():
    (BASE/"snapshots").mkdir(exist_ok=True)
    manifest = {"started_at": now(), "source": "CMS public API", "cohorts": [], "dictionaries": [], "errors": []}
    for year,uuid in DATASETS.items():
        d,rec=request(API+uuid+"/dictionary")
        path=BASE/"snapshots"/f"dictionary_{year}.json";save(path,d)
        rec.update({"year":year,"snapshot":str(path.relative_to(BASE)),"snapshot_sha256":sha(path.read_bytes())})
        manifest["dictionaries"].append(rec)
    jobs=[(y,c) for y in DATASETS for c in CODES]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures={pool.submit(fetch_cohort,y,c):(y,c) for y,c in jobs}
        for f in concurrent.futures.as_completed(futures):
            y,c=futures[f]
            try:
                cohort=f.result();manifest["cohorts"].append(cohort)
                print(f"Fetched {y} {c}: {cohort['rows']} rows; verified count and terminal empty page",flush=True)
            except Exception as exc:
                manifest["errors"].append({"year":y,"code":c,"error":str(exc)})
            save(BASE/"acquisition_manifest.json",manifest)
    manifest["cohorts"].sort(key=lambda x:(x["year"],x["code"]))
    manifest["completed_at"]=now();save(BASE/"acquisition_manifest.json",manifest)
    if manifest["errors"]:raise RuntimeError("Acquisition incomplete; see manifest")

def validate_catalog_periods():
    """The series UUID may point to a newer year later: fail instead of relabeling it."""
    catalog,rec=request("https://data.cms.gov/data.json")
    verified=[]
    for table,mapping in (("Supplier and Service",DATASETS),("Geography and Service",GEO_DATASETS)):
        for year,uuid in mapping.items():
            matches=[]
            for row in catalog["dataset"]:
                temporal=row.get("temporal",[])
                if not isinstance(temporal,list):continue
                urls=[row.get("identifier","")]+[d.get("accessURL","") or "" for d in row.get("distribution",[])]
                if table in row.get("title","") and any(uuid in u for u in urls):
                    matches.append(row)
            if not any(any(t.get("startDate","").startswith(str(year)) and t.get("endDate","").startswith(str(year)) for t in row.get("temporal",[]) if isinstance(t,dict)) for row in matches):
                raise ValueError(f"Dataset period drift: {table} {year} {uuid}. Review current catalog before fetching.")
            verified.append({"table":table,"year":year,"uuid":uuid,"matching_titles":[r["title"] for r in matches]})
    save(BASE/"period_validation.json",{"catalog_request":rec,"verified":verified})

def verify_local():
    manifest=json.loads((BASE/"acquisition_manifest.json").read_text())
    checks=[]
    assert not manifest["errors"]
    assert {(r["year"],r["code"]) for r in manifest["cohorts"]}=={(y,c) for y in DATASETS for c in CODES}
    for rec in manifest["cohorts"]:
        path=BASE/rec["snapshot"];rows=json.loads(path.read_text())
        assert sha(path.read_bytes())==rec["snapshot_sha256"]
        assert sha(canonical(rows))==rec["canonical_rows_sha256"]
        assert len(rows)==rec["stats"]["found_rows"]==rec["unique_exact_keys"]
        assert len({key(r) for r in rows})==len(rows)
        assert all(set(r)==set(FIELDS) for r in rows)
        assert all(D(r["Tot_Suplr_Clms"])>=11 for r in rows)
        assert rec["pages"][-1]["returned_rows"]==0
        assert rec["pages"][-1]["offset"]==len(rows)
        checks.append({"year":rec["year"],"code":rec["code"],"rows":len(rows),"snapshot_hash":"pass","canonical_hash":"pass","stats_count":"pass","exact_key_uniqueness":"pass","selected_non_contact_schema":"pass","minimum_11_claims":"pass","terminal_page":"pass"})
    national=BASE/"national_acquisition_manifest.json"
    if national.exists():
        n=json.loads(national.read_text());assert sha((BASE/n["snapshot"]).read_bytes())==n["snapshot_sha256"]
        recon=json.loads((BASE/"national_reconciliation.json").read_text())
        assert len(recon)==9 and all(D(r["detail_payment_coverage_pct"])<=100 for r in recon)
    save(BASE/"validation.json",{"checked_at":now(),"status":"pass","cohorts":checks,"total_supplier_rows":sum(r["rows"] for r in checks),"national_snapshot_hash":"pass" if national.exists() else "not_acquired","limitations":"Validates provenance and calculations, not clinical necessity, ownership, fraud, released cash, or suppressed individual records."})

if __name__ == "__main__":
    p=argparse.ArgumentParser();p.add_argument("--fetch",action="store_true");p.add_argument("--fetch-national",action="store_true");args=p.parse_args()
    if args.fetch or args.fetch_national:validate_catalog_periods()
    if args.fetch:fetch()
    if args.fetch_national:fetch_national()
    analyze()
    reconcile_national()
    verify_local()
