---
id: "BOLT-PC-T02"
type: "audit_protocol"
title: "Amount-weighted premium"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Amount-weighted premium

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "guard": "Do not average percentages equally or drop negative differences; no mixed ordered/invoiced/paid rows.",
    "id": "PC-T02",
    "inputs": [
      "eligible row quantity q",
      "actual comparable unit price p",
      "adjusted benchmark b"
    ],
    "name": "Amount-weighted premium",
    "output": "signed excess, positive-only difference separately, baseline-weighted percentage, amount coverage and uncertainty interval",
    "test": "For a single declared amount basis, compute E=sum(q*(p-b)), B=sum(q*b), A=sum(q*p); weighted_markup=E/B and excess_share_of_gross=E/A. Require B>0, A>0, finite numbers and common currency."
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

- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-16393c10eed2ade7f20d); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-553a51574c9c075f225b); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-6922e4673370d418e046); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-c43ed63ebda787ac63e9); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-cc7b8200204c9d993cf2); sources: [[BOLT-PC-MECH-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-3e4fa97e8d2bec26d7ba)
