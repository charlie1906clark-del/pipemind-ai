---
id: "agent-healthcare-managed-care"
type: "agent_specification"
title: "Medicare Advantage and Medicaid managed care"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Medicare Advantage and Medicaid managed care

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Plan/provider scope and coverage statement that prevents claims-level overinterpretation",
    "benign_alternatives": "Risk mix; coding changes; incomplete encounter data; plan consolidation",
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
    "hypotheses": "Risk-adjustment or encounter anomalies; capitation/fee-for-service measure mismatches; contract concentration",
    "id": "agent-healthcare-managed-care",
    "join_keys": "Contract/plan ID; NPI; state provider ID; service year; plan ownership",
    "kind": "sector_specialist",
    "method": "Use programme-specific denominator; distinguish diagnoses from payments; disclose unavailable records",
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
    "scope": "healthcare-managed-care",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "CMS managed-care data; HHS public Medicaid datasets; HHS OIG audits; state programme publications",
    "status": "specification_not_running",
    "title": "Medicare Advantage and Medicaid managed care",
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

- [[sector-medicaid-behavioral]]: assigned_primary_specification — planned (edge-b60a758c1c383152c0b4)
