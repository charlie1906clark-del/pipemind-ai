---
id: "workstream-HC-09"
type: "workstream"
title: "VA community care, prosthetics and medical procurement"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# VA community care, prosthetics and medical procurement

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "VA contract-rate auditor: reconstruct the contract/rate hierarchy and challenge false fraud labels for permitted terms.",
  "blind_spots": [
    "Patient-level VA claims and commercial upstream invoices usually restricted.",
    "Questioned costs and recommendations for better use of funds are not recoveries.",
    "2025 audit found most outpatient payments accurate; selecting only negative findings would distort evidence."
  ],
  "buyer_vs_payee": "CCN claim reimbursement and a VA purchase order are different procurement/payment paths. Contract-compliant margins can be a policy weakness without being fraud.",
  "funds_path": [
    "VA/VHA",
    "third-party administrator OR direct procurement vendor",
    "community care provider / distributor",
    "medical-device manufacturer / corporate parent"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "contract expressly permits rate-based reimbursement",
        "administration fees",
        "different invoice scope"
      ],
      "needed": "Executed contract and modifications, governing fee schedule, invoice and payment reconciliation.",
      "signal": "VA reimbursement exceeds provider invoice"
    },
    {
      "alternatives": [
        "sterility/quality specification",
        "quantity",
        "freight",
        "emergency delivery",
        "warranty",
        "different unit"
      ],
      "needed": "Item/NSN/UDI if available, comparable terms, quantities and period; no price-only fraud conclusion.",
      "signal": "Medical procurement price above catalogue/reference price"
    }
  ],
  "join_plan": [
    "Identify CCN region, administrator contract, payment period and applicable rate hierarchy.",
    "Trace actual award identifiers via the procurement system separately from NPI-based community-provider records.",
    "Keep contract price, provider invoice and VA reimbursement measures separate; source the contract clause governing each."
  ],
  "priority": "high_for_contract_terms_medium_for_new_fraud",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S23]]

## Outgoing relationships

- cites: [[src-HC-S23]] — documented_fact (edge-0078b58ef5c5bdfad4c4); sources: [[src-HC-S23]]
- has_research_hypothesis: [[workstream-HC-09-hyp-2]] — planned (edge-9733e56ffd54fdd9afcd); sources: 
- has_research_hypothesis: [[workstream-HC-09-hyp-1]] — planned (edge-d24b714d7981ab10cf16); sources: 

## Backlinks

None recorded.
