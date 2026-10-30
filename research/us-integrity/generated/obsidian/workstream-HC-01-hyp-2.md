---
id: "workstream-HC-01-hyp-2"
type: "hypothesis"
title: "Provider appears on exclusion data and billing aggregates"
status: "hypothesis"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Provider appears on exclusion data and billing aggregates

Evidence status: **hypothesis**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "alternatives": [
    "same-name different person",
    "reinstatement",
    "service dates predate exclusion",
    "payment adjustment after permitted service"
  ],
  "needed": "Exact identity, exclusion effective/reinstatement dates and actual dates of service; annual aggregates alone cannot prove prohibited billing.",
  "signal": "Provider appears on exclusion data and billing aggregates",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S05]]
- [[src-HC-S06]]
- [[src-HC-S17]]
- [[src-HC-S18]]

## Outgoing relationships

- cites: [[src-HC-S06]] — documented_fact (edge-5aeaea30f8070e2e7ed8); sources: [[src-HC-S06]]
- cites: [[src-HC-S18]] — documented_fact (edge-a1dc4c090039218eb036); sources: [[src-HC-S18]]
- cites: [[src-HC-S17]] — documented_fact (edge-a8181ee2b5e1e62bf7bf); sources: [[src-HC-S17]]
- cites: [[src-HC-S05]] — documented_fact (edge-c49782a9804073ef7f4a); sources: [[src-HC-S05]]

## Backlinks

- [[workstream-HC-01]]: has_research_hypothesis — planned (edge-db8e4c5fa30a72e72431)
