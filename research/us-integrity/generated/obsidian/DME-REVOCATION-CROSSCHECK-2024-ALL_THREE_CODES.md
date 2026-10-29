---
id: "DME-REVOCATION-CROSSCHECK-2024-ALL_THREE_CODES"
type: "finding"
title: "2024 ALL_THREE_CODES: current revocation intersection"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 ALL_THREE_CODES: current revocation intersection

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "code": "ALL_THREE_CODES",
    "cohort_unique_npis": 1440,
    "matches_to_current_revocation_snapshot_unique_npis": 34,
    "timing_relations": {
      "effective_after_service_year": {
        "associated_annual_puf_payment_measure_usd": "719611417.33",
        "unique_npis": 26
      },
      "effective_before_service_year": {
        "associated_annual_puf_payment_measure_usd": "1923512.54",
        "unique_npis": 2
      },
      "effective_during_service_year": {
        "associated_annual_puf_payment_measure_usd": "392038213.82",
        "unique_npis": 6
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
- [[DME-SRC-PUF-2024-A4352]]
- [[DME-SRC-PUF-2024-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-PUF-2024-A4352]] — documented_fact (edge-2f3745bba6d6c4e490f5); sources: [[DME-SRC-PUF-2024-A4352]]
- cites: [[DME-SRC-PUF-2024-A4351]] — documented_fact (edge-37f465485cc652386c92); sources: [[DME-SRC-PUF-2024-A4351]]
- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-46c72380db49771884a3); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-548790798954b340e5f7); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-6c5be0142602afd9d1c0); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PUF-2024-A4353]] — documented_fact (edge-b97f9044314c0b3d8f50); sources: [[DME-SRC-PUF-2024-A4353]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-e433b47f72652fee8167)
