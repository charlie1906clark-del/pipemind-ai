---
id: "workstream-HC-01"
type: "workstream"
title: "Original Medicare Part B and medical practice billing"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Original Medicare Part B and medical practice billing

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Claims-methodology auditor: reject invalid cohorts, enforce amount semantics and flag only reproducible aggregate anomalies.",
  "blind_spots": [
    "No patient-level identity or clinical record in public aggregates.",
    "Part B FFS is not the full US health market.",
    "Annual aggregates cannot establish impossible daily workloads, forged signatures or deliberate misrepresentation."
  ],
  "buyer_vs_payee": "The federal payer reimburses care; the patient is not the federal procurement buyer. Rendering and billing identities can differ.",
  "funds_path": [
    "CMS Medicare trust funds",
    "Medicare Administrative Contractor",
    "enrolled billing practitioner/group",
    "rendering practitioner or downstream laboratory/supplier"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "practice acquisition",
        "new specialist service",
        "coding or fee-schedule changes",
        "demand/case-mix shift"
      ],
      "needed": "Prior-year records, dictionary comparability, paid-vs-submitted amount, enrollment history and a validated peer cohort.",
      "signal": "Abrupt rise in units or paid amount for a narrow HCPCS family"
    },
    {
      "alternatives": [
        "same-name different person",
        "reinstatement",
        "service dates predate exclusion",
        "payment adjustment after permitted service"
      ],
      "needed": "Exact identity, exclusion effective/reinstatement dates and actual dates of service; annual aggregates alone cannot prove prohibited billing.",
      "signal": "Provider appears on exclusion data and billing aggregates"
    }
  ],
  "join_plan": [
    "Retain NPI as a ten-character string and validate check digit. Keep Type 1 individual and Type 2 organization separate.",
    "Join NPI to the same observation-period NPPES snapshot; retain taxonomy and professional practice state.",
    "Compare by HCPCS, place of service, specialty, calendar year, regional payment conditions and available risk/case-mix proxies.",
    "Resolve group ownership through explicit enrollment/registry evidence; never infer ownership from a shared practice address."
  ],
  "priority": "high_public_data_feasibility",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S05]]
- [[src-HC-S06]]
- [[src-HC-S17]]
- [[src-HC-S18]]

## Outgoing relationships

- cites: [[src-HC-S06]] — documented_fact (edge-44550ae19443425f7080); sources: [[src-HC-S06]]
- cites: [[src-HC-S18]] — documented_fact (edge-4d7c019245c113dd3f04); sources: [[src-HC-S18]]
- has_research_hypothesis: [[workstream-HC-01-hyp-1]] — planned (edge-a7516f9153398729f4e1); sources: 
- cites: [[src-HC-S05]] — documented_fact (edge-abece8b9f2f157de814b); sources: [[src-HC-S05]]
- cites: [[src-HC-S17]] — documented_fact (edge-d48b4158f6dee38cb835); sources: [[src-HC-S17]]
- has_research_hypothesis: [[workstream-HC-01-hyp-2]] — planned (edge-db8e4c5fa30a72e72431); sources: 

## Backlinks

None recorded.
