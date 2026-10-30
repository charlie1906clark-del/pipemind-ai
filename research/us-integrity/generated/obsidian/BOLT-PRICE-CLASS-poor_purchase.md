---
id: "BOLT-PRICE-CLASS-poor_purchase"
type: "audit_classification_definition"
title: "Poor purchase"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Poor purchase

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "applied_to_current_cohort": false,
  "definition": {
    "id": "poor_purchase",
    "meaning": "A feasible, equivalent, contemporaneous lower-cost option was reasonably available and not selected, with acquisition rationale evaluated.",
    "not_implied": "A cheaper catalog entry alone does not prove an avoidable overpayment or intent.",
    "required": "Qualified comparator, actual availability, selection terms and decision rationale."
  },
  "framework_origin": "Research classification, not an official finding",
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

- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-23d62e9abbb74d29076e); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-3a77ee68f3ec2ce10142); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-85f05425b09718a84a23); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-8dfda7a24ba7ee142e7c); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-974fa3f2d535b5290b91); sources: [[BOLT-PC-METHOD-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: defines_finding_class — planned (BOLT-E-4ca511e8b319da23e10d)
