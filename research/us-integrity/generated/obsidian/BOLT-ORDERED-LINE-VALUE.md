---
id: "BOLT-ORDERED-LINE-VALUE"
type: "money_measure"
title: "Order CLIN 0001: USD 824.46 ordered value"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Order CLIN 0001: USD 824.46 ordered value

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "aggregation_permitted": false,
  "independently_verified_collection": false,
  "money": {
    "amount": "824.46",
    "basis": "Explicit source-reported measure",
    "currency": "USD",
    "kind": "ordered_line_value",
    "period": "2026-10-19",
    "qualifier": "as_reported"
  },
  "no_payment_or_loss_inference": true,
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]

## Outgoing relationships

- cites: [[BOLT-CUR-S02]] — documented_fact (edge-92fec155fff6a7fcb7b6); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-c3972d70ed61bf593c80); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-ORDER-SPE4A627F0588]]: reports_ordered_value — documented_fact (BOLT-E-ac8bad080f05fced1436)
