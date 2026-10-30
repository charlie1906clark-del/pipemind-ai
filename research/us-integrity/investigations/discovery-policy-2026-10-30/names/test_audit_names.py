import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from audit_names import group_records, normalize_name, scripts, valid_uei, validate_capture


def row(name, uei="A12345678901", ident="record1", level="C"):
    return dict(name=name, uei=uei, id=ident, recipient_level=level)


class NameAuditTests(unittest.TestCase):
    def test_punctuation_and_case_are_only_a_comparison_key(self):
        self.assertEqual(normalize_name("  Example.COM, Inc. "), "example com inc")
        records = [row("Example.COM, Inc."), row("EXAMPLE COM INC", ident="record2")]
        result = group_records(records)[0]
        self.assertEqual(result["distinct_raw_names"], ["EXAMPLE COM INC", "Example.COM, Inc."])
        self.assertIn("same_uei_name_variation", result["observations"])
        self.assertFalse(result["automatic_entity_merge"])
        self.assertFalse(result["fraud_determination"])

    def test_different_identifiers_do_not_merge_after_punctuation(self):
        result = group_records([row("Example, Inc."), row("Example Inc", "B12345678901", "r2")])[0]
        self.assertEqual(len(result["distinct_valid_ueis"]), 2)
        self.assertIn("shared_comparison_key_distinct_ueis", result["observations"])
        self.assertNotIn("same_uei_name_variation", result["observations"])
        self.assertFalse(result["automatic_entity_merge"])

    def test_missing_identifier_cannot_be_filled_from_name(self):
        result = group_records([row("Example Inc", None), row("EXAMPLE INC", "B12345678901", "r2")])[0]
        self.assertEqual(result["missing_or_invalid_uei_rows"], 1)
        self.assertIn("identifier_unresolved_for_some_records", result["observations"])
        self.assertFalse(result["automatic_entity_merge"])

    def test_malformed_identifier_remains_unresolved(self):
        self.assertFalse(valid_uei("short"))
        self.assertFalse(valid_uei("A12345678901 "))
        self.assertFalse(valid_uei(None))
        self.assertTrue(valid_uei("A12345678901"))

    def test_parent_child_profile_pair_is_not_two_companies(self):
        result = group_records([row("Example Inc", level="P"), row("Example Inc", ident="r2", level="C")])[0]
        self.assertEqual(result["record_count"], 2)
        self.assertEqual(result["profile_level_pair_count"], 1)
        self.assertEqual(len(result["distinct_valid_ueis"]), 1)

    def test_dba_text_is_not_removed(self):
        self.assertNotEqual(normalize_name("Example LLC DBA Amazon"), normalize_name("Amazon"))
        self.assertIn("dba", normalize_name("Example LLC DBA Amazon"))

    def test_subsidiary_words_and_legal_suffixes_are_retained(self):
        self.assertNotEqual(normalize_name("Example Inc"), normalize_name("Example Services LLC"))
        self.assertNotEqual(normalize_name("Example Inc"), normalize_name("Example LLC"))

    def test_unicode_compatibility_does_not_remove_raw_name(self):
        records = [row("ＥＸＡＭＰＬＥ LLC"), row("Example LLC", ident="r2")]
        result = group_records(records)[0]
        self.assertEqual(result["record_count"], 2)
        self.assertIn("ＥＸＡＭＰＬＥ LLC", result["distinct_raw_names"])

    def test_mixed_script_lookalike_is_not_transliterated_or_merged(self):
        latin, lookalike = "Amazon", "Аmazon"  # second name starts with Cyrillic A
        self.assertNotEqual(normalize_name(latin), normalize_name(lookalike))
        self.assertEqual(scripts(lookalike), ["CYRILLIC", "LATIN"])
        self.assertEqual(len(group_records([row(latin), row(lookalike, ident="r2")])), 2)

    def test_missing_names_do_not_create_one_entity(self):
        self.assertEqual(len(group_records([row(None), row("", ident="r2")])), 2)

    def test_order_does_not_change_group_descriptions(self):
        records = [row("Example, Inc."), row("Example Inc", "B12345678901", "r2"), row("Other Inc", ident="r3")]
        original = copy.deepcopy(records)
        self.assertEqual(group_records(records), group_records(list(reversed(records))))
        self.assertEqual(records, original)

    def test_saved_capture_validates(self):
        capture = Path(__file__).parent / "capture-2026-10-30"
        self.assertTrue(validate_capture(capture)["success"])

    def test_snapshot_tampering_is_rejected(self):
        source = Path(__file__).parent / "capture-2026-10-30"
        manifest = json.loads((source / "manifest.json").read_text())
        first = manifest["requests"][0]
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "manifest.json").write_text(json.dumps(manifest))
            for key in ["snapshot_path", "request_path"]:
                path = folder / first[key]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((source / first[key]).read_bytes())
            (folder / first["snapshot_path"]).write_text("{}")
            with self.assertRaisesRegex(ValueError, "digest mismatch"):
                validate_capture(folder)

    def copy_capture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        folder = Path(temp.name) / "capture"
        shutil.copytree(Path(__file__).parent / "capture-2026-10-30", folder)
        return folder

    def test_claimed_count_cannot_replace_count_response(self):
        folder = self.copy_capture()
        path = folder / "manifest.json"
        data = json.loads(path.read_text())
        data["queries"]["amazon"]["before_count"] += 1
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Count snapshot differs"):
            validate_capture(folder)

    def test_claimed_complete_count_does_not_replace_terminal_page(self):
        folder = self.copy_capture()
        path = folder / "manifest.json"
        data = json.loads(path.read_text())
        data["requests"] = [r for r in data["requests"] if r["label"] != "amazon-awards-3"]
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "terminal empty page"):
            validate_capture(folder)

    def test_derived_parent_link_tampering_is_rejected(self):
        folder = self.copy_capture()
        path = folder / "profiles.json"
        data = json.loads(path.read_text())
        data[0]["parent_uei"] = "Z12345678901"
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Derived profile file differs"):
            validate_capture(folder)


if __name__ == "__main__":
    unittest.main()
