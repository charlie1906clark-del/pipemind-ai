---
id: "BOLT-CURRENT-UNIT-PRICE"
type: "money_measure"
title: "Executed parent and order price: USD 0.91 per EA"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Executed parent and order price: USD 0.91 per EA

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "aggregation_permitted": false,
  "independently_verified_collection": false,
  "money": {
    "amount": "0.9100",
    "basis": "Explicit source-reported measure",
    "currency": "USD",
    "kind": "contract_unit_price",
    "period": "2026-09-17 to 2026-10-19",
    "qualifier": "as_reported"
  },
  "no_historical_unit_inference": true,
  "unit_of_issue": "EA",
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]

## Outgoing relationships

- cites: [[BOLT-CUR-S01]] — documented_fact (edge-45f9cb578f8f97d729ca); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-c93519b3a913accfeb96); sources: [[BOLT-CUR-S02]]

## Backlinks

- [[BOLT-PARENT-SPE4A626D61WS]]: reports_unit_price — documented_fact (BOLT-E-22c62a7b052cfc753ae5)
- [[BOLT-BREV-F04]]: assesses_evidence — documented_fact (BOLT-E-7e13f06cf380a7506331)
- [[BOLT-ORDER-SPE4A627F0588]]: reports_unit_price — documented_fact (BOLT-E-ce891f6c48b0c668b5dc)
