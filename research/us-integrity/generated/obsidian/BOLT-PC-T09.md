---
id: "BOLT-PC-T09"
type: "audit_protocol"
title: "Amount and loss distinction"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Amount and loss distinction

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "id": "PC-T09",
    "inputs": [
      "price screen",
      "receipts",
      "invoices",
      "credits",
      "disbursements",
      "official loss methodology if any"
    ],
    "name": "Amount and loss distinction",
    "output": "basis-labeled amount with nulls for unsupported loss/payment/benefit",
    "test": "Report ordered comparison only from order documents. Upgrade to invoiced or paid comparison only with the corresponding records and adjustments. Separate benchmark-relative difference from an official recoverable loss finding."
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

- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-4eb00a67e7afad2ff7ff); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-677a71b9f1e9c6366593); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-b14f2967188e3b27340f); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-b716d8e8748f313dbe70); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-cfa59455c66e4b1abb5f); sources: [[BOLT-PC-METHOD-S02]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-725451f0dc468d5bbe98)
