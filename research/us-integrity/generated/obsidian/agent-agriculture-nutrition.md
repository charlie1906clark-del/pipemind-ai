---
id: "agent-agriculture-nutrition"
type: "agent_specification"
title: "Agriculture, SNAP, meals and childcare-related grants"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Agriculture, SNAP, meals and childcare-related grants

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Programme-specific operator map and explicit line between public capacity indicators and proof",
    "benign_alternatives": "Seasonal demand; sponsor/site structures; programme-specific reimbursement; changed rules",
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
    "hypotheses": "Site capacity/claim aggregate incompatibility; operator concentration; repeated audit findings; procurement anomalies",
    "id": "agent-agriculture-nutrition",
    "join_keys": "Programme; recipient UEI; site/operator public ID; state; period",
    "kind": "sector_specialist",
    "method": "No beneficiary dossiers; verify site/service period; require claim evidence beyond estimated capacity",
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
    "scope": "agriculture-nutrition",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "USDA OIG; USDA programme public data; USAspending; FAC; HHS/state childcare public reports",
    "status": "specification_not_running",
    "title": "Agriculture, SNAP, meals and childcare-related grants",
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

- [[sector-agriculture-food]]: assigned_primary_specification — planned (edge-456c7291ba2d4ef00045)
- [[sector-childcare-social]]: assigned_secondary_specification — planned (edge-96102ceb90299a6ae5c2)
