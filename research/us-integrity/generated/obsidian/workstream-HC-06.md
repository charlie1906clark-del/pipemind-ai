---
id: "workstream-HC-06"
type: "workstream"
title: "Telehealth, lead generation and remote prescribing"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Telehealth, lead generation and remote prescribing

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Telehealth rule and consent-evidence auditor: distinguish legal remote care from source-supported conduct; block unsupported consent conclusions.",
  "blind_spots": [
    "Call recordings, patient consent, identity theft and AI-generated consent records are not available in public spending tables.",
    "No scraping patient/social accounts or trying to impersonate beneficiaries."
  ],
  "buyer_vs_payee": "The platform can be a vendor, a clinical group or a billing entity; never assume these roles are interchangeable.",
  "funds_path": [
    "Medicare/Medicaid or plan",
    "billed practitioner/lab/DME supplier",
    "telehealth platform",
    "marketing/lead generation vendor",
    "owners/management"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "lawful remote care programme",
        "centralized specialty service",
        "changes to coverage"
      ],
      "needed": "Validated ordering linkage, encounter evidence and consent documentation; marginal aggregates cannot prove a path.",
      "signal": "DME/lab billing growth accompanies remote ordering concentration"
    },
    {
      "alternatives": [
        "group NPI/many clinicians",
        "seasonal volume",
        "acquisition"
      ],
      "needed": "Role-correct numerator, denominator and clinician capacity evidence.",
      "signal": "Unusual volume associated with a new telehealth group"
    }
  ],
  "join_plan": [
    "Preserve practitioner NPI, platform legal entity, billed supplier and marketer as distinct nodes.",
    "Use only explicit contracts/case records to connect lead seller and provider.",
    "Version telehealth place-of-service/payment rules and distinguish authorized telehealth expansion from misconduct."
  ],
  "priority": "high_typology_low_transaction_visibility",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S01]]
- [[src-HC-S02]]
- [[src-HC-S06]]
- [[src-HC-S18]]

## Outgoing relationships

- has_research_hypothesis: [[workstream-HC-06-hyp-1]] — planned (edge-1f9e56100e5c625e830c); sources: 
- cites: [[src-HC-S06]] — documented_fact (edge-43a06487c5d1643bf509); sources: [[src-HC-S06]]
- cites: [[src-HC-S01]] — documented_fact (edge-58ef9a605b9ca672bdab); sources: [[src-HC-S01]]
- cites: [[src-HC-S18]] — documented_fact (edge-9e9c65d64fc929e93474); sources: [[src-HC-S18]]
- cites: [[src-HC-S02]] — documented_fact (edge-b5895aefa3c89ed414e4); sources: [[src-HC-S02]]
- has_research_hypothesis: [[workstream-HC-06-hyp-2]] — planned (edge-d24230711291352f8dde); sources: 

## Backlinks

None recorded.
