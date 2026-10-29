---
id: "workstream-HC-07"
type: "workstream"
title: "Hospice, home health and skilled nursing ownership networks"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Hospice, home health and skilled nursing ownership networks

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Post-acute ownership and eligibility auditor: version every ownership edge and require authorized clinical evidence before eligibility conclusions.",
  "blind_spots": [
    "Current ownership snapshot can misrepresent the historical owner.",
    "Self-reported ownership may be incomplete or late.",
    "Public service aggregates cannot establish terminal prognosis, homebound status, forged signatures or actual staff attendance.",
    "Enhanced-oversight states are control jurisdictions, not a list of culpable providers."
  ],
  "buyer_vs_payee": "Patient referral, agency enrollment, facility operation and real-estate ownership are separate relations.",
  "funds_path": [
    "CMS Part A / Medicaid / other programme",
    "enrolled facility or home-care agency",
    "staffing/management company",
    "parent/chain/investor"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "legitimate chain acquisition",
        "corporate restructuring",
        "expansion to meet demand"
      ],
      "needed": "Snapshots/filings, provider operational dates, payment/quality denominators and explicit acquisition evidence.",
      "signal": "Rapid facility enrollment or ownership turnover and unusual service patterns"
    },
    {
      "alternatives": [
        "unrelated condition or permitted separate benefit",
        "adjustment timing"
      ],
      "needed": "Patient/service-level records and hospice coverage rules; aggregate overlap alone is not duplicate billing.",
      "signal": "Hospice and separate provider payments may overlap"
    }
  ],
  "join_plan": [
    "Use ENROLLMENT ID and ASSOCIATE ID to join PECOS ownership rows to the matching enrollment dataset; obtain NPI/CCN from that supported crosswalk.",
    "Keep owner ASSOCIATE ID distinct from provider ASSOCIATE ID and NPI.",
    "Represent ownership percentage, role, association date and snapshot date; sum percentages only where ownership layer and definitions permit.",
    "Recurse through evidenced organization owners; a self-reported intermediate owner is not proven ultimate beneficial ownership."
  ],
  "priority": "high",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S07]]
- [[src-HC-S08]]
- [[src-HC-S09]]
- [[src-HC-S10]]
- [[src-HC-S20]]
- [[src-HC-S21]]
- [[src-HC-S27]]
- [[src-HC-S28]]

## Outgoing relationships

- cites: [[src-HC-S21]] — documented_fact (edge-179de361455c35bfbd1d); sources: [[src-HC-S21]]
- cites: [[src-HC-S07]] — documented_fact (edge-3f45ece6a20065d14274); sources: [[src-HC-S07]]
- cites: [[src-HC-S20]] — documented_fact (edge-444adabc5ef4bf015a2b); sources: [[src-HC-S20]]
- cites: [[src-HC-S10]] — documented_fact (edge-4a158ca4563e6f9ffb38); sources: [[src-HC-S10]]
- cites: [[src-HC-S09]] — documented_fact (edge-675873aedfbf94c1f52d); sources: [[src-HC-S09]]
- has_research_hypothesis: [[workstream-HC-07-hyp-1]] — planned (edge-7904c90e45ff5caf4390); sources: 
- cites: [[src-HC-S08]] — documented_fact (edge-c3c9b925fe3cbdb3c66a); sources: [[src-HC-S08]]
- cites: [[src-HC-S27]] — documented_fact (edge-d7c1cc5a2236da160e65); sources: [[src-HC-S27]]
- cites: [[src-HC-S28]] — documented_fact (edge-eb420ece9d6bc1b3e871); sources: [[src-HC-S28]]
- has_research_hypothesis: [[workstream-HC-07-hyp-2]] — planned (edge-eccfd45c79bfbe6309f3); sources: 

## Backlinks

None recorded.
