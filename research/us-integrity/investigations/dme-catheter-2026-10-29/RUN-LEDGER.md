# Specialist execution and handoff

Date: 2026-10-29. These are workers used in this research session, not permanently deployed services. They shared this checkout and used separate output directories. A separate ChatGPT conversation was not automatically connected.

| Worker | Bounded assignment | Evidence/output | Reviewer |
|---|---|---|---|
| catheter_data_auditor | Acquire every published A4351/A4352/A4353 supplier row for 2022–2024; counts, pagination, hashes, annual decomposition, national reconciliation | `data-audit/` | catheter_falsification; root |
| catheter_case_tracer | Read original complaints/indictments and later official case updates; separate payer amounts, legal events and overlap | `case-trace/` | root; catheter_falsification |
| catheter_ownership_auditor | Exact NPI and corporate identity; separate authorized official, registered agent, alleged owner and beneficial control; public LEIE | `identity/` | root; revocation_crosscheck |
| revocation_crosscheck | Resolve latest CMS data version; retrieve all published revoked enrollments and companion NPIs; exact matches and aggregate intersection | `enrollment/` | root; catheter_ownership_auditor |
| catheter_falsification | Challenge candidate selection, cash inference, code controls, suppression, dates and claimed public availability; independently recompute data | `falsification/` | root |
| catheter_graph_integrator | Preserve reviewed findings as separate source-linked nodes; explicit extension loading; regenerateable Obsidian integration | graph extension and assembly changes | root; graph validator/tests |

## Operating contract for this investigation

- Follow discrepancies until resolved, bounded by source availability. A null result is a valid result. Never manufacture a finding to satisfy a quota.
- Use exact professional/business identifiers; record time and role. Name-only matching is discovery, not a completed entity merge.
- An administrative action, criminal allegation, plea, sentence and recovered amount are separate events. Do not propagate a group's guilt to an individual.
- Every amount has a payer, period, accounting meaning and source. Claims submitted, claims processed, escrow, receipts, transfers, ordered forfeiture and collected recovery must not be conflated.
- Preserve source provenance and failed attempts. A hash of a sanitized extract does not certify bytes of the original full download.
- Test alternative explanations and denominators before ranking. Publish aggregate descriptive results and already published case facts; do not create new named public accusations from an outlier screen.
- Questions needing a new public source remain open. A claim of general authorization does not make an unavailable source appear or supply authenticated access.

## Completed reviewer challenges

The independent calculation review is saved in `falsification/data_review.json`. It recomputes all nine cohort aggregates, all six annual decompositions, two cross-code entry checks and nine national reconciliations from the selected source rows. The source-method review identifies suppression ambiguity, affected comparison codes, historical-data limits and the distinction between claimed payment and actual cash movement. Original-document image checks resolved a potential 2023/2025 acquisition-year transcription error before publication; the retained year is 2025.

## Other-session handoff

Read `REPORT.md`, the five specialist reports and the current repository commit before starting. Select one finite task from `FOLLOW-UP-QUEUE.json` and announce its ID through a shared coordinator. Separate chat sessions do not share a live lock merely because they can read this Git branch. Record your source, exact query, date, evidence status, alternative explanation and missing evidence. Submit proposed changes on a separate branch and request an independent evidence review. Do not automatically overwrite this run's dated snapshots.

See the existing [second-model handoff](../../agents/SECOND-MODEL-HANDOFF.md) and [task lease protocol](../../engine/README.md) for the broader system. This run's research findings do not retroactively complete all 24 foundation work packages.
