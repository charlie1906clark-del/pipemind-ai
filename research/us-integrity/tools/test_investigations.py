"""Approval-boundary and provenance regressions for investigation extensions."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from investigation_extensions import load_approved_extensions

ROOT = Path(__file__).resolve().parents[1]
DAY = "2026-10-29"


class InvestigationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ["data", "investigations/case", "engine"]:
            (self.root / folder).mkdir(parents=True)
        shutil.copyfile(ROOT / "engine/integrity.py", self.root / "engine/integrity.py")
        self.source = dict(id="source-original", type="source", title="Official source", status="source",
            source_ids=[], properties=dict(url="https://example.gov/source", accessed_at=DAY))
        self.record = dict(id="finding-new", type="finding", title="Bounded reviewed fact",
            status="documented_fact", source_ids=["source-original"], properties=dict(visibility="public"))
        self.extension = dict(version="1.0", as_of=DAY, nodes=[self.record], edges=[])

    def approve(self, extension=None, path="investigations/case/graph.json"):
        target = self.root / path
        target.write_text(json.dumps(extension or self.extension))
        approval = dict(version="1.0", extensions=[dict(path=path,
            sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
            review_status="accepted_for_public_graph", review_note="Test explicit review")])
        (self.root / "data/approved-investigations.json").write_text(json.dumps(approval))

    def load(self):
        return load_approved_extensions(self.root, [copy.deepcopy(self.source)], [], DAY)

    def test_unlisted_extension_is_never_discovered(self):
        (self.root / "investigations/case/unreviewed.json").write_text(json.dumps(self.extension))
        self.assertEqual(self.load(), [])

    def test_explicit_review_can_link_existing_source(self):
        self.approve()
        nodes, edges = [copy.deepcopy(self.source)], []
        result = load_approved_extensions(self.root, nodes, edges, DAY)
        self.assertEqual([node["id"] for node in nodes], ["source-original", "finding-new"])
        self.assertEqual(result[0]["nodes"], 1)

    def test_changed_extension_requires_new_review_digest(self):
        self.approve()
        (self.root / "investigations/case/graph.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            self.load()

    def test_historical_extension_keeps_its_observation_date(self):
        self.approve()
        nodes = [copy.deepcopy(self.source)]
        result = load_approved_extensions(self.root, nodes, [], "2026-10-30")
        self.assertEqual(result[0]["as_of"], DAY)
        self.assertEqual(nodes[0]["properties"]["accessed_at"], DAY)

    def test_future_extension_is_refused(self):
        self.extension["as_of"] = "2026-10-30"
        self.approve()
        with self.assertRaisesRegex(ValueError, "cannot exceed"):
            self.load()

    def test_invalid_extension_date_is_refused(self):
        self.extension["as_of"] = "2026-99-99"
        self.approve()
        with self.assertRaisesRegex(ValueError, "Invalid investigation"):
            self.load()

    def test_existing_ids_cannot_be_replaced(self):
        self.extension["nodes"][0]["id"] = "source-original"
        self.approve()
        with self.assertRaisesRegex(ValueError, "cannot replace"):
            self.load()

    def test_escaping_path_is_rejected(self):
        self.approve(path="data/outside.json")
        with self.assertRaisesRegex(ValueError, "extension path"):
            self.load()

    def test_changed_reviewed_input_is_rejected(self):
        p = self.root / "investigations/case/evidence.json"
        p.write_text('{"fact":"before"}')
        self.extension["input_artifacts"] = [dict(path="investigations/case/evidence.json",
            sha256=hashlib.sha256(p.read_bytes()).hexdigest())]
        self.approve()
        p.write_text('{"fact":"after"}')
        with self.assertRaisesRegex(ValueError, "reviewed input changed"):
            self.load()

    def test_dangling_provenance_fails_without_partial_append(self):
        self.record["source_ids"] = ["missing-source"]
        self.approve()
        nodes, edges = [copy.deepcopy(self.source)], []
        with self.assertRaisesRegex(ValueError, "provenance"):
            load_approved_extensions(self.root, nodes, edges, DAY)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(edges, [])

    def test_novel_named_private_lead_is_refused(self):
        self.record["type"] = "lead"
        self.record["properties"].update(novel_lead=True, public_record=False)
        self.approve()
        with self.assertRaisesRegex(ValueError, "nonpublic lead"):
            self.load()

    def test_false_conviction_label_is_refused(self):
        self.record.update(type="case", status="conviction")
        self.record["properties"].update(public_record=True, legal_status="charged")
        self.approve()
        with self.assertRaisesRegex(ValueError, "conviction label"):
            self.load()

    def test_nonfinite_money_is_refused(self):
        self.record["properties"]["money"] = dict(amount="NaN", currency="USD", kind="claimed")
        self.approve()
        with self.assertRaisesRegex(ValueError, "invalid money"):
            self.load()

    def test_archived_source_hash_is_verified(self):
        self.record.update(type="source", status="source", source_ids=[])
        self.record["properties"].update(url="https://example.gov/capture", accessed_at=DAY,
            source_bytes_archived=True, snapshot_path="investigations/case/capture.json",
            content_sha256="0" * 64)
        (self.root / "investigations/case/capture.json").write_text("[]")
        self.approve()
        with self.assertRaisesRegex(ValueError, "source digest mismatch"):
            self.load()


if __name__ == "__main__":
    unittest.main()
