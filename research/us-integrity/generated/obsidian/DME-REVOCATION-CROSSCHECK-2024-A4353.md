---
id: "DME-REVOCATION-CROSSCHECK-2024-A4353"
type: "finding"
title: "2024 A4353: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4353: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "A4353",
    "cohort_unique_npis": 332,
    "matches_to_current_revocation_snapshot_unique_npis": 14,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "719147225.11",
        "unique_npis": 8
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "573041.37",
        "unique_npis": 1
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "392037653.47",
        "unique_npis": 5
      }
    },
    "year": 2024
  },
  "inference_limits": [
    "Exact NPI linkage only; current snapshot is not historical enrollment status.",
    "Annual PUF service-year measures cannot establish transaction payment dates or released cash.",
    "A revocation effective during a year does not place that year's services before or after the effective date.",
    "A current revoked enrollment may coexist with another active enrollment under the same TIN; NPI linkage alone does not identify the billed enrollment.",
    "The current-bar snapshot omits completed bars, appeal outcomes and other historically relevant records; matching share is not a fraud or revocation rate.",
    "Relation buckets can overlap for an NPI with more than one revoked enrollment; do not sum them.",
    "No new named suspected actor or alleged loss is emitted."
  ],
  "named_new_suspicions_published": false,
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-ENROLLMENT-cms-methodology]]
- [[DME-SRC-PUF-2024-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-7b27b1cab66382525551); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PUF-2024-A4353]] — documented_fact (edge-c4227548bbbe311836e6); sources: [[DME-SRC-PUF-2024-A4353]]
- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-cbfaa309a257007b0520); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-d4df2d2bc0a977f2bae0); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-d5b9a3a22f8184358e8a)
