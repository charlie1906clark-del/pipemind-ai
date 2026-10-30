---
id: "DME-REVOCATION-COHORT-OVERVIEW"
type: "finding"
title: "64 of 1,976 cohort NPIs match the current revocation snapshot"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 64 of 1,976 cohort NPIs match the current revocation snapshot

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "additional_npi_rows": 94,
    "additional_orphan_rows": 0,
    "cohort_unique_npis_across_years_and_codes": 1976,
    "flattened_enrollment_npi_rows_including_blanks": 8714,
    "flattened_unique_nonblank_npis": 7462,
    "interpretation": [
      "Exact NPI linkage only; current snapshot is not historical enrollment status.",
      "Annual PUF service-year measures cannot establish transaction payment dates or released cash.",
      "A revocation effective during a year does not place that year's services before or after the effective date.",
      "A current revoked enrollment may coexist with another active enrollment under the same TIN; NPI linkage alone does not identify the billed enrollment.",
      "The current-bar snapshot omits completed bars, appeal outcomes and other historically relevant records; matching share is not a fraud or revocation rate.",
      "Relation buckets can overlap for an NPI with more than one revoked enrollment; do not sum them.",
      "No new named suspected actor or alleged loss is emitted."
    ],
    "main_blank_npi_rows": 128,
    "main_rows": 8620,
    "main_unique_enrollment_npi_keys": 8620,
    "main_unique_enrollments": 8620,
    "unique_cohort_npis_matching_current_snapshot": 64,
    "validation": {
      "additional_all_enrollments_linked": true,
      "additional_enrollment_npi_keys_unique": true,
      "main_enrollment_npi_keys_unique": true,
      "stats_row_count_equal": true,
      "terminal_empty_page": true
    }
  },
  "inference_limit": "An exact NPI intersection is neither a fraud rate nor proof the corresponding annual claims were paid after revocation.",
  "review_packet": "enrollment/evidence_records.json",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-ENROLLMENT-cms-methodology]]
- [[DME-SRC-PUF-2022-A4351]]
- [[DME-SRC-PUF-2022-A4352]]
- [[DME-SRC-PUF-2022-A4353]]
- [[DME-SRC-PUF-2023-A4351]]
- [[DME-SRC-PUF-2023-A4352]]
- [[DME-SRC-PUF-2023-A4353]]
- [[DME-SRC-PUF-2024-A4351]]
- [[DME-SRC-PUF-2024-A4352]]
- [[DME-SRC-PUF-2024-A4353]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-PUF-2024-A4352]] — documented_fact (edge-272dc479e1d3bda1eefc); sources: [[DME-SRC-PUF-2024-A4352]]
- cites: [[DME-SRC-PUF-2024-A4353]] — documented_fact (edge-352b3f7b9cfef3365d38); sources: [[DME-SRC-PUF-2024-A4353]]
- cites: [[DME-SRC-PUF-2022-A4353]] — documented_fact (edge-5ae604c949d8bd0d3929); sources: [[DME-SRC-PUF-2022-A4353]]
- cites: [[DME-SRC-PUF-2022-A4351]] — documented_fact (edge-64343aeebf64c53b2b47); sources: [[DME-SRC-PUF-2022-A4351]]
- cites: [[DME-SRC-PUF-2023-A4353]] — documented_fact (edge-79786b8199877b9b9186); sources: [[DME-SRC-PUF-2023-A4353]]
- cites: [[DME-SRC-PUF-2022-A4352]] — documented_fact (edge-9125d69cd4c03859df30); sources: [[DME-SRC-PUF-2022-A4352]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-a2f27793b89f9218c136); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-PUF-2024-A4351]] — documented_fact (edge-aa8963768d8b633ed84e); sources: [[DME-SRC-PUF-2024-A4351]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-ba406474629ab729329c); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-db4374747f16efd62a89); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-PUF-2023-A4352]] — documented_fact (edge-dd08679030ba8cfb972e); sources: [[DME-SRC-PUF-2023-A4352]]
- cites: [[DME-SRC-PUF-2023-A4351]] — documented_fact (edge-f5bdd66b56d551793248); sources: [[DME-SRC-PUF-2023-A4351]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-a99451648304275ab6de)
