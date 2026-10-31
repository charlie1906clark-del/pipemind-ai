---
id: "BOLT-PC-R06"
type: "research_question"
title: "Receipts, acceptance, invoices, credits/returns and corresponding disbursement records"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Receipts, acceptance, invoices, credits/returns and corresponding disbursement records

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "acquisition_requirement": {
    "availability": "Not in supplied order or summary obligation data; detailed agency systems generally require authorized access or releases",
    "current": "Future delivery due on current order; payment not verified",
    "id": "PC-R06",
    "next_action": "No payment/annualization inference pending source records.",
    "priority": 6,
    "reason": "Separates ordered amount from net amount actually paid",
    "record": "Receipts, acceptance, invoices, credits/returns and corresponding disbursement records"
  },
  "requested_or_obtained_by_this_node": false,
  "visibility": "public"
}
```

## Sources

- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]

## Outgoing relationships

- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-7a4d5df58ee80283c27e); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-820158b2e10312a1b14e); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-ae37eba36da74dec5a20); sources: [[BOLT-PC-METHOD-S02]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: requires_evidence — planned (BOLT-E-4f03d8dc2563136e3119)
