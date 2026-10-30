#!/usr/bin/env python3
"""Independent offline review of the saved name pilot, without its audit module."""
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import unicodedata

HERE = Path(__file__).resolve().parent
NAMES = HERE.parent / "names"
CAPTURE = NAMES / "capture-2026-10-30"


def read(path):
    return json.loads(path.read_text())


def fingerprint(path):
    return sha256(path.read_bytes()).hexdigest()


def normalize(text):
    value = unicodedata.normalize("NFKC", text).casefold()
    return " ".join("".join(char if char.isalnum() or char.isspace() else " "
                            for char in value).split())


def verify():
    manifest = read(CAPTURE / "manifest.json")
    assert manifest["success"] is True
    pins = {}
    for meta in manifest["requests"]:
        assert meta["http_status"] == 200
        for label in ["request", "snapshot"]:
            if label + "_path" not in meta:
                continue
            path = CAPTURE / meta[label + "_path"]
            assert fingerprint(path) == meta[label + "_sha256"]
            pins[str(path.relative_to(HERE.parent))] = fingerprint(path)
    requests = {row["label"]: row for row in manifest["requests"]}
    cohorts = {}
    for slug in ["amazon", "amazon-dot"]:
        awards, recipients = [], []
        for family, output in [("awards", awards), ("recipients", recipients)]:
            pages = [row for row in manifest["requests"]
                     if row["label"].startswith(slug + "-" + family + "-")]
            pages.sort(key=lambda row: int(row["label"].rsplit("-", 1)[1]))
            assert pages
            for page_number, record in enumerate(pages, 1):
                payload = read(CAPTURE / record["snapshot_path"])
                assert payload["page_metadata"]["page"] == page_number
                output.extend(payload["results"])
            assert read(CAPTURE / pages[-1]["snapshot_path"])["results"] == []
            assert output == read(CAPTURE / (slug + "-" + family + ".json"))
        before = read(CAPTURE / requests[slug + "-count-before"]["snapshot_path"])["results"]["contracts"]
        after = read(CAPTURE / requests[slug + "-count-after"]["snapshot_path"])["results"]["contracts"]
        assert before == after == len(awards)
        assert len({row["generated_internal_id"] for row in awards}) == len(awards)
        assert len({row["id"] for row in recipients}) == len(recipients)
        first = read(CAPTURE / requests[slug + "-recipients-1"]["snapshot_path"])
        assert len(recipients) == first["page_metadata"]["total"]
        cohorts[slug] = (awards, recipients)
    profiles = [read(CAPTURE / row["snapshot_path"]) for row in manifest["requests"]
                if row["label"].startswith("profile-")]
    assert profiles == read(CAPTURE / "profiles.json")
    base_awards, base_recipients = cohorts["amazon"]
    dot_awards, dot_recipients = cohorts["amazon-dot"]
    base_ids = {row["generated_internal_id"] for row in base_awards}
    dot_ids = {row["generated_internal_id"] for row in dot_awards}
    levels = defaultdict(set)
    same_id_names = defaultdict(set)
    groups = defaultdict(list)
    for row in base_recipients:
        assert re.fullmatch(r"[A-Z0-9]{12}", row["uei"])
        levels[row["uei"]].add(row["recipient_level"])
        groups[normalize(row["name"])].append(row)
        same_id_names[row["uei"]].add(row["name"])
    for row in base_awards:
        assert re.fullmatch(r"[A-Z0-9]{12}", row["Recipient UEI"])
        same_id_names[row["Recipient UEI"]].add(row["Recipient Name"])
    children = [row for row in profiles if row["recipient_level"] == "C"]
    parents = [row for row in profiles if row["recipient_level"] == "P"]
    summary = {
        "amazon_awards": len(base_awards), "amazon_dot_awards": len(dot_awards),
        "award_intersection": len(base_ids & dot_ids),
        "award_only_amazon": len(base_ids - dot_ids), "award_only_amazon_dot": len(dot_ids - base_ids),
        "amazon_recipient_profiles": len(base_recipients),
        "amazon_dot_recipient_profiles": len(dot_recipients),
        "distinct_recipient_ueis": len(levels),
        "profile_level_counts": dict(Counter(row["recipient_level"] for row in base_recipients)),
        "same_uei_parent_child_pairs": sum(value == {"P", "C"} for value in levels.values()),
        "normalized_name_groups": len(groups),
        "distinct_uei_name_collisions": sum(len({row["uei"] for row in values}) > 1 for values in groups.values()),
        "same_uei_multiple_names": sum(len(value) > 1 for value in same_id_names.values()),
        "child_profile_count": len(children),
        "distinct_reported_parent_ueis_among_child_profiles": len({row["parent_uei"] for row in children}),
        "parent_profiles_reporting_self_parent": sum(row["uei"] == row["parent_uei"] for row in parents),
        "money_summed": False, "fraud_determination": False,
    }
    reported = read(NAMES / "analysis.json")
    assert reported["award_rows"] == summary["amazon_awards"]
    assert reported["recipient_profile_rows"] == summary["amazon_recipient_profiles"]
    assert reported["distinct_valid_recipient_ueis"] == summary["distinct_recipient_ueis"]
    assert reported["recipient_levels"] == summary["profile_level_counts"]
    assert reported["keyword_variant_symmetric_difference_count"] == len(base_ids ^ dot_ids)
    assert reported["same_uei_multiple_raw_names_count"] == summary["same_uei_multiple_names"]
    for group in reported["recipient_groups"]:
        source = groups[group["comparison_key"]]
        assert group["record_count"] == len(source)
        assert group["distinct_raw_names"] == sorted({row["name"] for row in source})
        assert group["distinct_valid_ueis"] == sorted({row["uei"] for row in source})
        assert group["automatic_entity_merge"] is False
        assert group["fraud_determination"] is False
    assert reported["money_summed"] is False
    assert reported["fraud_scoring_performed"] is False
    for path in [CAPTURE / "manifest.json", NAMES / "analysis.json", NAMES / "audit_names.py"]:
        pins[str(path.relative_to(HERE.parent))] = fingerprint(path)
    return {"reviewed_at": "2026-10-30", "passed": True,
            "method": "Independent reconstruction from saved responses; audit module not imported",
            "request_count": len(manifest["requests"]), "summary": summary,
            "input_sha256": dict(sorted(pins.items())),
            "limits": "Verifies captured-query consistency and calculations, not legal identity, beneficial ownership, fraud, cash loss or national coverage."}


if __name__ == "__main__":
    result = verify()
    (HERE / "name_data_review.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "input_sha256"}, indent=2))
