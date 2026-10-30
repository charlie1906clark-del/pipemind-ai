---
id: "BOLT-RFQ-TERM-CHANGES"
type: "finding"
title: "Minimum order quantity and delivery days changed between RFQ and parent award"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Minimum order quantity and delivery days changed between RFQ and parent award

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "inference_limit": "RFQ terms cannot automatically substitute for executed terms; no misconduct inference",
  "observation": {
    "delivery_days": {
      "award": "76",
      "rfq": "78"
    },
    "meaning": "Terms can change from request to award; original RFQ is not an automatic proxy for executed terms. No misconduct inferred.",
    "minimum_delivery_order_quantity": {
      "award": "1",
      "rfq": "555",
      "unit": "EA"
    },
    "reference_rfq": "SPE4A626U3619"
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- cites: [[BOLT-CUR-S01]] — documented_fact (edge-608f697085a6e088f8b8); sources: [[BOLT-CUR-S01]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-cad3b20afcc7b9580675); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Backlinks

- [[BOLT-BREV-F06]]: assesses_evidence — documented_fact (BOLT-E-55cfda6c8300880b7988)
- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-7a4f1309656caf8a7a1c)
