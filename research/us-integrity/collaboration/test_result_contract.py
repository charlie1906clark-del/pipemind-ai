"""Synthetic contract fixtures; these are not model responses or research evidence."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from validate_result import archive, digest, validate, verify_inputs

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.task = json.loads((HERE / "tasks/GROK-IDENTITY-001.json").read_text())
        self.result = {
            "schema_version": "1.0", "task_id": self.task["task_id"],
            "task_spec_sha256": digest(self.task), "input_commit": self.task["input_commit"],
            "created_at": "2026-10-30T12:00:00Z", "visibility": "public", "status": "submitted",
            "no_new_fraud_determination": True, "sensitive_material_included": False,
            "worker": {"provider": "xai", "agent_id": "fixture-worker", "model": "synthetic-test-only",
                       "session_id": "fixture-session-A", "identity_basis": "self_reported"},
            "execution_mode": "manual_repo_handoff", "scope": "Synthetic single query",
            "coverage_limit": "Test fixture, no actual records", "limitations": ["Synthetic, not evidence"],
            "sources": [{"source_id": "S1", "url": "https://example.gov/test", "title": "Fixture",
                         "publisher": "Test", "source_kind": "synthetic_fixture", "accessed_at": "2026-10-30",
                         "publication_date": None, "retrieval_status": "read"}],
            "claims": [{"claim_id": "C1", "statement": "Synthetic null observation",
                        "evidence_type": "null_result", "subject_scope": "aggregate", "adverse_inference": False,
                        "named_subjects": [], "novelty": {"status": "not_applicable", "search_scope": "Fixture",
                        "limitation": "No real search"}, "source_refs": [{"source_id": "S1", "locator": "test row"}],
                        "alternatives": ["Source unavailable"], "next_discriminating_evidence": "No action; synthetic test"}],
            "amounts": [],
        }

    def review(self):
        return {"schema_version": "1.0", "task_id": self.task["task_id"], "result_sha256": digest(self.result),
                "reviewer": {"agent_id": "fixture-reviewer", "session_id": "fixture-session-B"},
                "reviewed_at": "2026-10-30T12:30:00Z", "decision": "supported_as_worded",
                "checked_claim_ids": ["C1"], "material_checks_reproduced": True,
                "reason": "Synthetic contract test only"}

    def amount(self):
        return {"amount_id": "M1", "value": "100.00", "currency": "USD", "measure": "submitted_claims",
                "source_measure": "submitted_claims", "payer": "Test", "period": "2026", "basis": "Fixture",
                "qualifier": "synthetic", "is_recoverable_loss": False, "source_ids": ["S1"]}

    def test_valid_null_result_is_awaiting_review(self):
        self.assertEqual(validate(self.task, self.result)["status"], "awaiting_independent_review")

    def test_wrong_task_rejected(self):
        self.result["task_id"] = "OTHER"
        with self.assertRaisesRegex(ValueError, "Task ID mismatch"):
            validate(self.task, self.result)

    def test_stale_base_rejected(self):
        self.result["input_commit"] = "a" * 40
        with self.assertRaisesRegex(ValueError, "commit mismatch"):
            validate(self.task, self.result)

    def test_changed_task_contract_rejected(self):
        self.task["question"] = "Changed scope"
        with self.assertRaisesRegex(ValueError, "specification digest mismatch"):
            validate(self.task, self.result)

    def test_claim_without_locator_rejected(self):
        self.result["claims"][0]["source_refs"][0]["locator"] = ""
        with self.assertRaisesRegex(ValueError, "exact locator"):
            validate(self.task, self.result)

    def test_unread_source_cannot_support_substantive_claim(self):
        self.result["sources"][0]["retrieval_status"] = "unavailable"
        self.result["claims"][0]["evidence_type"] = "reported_fact"
        with self.assertRaisesRegex(ValueError, "unread source"):
            validate(self.task, self.result)

    def test_billed_amount_cannot_be_relabelled_cash(self):
        amount = self.amount(); amount["measure"] = "disbursed_cash"
        self.result["amounts"] = [amount]
        with self.assertRaisesRegex(ValueError, "Cannot relabel"):
            validate(self.task, self.result)

    def test_ceiling_cannot_be_basis_for_unit_difference(self):
        amount = self.amount(); amount.update(measure="price_difference", source_measure="contract_ceiling", calculation="ceiling / estimated units")
        self.result["amounts"] = [amount]
        with self.assertRaisesRegex(ValueError, "not a comparable unit-price"):
            validate(self.task, self.result)

    def test_unit_price_needs_comparison_terms(self):
        amount = self.amount(); amount.update(measure="unit_price", source_measure="unit_price")
        self.result["amounts"] = [amount]
        with self.assertRaisesRegex(ValueError, "comparison terms incomplete"):
            validate(self.task, self.result)

    def test_novel_named_adverse_inference_rejected(self):
        claim = self.result["claims"][0]
        claim.update(adverse_inference=True, named_subjects=["Synthetic Supplier"], subject_scope="named_public_business")
        claim["novelty"]["status"] = "not_found_in_bounded_search"
        with self.assertRaisesRegex(ValueError, "Novel named adverse"):
            validate(self.task, self.result)

    def test_worker_cannot_self_accept(self):
        self.result["status"] = "accepted"
        with self.assertRaisesRegex(ValueError, "cannot accept its own"):
            validate(self.task, self.result)

    def test_separate_receipt_cannot_hide_self_review(self):
        review = self.review(); review["reviewer"]["session_id"] = self.result["worker"]["session_id"]
        with self.assertRaisesRegex(ValueError, "Self-review"):
            validate(self.task, self.result, review)

    def test_review_of_different_result_rejected(self):
        review = self.review(); self.result["scope"] = "A changed scope"
        with self.assertRaisesRegex(ValueError, "different result bytes"):
            validate(self.task, self.result, review)

    def test_independent_review_must_reproduce_checks(self):
        review = self.review(); review["material_checks_reproduced"] = False
        with self.assertRaisesRegex(ValueError, "reproduced checks"):
            validate(self.task, self.result, review)

    def test_supported_review_and_narrowing_have_distinct_states(self):
        review = self.review()
        self.assertEqual(validate(self.task, self.result, review)["status"], "accepted_as_worded_by_declared_reviewer")
        review["decision"] = "supported_with_narrowing"
        self.assertEqual(validate(self.task, self.result, review)["status"], "revision_or_more_evidence_required")

    def test_content_addressed_archive_is_idempotent_and_detects_tamper(self):
        with tempfile.TemporaryDirectory() as folder:
            path = archive(self.result, folder)
            self.assertEqual(archive(self.result, folder), path)
            Path(path).write_text("changed")
            with self.assertRaisesRegex(ValueError, "Immutable result file was changed"):
                archive(self.result, folder)

    def test_pinned_repository_input_hashes(self):
        self.assertEqual(verify_inputs(self.task, REPO), len(self.task["input_files"]))
        broken = copy.deepcopy(self.task); broken["input_files"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "input digest mismatch"):
            verify_inputs(broken, REPO)


if __name__ == "__main__":
    unittest.main()
