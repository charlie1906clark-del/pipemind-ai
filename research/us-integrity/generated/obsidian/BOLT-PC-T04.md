---
id: "BOLT-PC-T04"
type: "audit_protocol"
title: "Mix, quantity and time control"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Mix, quantity and time control

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "guard": "Do not impose a generic inflation series or assume retail availability at a government delivery date. No regression on eight incomparable records.",
    "id": "PC-T04",
    "inputs": [
      "exact SKU/revision strata",
      "quantity tiers",
      "quote dates",
      "freight and delivery",
      "benchmark provenance"
    ],
    "name": "Mix, quantity and time control",
    "output": "within-stratum premium versus composition effect",
    "test": "Compare within the same item/specification and feasible quantity tier. Construct a fixed-basket comparison using baseline quantities. Match time windows or document an item-relevant dated adjustment; run no-adjustment and bounded-adjustment sensitivity. Report how product mix and urgent delivery change the result."
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-PC-MECH-S01]]
- [[BOLT-PC-MECH-S02]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]

## Outgoing relationships

- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-18352edbd53d85360ef0); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-37b120bf2b22f4b3d1d8); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-545a35dfb9a269f13a44); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-a3ef393782b513b24351); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-e163f1627aaa5f911a9a); sources: [[BOLT-PC-MECH-S02]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-237740da95bd21818d4d)
