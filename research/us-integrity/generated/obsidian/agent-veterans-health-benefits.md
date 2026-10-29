---
id: "agent-veterans-health-benefits"
type: "agent_specification"
title: "Veterans healthcare and benefits"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Veterans healthcare and benefits

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "VA-specific award/provider paths and explicit distinction between public awards and private benefits records",
    "benign_alternatives": "Rural access needs; special product specifications; programme reporting lag",
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
    "hypotheses": "Provider or supplier contract anomalies; duplicate charges when documented; eligibility intermediary misconduct patterns",
    "id": "agent-veterans-health-benefits",
    "join_keys": "Award key; UEI/CAGE; VA facility; programme; public provider ID",
    "kind": "sector_specialist",
    "method": "Keep healthcare contracts separate from individual benefit claims; do not acquire claimant identities",
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
    "scope": "veterans-health-benefits",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "VA OIG; USAspending VA awards; SAM; public facility and programme reports",
    "status": "specification_not_running",
    "title": "Veterans healthcare and benefits",
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

- [[sector-veterans]]: assigned_primary_specification — planned (edge-aadeb8b7ee28700cc3d4)
