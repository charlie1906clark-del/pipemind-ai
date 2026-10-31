---
id: "BOLT-PC-T08"
type: "audit_protocol"
title: "Alternative and sensitivity review"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Alternative and sensitivity review

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "id": "PC-T08",
    "inputs": [
      "all accepted and excluded benchmarks",
      "selection rules",
      "supplier response if already in public record"
    ],
    "name": "Alternative and sensitivity review",
    "output": "accept / narrow / reject / unresolved independently signed",
    "test": "Try to invalidate the apparent premium using pack rounding, full-order cost, compliant certifications, delivery capacity, freight, returns, credit terms, warranty, quantity discounts and timestamp alignment; document why each survives or fails."
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

- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-2a8c38fbf71f31116e7f); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-3622e5500a3f2482d9af); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-86edf0c5f4a2b993122e); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-95d09db99eb84af9f2b9); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-e634705eb8721f4d18cd); sources: [[BOLT-PC-MECH-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-f1b0fc0e17b4a865f619)
