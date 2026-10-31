---
id: "BOLT-PRICE-CLASS-ordinary_margin"
type: "audit_classification_definition"
title: "Ordinary margin"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Ordinary margin

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "applied_to_current_cohort": false,
  "definition": {
    "id": "ordinary_margin",
    "meaning": "A distributor's sales price exceeds its acquisition cost; services, costs, risk and competition may explain the difference.",
    "not_implied": "A markup is neither automatically excessive nor a buyer kickback.",
    "required": "Documented acquisition cost plus relevant cost/service and sale terms if making a margin claim."
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

- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-7c1679d1b9210881be85); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-97afb2cda2e523ae9cd2); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-d0d83fe292b7290af183); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-d52325e5a24a24e7ae7e); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-dcd7a79491303bd735cd); sources: [[BOLT-PC-MECH-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: defines_finding_class — planned (BOLT-E-f30a86e647c15b0c2d3f)
