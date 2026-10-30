---
id: "BOLT-ORDER-SPE4A627F0588"
type: "order_observation"
title: "SPE4A627F0588: 906 EA ordered at USD 0.91 each"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A627F0588: 906 EA ordered at USD 0.91 each

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "archived_scope": "Selected neutral page 2; full PDF is not in the public repository",
  "money_aggregation_permitted": false,
  "observation": {
    "acceptance": "DESTINATION",
    "all_orders_under_parent_acquired": false,
    "arithmetic": {
      "equals_order_line_total": true,
      "expression": "906.000 * 0.9100",
      "result": "824.4600000"
    },
    "basic_reference_clin": "0001",
    "clin": "0001",
    "contract": "SPE4A627F0588",
    "contractor_cage": "8A1E8",
    "currency": "USD",
    "currency_basis": "DOLLAR VALUE heading and linked parent CLIN explicit USD",
    "delivery_date": "2027-01-04",
    "delivery_verified": false,
    "fob": "ORIGIN",
    "fob_payment_method": "GOVERNMENT",
    "inspection": "DESTINATION",
    "measure": "ordered_line_value_not_verified_payment",
    "order_date": "2026-10-19",
    "order_line_total": "824.46",
    "parent_contract": "SPE4A626D61WS",
    "payment_verified": false,
    "quantity": "906.000",
    "receipt_or_acceptance_verified": false,
    "reported_business_name": "KAREN CARLISLE",
    "source_id": "BOLT-CUR-S02",
    "source_pages": [
      1,
      2
    ],
    "unit_of_issue": "EA",
    "unit_price": "0.9100"
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]

## Outgoing relationships

- source_reports_contractor: [[BOLT-SUPPLIER-8A1E8]] — documented_fact (BOLT-E-41086893fa2f5516dcdc); sources: [[BOLT-CUR-S02]]
- reports_ordered_value: [[BOLT-ORDERED-LINE-VALUE]] — documented_fact (BOLT-E-ac8bad080f05fced1436); sources: [[BOLT-CUR-S02]]
- orders_item: [[DISC-NSN-5306016864912]] — documented_fact (BOLT-E-ce41268a5b7e7a02ba06); sources: [[BOLT-CUR-S02]]
- reports_unit_price: [[BOLT-CURRENT-UNIT-PRICE]] — documented_fact (BOLT-E-ce891f6c48b0c668b5dc); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]]
- issued_under: [[BOLT-PARENT-SPE4A626D61WS]] — documented_fact (BOLT-E-e51014a51c0db5a26517); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-0c4c51c407e22ed00662); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-8555e88079a1b2e31457); sources: [[BOLT-CUR-S02]]

## Backlinks

- [[BOLT-PRICE-ACTUAL-BLOCKED]]: evaluates_ordered_line — documented_fact (BOLT-E-c44e23f022fb915dcceb)
