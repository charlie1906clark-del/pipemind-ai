---
id: "BOLT-PC-T05"
type: "audit_protocol"
title: "Independent competition challenge"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Independent competition challenge

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "guard": "An offers-received number, distinct legal names or different unit prices does not establish independence. A shared manufacturer does not establish collusion.",
    "id": "PC-T05",
    "inputs": [
      "all actual bids",
      "bidder identity as of bid date",
      "bid metadata",
      "evaluation and withdrawals"
    ],
    "name": "Independent competition challenge",
    "output": "documented pattern with alternatives and missing fields",
    "test": "Reconstruct submitted prices, technical acceptability, timestamps and spread. Review common errors, author metadata, bid rotation, withdrawals and losing-bidder subcontracts against neutral templates, shared upstream supply, specialization and capacity."
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

- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-069b081a26eca2ecf7ef); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-77125f2bbf9f94b97f89); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-95b3a7bbbfd43d200312); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-ac031c277c00d08c8736); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-dea82610971509dd8921); sources: [[BOLT-PC-METHOD-S03]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-80132cf00a7a2d5058ec)
