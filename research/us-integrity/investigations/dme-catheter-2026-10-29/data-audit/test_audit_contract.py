"""Adversarial provenance checks and independent reconciliation of acquired data."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from decimal import Decimal

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("catheter_audit", HERE / "audit_catheters.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


@contextlib.contextmanager
def isolated_snapshot():
    """Mutations exist only in an owned temporary copy, never primary evidence."""
    with tempfile.TemporaryDirectory(prefix="qa_", dir=HERE) as tmp:
        root = Path(tmp)
        shutil.copytree(HERE / "snapshots", root / "snapshots")
        for name in ("acquisition_manifest.json", "national_acquisition_manifest.json", "national_reconciliation.json"):
            shutil.copyfile(HERE / name, root / name)
        old = audit.BASE
        audit.BASE = root
        try:
            yield root
        finally:
            audit.BASE = old


class CohortContractTests(unittest.TestCase):
    def test_current_evidence_validates(self):
        with isolated_snapshot() as root:
            audit.verify_local()
            validation = json.loads((root / "validation.json").read_text())
            self.assertEqual(validation["total_supplier_rows"], 6870)
            self.assertEqual(len(validation["cohorts"]), 9)

    def test_response_snapshot_tampering_rejected(self):
        with isolated_snapshot() as root:
            manifest = json.loads((root / "acquisition_manifest.json").read_text())
            path = root / manifest["cohorts"][0]["snapshot"]
            path.write_bytes(path.read_bytes() + b" ")
            with self.assertRaises(AssertionError):
                audit.verify_local()

    def test_duplicate_exact_grain_rejected_even_if_hashes_recomputed(self):
        with isolated_snapshot() as root:
            manifest_path = root / "acquisition_manifest.json"
            manifest = json.loads(manifest_path.read_text())
            cohort = manifest["cohorts"][0]
            path = root / cohort["snapshot"]
            rows = json.loads(path.read_text())
            rows[1]["Suplr_NPI"] = rows[0]["Suplr_NPI"]
            rows[1]["HCPCS_Cd"] = rows[0]["HCPCS_Cd"]
            rows[1]["Suplr_Rentl_Ind"] = rows[0]["Suplr_Rentl_Ind"]
            audit.save(path, rows)
            cohort["snapshot_sha256"] = audit.sha(path.read_bytes())
            cohort["canonical_rows_sha256"] = audit.sha(audit.canonical(rows))
            audit.save(manifest_path, manifest)
            with self.assertRaises(AssertionError):
                audit.verify_local()

    def test_missing_api_row_rejected_by_independent_stats_count(self):
        with isolated_snapshot() as root:
            path = root / "acquisition_manifest.json"
            manifest = json.loads(path.read_text())
            manifest["cohorts"][0]["stats"]["found_rows"] += 1
            audit.save(path, manifest)
            with self.assertRaises(AssertionError):
                audit.verify_local()

    def test_longitudinal_decomposition_independently_reconciles(self):
        analysis = json.loads((HERE / "analysis.json").read_text())
        for c in analysis["comparisons"]:
            with self.subTest(code=c["code"], years=(c["before_year"], c["after_year"])):
                # Independent arithmetic on displayed USD amounts permits cent rounding.
                components = Decimal(c["matched_payment_delta_usd"]) + Decimal(c["newly_observed_payment_usd"]) - Decimal(c["no_longer_observed_prior_payment_usd"])
                self.assertLessEqual(abs(components - Decimal(c["payment_change_usd"])), Decimal("0.02"))

    def test_suppressed_beneficiaries_stay_unknown_and_do_not_deduplicate(self):
        rows = json.loads((HERE / "snapshots" / "suppliers_2023_A4353.json").read_text())
        national = json.loads((HERE / "snapshots" / "national_2022_2024.json").read_text())
        national_row = next(r for r in national if r["year"] == 2023 and r["HCPCS_Cd"] == "A4353")
        self.assertEqual(sum(r["Tot_Suplr_Benes"] == "" for r in rows), 230)
        # A concrete counterexample to treating supplier counts as distinct people.
        supplier_sum = sum(int(r["Tot_Suplr_Benes"]) for r in rows if r["Tot_Suplr_Benes"])
        self.assertGreater(supplier_sum, int(national_row["Tot_Suplr_Benes"]))


if __name__ == "__main__":
    unittest.main()
