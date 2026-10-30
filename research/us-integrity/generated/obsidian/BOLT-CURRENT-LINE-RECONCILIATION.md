---
id: "BOLT-CURRENT-LINE-RECONCILIATION"
type: "finding"
title: "The current ordered line reconciles: 906 EA × USD 0.91 = USD 824.46"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# The current ordered line reconciles: 906 EA × USD 0.91 = USD 824.46

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "all_orders_under_parent_acquired": false,
  "arithmetic": {
    "equals_order_line_total": true,
    "expression": "906.000 * 0.9100",
    "result": "824.4600000"
  },
  "delivery_verified": false,
  "parent_child_price_consistent": true,
  "payment_verified": false,
  "receipt_or_acceptance_verified": false,
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]

## Outgoing relationships

- cites: [[BOLT-CUR-S02]] — documented_fact (edge-2899dc2980af7e266be4); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-9e5c5aad2298a638c02e); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-2dc6954c9908874c0df1)
- [[BOLT-BREV-F03]]: assesses_evidence — documented_fact (BOLT-E-827e8cccbfefdb5e3ff8)
