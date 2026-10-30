#!/usr/bin/env python3
"""Offline contract checks for model handoffs; no model, network or publishing calls.

Validation checks declarations and evidence structure. It cannot authenticate a
model identity, certify a source's truth, detect all private text, or decide fraud.
"""
import argparse
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

SHA = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
MEASURES = {
    "submitted_claims", "contract_ceiling", "obligations", "outlays", "invoiced",
    "disbursed_cash", "withheld_escrow", "recovered_cash", "unit_price",
    "reference_unit_price", "estimated_exposure", "price_difference",
}
DECISIONS = {"supported_as_worded", "supported_with_narrowing", "unsupported",
             "contradicted", "needs_more_evidence"}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def iso_date(value):
    require(isinstance(value, str), "Date must be an ISO string")
    if len(value) == 10:
        date.fromisoformat(value)
    else:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        require(parsed.tzinfo is not None, "Datetime requires timezone")


def refs(value, sources):
    require(isinstance(value, list) and value, "Evidence references cannot be empty")
    require(all(isinstance(x, str) and x in sources for x in value), "Missing source reference")


def verify_inputs(task, repo_root):
    """Check immutable baseline blobs, not mutable working files; no remote fetch."""
    require(COMMIT.fullmatch(task["input_commit"]), "Invalid input commit")
    for item in task["input_files"]:
        path = Path(item["path"])
        require(not path.is_absolute() and ".." not in path.parts, "Input path escapes repository")
        require(SHA.fullmatch(item["sha256"]), "Invalid input digest")
        blob = subprocess.check_output([
            "git", "-C", str(repo_root), "show", task["input_commit"] + ":" + path.as_posix()
        ], stderr=subprocess.PIPE)
        require(hashlib.sha256(blob).hexdigest() == item["sha256"], "Pinned input digest mismatch")
    return len(task["input_files"])


def validate(task, result, review=None):
    require(task.get("schema_version") == "1.0" and result.get("schema_version") == "1.0",
            "Unsupported contract version")
    require(result.get("task_id") == task["task_id"], "Task ID mismatch")
    require(result.get("input_commit") == task["input_commit"], "Input commit mismatch")
    require(COMMIT.fullmatch(result["input_commit"]), "Invalid input commit")
    require(result.get("task_spec_sha256") == digest(task), "Task specification digest mismatch")
    require(result.get("visibility") == "public", "This handoff accepts public output only")
    require(result.get("status") == "submitted", "A worker cannot accept its own result")
    require("review_status" not in result and "review_decision" not in result,
            "Review belongs in a separate independent receipt")
    require(result.get("no_new_fraud_determination") is True, "Research output cannot declare a new fraud verdict")
    require(result.get("sensitive_material_included") is False, "Sensitive material cannot enter public output")
    worker = result["worker"]
    require(worker.get("provider") == task["assigned_provider"], "Unexpected worker provider")
    for field in ["agent_id", "model", "session_id"]:
        require(nonempty(worker.get(field)), "Worker identity fields are required")
    require(worker.get("identity_basis") in {"self_reported", "coordinator_verified_receipt"},
            "Worker identity basis must be explicit")
    require(result.get("execution_mode") in {"manual_repo_handoff", "authorized_model_api"},
            "Unknown execution mode")
    if result["execution_mode"] == "authorized_model_api":
        require(nonempty(result.get("provider_response_id")), "API result needs a response receipt ID")
    iso_date(result["created_at"])
    require(nonempty(result.get("scope")) and nonempty(result.get("coverage_limit")),
            "Bounded scope and coverage limit required")
    require(isinstance(result.get("limitations"), list) and result["limitations"], "Limitations required")

    sources = {}
    for source in result["sources"]:
        sid = source["source_id"]
        require(nonempty(sid) and sid not in sources, "Duplicate or empty source ID")
        url = urlsplit(source["url"])
        require(url.scheme in {"http", "https"} and bool(url.hostname) and not url.username and not url.password,
                "Source needs an HTTP(S) URL without credentials")
        for field in ["title", "publisher", "source_kind"]:
            require(nonempty(source.get(field)), "Source description incomplete")
        iso_date(source["accessed_at"])
        if source.get("publication_date") is not None:
            iso_date(source["publication_date"])
        require(source.get("retrieval_status") in {"read", "unavailable"}, "Source retrieval status required")
        if source.get("snapshot_sha256") is not None:
            require(SHA.fullmatch(source["snapshot_sha256"]) and nonempty(source.get("hash_scope")),
                    "Snapshot hash requires explicit byte scope")
        sources[sid] = source
    require(sources, "At least one source or documented access attempt required")

    claims = set()
    for claim in result["claims"]:
        cid = claim["claim_id"]
        require(nonempty(cid) and cid not in claims, "Duplicate or empty claim ID")
        claims.add(cid)
        require(nonempty(claim.get("statement")), "Claim statement required")
        require(claim.get("evidence_type") in {
            "reported_fact", "derived_observation", "hypothesis", "null_result",
            "published_allegation", "published_adjudication"
        }, "Unknown evidence type")
        require(claim.get("subject_scope") in {"aggregate", "published_case", "named_public_business", "anonymous_candidate"},
                "Subject scope required")
        require(isinstance(claim.get("adverse_inference"), bool), "Adverse-inference declaration required")
        novelty = claim["novelty"]
        require(novelty.get("status") in {"known_public_case", "not_found_in_bounded_search", "unassessed", "not_applicable"},
                "Unknown novelty status")
        require(nonempty(novelty.get("search_scope")) and nonempty(novelty.get("limitation")),
                "Novelty search scope and limitation required")
        if claim["adverse_inference"] and claim.get("named_subjects"):
            require(claim["subject_scope"] == "published_case" and novelty["status"] == "known_public_case",
                    "Novel named adverse inference cannot enter public output")
            require(nonempty(claim.get("legal_status")) and nonempty(claim.get("legal_status_date")),
                    "Published adverse claim needs dated legal status")
            iso_date(claim["legal_status_date"])
        require(isinstance(claim.get("source_refs"), list) and claim["source_refs"], "Claim needs source locators")
        for reference in claim["source_refs"]:
            require(reference.get("source_id") in sources and nonempty(reference.get("locator")),
                    "Claim needs a valid source and exact locator")
            require(sources[reference["source_id"]]["retrieval_status"] == "read" or claim["evidence_type"] == "null_result",
                    "An unread source cannot support a substantive observation")
        require(isinstance(claim.get("alternatives"), list) and claim["alternatives"], "Alternative explanations required")
        require(nonempty(claim.get("next_discriminating_evidence")), "Next evidence or closure reason required")
    require(claims, "Record at least a bounded null result")

    amount_ids = set()
    for amount in result.get("amounts", []):
        require(nonempty(amount.get("amount_id")) and amount["amount_id"] not in amount_ids, "Duplicate amount ID")
        amount_ids.add(amount["amount_id"])
        require(isinstance(amount.get("value"), str), "Money must use a decimal string")
        try:
            number = Decimal(amount["value"])
        except InvalidOperation as exc:
            raise ValueError("Invalid monetary number") from exc
        require(number.is_finite(), "Nonfinite monetary value")
        require(re.fullmatch(r"[A-Z]{3}", amount.get("currency", "")), "Currency required")
        measure = amount.get("measure")
        require(measure in MEASURES, "Unknown money measure")
        require(amount.get("source_measure") in MEASURES, "Source money measure required")
        if measure not in {"estimated_exposure", "price_difference"}:
            require(measure == amount["source_measure"], "Cannot relabel billing, obligation, escrow or cash")
        else:
            require(nonempty(amount.get("calculation")), "Derived amount needs its calculation")
        if measure == "price_difference":
            require(amount["source_measure"] in {"unit_price", "reference_unit_price"},
                    "A ceiling or obligation is not a comparable unit-price basis")
        for field in ["payer", "period", "basis", "qualifier"]:
            require(nonempty(amount.get(field)), "Money context incomplete")
        require(amount.get("is_recoverable_loss") is False, "No automatic recoverable-loss inference")
        refs(amount.get("source_ids"), sources)
        require(all(sources[s]["retrieval_status"] == "read" for s in amount["source_ids"]), "Money source unread")
        if measure in {"unit_price", "reference_unit_price", "price_difference"}:
            terms = amount.get("comparison_terms", {})
            for field in task.get("price_comparison_fields", ["unit_of_issue", "quantity", "item_identifier"]):
                require(nonempty(terms.get(field)), "Unit-price comparison terms incomplete: " + field)

    output = {"task_id": task["task_id"], "result_sha256": digest(result),
              "status": "awaiting_independent_review", "claims": len(claims),
              "sources": len(sources), "authentication_verified_by_validator": False,
              "fraud_or_reward_eligibility_decided": False}
    if review is not None:
        require(review.get("schema_version") == "1.0" and review.get("task_id") == task["task_id"], "Review task mismatch")
        require(review.get("result_sha256") == digest(result), "Review refers to different result bytes")
        reviewer = review["reviewer"]
        require(nonempty(reviewer.get("session_id")) and nonempty(reviewer.get("agent_id")), "Reviewer identity required")
        require(reviewer["session_id"] != worker["session_id"] and reviewer["agent_id"] != worker["agent_id"],
                "Self-review cannot accept a result")
        require(review.get("decision") in DECISIONS, "Invalid review decision")
        iso_date(review["reviewed_at"])
        require(set(review.get("checked_claim_ids", [])) == claims, "Reviewer must account for every claim")
        require(nonempty(review.get("reason")), "Independent review reason required")
        if review["decision"] == "supported_as_worded":
            require(review.get("material_checks_reproduced") is True, "Acceptance requires reproduced checks")
            output["status"] = "accepted_as_worded_by_declared_reviewer"
        else:
            output["status"] = "revision_or_more_evidence_required"
        output["review_sha256"] = digest(review)
    return output


def archive(result, output_directory):
    """Content-addressed write; existing bytes are never silently replaced."""
    folder = Path(output_directory)
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / (digest(result) + ".json")
    body = (canonical(result) + "\n").encode()
    try:
        with path.open("xb") as stream:
            stream.write(body)
    except FileExistsError:
        require(path.read_bytes() == body, "Immutable result file was changed")
    return str(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--review", type=Path)
    parser.add_argument("--verify-inputs", type=Path, metavar="REPOSITORY_ROOT")
    parser.add_argument("--archive", type=Path, metavar="OUTPUT_DIRECTORY")
    args = parser.parse_args()
    task = json.loads(args.task.read_text())
    result = json.loads(args.result.read_text())
    review = json.loads(args.review.read_text()) if args.review else None
    output = validate(task, result, review)
    if args.verify_inputs:
        output["pinned_input_files_verified"] = verify_inputs(task, args.verify_inputs)
    if args.archive:
        output["archived_result"] = archive(result, args.archive)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
