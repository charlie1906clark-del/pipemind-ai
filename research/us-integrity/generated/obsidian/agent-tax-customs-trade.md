---
id: "agent-tax-customs-trade"
type: "agent_specification"
title: "Tax, customs, tariffs and international trade"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Tax, customs, tariffs and international trade

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Evidence-access map and source-backed public typologies, with non-public requirements documented",
    "benign_alternatives": "Lawful tariff classification; transfer pricing requiring private records; timing and origin rules",
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
    "hypotheses": "Published evasion/misclassification typologies; publicly testable importer/product inconsistencies",
    "id": "agent-tax-customs-trade",
    "join_keys": "Public case/entry identifiers where released; entity registry ID; product classification; period",
    "kind": "sector_specialist",
    "method": "Do not claim access to returns, bank records or confidential entries; distinguish trade statistics from company transactions",
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
    "scope": "tax-customs-trade",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "IRS whistleblower public guidance; GAO; Treasury OIG/TIGTA; CBP public enforcement/statistics; DOJ",
    "status": "specification_not_running",
    "title": "Tax, customs, tariffs and international trade",
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

- [[sector-tax]]: assigned_primary_specification — planned (edge-8e2350630976338822da)
- [[sector-customs-trade]]: assigned_primary_specification — planned (edge-e374209fa8a362ffe9e6)
