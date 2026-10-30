---
id: "agent-pensions-benefits"
type: "agent_specification"
title: "Social Security, federal pensions and personnel"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Social Security, federal pensions and personnel

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Public control/procurement evidence map, with restricted individual records and misleading deceased-name matching explicitly excluded",
    "benign_alternatives": "Death-data lag; identity theft victims; lawful survivor benefits; appeals; timing adjustments; incomplete matching",
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
    "hypotheses": "Published control failures; administrator performance discrepancies; contractor billing anomalies; benefit/payment reconciliation risks",
    "id": "agent-pensions-benefits",
    "join_keys": "Programme; period; public agency/vendor UEI; audit ID; aggregate measure",
    "kind": "sector_specialist",
    "method": "Work with aggregate/public vendor records; do not reconstruct private beneficiaries or personnel files; distinguish error estimates, recovered payments and fraud convictions",
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
    "scope": "pensions-benefits",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "SSA OIG; OPM OIG; GAO; official programme/payroll aggregates; USAspending administrator/vendor contracts",
    "status": "specification_not_running",
    "title": "Social Security, federal pensions and personnel",
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

- [[sector-pensions-benefits]]: assigned_primary_specification — planned (edge-30c223d5588d93bfbdd5)
- [[sector-veterans]]: assigned_secondary_specification — planned (edge-6838ae9b4b3ce89c877d)
