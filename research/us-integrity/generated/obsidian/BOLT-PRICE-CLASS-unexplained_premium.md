---
id: "BOLT-PRICE-CLASS-unexplained_premium"
type: "audit_classification_definition"
title: "Unexplained premium"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Unexplained premium

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "applied_to_current_cohort": false,
  "definition": {
    "id": "unexplained_premium",
    "meaning": "A reproducible price difference remains after declared comparability controls and plausible alternatives are tested.",
    "not_implied": "It is a request for further explanation, not established loss or corruption.",
    "required": "Qualified benchmark and uncertainty range, source-level coverage and independent challenge."
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

- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-0abf883d9697548898fe); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-21d129601e8a5460e3ac); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-2ea096a614db59b2eec6); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-46c54d87c7e20abe5a34); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-785c846e73858b43d8fb); sources: [[BOLT-PC-MECH-S01]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: defines_finding_class — planned (BOLT-E-165d588fcb7e3dfbf7cd)
