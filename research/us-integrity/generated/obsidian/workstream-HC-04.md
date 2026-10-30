---
id: "workstream-HC-04"
type: "workstream"
title: "Pharmaceutical supply, Part D prescribing, PBMs and rebates"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Pharmaceutical supply, Part D prescribing, PBMs and rebates

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Drug-pricing and formulary auditor: normalize drug/packaging/payment measures and challenge gross-cost versus net-cost mistakes.",
  "blind_spots": [
    "Manufacturer rebates, PBM spread contracts and net prices often confidential.",
    "Part D prescriber tables do not identify every dispensing pharmacy transaction.",
    "FTC competition proceedings are not automatically criminal or FCA findings."
  ],
  "buyer_vs_payee": "Drug acquisition, dispensing reimbursement, prescribing and rebate flows are distinct. Public Part D drug cost is not net federal spending, pharmacy revenue or manufacturer realized price.",
  "funds_path": [
    "CMS Part D subsidies and other payer contributions",
    "Part D plan sponsor",
    "PBM and affiliated group purchasing organization",
    "dispensing pharmacy",
    "wholesaler",
    "manufacturer"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "specialty patient mix",
        "clinical contraindication",
        "formulary requirements",
        "different dosage/packaging",
        "gross-vs-net price differences"
      ],
      "needed": "Drug identity, days supply, specialty, formulary/year and rebate limitations.",
      "signal": "Very high brand share or spend per standardized fill in matched peers"
    },
    {
      "alternatives": [
        "lawful research",
        "consulting",
        "education",
        "common specialty manufacturer relationship"
      ],
      "needed": "Actual agreement, timing, services and a legally supported inducement theory. Correlation is insufficient.",
      "signal": "Payment relationship and unusual prescribing co-occur"
    }
  ],
  "join_plan": [
    "Use prescribing NPI + brand/generic drug + year for Part D; NDC-bearing Medicaid data has a different grain.",
    "Preserve NDC format and package/product meaning; do not coerce away leading zeros or infer drug equality from string similarity.",
    "Use explicit corporate evidence for PBM/plan/pharmacy/manufacturer ownership and effective dates.",
    "Open Payments linking needs the current file layout and validated recipient crosswalk; do not assume every release exposes NPI. Keep payments, research and ownership as separate relations."
  ],
  "priority": "medium_public_data_feasibility",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S13]]
- [[src-HC-S14]]
- [[src-HC-S15]]
- [[src-HC-S16]]
- [[src-HC-S30]]
- [[src-HC-S31]]

## Outgoing relationships

- has_research_hypothesis: [[workstream-HC-04-hyp-1]] — planned (edge-1c01339e8495fdf349cf); sources: 
- has_research_hypothesis: [[workstream-HC-04-hyp-2]] — planned (edge-52b52d5d7cd72935f673); sources: 
- cites: [[src-HC-S30]] — documented_fact (edge-81be79d7b6177f6270f6); sources: [[src-HC-S30]]
- cites: [[src-HC-S31]] — documented_fact (edge-b07b52bf073b21250279); sources: [[src-HC-S31]]
- cites: [[src-HC-S15]] — documented_fact (edge-b7cd48c0139a5d8b2a28); sources: [[src-HC-S15]]
- cites: [[src-HC-S16]] — documented_fact (edge-e2a23909adeb1cb75e78); sources: [[src-HC-S16]]
- cites: [[src-HC-S14]] — documented_fact (edge-f619495ca5736e43f5b8); sources: [[src-HC-S14]]
- cites: [[src-HC-S13]] — documented_fact (edge-fed8eee2f5991d1223b4); sources: [[src-HC-S13]]

## Backlinks

None recorded.
