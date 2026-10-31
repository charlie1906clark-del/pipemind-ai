---
id: "BOLT-PC-T06"
type: "audit_protocol"
title: "Buyer decision event study"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Buyer decision event study

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "guard": "An award signatory is not assumed to have selected the item, supplier or price. Staffing/capacity/mission changes are confounders.",
    "id": "PC-T06",
    "inputs": [
      "sourced decision roles and dates",
      "eligible office procurement universe",
      "same-item quotations",
      "supplier outcomes"
    ],
    "name": "Buyer decision event study",
    "output": "a decision pattern requiring explanation, not causation",
    "test": "Separate requisitioner, buyer, contracting officer, evaluator, inspector and disbursing official. Compare same-item/same-terms outcomes before and after role changes and against other offices where technically comparable. Report vendor win share, exclusion rationale, amendment timing and split/urgent buys with eligible denominators."
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

- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-1779e4a6492e51771df4); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-249988313dad15434546); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-aabb5539757602c084a7); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-cfab562b81b54d971be2); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-fade9b0e8486a489a8e4); sources: [[BOLT-PC-METHOD-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-1e304448fa02bd85863c)
