---
id: "agent-healthcare-dme"
type: "agent_specification"
title: "DME and medical supplies"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# DME and medical supplies

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "A reproducible NPI/service cohort with missingness table and source-dated corporate-role edges",
    "benign_alternatives": "Legitimate specialisation; referral concentration; suppression; lagged exclusions; pack/unit mismatch",
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
    "hypotheses": "Outlier units or payment per beneficiary; abrupt new supplier concentration; billing after exclusion or closure",
    "id": "agent-healthcare-dme",
    "join_keys": "NPI; HCPCS; supplier location; service year; UEI/CAGE for supply contracts",
    "kind": "sector_specialist",
    "method": "Normalise HCPCS and service period; compare matched supplier cohorts; verify effective dates; never infer medical necessity from aggregate claims alone",
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
    "scope": "healthcare-dme",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "CMS DME public use files; NPPES; CMS ownership/enrolment; HHS OIG exclusions; USAspending medical supply awards",
    "status": "specification_not_running",
    "title": "DME and medical supplies",
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

- [[sector-defense-spares]]: assigned_secondary_specification — planned (edge-609d4d25028bf680f84c)
- [[sector-healthcare-dme]]: assigned_primary_specification — planned (edge-e18defcb3cfd4fa3ed66)
