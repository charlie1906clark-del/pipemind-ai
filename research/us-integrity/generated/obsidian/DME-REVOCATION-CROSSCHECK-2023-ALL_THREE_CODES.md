---
id: "DME-REVOCATION-CROSSCHECK-2023-ALL_THREE_CODES"
type: "finding"
title: "2023 ALL_THREE_CODES: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 ALL_THREE_CODES: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "ALL_THREE_CODES",
    "cohort_unique_npis": 1520,
    "matches_to_current_revocation_snapshot_unique_npis": 47,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "3209673444.39",
        "unique_npis": 42
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "2277224.96",
        "unique_npis": 4
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "194753411.08",
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
- [[DME-SRC-PUF-2023-A4351]]
- [[DME-SRC-PUF-2023-A4352]]
- [[DME-SRC-PUF-2023-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-PUF-2023-A4351]] — documented_fact (edge-08a5e9b9e74b072b07b5); sources: [[DME-SRC-PUF-2023-A4351]]
- cites: [[DME-SRC-PUF-2023-A4352]] — documented_fact (edge-65dcb782dd96c106a760); sources: [[DME-SRC-PUF-2023-A4352]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-7e0f39c828d8dd00f8e1); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-8c15c4f1501fd80ceed7); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-a52bc6bf01f8ae118dd6); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-PUF-2023-A4353]] — documented_fact (edge-b84ed8f0cf36bef5af2d); sources: [[DME-SRC-PUF-2023-A4353]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-62016ed304da9ad6e699)
