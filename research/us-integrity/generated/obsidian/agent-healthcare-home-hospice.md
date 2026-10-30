---
id: "agent-healthcare-home-hospice"
type: "agent_specification"
title: "Home health and hospice"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Home health and hospice

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Service-specific cohort, ownership chronology and explicit patient-level evidence gap",
    "benign_alternatives": "Case mix; rural coverage; changes in reporting; acquisition; multiple legal sites",
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
    "hypotheses": "Rapid enrolment or ownership turnover; unusual visit/intensity aggregates; geographically implausible service footprint",
    "id": "agent-healthcare-home-hospice",
    "join_keys": "CCN; NPI; ownership record; facility; service year",
    "kind": "sector_specialist",
    "method": "Compare peers and years; distinguish hospice from home-health measures; verify licence and operation dates",
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
    "scope": "healthcare-home-hospice",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "CMS hospice/home-health public files and ownership; Care Compare; HHS OIG; state licensing",
    "status": "specification_not_running",
    "title": "Home health and hospice",
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

- [[sector-healthcare-services]]: assigned_primary_specification — planned (edge-e37fedb84c3804f5ee7e)
