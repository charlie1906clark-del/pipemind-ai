---
id: "agent-justice-detention"
type: "agent_specification"
title: "Justice, detention, corrections and homeland services"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Justice, detention, corrections and homeland services

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Facility-contract-inspection chronology, measure-normalised cost comparison and missing invoice/detainee evidence statement",
    "benign_alternatives": "Minimum guarantees; surge capacity; emergency mobilisation; occupancy changes; different medical/security service bundles",
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
    "hypotheses": "False contractual service/capacity representations; inspection/compliance contradictions; unsupported invoicing hypotheses; subcontractor delivery anomalies",
    "id": "agent-justice-detention",
    "join_keys": "Facility ID; award/action; UEI; contract period; capacity/occupancy measure; dated corporate ownership",
    "kind": "sector_specialist",
    "method": "Compare the precise contract standard with dated inspections and payment measure; a facility deficiency is not automatically fraud; no detainee-level health or immigration dossiers",
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
    "scope": "justice-detention",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "DOJ OIG; DHS OIG; GAO; BOP/ICE public contracts/inspection reports; USAspending; SAM; public SEC operator filings",
    "status": "specification_not_running",
    "title": "Justice, detention, corrections and homeland services",
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

- [[sector-justice-detention]]: assigned_primary_specification — planned (edge-3393361a2e84fb9b3ba6)
