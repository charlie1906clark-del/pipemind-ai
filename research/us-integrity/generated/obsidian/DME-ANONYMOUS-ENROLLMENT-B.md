---
id: "DME-ANONYMOUS-ENROLLMENT-B"
type: "finding"
title: "Candidate B: unresolved enrollment-scope follow-up"
status: "unknown"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Candidate B: unresolved enrollment-scope follow-up

Evidence status: **unknown**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "bounded_observation": {
    "appeal_disposition": null,
    "approved_enrollment_distinct_from_revoked_enrollment": null,
    "approved_enrollment_scope": null,
    "conclusive_published_enforcement_match": null,
    "historical_2024_enrollment_status": null,
    "interpretation": "No exact hit in the three primary enrollment snapshots or latest companion file. This neither establishes 2024 status nor proves improper billing; retrospective action, different enrollment and correction histories remain untested.",
    "label": "Candidate B",
    "primary_npi_rows_Q1_Q3_Q4": [
      0,
      0,
      0
    ],
    "q4_additional_npi_rows": 0,
    "released_claim_cash_after_revocation": null,
    "revocation_notice_date": null,
    "revoked_scope": "DME SUPPLIER - MEDICAL SUPPLY COMPANY"
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

- cites: [[DME-SRC-PPEF-ADDITIONAL]] — documented_fact (edge-1b0838b0fdb50c8b71dd); sources: [[DME-SRC-PPEF-ADDITIONAL]]
- cites: [[DME-SRC-PPEF-METHOD]] — documented_fact (edge-28891dcac463d12a45e7); sources: [[DME-SRC-PPEF-METHOD]]
- cites: [[DME-SRC-REVOCATIONS-Q3-2026]] — documented_fact (edge-5af90af5034d504d13a4); sources: [[DME-SRC-REVOCATIONS-Q3-2026]]
- cites: [[DME-SRC-PPEF-Q1-2026]] — documented_fact (edge-7142464f531599cef8b7); sources: [[DME-SRC-PPEF-Q1-2026]]
- cites: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]] — documented_fact (edge-8bb0835d590163e5ee27); sources: [[DME-SRC-REVOCATIONS-ADDITIONAL-NPIS]]
- cites: [[DME-SRC-ENROLLMENT-cms-methodology]] — documented_fact (edge-9b7c9d01602cb7e258b4); sources: [[DME-SRC-ENROLLMENT-cms-methodology]]
- cites: [[DME-SRC-PPEF-Q3-2026]] — documented_fact (edge-a18348f335da44ed91b2); sources: [[DME-SRC-PPEF-Q3-2026]]
- cites: [[DME-SRC-PPEF-Q4-2026]] — documented_fact (edge-ddff097a46e06ff298c6); sources: [[DME-SRC-PPEF-Q4-2026]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — unknown (DME-E-034af5579dc6b655bca4)
