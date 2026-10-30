---
id: "DME-REVOCATION-CROSSCHECK-2023-A4353"
type: "finding"
title: "2023 A4353: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4353: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "A4353",
    "cohort_unique_npis": 332,
    "matches_to_current_revocation_snapshot_unique_npis": 21,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "2986805166.65",
        "unique_npis": 18
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "698981.04",
        "unique_npis": 2
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "29514092.71",
        "unique_npis": 1
      }
    },
    "year": 2023
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
- [[DME-SRC-PUF-2023-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-3f346d94ba8dd71e23d6); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-PUF-2023-A4353]] — documented_fact (edge-4ebdab1c52845de55434); sources: [[DME-SRC-PUF-2023-A4353]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-846be486e5d5ef8d8ff8); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-f665d3a4943bb131b130); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-baa57e146a02c4d3d535)
