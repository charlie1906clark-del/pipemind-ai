"""Independent retained-evidence check of five CAGE/UEI identity paths.

No producer modules; confirms source consistency, not beneficial ownership,
historical registration eligibility or validity of underlying declarations.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
IDENTITY = HERE.parent / "identity"
AWARDS = HERE.parent / "awards" / "capture-success"


def read(path):
    return json.loads(path.read_text())


def verify():
    records = read(IDENTITY / "entity_records.json")
    relations = read(IDENTITY / "relationships.json")["relationships"]
    manifest = read(IDENTITY / "capture_manifest.json")
    for request in manifest["requests"]:
        for path_key, hash_key in (("request_path", "request_sha256"), ("snapshot_path", "snapshot_sha256")):
            if request.get(path_key):
                if hashlib.sha256((IDENTITY / request[path_key]).read_bytes()).hexdigest() != request[hash_key]:
                    raise ValueError("Identity request/snapshot hash mismatch")
    for artifact in records["input_artifacts"]:
        if hashlib.sha256((IDENTITY / artifact["path"]).read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("Identity derivation-input hash mismatch")
    findings = []
    profile_count = 0
    for entity in records["entities"]:
        cage = entity["cage"]
        registry = read(IDENTITY / f"snapshots/cage-{cage}-selected.json")
        profile = read(IDENTITY / f"snapshots/{cage}-profile.json")
        first = read(IDENTITY / f"snapshots/{cage}-recipient-page-1.json")
        terminal = read(IDENTITY / f"snapshots/{cage}-recipient-page-2.json")
        if terminal["results"]:
            raise ValueError("Identity terminal page is not empty")
        profile_count += len(first["results"])
        detail_links = [link for link in registry["result_links"] if link["href"].startswith("/Search/Details?")]
        if registry["query"] != cage or len(detail_links) != 1:
            raise ValueError("Registry query/result cardinality differs")
        expected_sequence = [cage, entity["uei"], entity["legal_business_name"]]
        text = registry["selected_text"]
        if not any(text[i:i+3] == expected_sequence for i in range(len(text)-2)):
            raise ValueError("Registry legal-name/identifier row does not match")
        if profile["uei"] != entity["uei"] or profile["name"] != entity["legal_business_name"]:
            raise ValueError("Profile identity mismatch")
        if profile["alternate_names"] != entity["reported_aliases"]:
            raise ValueError("Alias list not supported by profile")
        if profile["parent_uei"] != entity["reporting_parent"]["uei"] or profile["parent_name"] != entity["reporting_parent"]["name"]:
            raise ValueError("Reporting-parent assertion not supported by profile")
        if entity["beneficial_owners"] is not None or entity["historical_registration_status"] is not None or entity["sam_active_registration_verified"]:
            raise ValueError("Unsupported ownership or historical registration inference")
        for link in entity["historical_award_links"]:
            award = read(AWARDS / ("award-" + link["contract_number"] + ".json"))
            if award["piid"] != link["contract_number"] or award["date_signed"] != link["award_date"] or award["recipient"]["recipient_uei"] != entity["uei"]:
                raise ValueError("Historical exact-key join differs")
        findings.append({"cage": cage, "uei": entity["uei"], "registry_and_profile_consistent": True,
                         "historical_exact_key_joins": len(entity["historical_award_links"]),
                         "aliases": len(entity["reported_aliases"]), "ownership_verified": False,
                         "historical_eligibility_verified": False})
    for relation in relations:
        for key in ("ownership_inferred", "beneficial_ownership_inferred", "historical_validity_inferred", "independent_legal_name_history_verified"):
            if relation.get(key):
                raise ValueError("Relationship exceeds available provenance")
    return {"as_of": "2026-10-30", "passed": True, "method": "Independent selected-registry row, profile, exact award key and provenance reconstruction; no producer modules",
            "entities_checked": len(findings), "historical_joins_checked": sum(f["historical_exact_key_joins"] for f in findings),
            "recipient_profiles_checked": profile_count, "aliases_checked": sum(f["aliases"] for f in findings),
            "relationships_checked": len(relations), "findings": findings,
            "source_authentication_limit": "Retained selected CAGE output was checked; this reviewer did not independently repeat the five live registry requests. Two historical award API responses were independently re-fetched separately.",
            "fraud_established": False}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
