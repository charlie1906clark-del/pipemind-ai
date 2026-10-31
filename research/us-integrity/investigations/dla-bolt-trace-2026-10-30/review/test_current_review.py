"""Evidence-bound regressions for the independent current-order check."""
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from verify_current import CURRENT, verify


class CurrentReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.current = Path(self.temp.name) / "current"
        self.current.mkdir()
        for name in ("selected_manifest.json", "observations.json"):
            shutil.copyfile(CURRENT / name, self.current / name)
        shutil.copytree(CURRENT / "snapshots", self.current / "snapshots")

    def tearDown(self):
        self.temp.cleanup()

    def edit_observation(self, change):
        path = self.current / "observations.json"
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data))

    def test_public_snapshots_work_without_private_pdf(self):
        result = verify(current_dir=self.current)
        self.assertTrue(result["current_line_price_verified"])
        self.assertFalse(result["original_pdfs_replayed_this_run"])
        self.assertEqual(result["ordered_line_amount_usd"], "824.46")

    def test_ceiling_derived_unit_price_rejected(self):
        self.edit_observation(lambda d: d["child_order"].update(unit_price="157.5867"))
        with self.assertRaises(ValueError):
            verify(current_dir=self.current)

    def test_amount_tampering_rejected(self):
        self.edit_observation(lambda d: d["child_order"].update(order_line_total="8244.60"))
        with self.assertRaises(ValueError):
            verify(current_dir=self.current)

    def test_payment_assumption_rejected(self):
        self.edit_observation(lambda d: d["child_order"].update(payment_verified=True))
        with self.assertRaises(ValueError):
            verify(current_dir=self.current)

    def test_missing_selected_page_rejected(self):
        (self.current / "snapshots/order-page2.txt").unlink()
        with self.assertRaises(FileNotFoundError):
            verify(current_dir=self.current)

    def test_changed_page_rejected_even_if_manifest_repinned(self):
        path = self.current / "snapshots/order-page2.txt"
        path.write_text(path.read_text().replace("0.9100", "9.1000"))
        manifest_path = self.current / "selected_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        for record in manifest["records"]:
            for artifact in record["selected_artifacts"]:
                if artifact["path"] == "snapshots/order-page2.txt":
                    artifact["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaises(ValueError):
            verify(current_dir=self.current)

    def test_nonfinite_price_rejected(self):
        self.edit_observation(lambda d: d["child_order"].update(unit_price="NaN"))
        with self.assertRaises(ValueError):
            verify(current_dir=self.current)


if __name__ == "__main__":
    unittest.main()
