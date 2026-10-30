---
id: "DME-REVOCATION-CROSSCHECK-2024-A4352"
type: "finding"
title: "2024 A4352: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4352: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "A4352",
    "cohort_unique_npis": 569,
    "matches_to_current_revocation_snapshot_unique_npis": 10,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "279410.46",
        "unique_npis": 9
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "857665.72",
        "unique_npis": 1
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "0.00",
        "unique_npis": 0
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
- [[DME-SRC-PUF-2024-A4352]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-220eb6ac1bf566d9558f); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-aa85fa92737901cda14b); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PUF-2024-A4352]] — documented_fact (edge-cfe0c4d8cee3b7d5653b); sources: [[DME-SRC-PUF-2024-A4352]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-d97aa50dbaa47c27079e); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-ff976ba1eb4e291a8516)
