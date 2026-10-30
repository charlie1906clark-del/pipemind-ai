---
id: "BOLT-PARENT-SPE4A626D61WS"
type: "contract_observation"
title: "SPE4A626D61WS: parent contract terms"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626D61WS: parent contract terms

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "archived_scope": "Selected neutral pages 2 and 5; full PDF is not in the public repository",
  "money_aggregation_permitted": false,
  "observation": {
    "acceptance": "DESTINATION",
    "award_date": "2026-09-17",
    "base_line_quantity_as_printed": "0.000",
    "base_line_quantity_is_purchased_quantity": false,
    "clin": "0001",
    "contract": "SPE4A626D61WS",
    "contract_ceiling": "350000.00",
    "contractor_cage": "8A1E8",
    "currency": "USD",
    "delivery_days": "76",
    "estimate_is_order": false,
    "estimated_annual_quantity": "2221.000",
    "guaranteed_minimum_condition": "Unilateral IDC becomes binding after an order and acceptable performance; completion not verified",
    "guaranteed_minimum_quantity": "222",
    "inspection": "DESTINATION",
    "minimum_delivery_order_quantity": "1",
    "payment_verified": false,
    "quantity_per_unit_pack": "001",
    "reported_business_name": "KAREN CARLISLE",
    "source_id": "BOLT-CUR-S01",
    "source_pages": [
      1,
      2,
      5
    ],
    "technical_reference": "TDP Rev A Gen 1; IAW BASIC NON GOVT STD ASMEB18.24 dated10/16/2023",
    "unit_of_issue": "EA",
    "unit_price": "0.91000"
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]

## Outgoing relationships

- reports_unit_price: [[BOLT-CURRENT-UNIT-PRICE]] — documented_fact (BOLT-E-22c62a7b052cfc753ae5); sources: [[BOLT-CUR-S01]]
- reports_ceiling: [[BOLT-PARENT-CEILING]] — documented_fact (BOLT-E-3e63becb8b25f08cc521); sources: [[BOLT-CUR-S01]]
- source_reports_contractor: [[BOLT-SUPPLIER-8A1E8]] — documented_fact (BOLT-E-44903394f6e23532ef71); sources: [[BOLT-CUR-S01]]
- orders_item: [[DISC-NSN-5306016864912]] — documented_fact (BOLT-E-71e4b9bf03f67c9dc87e); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-d69495f9add117455920); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-BREV-F05]]: assesses_evidence — documented_fact (BOLT-E-1c62b9a652adde30e54f)
- [[BOLT-TRACE-20261030]]: includes_current_contract — documented_fact (BOLT-E-323a540e25e09ab3c6c3)
- [[BOLT-ORDER-SPE4A627F0588]]: issued_under — documented_fact (BOLT-E-e51014a51c0db5a26517)
