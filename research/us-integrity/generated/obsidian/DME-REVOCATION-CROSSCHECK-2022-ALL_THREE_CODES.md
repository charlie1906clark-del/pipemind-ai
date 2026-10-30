---
id: "DME-REVOCATION-CROSSCHECK-2022-ALL_THREE_CODES"
type: "finding"
title: "2022 ALL_THREE_CODES: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 ALL_THREE_CODES: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "ALL_THREE_CODES",
    "cohort_unique_npis": 1616,
    "matches_to_current_revocation_snapshot_unique_npis": 39,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "106115872.22",
        "unique_npis": 35
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "2021405.45",
        "unique_npis": 3
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "189116.44",
        "unique_npis": 1
      }
    },
    "year": 2022
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
- [[DME-SRC-PUF-2022-A4351]]
- [[DME-SRC-PUF-2022-A4352]]
- [[DME-SRC-PUF-2022-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-39d8585e7c1c58e9ffc6); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-PUF-2022-A4351]] — documented_fact (edge-41fe9797b1f5f60ac59c); sources: [[DME-SRC-PUF-2022-A4351]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-5db30ac269b205ef3b98); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-PUF-2022-A4352]] — documented_fact (edge-84993ba925eae574b1fc); sources: [[DME-SRC-PUF-2022-A4352]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-af22a3d268eb2c7f49f1); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PUF-2022-A4353]] — documented_fact (edge-b066335e54cc21197f8f); sources: [[DME-SRC-PUF-2022-A4353]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-51c7cb9cfc3f894cb45a)
