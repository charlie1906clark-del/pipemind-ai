---
id: "agent-foreign-aid"
type: "agent_specification"
title: "Foreign assistance and overseas procurement"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Foreign assistance and overseas procurement

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Country/programme-bounded implementing chain with exchange-rate basis and explicit end-use verification gaps",
    "benign_alternatives": "Security restrictions; currency fluctuations; legitimate local price differences; authorised partner changes; emergency logistics",
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
    "hypotheses": "Unverified delivery; changing subrecipient roles; related-party procurement; allegedly false certifications; duplicate funded scope",
    "id": "agent-foreign-aid",
    "join_keys": "Programme; award/FAIN; UEI; implementing partner; local registry ID; currency; delivery period",
    "kind": "sector_specialist",
    "method": "Use programme-specific award terms and dated local identities; distinguish obligated aid from disbursed funds and delivered benefit; document incomplete local/subaward visibility",
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
    "scope": "foreign-aid",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "State/USAID OIG; DoD OIG; SIGAR archived records; USAspending; SAM; official programme and local registry records where accessible",
    "status": "specification_not_running",
    "title": "Foreign assistance and overseas procurement",
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

- [[sector-foreign-aid]]: assigned_primary_specification — planned (edge-c9d016ebd1fa919a7ca5)
