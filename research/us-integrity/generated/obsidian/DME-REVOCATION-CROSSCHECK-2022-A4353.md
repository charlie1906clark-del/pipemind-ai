---
id: "DME-REVOCATION-CROSSCHECK-2022-A4353"
type: "finding"
title: "2022 A4353: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4353: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "A4353",
    "cohort_unique_npis": 322,
    "matches_to_current_revocation_snapshot_unique_npis": 7,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "129593.70",
        "unique_npis": 5
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "618062.77",
        "unique_npis": 1
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "47812.64",
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
- [[DME-SRC-PUF-2022-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-2a4fbe4efb5e7ee0f5cf); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-4af4c0ba5ebb63d87584); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-PUF-2022-A4353]] — documented_fact (edge-55e6ad12bbe403447bed); sources: [[DME-SRC-PUF-2022-A4353]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-930f06277468588989e3); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-61310e77cca3d285a016)
