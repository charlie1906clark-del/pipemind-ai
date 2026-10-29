---
id: "agent-quality-evaluator"
type: "agent_specification"
title: "Research quality and regression evaluator"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Research quality and regression evaluator

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Pass/fail evidence, observed limitations and bounded release recommendation",
    "benign_alternatives": "Source error; identifier collision; stale records; incomplete coverage; lawful conduct; incorrect analytical assumptions.",
    "capabilities": [
      "read approved public sources",
      "analyse bounded extracts",
      "write proposed evidence patches in assigned workspace"
    ],
    "escalation": [
      "source access or legal authority unclear",
      "identifiers conflict",
      "novel named suspicion survives falsification",
      "confidential or personal data encountered",
      "written programme rules conflict",
      "source/schema drift invalidates comparison"
    ],
    "forbidden_actions": [
      "contact individuals or organisations",
      "submit tips or claims",
      "publish novel named allegations",
      "access private patient, benefit, bank or tax records",
      "bypass authentication or source access controls",
      "deploy services or incur paid API spend"
    ],
    "hypotheses": "Evaluate the assigned claim or workflow; never create a conclusion before evidence.",
    "id": "agent-quality-evaluator",
    "join_keys": "Fixture ID; code commit; input hashes; expected result",
    "kind": "cross_cutting",
    "method": "Prevent hindsight leakage, self-evaluation and arbitrary score-to-guilt claims.",
    "required_output": [
      "task_id",
      "agent_id",
      "input_commit",
      "cohort",
      "source_ids",
      "direct_findings",
      "inferences",
      "contradictions",
      "benign_alternatives_tested",
      "missing_data",
      "method",
      "visibility",
      "legal_status_if_case",
      "next_step",
      "review_status"
    ],
    "scope": "Run reproducibility and failure-case evaluations across entity joins, money semantics, legal language and collaboration races.",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "Frozen fixtures; independent source checks; engine tests; cohort reports",
    "status": "specification_not_running",
    "title": "Research quality and regression evaluator",
    "version": "1.0"
  },
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

None recorded.
