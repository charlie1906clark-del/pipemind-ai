---
id: "DME-ANONYMOUS-ENROLLMENT-A"
type: "finding"
title: "Candidate A: unresolved enrollment-scope follow-up"
status: "unknown"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Candidate A: unresolved enrollment-scope follow-up

Evidence status: **unknown**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "bounded_observation": {
    "appeal_disposition": null,
    "approved_enrollment_distinct_from_revoked_enrollment": true,
    "approved_enrollment_scope": "PART B SUPPLIER - MASS IMMUNIZATION (ROSTER BILLER ONLY)",
    "approved_enrollment_type": "12-73",
    "conclusive_published_enforcement_match": null,
    "historical_2024_enrollment_status": null,
    "interpretation": "Different approved enrollment demonstrated. Its immunization-only scope does not establish DME/catheter permission. This does not determine the enrollment used by 2024 claims.",
    "label": "Candidate A",
    "primary_npi_rows_Q1_Q3_Q4": [
      0,
      0,
      0
    ],
    "q4_additional_npi_rows": 1,
    "released_claim_cash_after_revocation": null,
    "revocation_notice_date": null,
    "revoked_scope": "DME SUPPLIER - PHARMACY"
  },
  "fraud_finding": false,
  "public_reproducibility": "Identifying query parameters and responses intentionally omitted; no named allegation is published",
  "scope": "Two anonymized NPIs with a current revoked enrollment effective before 2024 and a released 2024 catheter PUF row. Linkage review only, not an allegation.",
  "source_record": "enrollment/candidate_followup_summary.json",
  "unknowns": [
    "Historical billed enrollment ID and service dates",
    "Dates of decision, notice, appeal and any reinstatement",
    "Cash release, suspension, reversal and recoupment history"
  ],
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-ENROLLMENT-cms-methodology]]
- [[DME-SRC-PPEF-ADDITIONAL]]
- [[DME-SRC-PPEF-METHOD]]
- [[DME-SRC-PPEF-Q1-2026]]
- [[DME-SRC-PPEF-Q3-2026]]
- [[DME-SRC-PPEF-Q4-2026]]
- [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- [[DME-SRC-REVOCATIONS-Q3-2026]]

## Outgoing relationships

- cites: [[DME-SRC-PPEF-Q1-2026]] — documented_fact (edge-76c63386a4ae6573b2d6); sources: [[DME-SRC-PPEF-Q1-2026]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-816dc59b9c0705d5592f); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-PPEF-Q3-2026]] — documented_fact (edge-94c0c9db29f1abf33754); sources: [[DME-SRC-PPEF-Q3-2026]]
- cites: [[DME-SRC-PPEF-Q4-2026]] — documented_fact (edge-d71d8c7b399264116e63); sources: [[DME-SRC-PPEF-Q4-2026]]
- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-ef0dae9699a2fc6611b0); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-PPEF-ADDITIONAL]] — documented_fact (edge-ef8ca8a929ec0186e2bc); sources: [[DME-SRC-PPEF-ADDITIONAL]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-f74cf60d0a54852951d5); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PPEF-METHOD]] — documented_fact (edge-fad62d08ab0037aa444d); sources: [[DME-SRC-PPEF-METHOD]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — unknown (DME-E-de3079eee313429ee79a)
