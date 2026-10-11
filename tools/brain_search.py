"""Deterministic, local markdown retrieval for PipeMind's Obsidian/GitHub brain.

This is source retrieval, NOT RAG with model embeddings, not fact-checking,
and not evidence of training a neural network. Returned notes may be wrong.
Only repo-local markdown is scanned; no network or code execution.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


_WORDS = re.compile(r"[a-z0-9]+", re.IGNORECASE)
MAX_BYTES = 256_000
SCANNED_DIRS = ("docs", "research", ".claude/agents")


@dataclass(frozen=True)
class Passage:
    path: str
    heading: str
    start_line: int
    end_line: int
    snippet: str
    score: int

    def to_dict(self) -> dict:
        return asdict(self)


def _tokens(value: str) -> list[str]:
    return [part.lower() for part in _WORDS.findall(value) if len(part) >= 2]


def _allowed_notes(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for dirname in SCANNED_DIRS:
        folder = root / dirname
        if folder.exists():
            candidates.extend(folder.rglob("*.md"))
    candidates.extend(root.glob("*.md"))
    # Ignore symlinks: cannot escape repository root or ingest third-party paths.
    return sorted(set(p for p in candidates if p.is_file() and not p.is_symlink()))


def _sections(path: Path, root: Path):
    if path.stat().st_size > MAX_BYTES:
        return
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (UnicodeError, OSError):
        return
    heading = path.stem
    start = 1
    section: list[str] = []
    relative = path.relative_to(root).as_posix()
    for index, line in enumerate(lines, 1):
        if line.lstrip().startswith("# ") or line.lstrip().startswith("## ") or line.lstrip().startswith("### "):
            if section:
                yield relative, heading, start, index - 1, "\n".join(section)
            heading = line.lstrip("# ").strip()
            start = index
            section = [line]
        else:
            section.append(line)
    if section:
        yield relative, heading, start, len(lines), "\n".join(section)


def search(root: str | Path, question: str, limit: int = 8) -> list[Passage]:
    """Retrieve ranked note sections with stable file paths and line citations."""
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError("root must be a directory")
    terms = set(_tokens(question))
    if not terms:
        raise ValueError("Question requires at least one alphanumeric word of length >= 2")
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    results = []
    for path in _allowed_notes(root):
        for relative, heading, start, end, text in _sections(path, root):
            text_tokens = _tokens(text)
            counts = {term: text_tokens.count(term) for term in terms}
            matched = sum(value > 0 for value in counts.values())
            if not matched:
                continue
            # Source title and section relevance outweigh repeated keyword stuffing.
            name_matches = sum(term in _tokens(relative + " " + heading) for term in terms)
            score = matched * 10 + min(sum(counts.values()), 20) + name_matches * 5
            nonempty = [line.strip() for line in text.splitlines() if line.strip()]
            snippet = " ".join(nonempty)[:500]
            results.append(Passage(relative, heading, start, end, snippet, score))
    return sorted(results, key=lambda p: (-p.score, p.path, p.start_line))[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search PipeMind markdown notes without AI-generated claims")
    parser.add_argument("question", help="Keyword question")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    print(json.dumps([item.to_dict() for item in search(args.root, args.question, args.limit)], indent=2))


if __name__ == "__main__":
    main()
