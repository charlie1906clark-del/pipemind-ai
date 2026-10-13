# First runnable brain capability — local grounded retrieval

Run `python tools/brain_search.py "liquid hydrogen cooling"` from repository root.

The tool indexes **existing** repository Markdown under `docs/`, `research/`, `.claude/agents/` and root `*.md` without destructive migration. It returns scored sections, exact source path, line interval and raw snippet. It deliberately ignores symlinks and oversized notes, and does not need external AI API keys.

## Scope and limitations
- This is deterministic keyword retrieval, not semantic vector search, Obsidian sync, fact verification, internet research or automatic model training.
- A retrieved claim is not necessarily true. Technical numbers must go through the research-verifier role and an independent primary source before use.
- Results are traceable to the repository note; maintain evidence provenance separately.
- It does not read private external vaults, third-party connectors or run on a schedule.

## Next steps
1. Add tests for sections, markdown wikilinks, citations and provenance IDs.
2. Create approved primary-source fact cards with versioned review.
3. Add per-document access control and customer-data classification before private datasets.
4. Introduce retrieval quality fixtures and only then test semantic search as a separate replacement.
5. Connect to advisory orchestration; prohibit tool output from bypassing solver/safety gates.
