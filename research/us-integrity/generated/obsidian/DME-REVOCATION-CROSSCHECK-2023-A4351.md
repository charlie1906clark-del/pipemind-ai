---
id: "DME-REVOCATION-CROSSCHECK-2023-A4351"
type: "finding"
title: "2023 A4351: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4351: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "A4351",
    "cohort_unique_npis": 1382,
    "matches_to_current_revocation_snapshot_unique_npis": 34,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "9992121.81",
        "unique_npis": 30
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "601597.10",
        "unique_npis": 4
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "0.00",
        "unique_npis": 0
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
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-288cd5b4b3a5b8cddfcd); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-7dcce376096ab74667ca); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PUF-2023-A4351]] — documented_fact (edge-a1e20d56466fb529a057); sources: [[DME-SRC-PUF-2023-A4351]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-b5dc0c2c4ea216ed87ca); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-73d9378f02ba53a3e9a5)
