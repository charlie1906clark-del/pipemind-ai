---
id: "BOLT-PC-T01"
type: "audit_protocol"
title: "Exact technical and commercial qualification"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Exact technical and commercial qualification

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "current_status": "blocked; complete primary NSN product specification and compliant independent quote missing",
    "id": "PC-T01",
    "inputs": [
      "product",
      "commercial_terms",
      "benchmark"
    ],
    "name": "Exact technical and commercial qualification",
    "output": "qualified / unresolved / rejected, with field-level reasons",
    "test": "For every hard-required field compare source-supported values. Unknown is unresolved, explicit conflict is rejected. A technical difference requires a documented adjustment or separate non-comparable cohort."
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

- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-0de1fecfc9b07c7a6ed8); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-507e3daaa96c7973615a); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-57304f1d2d57bfa29b40); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-b523f1d8a811cb9e4820); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-b783164395301a2e48ef); sources: [[BOLT-PC-METHOD-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-65b102723c7e3c6314f0)
