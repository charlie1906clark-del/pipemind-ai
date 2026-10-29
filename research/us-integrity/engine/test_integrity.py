import copy
import csv
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest

SPEC = importlib.util.spec_from_file_location("integrity", Path(__file__).with_name("integrity.py"))
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def fixture():
    return {"version": "1.0", "as_of": "2026-10-29", "nodes": [
        {"id": "SRC-ONE", "type": "source", "title": "Official audit", "status": "source", "source_ids": [], "properties": {"url": "https://example.gov/audit", "accessed_at": "2026-10-29"}},
        {"id": "ORG-ONE", "type": "organization", "title": "Same name", "status": "documented_fact", "source_ids": ["SRC-ONE"], "properties": {"business_address": "Public office", "money": {"amount": "100.20", "currency": "USD", "kind": "obligation"}}},
        {"id": "ORG-TWO", "type": "organization", "title": "Same name", "status": "documented_fact", "source_ids": ["SRC-ONE"], "properties": {"identity_status": "unresolved"}},
        {"id": "CASE-ONE", "type": "case", "title": "Alleged matter", "status": "allegation", "source_ids": ["SRC-ONE"], "properties": {"legal_status": "charged", "public_record": True}}
    ], "edges": [{"id": "EDGE-ONE", "type": "mentions", "source": "SRC-ONE", "target": "ORG-ONE", "status": "documented_fact", "source_ids": ["SRC-ONE"], "properties": {}}]}


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = fixture()
        self.tmp = tempfile.TemporaryDirectory()
        self.output = Path(self.tmp.name) / "build"

    def tearDown(self):
        self.tmp.cleanup()

    def test_good_graph(self):
        self.assertEqual(engine.validate_graph(self.graph, public=True), {"nodes": 4, "edges": 1, "sources": 1})

    def test_dangling_endpoint(self):
        self.graph["edges"][0]["target"] = "NO-SUCH-NODE"
        with self.assertRaisesRegex(engine.IntegrityError, "dangling"):
            engine.validate_graph(self.graph)

    def test_provenance_must_be_source(self):
        self.graph["nodes"][1]["source_ids"] = ["ORG-TWO"]
        with self.assertRaisesRegex(engine.IntegrityError, "non-source"):
            engine.validate_graph(self.graph)

    def test_unknown_status(self):
        self.graph["nodes"][1]["status"] = "probably_fraud"
        with self.assertRaisesRegex(engine.IntegrityError, "unknown status"):
            engine.validate_graph(self.graph)

    def test_case_legal_status_required(self):
        del self.graph["nodes"][-1]["properties"]["legal_status"]
        with self.assertRaisesRegex(engine.IntegrityError, "legal_status"):
            engine.validate_graph(self.graph)

    def test_allegation_cannot_be_conviction(self):
        self.graph["nodes"][-1]["status"] = "conviction"
        with self.assertRaisesRegex(engine.IntegrityError, "conflicts"):
            engine.validate_graph(self.graph)

    def test_restricted_build_fails_before_writing(self):
        self.graph["nodes"][1]["properties"]["visibility"] = "restricted"
        with self.assertRaisesRegex(engine.IntegrityError, "restricted"):
            engine.build_graph(self.graph, self.output)
        self.assertFalse(self.output.exists())

    def test_private_field_nested_rejected(self):
        self.graph["nodes"][1]["properties"]["contact"] = {"personal_email": "private@example.com"}
        with self.assertRaisesRegex(engine.IntegrityError, "sensitive"):
            engine.build_graph(self.graph, self.output)

    def test_private_field_outside_properties_rejected(self):
        self.graph["nodes"][1]["ssn"] = "private"
        with self.assertRaisesRegex(engine.IntegrityError, "sensitive"):
            engine.build_graph(self.graph, self.output)

    def test_top_level_restricted_visibility_rejected(self):
        self.graph["nodes"][1]["visibility"] = "restricted"
        with self.assertRaisesRegex(engine.IntegrityError, "restricted"):
            engine.build_graph(self.graph, self.output)

    def test_business_address_not_private_address_false_positive(self):
        engine.build_graph(self.graph, self.output)
        self.assertTrue((self.output / "obsidian" / "ORG-ONE.md").exists())

    def test_public_person_needs_professional_source(self):
        node = self.graph["nodes"][1]
        node["type"] = "person"
        with self.assertRaisesRegex(engine.IntegrityError, "public_record"):
            engine.build_graph(self.graph, self.output)
        node["properties"]["public_record"] = True
        engine.build_graph(self.graph, self.output)

    def test_novel_nonpublic_lead_rejected(self):
        self.graph["nodes"][1]["properties"]["novel_lead"] = True
        with self.assertRaisesRegex(engine.IntegrityError, "novel"):
            engine.build_graph(self.graph, self.output)

    def test_unsafe_filename_rejected(self):
        for ident in ("../escape", "X/escape", "X\\escape", "X:drive", "X..escape", ".hidden", "[[X]]"):
            with self.subTest(ident=ident):
                graph = fixture()
                graph["nodes"][1]["id"] = ident
                with self.assertRaises(engine.IntegrityError):
                    engine.build_graph(graph, self.output)

    def test_same_name_entities_remain_distinct(self):
        engine.build_graph(self.graph, self.output)
        with engine.connect_db(self.output / "graph.sqlite") as db:
            results = engine.search_nodes(db, "Same")
        self.assertEqual({row["id"] for row in results}, {"ORG-ONE", "ORG-TWO"})

    def test_search_parameterization_and_literal_wildcards(self):
        engine.build_graph(self.graph, self.output)
        with engine.connect_db(self.output / "graph.sqlite") as db:
            self.assertEqual(engine.search_nodes(db, "'; DROP TABLE nodes; --"), [])
            self.assertEqual(db.execute("SELECT count(*) FROM nodes").fetchone()[0], 4)
            db.execute("INSERT OR REPLACE INTO metadata VALUES('search_backend','like')")
            self.assertEqual(engine.search_nodes(db, "%"), [])

    def test_hash_is_of_graph_not_source_bytes(self):
        result = engine.build_graph(self.graph, self.output)
        self.assertEqual(len(result["graph_sha256"]), 64)
        self.assertIn("not downloaded source content", result["hash_scope"])
        self.assertNotIn("content_sha256", self.graph["nodes"][0]["properties"])

    def test_content_hash_format(self):
        self.graph["nodes"][0]["properties"]["content_sha256"] = "not-a-hash"
        with self.assertRaisesRegex(engine.IntegrityError, "content_sha256"):
            engine.validate_graph(self.graph)

    def test_money_units_required(self):
        del self.graph["nodes"][1]["properties"]["money"]["currency"]
        with self.assertRaisesRegex(engine.IntegrityError, "currency"):
            engine.validate_graph(self.graph)

    def test_money_qualifier_period_and_basis_preserved(self):
        money = self.graph["nodes"][1]["properties"]["money"]
        money.update(qualifier="greater_than", period="FY2026", basis="Published announcement; not verified collection", condition="Conditional transfer milestone")
        engine.build_graph(self.graph, self.output)
        with (self.output / "exports" / "money.csv").open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(rows[0]["qualifier"], "greater_than")
        self.assertEqual(rows[0]["period"], "FY2026")
        self.assertIn("not verified collection", rows[0]["basis"])
        self.assertEqual(rows[0]["condition"], "Conditional transfer milestone")

    def test_negative_money_remains_numeric_in_csv(self):
        self.graph["nodes"][1]["properties"]["money"].update(amount="-100.20", kind="deobligation")
        engine.build_graph(self.graph, self.output)
        with (self.output / "exports" / "money.csv").open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(rows[0]["amount"], "-100.20")

    def test_reproducible_exports_and_backlinks(self):
        first = engine.build_graph(self.graph, self.output)
        exports = {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file() and p.suffix != ".sqlite"}
        second = engine.build_graph({**self.graph, "nodes": list(reversed(self.graph["nodes"]))}, self.output)
        self.assertEqual(first, second)
        self.assertEqual(exports, {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file() and p.suffix != ".sqlite"})
        self.assertIn("[[SRC-ONE]]: mentions", (self.output / "obsidian" / "ORG-ONE.md").read_text())

    def test_csv_formula_protection(self):
        self.assertEqual(engine.csv_value("=IMPORTXML('url')"), "'=IMPORTXML('url')")
        self.assertEqual(engine.csv_value("@SUM(1)"), "'@SUM(1)")

    def test_only_generated_stale_notes_removed(self):
        engine.build_graph(self.graph, self.output)
        custom = self.output / "obsidian" / "CUSTOM.md"
        custom.write_text("Keep my handwritten note")
        self.graph["nodes"] = self.graph["nodes"][:-1]
        engine.build_graph(self.graph, self.output)
        self.assertFalse((self.output / "obsidian" / "CASE-ONE.md").exists())
        self.assertTrue(custom.exists())

    def test_symlink_output_refused(self):
        elsewhere = Path(self.tmp.name) / "elsewhere"
        elsewhere.mkdir()
        self.output.mkdir()
        (self.output / "obsidian").symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaisesRegex(engine.IntegrityError, "symlink"):
            engine.build_graph(self.graph, self.output)
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_symlink_database_refused(self):
        target = Path(self.tmp.name) / "actual.sqlite"
        target.touch()
        link = Path(self.tmp.name) / "linked.sqlite"
        link.symlink_to(target)
        with self.assertRaisesRegex(engine.IntegrityError, "symlink"):
            engine.connect_db(link)
        self.assertEqual(target.stat().st_size, 0)

    def test_rebuild_preserves_completed_tasks_and_rolls_back_conflicts(self):
        tasks = [{"id": "TASK-A", "title": "Check", "status": "queued"}]
        engine.build_graph(self.graph, self.output, tasks)
        db = engine.connect_db(self.output / "graph.sqlite")
        claim = engine.claim_task(db, "TASK-A", "model", now=100)
        engine.complete_task(db, "TASK-A", "model", "Done", claim["lease_token"], now=101)
        db.close()
        engine.build_graph(self.graph, self.output, tasks)
        db = engine.connect_db(self.output / "graph.sqlite")
        self.assertEqual(db.execute("SELECT status FROM tasks").fetchone()[0], "completed")
        db.close()
        self.graph["nodes"][1]["title"] = "Changed title"
        tasks[0]["title"] = "Changed task definition"
        with self.assertRaisesRegex(engine.IntegrityError, "changed"):
            engine.build_graph(self.graph, self.output, tasks)
        db = engine.connect_db(self.output / "graph.sqlite")
        self.assertEqual(db.execute("SELECT title FROM nodes WHERE id='ORG-ONE'").fetchone()[0], "Same name")
        db.close()


class TaskTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "queue.sqlite"
        self.db = engine.connect_db(self.path)
        self.tasks = [{"id": "TASK-A", "title": "Check source", "status": "queued", "depends_on": []}, {"id": "TASK-B", "title": "Review", "status": "queued", "depends_on": ["TASK-A"]}]
        engine.import_tasks(self.db, self.tasks)

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def test_claim_idempotency_and_ownership(self):
        first = engine.claim_task(self.db, "TASK-A", "model-one", now=100)
        second = engine.claim_task(self.db, "TASK-A", "model-one", now=101)
        self.assertFalse(first["idempotent"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(first["lease_until"], second["lease_until"])
        with self.assertRaisesRegex(engine.IntegrityError, "leased"):
            engine.claim_task(self.db, "TASK-A", "model-two", now=101)
        with self.assertRaisesRegex(engine.IntegrityError, "owner"):
            engine.complete_task(self.db, "TASK-A", "model-two", "Review", first["lease_token"], now=102)

    def test_expired_lease_reclaim(self):
        first = engine.claim_task(self.db, "TASK-A", "model-one", lease_seconds=30, now=100)
        with self.assertRaisesRegex(engine.IntegrityError, "expired"):
            engine.complete_task(self.db, "TASK-A", "model-one", "Review", first["lease_token"], now=131)
        engine.claim_task(self.db, "TASK-A", "model-two", now=131)
        with self.assertRaisesRegex(engine.IntegrityError, "token"):
            engine.complete_task(self.db, "TASK-A", "model-one", "Review", first["lease_token"], now=132)

    def test_completion_idempotency_and_dependencies(self):
        with self.assertRaisesRegex(engine.IntegrityError, "dependency"):
            engine.claim_task(self.db, "TASK-B", "model-two", now=100)
        first = engine.claim_task(self.db, "TASK-A", "model-one", now=100)
        self.assertFalse(engine.complete_task(self.db, "TASK-A", "model-one", "Evidence URL reviewed", first["lease_token"], now=101)["idempotent"])
        self.assertTrue(engine.complete_task(self.db, "TASK-A", "model-one", "Evidence URL reviewed", first["lease_token"], now=102)["idempotent"])
        with self.assertRaises(engine.IntegrityError):
            engine.complete_task(self.db, "TASK-A", "model-one", "Different claim", first["lease_token"], now=103)
        engine.claim_task(self.db, "TASK-B", "model-two", now=104)

    def test_task_definition_import_does_not_reset_claim(self):
        engine.claim_task(self.db, "TASK-A", "model-one", now=100)
        engine.import_tasks(self.db, self.tasks)
        self.assertEqual(self.db.execute("SELECT status FROM tasks WHERE id='TASK-A'").fetchone()[0], "claimed")
        self.tasks[0]["title"] = "Changed work"
        with self.assertRaisesRegex(engine.IntegrityError, "changed"):
            engine.import_tasks(self.db, self.tasks)

    def test_cycle_and_missing_dependencies_rejected(self):
        self.tasks[0]["depends_on"] = ["TASK-B"]
        with self.assertRaisesRegex(engine.IntegrityError, "cyclic"):
            engine.validate_tasks(self.tasks)
        self.tasks[0]["depends_on"] = ["NO-TASK"]
        with self.assertRaisesRegex(engine.IntegrityError, "missing"):
            engine.validate_tasks(self.tasks)

    def test_blocked_task_cannot_be_claimed(self):
        engine.import_tasks(self.db, [{"id": "TASK-C", "title": "Await permission", "status": "blocked"}])
        with self.assertRaisesRegex(engine.IntegrityError, "blocked"):
            engine.claim_task(self.db, "TASK-C", "model-one")

    def test_lease_fences_stale_same_owner_completion(self):
        old = engine.claim_task(self.db, "TASK-A", "same-owner", lease_seconds=30, now=100)
        new = engine.claim_task(self.db, "TASK-A", "same-owner", now=131)
        self.assertNotEqual(old["lease_token"], new["lease_token"])
        with self.assertRaisesRegex(engine.IntegrityError, "token"):
            engine.complete_task(self.db, "TASK-A", "same-owner", "Stale result", old["lease_token"], now=132)
        engine.complete_task(self.db, "TASK-A", "same-owner", "Current result", new["lease_token"], now=132)

    def test_concurrent_claims_one_winner(self):
        winners, failures = [], []
        barrier = threading.Barrier(2)
        def contender(owner):
            db = engine.connect_db(self.path)
            try:
                barrier.wait()
                winners.append(engine.claim_task(db, "TASK-A", owner, now=100))
            except engine.IntegrityError as exc:
                failures.append(str(exc))
            finally:
                db.close()
        threads = [threading.Thread(target=contender, args=(name,)) for name in ("model-one", "model-two")]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(len(winners), 1)
        self.assertEqual(len(failures), 1)
        self.assertEqual(self.db.execute("SELECT count(*) FROM task_events").fetchone()[0], 1)


if __name__ == "__main__":
    unittest.main()
