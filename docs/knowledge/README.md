# PipeMind knowledge governance

Existing `docs/research/`, `docs/modules/`, `docs/intelligence/`, `research/` and `docs/02-obsidian-brain.md` remain the preserved source of the Obsidian-compatible knowledge corpus.

**Important:** markdown 'training' summaries are external knowledge notes and system instructions. They do not update any model weights or confer certification.

## Evidence protocol
Every new technical claim should include:
- claim ID, one-sentence claim and module
- primary source title/URL/DOI; accessed date and publication date
- exact value and **units** if quantitative, reference scenario and validity range
- evidence tier: primary measured; primary calculated; secondary; assumption; hypothesis
- confirmed/requires-verification/superseded status
- owner/reviewer, checked date and implications for code/tests

No historical number may silently become a production default. Record competing definitions (e.g., cooling watts at 20K vs electrical watts, gross boil-off vs unrecovered loss).

## Obsidian conventions
Preserve relative links or `[[note title]]` links. Put new decisions in `docs/decisions/`, models in `docs/validation/`, verified sources in `docs/knowledge/`, dated discoveries in `docs/research/updates/`. Use Git revisions for the audit trail. The repository alone does not provide full-text retrieval/RAG, scheduling, internet updates or agent execution.

## Highest-risk historical claims to review
1. Source and scenario behind heat leakage values (~1–2 W/m) before using for design.
2. TEMOA €/km/MW cost thresholds and denominator definitions; no universal commercial cut-off.
3. NFPA 2 scenario-size descriptions: do **not** assume a single leak fraction universally establishes setbacks.
4. Route/vacuum-failure figures, cooling station spacing and MgB2 temperature/current limits need explicit sources and domains.
5. Recent dated company intelligence requires primary-source recertification before customer-facing distribution.
6. X-algorithm and marketing claims are not relevant inputs to engineering calculations.
