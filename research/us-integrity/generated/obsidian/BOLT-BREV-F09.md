---
id: "BOLT-BREV-F09"
type: "review_assessment"
title: "Empty current API searches do not prove a nonexistent award"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Empty current API searches do not prove a nonexistent award

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "evidence_limits": "A90-day delay is general portal guidance, not a verified cause of a particular empty result. HTTP503 remains failure, not zero results.",
  "locator": "Current query result and failure manifests; original documents",
  "new_named_adverse_allegation": false,
  "review_decision": "reject_inference",
  "review_input_paths": [
    "current/observations.json"
  ],
  "statement": "Original current award/order documents were acquired despite empty USAspending queries; official display-lag notice supplies a plausible timing explanation.",
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-SRC-BR-S08]]

## Outgoing relationships

- assesses_evidence: [[BOLT-PUBLICATION-LAG-LIMIT]] — documented_fact (BOLT-E-65798f7b30036f1c0f31); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-SRC-BR-S08]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-14ae098dbfb964ca8cd5); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-SRC-BR-S08]] — documented_fact (edge-3e081b824397c5b2df86); sources: [[BOLT-SRC-BR-S08]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-7e7c622ab203161ea167); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-65e6a7815fa05677da5c)
- [[BOLT-INDEPENDENT-REVIEW]]: records_review_assessment — documented_fact (BOLT-E-dfd3552e173fcf323177)
