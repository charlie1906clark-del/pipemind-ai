#!/usr/bin/env python3
"""Bounded USAspending name-variation check. No fraud score or automatic merge.

Default execution validates and analyses saved, selected public responses.
--acquire NEW_DIRECTORY explicitly performs bounded public API calls.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.request import Request, urlopen

BASE = "https://api.usaspending.gov/api/v2/"
TIMEOUT = 20
MAX_BYTES = 4 * 1024 * 1024
MAX_PAGES = 20
VARIANTS = {"amazon": "Amazon", "amazon-dot": "Amazon."}
FIELDS = ["Award ID", "generated_internal_id", "Recipient Name", "Recipient UEI",
          "recipient_id", "Awarding Agency", "Awarding Agency Code",
          "Awarding Sub Agency", "Start Date", "End Date", "Award Amount",
          "Place of Performance State Code", "PSC"]


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded(value))


def normalize_name(value):
    """Comparison key only: NFKC, case folding, punctuation-as-space, whitespace.

    Legal suffixes, DBA text and subsidiary words are deliberately retained.
    No ASCII transliteration or Unicode confusable substitution is performed.
    """
    if not isinstance(value, str):
        return ""
    text = unicodedata.normalize("NFKC", value).casefold()
    return " ".join("".join(c if c.isalnum() or c.isspace() else " " for c in text).split())


def scripts(value):
    found = set()
    for c in value or "":
        if not c.isalpha():
            continue
        name = unicodedata.name(c, "UNKNOWN")
        for script in ["LATIN", "CYRILLIC", "GREEK", "HEBREW", "ARABIC"]:
            if script in name:
                found.add(script)
                break
    return sorted(found)


def valid_uei(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[A-Z0-9]{12}", value))


def group_records(records):
    """Describe identifier/name relationships, not entity identity or culpability."""
    grouped = defaultdict(list)
    for index, record in enumerate(records):
        key = normalize_name(record.get("name"))
        if not key:
            key = f"__missing_name_{record.get('id', index)}"
        grouped[key].append(record)
    result = []
    for key, rows in sorted(grouped.items()):
        raw_names = sorted({r["name"] for r in rows if isinstance(r.get("name"), str)})
        ueis = sorted({r["uei"] for r in rows if valid_uei(r.get("uei"))})
        missing = sum(not valid_uei(r.get("uei")) for r in rows)
        observations = []
        if len(raw_names) > 1:
            observations.append("name_format_variation")
        if len(ueis) > 1:
            observations.append("shared_comparison_key_distinct_ueis")
        if missing:
            observations.append("identifier_unresolved_for_some_records")
        levels = defaultdict(set)
        names_by_uei = defaultdict(set)
        for row in rows:
            if valid_uei(row.get("uei")):
                levels[row["uei"]].add(row.get("recipient_level"))
                names_by_uei[row["uei"]].add(row.get("name"))
        if any(len(names) > 1 for names in names_by_uei.values()):
            observations.append("same_uei_name_variation")
        profile_duplicates = sum({"P", "C"}.issubset(v) for v in levels.values())
        if profile_duplicates:
            observations.append("same_uei_parent_and_child_profile_levels")
        result.append({"comparison_key": key, "record_count": len(rows),
                       "distinct_raw_names": raw_names, "distinct_valid_ueis": ueis,
                       "missing_or_invalid_uei_rows": missing,
                       "profile_level_pair_count": profile_duplicates,
                       "observations": observations,
                       "automatic_entity_merge": False, "fraud_determination": False})
    return result


def filters(keyword):
    return {"award_type_codes": ["A", "B", "C", "D"],
            "recipient_search_text": [keyword],
            "time_period": [{"start_date": "2025-10-01", "end_date": "2026-09-30"}]}


def select_profile(raw):
    allowed = ["name", "alternate_names", "duns", "uei", "recipient_id",
               "recipient_level", "parent_id", "parent_name", "parent_duns",
               "parent_uei", "business_types"]
    result = {key: raw.get(key) for key in allowed}
    location = raw.get("location") or {}
    result["location"] = {key: location.get(key) for key in ["state_code", "country_code"]}
    # Nested parents are omitted; only documented top-level parent fields survive.
    return result


def acquire(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=False)
    manifest = {"started_at": datetime.now(timezone.utc).isoformat(),
                "scope": "Two literal recipient keywords, contract recipients and FY2026 prime contracts; no national entity census",
                "hash_scope": "Wire hash covers actual HTTP response; retained snapshot hash covers selected/normalized JSON, not original wire bytes",
                "original_response_archived": False, "requests": [], "queries": {},
                "timeout_seconds": TIMEOUT, "max_response_bytes": MAX_BYTES,
                "max_pages_per_query": MAX_PAGES, "automatic_retries": 0,
                "success": False}

    def request(label, endpoint, payload=None, select=None):
        url = endpoint if endpoint.startswith("https://") else BASE + endpoint
        body = encoded(payload) if payload is not None else None
        meta = {"label": label, "url": url, "method": "POST" if body else "GET",
                "retrieved_at": datetime.now(timezone.utc).isoformat()}
        if body:
            request_path = "requests/" + label + ".json"
            (folder / "requests").mkdir(exist_ok=True)
            (folder / request_path).write_bytes(body)
            meta.update(request_path=request_path, request_sha256=digest(body))
        req = Request(url, data=body, headers={"Content-Type": "application/json",
                      "User-Agent": "PipeMind-Public-Identity-Research/1.0"})
        with urlopen(req, timeout=TIMEOUT) as response:
            wire = response.read(MAX_BYTES + 1)
            meta.update(http_status=response.status, response_date=response.headers.get("Date"))
        if len(wire) > MAX_BYTES:
            raise ValueError("Response exceeded bounded size")
        raw = json.loads(wire)
        selected = select(raw) if select else raw
        path = "snapshots/" + label + ".json"
        write(folder / path, selected)
        meta.update(wire_response_sha256=digest(wire), wire_bytes=len(wire),
                    snapshot_path=path, snapshot_sha256=digest((folder / path).read_bytes()),
                    selection="field-selected" if select else "JSON reformatted only")
        manifest["requests"].append(meta)
        write(folder / "manifest.json", manifest)
        return selected

    try:
        for slug, keyword in VARIANTS.items():
            recipient_rows = []
            recipient_total = None
            for page in range(1, MAX_PAGES + 1):
                payload = {"keyword": keyword, "award_type": "contracts", "sort": "name",
                           "order": "asc", "limit": 1000, "page": page}
                response = request(slug + f"-recipients-{page}", "recipient/", payload)
                rows, meta = response["results"], response["page_metadata"]
                if meta["page"] != page:
                    raise ValueError("Incorrect recipient page")
                if recipient_total is None:
                    recipient_total = meta["total"]
                elif recipient_total != meta["total"]:
                    raise ValueError("Recipient count drift")
                recipient_rows.extend(rows)
                if not rows:
                    break
            else:
                raise ValueError("Recipient page cap reached; extraction incomplete")
            if len(recipient_rows) != recipient_total or len({r["id"] for r in recipient_rows}) != len(recipient_rows):
                raise ValueError("Recipient count/unique profile mismatch")
            before = request(slug + "-count-before", "search/spending_by_award_count/",
                             {"filters": filters(keyword), "subawards": False})["results"]["contracts"]
            award_rows = []
            for page in range(1, MAX_PAGES + 1):
                payload = {"filters": filters(keyword), "fields": FIELDS, "limit": 100,
                           "page": page, "sort": "Award ID", "order": "asc", "subawards": False}
                response = request(slug + f"-awards-{page}", "search/spending_by_award/", payload)
                rows = response["results"]
                if response["page_metadata"]["page"] != page:
                    raise ValueError("Incorrect award page")
                award_rows.extend(rows)
                if not rows:
                    break
            else:
                raise ValueError("Award page cap reached; extraction incomplete")
            after = request(slug + "-count-after", "search/spending_by_award_count/",
                            {"filters": filters(keyword), "subawards": False})["results"]["contracts"]
            if before != after or before != len(award_rows):
                raise ValueError("Award count changed or extraction incomplete")
            if len({r["generated_internal_id"] for r in award_rows}) != len(award_rows):
                raise ValueError("Duplicate award ID across pages")
            manifest["queries"][slug] = {"keyword": keyword, "recipient_profiles": len(recipient_rows),
                "award_rows": len(award_rows), "before_count": before, "after_count": after,
                "recipient_terminal_empty_page": True, "award_terminal_empty_page": True,
                "unique_awards": True, "complete_for_bounded_query": True}
            write(folder / (slug + "-recipients.json"), recipient_rows)
            write(folder / (slug + "-awards.json"), award_rows)
        recipients = json.loads((folder / "amazon-recipients.json").read_text())
        profiles = []
        for index, row in enumerate(recipients):
            profiles.append(request(f"profile-{index+1:02d}", "recipient/" + row["id"] + "/",
                                    select=select_profile))
        write(folder / "profiles.json", profiles)
        manifest["success"] = True
    finally:
        manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
        write(folder / "manifest.json", manifest)
    return manifest


def validate_capture(folder):
    folder = Path(folder)
    manifest = json.loads((folder / "manifest.json").read_text())
    if not manifest["success"]:
        raise ValueError("Capture not complete")
    for meta in manifest["requests"]:
        for key in ["snapshot", "request"]:
            if key + "_path" in meta:
                path = (folder / meta[key + "_path"]).resolve()
                if not path.is_relative_to(folder.resolve()):
                    raise ValueError("Capture path escapes folder")
                if digest(path.read_bytes()) != meta[key + "_sha256"]:
                    raise ValueError("Capture digest mismatch")
    for slug, query in manifest["queries"].items():
        awards = []
        recipient_rows = []
        award_pages = []
        recipient_pages = []
        counts = {}
        for meta in manifest["requests"]:
            data = json.loads((folder / meta["snapshot_path"]).read_text())
            if meta["label"].startswith(slug + "-awards-"):
                awards.extend(data["results"])
                award_pages.append(data)
            if meta["label"].startswith(slug + "-recipients-"):
                recipient_rows.extend(data["results"])
                recipient_pages.append(data)
            for when in ["before", "after"]:
                if meta["label"] == slug + "-count-" + when:
                    counts[when] = data["results"]["contracts"]
        for pages in [award_pages, recipient_pages]:
            if not pages or pages[-1]["results"]:
                raise ValueError("Missing terminal empty page")
            if [p["page_metadata"]["page"] for p in pages] != list(range(1, len(pages) + 1)):
                raise ValueError("Noncontiguous capture pages")
        if set(counts) != {"before", "after"} or counts["before"] != counts["after"]:
            raise ValueError("Count snapshot missing or drifted")
        if counts["before"] != query["before_count"] or counts["after"] != query["after_count"]:
            raise ValueError("Count snapshot differs from manifest")
        if any(page["page_metadata"]["total"] != len(recipient_rows) for page in recipient_pages):
            raise ValueError("Recipient total differs from captured profiles")
        if awards != json.loads((folder / (slug + "-awards.json")).read_text()):
            raise ValueError("Derived award file differs from snapshots")
        if recipient_rows != json.loads((folder / (slug + "-recipients.json")).read_text()):
            raise ValueError("Derived recipient file differs from snapshots")
        if len(awards) != query["before_count"] or len(awards) != query["after_count"]:
            raise ValueError("Count mismatch")
        if len({r["generated_internal_id"] for r in awards}) != len(awards):
            raise ValueError("Duplicate award identity")
        if len({r["id"] for r in recipient_rows}) != len(recipient_rows):
            raise ValueError("Duplicate recipient profile")
    profile_rows = [json.loads((folder / meta["snapshot_path"]).read_text())
                    for meta in manifest["requests"] if meta["label"].startswith("profile-")]
    if profile_rows != json.loads((folder / "profiles.json").read_text()):
        raise ValueError("Derived profile file differs from snapshots")
    return manifest


def analyse(folder):
    folder = Path(folder)
    manifest = validate_capture(folder)
    recipients = json.loads((folder / "amazon-recipients.json").read_text())
    profiles = json.loads((folder / "profiles.json").read_text())
    awards = {slug: json.loads((folder / (slug + "-awards.json")).read_text()) for slug in VARIANTS}
    award_records = [{"id": r["generated_internal_id"], "name": r.get("Recipient Name"),
                      "uei": r.get("Recipient UEI"), "recipient_level": "award"}
                     for r in awards["amazon"]]
    groups = group_records(recipients)
    award_groups = group_records(award_records)
    same_uei = defaultdict(set)
    for row in recipients + award_records:
        if valid_uei(row.get("uei")):
            same_uei[row["uei"]].add(row["name"])
    ids = {slug: {row["generated_internal_id"] for row in rows} for slug, rows in awards.items()}
    return {"as_of": manifest["finished_at"][:10], "query_scope": manifest["scope"],
            "recipient_profile_rows": len(recipients),
            "distinct_valid_recipient_ueis": len({r["uei"] for r in recipients if valid_uei(r.get("uei"))}),
            "recipient_levels": dict(Counter(r["recipient_level"] for r in recipients)),
            "award_rows": len(awards["amazon"]),
            "award_raw_name_count": len({r["Recipient Name"] for r in awards["amazon"]}),
            "award_distinct_uei_count": len({r["Recipient UEI"] for r in awards["amazon"] if valid_uei(r.get("Recipient UEI"))}),
            "award_missing_uei_rows": sum(not valid_uei(r.get("Recipient UEI")) for r in awards["amazon"]),
            "keyword_variants_return_identical_award_ids": ids["amazon"] == ids["amazon-dot"],
            "keyword_variant_symmetric_difference_count": len(ids["amazon"] ^ ids["amazon-dot"]),
            "recipient_groups": groups, "award_groups": award_groups,
            "same_uei_multiple_raw_names_count": sum(len(names) > 1 for names in same_uei.values()),
            "profile_parent_uei_present_rows": sum(bool(p.get("parent_uei")) for p in profiles),
            "scope_limitations": [
                "Comparison keys do not merge legal entities, beneficial owners or liabilities.",
                "Recipient P/C/R profile levels are not separate companies; amounts must not be summed across them.",
                "Recipient amounts are trailing-12-month transaction aggregates; award amounts are cumulative award measures, not FY2026 cash or fraud loss.",
                "Award date filter uses documented default award-search timing; this is not a list of every FY2026 transaction.",
                "Keyword matching is an index search, not an exact legal-name search; these queries exclude other sectors and aliases without this token.",
                "Parent links are source-reported profile relationships, not verified ultimate beneficial ownership.",
                "No name variation establishes a fake company, false claim, improper payment or reward eligibility."],
            "new_fraud_established": False, "fraud_scoring_performed": False, "money_summed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acquire", type=Path)
    parser.add_argument("--capture", type=Path, default=Path(__file__).parent / "capture-2026-10-30")
    args = parser.parse_args()
    folder = args.acquire or args.capture
    if args.acquire:
        acquire(folder)
    result = analyse(folder)
    write(folder.parent / "analysis.json", result)
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ["recipient_groups", "award_groups", "scope_limitations"]}, indent=2))


if __name__ == "__main__":
    main()
