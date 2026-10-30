---
id: "workstream-HC-02"
type: "workstream"
title: "DMEPOS, catheters, orthotics and medical supply distribution"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# DMEPOS, catheters, orthotics and medical supply distribution

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "DME coding and network auditor: compare product-specific longitudinal cohorts and distinguish NPI/provider enrollment changes from legal-entity ownership changes.",
  "blind_spots": [
    "Public aggregate data cannot establish delivery, beneficiary death, consent or medical necessity.",
    "Commercial supplier-to-wholesaler/manufacturer sales are usually not public.",
    "2026 suspected billing cannot be confirmed with a 2024 aggregate dataset."
  ],
  "buyer_vs_payee": "A billed supplier is not necessarily the manufacturer or federal contract vendor. Reimbursement does not expose its wholesale purchase invoice.",
  "funds_path": [
    "CMS FFS through MAC OR MA plan",
    "DMEPOS billing supplier",
    "commercial wholesaler/distributor",
    "device manufacturer"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "valid acquisition",
        "consolidated billing",
        "coding changes",
        "new service territory"
      ],
      "needed": "Longitudinal supplier rows, valid acquisition source, product mix, beneficiary-count denominator and payer-specific data.",
      "signal": "New or acquired supplier shows an extreme catheter billing increase relative to peers"
    },
    {
      "alternatives": [
        "legitimate chain",
        "shared billing service",
        "mailing office",
        "registered agent"
      ],
      "needed": "Explicit ownership/control records and distinct contemporaneous entities; cluster is a lead, not conspiracy proof.",
      "signal": "Several suppliers share an officer/address and similar billing shocks"
    }
  ],
  "join_plan": [
    "Use supplier NPI + HCPCS + rental indicator + service year as aggregate grain.",
    "Create separate records for referring-provider and supplier datasets. They are marginal aggregates; shared HCPCS does not establish a direct referrer-to-supplier transaction.",
    "Use NPI business identity and explicit corporate filings to trace registered entity/parents. Record each unsupported upstream manufacturer or beneficial-owner link as unknown.",
    "Version enrollment, deactivation, revocation and exclusion as different statuses with effective dates. A billing transition to another payer requires payer-specific data."
  ],
  "priority": "first_pilot",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S01]]
- [[src-HC-S02]]
- [[src-HC-S03]]
- [[src-HC-S04]]
- [[src-HC-S05]]
- [[src-HC-S06]]
- [[src-HC-S17]]

## Outgoing relationships

- has_research_hypothesis: [[workstream-HC-02-hyp-2]] — planned (edge-28bc5fedee5c2fd22358); sources: 
- cites: [[src-HC-S17]] — documented_fact (edge-470c0dc36ee6d29f7fa7); sources: [[src-HC-S17]]
- cites: [[src-HC-S05]] — documented_fact (edge-476e138837ad4a6f6059); sources: [[src-HC-S05]]
- cites: [[src-HC-S01]] — documented_fact (edge-9f161cebc6c4681ac7d2); sources: [[src-HC-S01]]
- cites: [[src-HC-S03]] — documented_fact (edge-a50fea53ecc55101af63); sources: [[src-HC-S03]]
- cites: [[src-HC-S06]] — documented_fact (edge-b9e9c2558d10bf2653f7); sources: [[src-HC-S06]]
- has_research_hypothesis: [[workstream-HC-02-hyp-1]] — planned (edge-bd3c69beba31948a7441); sources: 
- cites: [[src-HC-S04]] — documented_fact (edge-c42ace99cbdec99d03da); sources: [[src-HC-S04]]
- cites: [[src-HC-S02]] — documented_fact (edge-fdcb8bc7896858b16a30); sources: [[src-HC-S02]]

## Backlinks

None recorded.
