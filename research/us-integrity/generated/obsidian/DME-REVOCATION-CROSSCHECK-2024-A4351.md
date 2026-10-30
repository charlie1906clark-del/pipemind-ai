---
id: "DME-REVOCATION-CROSSCHECK-2024-A4351"
type: "finding"
title: "2024 A4351: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4351: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "A4351",
    "cohort_unique_npis": 1297,
    "matches_to_current_revocation_snapshot_unique_npis": 22,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "184781.76",
        "unique_npis": 19
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "492805.45",
        "unique_npis": 2
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "560.35",
        "unique_npis": 1
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
- [[DME-SRC-PUF-2024-A4351]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-3e22a51e6d6cc2d4b6c7); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-PUF-2024-A4351]] — documented_fact (edge-4986abd11ce2659971fe); sources: [[DME-SRC-PUF-2024-A4351]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-750e0d05e36f5e6957c1); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-c816a3f59665e2616578); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-66d8741a72d9723e9ad8)
