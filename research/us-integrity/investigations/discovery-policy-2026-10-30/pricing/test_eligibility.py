"""Negative controls prevent ceilings, missing units and unmatched terms becoming claims."""
import copy
from pathlib import Path
import unittest
from eligibility import eligible_pair, pilot_result


def fixture():
    # Synthetic fixture only; no actual supplier, contract or price claim.
    return dict(nsn="SYNTHETIC", unit_of_issue="EA", pack_quantity=1,
                item_revision="A", condition="new", delivery_terms="FOB origin; 60 days",
                inspection_acceptance="destination", warranty_basis="same standard warranty",
                nonrecurring_cost_treatment="documented zero", currency="USD", quantity=100,
                unit_price=2.0, price_date="2026-01-01", source_sha256="synthetic-hash",
                source_page=1, unit_conversion_evidence="documented EA to EA",
                price_kind="verified_award_clin")


class PriceGateTests(unittest.TestCase):
    def test_ceiling_is_rejected_even_with_full_terms(self):
        left, right = fixture(), fixture()
        left["price_kind"] = "idv_ceiling"
        self.assertFalse(eligible_pair(left, right)["eligible"])

    def test_same_item_does_not_supply_missing_unit(self):
        left, right = fixture(), fixture()
        left["unit_of_issue"] = None
        self.assertFalse(eligible_pair(left, right)["eligible"])

    def test_nonfinite_amounts_cannot_pass(self):
        for invalid in (float("nan"), float("inf"), float("-inf")):
            left, right = fixture(), fixture()
            left["unit_price"] = invalid
            self.assertFalse(eligible_pair(left, right)["eligible"])

    def test_terms_difference_needs_specific_reviewed_adjustment(self):
        left, right = fixture(), fixture()
        right["quantity"] = 500
        self.assertFalse(eligible_pair(left, right)["eligible"])
        unrelated = dict(reviewed=True, source_refs=["synthetic"], covered_fields=["price_date"])
        self.assertFalse(eligible_pair(left, right, unrelated)["eligible"])
        approved = dict(reviewed=True, source_refs=["synthetic"], covered_fields=["quantity"])
        self.assertTrue(eligible_pair(left, right, approved)["eligible"])

    def test_complete_comparable_price_is_not_a_fraud_finding(self):
        left, right = fixture(), copy.deepcopy(fixture())
        right["unit_price"] = 20.0
        result = eligible_pair(left, right)
        self.assertTrue(result["eligible"])
        self.assertFalse(result["fraud_inference_permitted"])
        self.assertFalse(result["automatic_savings_inference_permitted"])
        self.assertFalse(result["input_authenticity_independently_verified_by_this_code"])

    def test_actual_history_cannot_pass_as_invoice_evidence(self):
        result = pilot_result(Path(__file__).resolve().parent)
        self.assertEqual(result["observations"], 7)
        self.assertEqual(result["possible_pairs"], 21)
        self.assertEqual(result["eligible_pairs"], 0)
        self.assertIsNone(result["potential_savings_usd"])


if __name__ == "__main__":
    unittest.main()
