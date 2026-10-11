import tempfile
import unittest
from pathlib import Path

from brain_search import search


class MarkdownBrainTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs" / "research").mkdir(parents=True)
        (self.root / "docs" / "research" / "cryogenic.md").write_text(
            "# Cryogenic\nHydrogen heat ingress is important.\n\n"
            "## Cooling\nCooling power is not free electricity.\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "research" / "route.md").write_text(
            "# Route\nRoad crossings require civil engineering.\n", encoding="utf-8"
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_search_returns_source_lines(self):
        hits = search(self.root, "hydrogen heat ingress")
        self.assertTrue(hits)
        self.assertEqual(hits[0].path, "docs/research/cryogenic.md")
        self.assertEqual(hits[0].start_line, 1)
        self.assertIn("heat ingress", hits[0].snippet)

    def test_separate_heading_section(self):
        hits = search(self.root, "cooling electricity")
        self.assertEqual(hits[0].heading, "Cooling")
        self.assertEqual(hits[0].start_line, 4)

    def test_empty_or_invalid_input(self):
        for query in ("", "a"):
            with self.assertRaises(ValueError):
                search(self.root, query)
        with self.assertRaises(ValueError):
            search(self.root, "hydrogen", limit=0)

    def test_does_not_follow_symlinks(self):
        other = self.root.parent / "external-sensitive.md"
        (self.root / "docs" / "secret.md").symlink_to(other)
        self.assertEqual(search(self.root, "secret"), [])


if __name__ == "__main__":
    unittest.main()
