import copy
import json
import unittest
from decimal import Decimal
from pathlib import Path
from acquire import build_request, validate_search
from analyze import build, validate_lines

HERE = Path(__file__).resolve().parent


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads((HERE / "capture/dla-bolts.json").read_text())
        self.lines = json.loads((HERE / "line_observations.json").read_text())["observations"]

    def test_actual_captures_hashes_and_output_replay(self):
        outputs = build()
        self.assertEqual(len(outputs["observations.json"]["observations"]), 30)
        for path, expected in outputs.items():
            self.assertEqual(json.loads((HERE / path).read_text()), expected, path)

    def test_filter_is_new_awards_not_performance_or_transaction_spend(self):
        time_filter = build_request("dla-bolts")["filters"]["time_period"][0]
        self.assertEqual(time_filter, {"start_date": "2026-07-03", "end_date": "2026-07-31", "date_type": "new_awards_only"})
        self.sample["results"][0]["Start Date"] = "2020-01-01"
        validate_search(self.sample, "dla-bolts")
        self.sample["results"][0]["Base Obligation Date"] = "2026-08-01"
        with self.assertRaises(ValueError):
            validate_search(self.sample, "dla-bolts")

    def test_duplicate_missing_and_non_string_ids_rejected(self):
        for value in (None, "", 123, self.sample["results"][1]["generated_internal_id"]):
            mutated = copy.deepcopy(self.sample)
            mutated["results"][0]["generated_internal_id"] = value
            with self.assertRaises(ValueError):
                validate_search(mutated, "dla-bolts")

    def test_nonfinite_amounts_rejected(self):
        for value in ("NaN", "Infinity", "-Infinity"):
            mutated = copy.deepcopy(self.sample)
            mutated["results"][0]["Award Amount"] = value
            with self.assertRaises(ValueError):
                validate_search(mutated, "dla-bolts")

    def test_wrong_agency_and_psc_rejected(self):
        for field, value in (("Awarding Sub Agency", "Other"), ("PSC", {"code": "6515"})):
            mutated = copy.deepcopy(self.sample)
            mutated["results"][0][field] = value
            with self.assertRaises(ValueError):
                validate_search(mutated, "dla-bolts")

    def test_pagination_required_and_sample_cap_enforced(self):
        for mutation in ("page", "hasNext", "over_cap"):
            mutated = copy.deepcopy(self.sample)
            if mutation == "over_cap":
                mutated["results"].append(copy.deepcopy(mutated["results"][0]))
            else:
                mutated["page_metadata"].pop(mutation)
            with self.assertRaises(ValueError):
                validate_search(mutated, "dla-bolts")

    def test_first_article_is_not_an_extra_production_unit(self):
        self.assertEqual(validate_lines(self.lines, "615816.57"), Decimal("615816.57"))
        self.assertEqual(sum(Decimal(line["quantity"]) for line in self.lines if line["line_type"] == "production_item"), Decimal("2243"))
        self.lines[1]["item_id"] = "5306004457358"
        with self.assertRaises(ValueError):
            validate_lines(self.lines, "615816.57")

    def test_wrong_line_math_and_obligation_rejected(self):
        with self.assertRaises(ValueError):
            validate_lines(self.lines, "615816.58")
        self.lines[0]["quantity"] = "2244.000"
        with self.assertRaises(ValueError):
            validate_lines(self.lines, "615816.57")

    def test_negative_ocr_values_cannot_cancel(self):
        self.lines[0]["quantity"] = "-2243.000"
        self.lines[0]["unit_price_usd"] = "-272.99"
        with self.assertRaises(ValueError):
            validate_lines(self.lines, "615816.57")
        self.lines[0]["quantity"] = "0"
        self.lines[0]["unit_price_usd"] = "272.99"
        self.lines[0]["extended_amount_usd"] = "0"
        with self.assertRaises(ValueError):
            validate_lines(self.lines, "3500.00")

    def test_obligations_not_promoted_to_unit_prices(self):
        rows = build()["observations.json"]["observations"]
        self.assertTrue(all(r["unit_price_usd"] is None and r["estimated_loss_usd"] is None for r in rows))
        self.assertEqual(sum(bool(r["line_observation_ids"]) for r in rows), 1)
        self.assertTrue(all(not r["line_observation_ids"] for r in rows if r["express_report_in_description"]))

    def test_rejected_catalog_items_cannot_become_benchmarks(self):
        rejected = json.loads((HERE / "rejected_comparators.json").read_text())
        self.assertEqual({r["catalog_number"] for r in rejected["observations"]}, {"240031300", "P1806UD"})
        self.assertTrue(all(r["rejection_reason"] for r in rejected["observations"]))
        self.assertEqual(build()["coverage.json"]["independent_matched_price_comparators"], 0)


if __name__ == "__main__":
    unittest.main()
