---
task_id: REPLACE
agent_id: REPLACE
input_commit: REPLACE
created_at: REPLACE_UTC_TIMESTAMP
visibility: public
review_status: awaiting_independent_review
---

# Bounded research result

## Question and cohort

Exact question, programme/agency, fiscal or calendar period, inclusion/exclusion rules and why the cohort was chosen before looking at rankings.

## Sources and acquisition

Source IDs; exact primary URLs/locators; publication/retrieval dates; API query and cursor/pagination ledger; raw byte snapshot/hash only when actually retained; row counts; duplicates; suppressed/missing fields; update lag; access and licence limitations.

## Direct findings

One claim per row, each with its source ID/locator, subject, period, measure and narrow wording. Distinguish what the publisher says from independently established fact. Include a case's precise legal status and date.

| Claim ID | Direct observation | Source and locator | Period/measure | Status |
|---|---|---|---|---|
| REPLACE | REPLACE | REPLACE | REPLACE | REPLACE |

## Entity and money controls

Exact identifiers and temporal joins; ambiguous or unmatched identities; documented roles versus ultimate ownership; decimal amount/currency/measure/period/basis; duplicate policy; no prime/subaward or billing/payment conflation.

## Method and reproducibility

Frozen input manifests, code commit, query/transformation, control population, parameters and expected output counts. Include the result path and hash where available.

## Hypotheses and falsification

Hypothesis; predicted observable evidence; tested legitimate/data-quality alternatives; matched controls; contradictory evidence; sensitivity to exclusions; what would disprove the hypothesis. Record nulls, rejected alerts and unresolved tests.

## Interpretation and limits

Separate inference from direct observation. Explain the exact edge/data access boundary preventing a stronger conclusion. Do not call an unexplained anomaly fraud.

## Publication and route review

Confirm role-relevant public records only. If a novel named suspicion survives, omit it from public output and create a separately authorized restricted handoff. Record potential route questions for counsel without deciding reward eligibility or submitting anything.

## Proposed graph patch

Additive nodes/edges using canonical IDs and source IDs; classification; legal status where applicable; `supersedes` links for corrections; no overwritten competing assertion.

## Independent reviewer decision

Reviewer/session; reproduction result; `supported_as_worded`, `supported_with_narrowing`, `unsupported`, `contradicted` or `needs_more_evidence`; sources and reasons; unresolved disagreement.

## Next bounded action

Specific evidence gap, proposed task ID/owner, acceptance test and stopping condition. A completed task can conclude that the lead was disproved.
