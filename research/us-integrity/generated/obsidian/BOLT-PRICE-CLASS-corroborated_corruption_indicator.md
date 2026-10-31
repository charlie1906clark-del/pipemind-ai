---
id: "BOLT-PRICE-CLASS-corroborated_corruption_indicator"
type: "audit_classification_definition"
title: "Corroborated corruption indicator"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Corroborated corruption indicator

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "applied_to_current_cohort": false,
  "definition": {
    "id": "corroborated_corruption_indicator",
    "meaning": "A documented procurement decision is linked to evidence of improper influence or benefit, with provenance and ordinary alternatives reviewed.",
    "not_implied": "A screening analyst does not turn the indicator into a legal finding.",
    "required": "Role/timing evidence, actual communication/benefit evidence and nexus to the procurement."
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

- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-6a6259bdf23c1fd2abee); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-8b13856d63f0f528efc2); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-af11b4ee2d167e9ca129); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-cb0296e38da78a66ee8d); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-dbe914bbabc2918db7e9); sources: [[BOLT-PC-METHOD-S02]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: defines_finding_class — planned (BOLT-E-77ccb09c9d85db197520)
