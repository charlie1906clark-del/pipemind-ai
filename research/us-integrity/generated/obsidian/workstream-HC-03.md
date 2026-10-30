---
id: "workstream-HC-03"
type: "workstream"
title: "Medicaid/CHIP, managed care, behavioural health and home/community services"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Medicaid/CHIP, managed care, behavioural health and home/community services

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Medicaid state-policy auditor: condition every rule on state, year, programme and payment method; route missing definitions to blocked-data status.",
  "blind_spots": [
    "T-MSIS is state-submitted and has completeness/comparability limitations.",
    "Suppression prevents reconstructing small cells.",
    "No patient identities; do not attempt reidentification or deceased-beneficiary joins.",
    "Managed-care subcontract and staffing contracts may be unavailable."
  ],
  "buyer_vs_payee": "State expenditure, MCO capitation, provider reimbursement and managed-care encounter value are different measures and must not be summed as independent spending.",
  "funds_path": [
    "Federal/state Medicaid funds",
    "state Medicaid agency",
    "FFS provider OR capitated managed-care organization",
    "billing/servicing provider",
    "staffing or other subcontractor"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "expanded state eligibility",
        "rate increase",
        "new covered benefit",
        "backlogged submissions",
        "MCO reporting changes"
      ],
      "needed": "State benefit/rate chronology, claim revisions, enrollment spans, code dictionaries and comparable states/regions.",
      "signal": "Rapid provider-month growth in behavioural health or personal-care units"
    },
    {
      "alternatives": [
        "group NPI billing many staff",
        "unit duration differs",
        "institutional bundled payments"
      ],
      "needed": "Provider role, unit semantics, staffing evidence and appropriately authorized service records; public aggregate totals cannot prove impossible individual hours.",
      "signal": "Same provider has apparent high hours per month"
    }
  ],
  "join_plan": [
    "Retrieve HHS HCPCS, NDC and enrollment extracts, schema, suppression and revision documentation before querying.",
    "Preserve billing NPI, servicing NPI and prescribing NPI as distinct roles. Add state, month and code-system version where fields support it.",
    "Validate cross-state/method comparability and managed-care encounter amount definitions; do not assume an encounter paid amount equals a state payment.",
    "Join provider enrollment segments temporally, keeping state-specific enrollment identifiers and spans."
  ],
  "priority": "first_pilot_after_schema_verification",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S11]]
- [[src-HC-S12]]
- [[src-HC-S13]]
- [[src-HC-S17]]
- [[src-HC-S29]]

## Outgoing relationships

- cites: [[src-HC-S11]] — documented_fact (edge-3fe1a00d0843cc4ff6af); sources: [[src-HC-S11]]
- has_research_hypothesis: [[workstream-HC-03-hyp-2]] — planned (edge-419f927fc6e5b45b7ec2); sources: 
- has_research_hypothesis: [[workstream-HC-03-hyp-1]] — planned (edge-47bd78cd964b5d588ae1); sources: 
- cites: [[src-HC-S17]] — documented_fact (edge-8a0e4f4c1d3a613e2d86); sources: [[src-HC-S17]]
- cites: [[src-HC-S29]] — documented_fact (edge-a67f46d04fc8aee07ed5); sources: [[src-HC-S29]]
- cites: [[src-HC-S12]] — documented_fact (edge-d90d700990a211f80441); sources: [[src-HC-S12]]
- cites: [[src-HC-S13]] — documented_fact (edge-e3ddf3980269d42a5d5a); sources: [[src-HC-S13]]

## Backlinks

None recorded.
