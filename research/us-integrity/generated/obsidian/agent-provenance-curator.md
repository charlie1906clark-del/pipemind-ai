---
id: "agent-provenance-curator"
type: "agent_specification"
title: "Provenance and source curator"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Provenance and source curator

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Validated source/claim links and reproducibility manifest",
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
    "id": "agent-provenance-curator",
    "join_keys": "Source ID; canonical URL; retrieved time; content hash if archived",
    "kind": "cross_cutting",
    "method": "Reject citation laundering, missing pages, synthetic URLs, unverifiable dates and unsupported raw-archive claims.",
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
    "scope": "Maintain source lineage, canonical IDs, retrieval manifests, byte-hash honesty, dates and exact locators.",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "Original official sources; saved response manifests; source registry",
    "status": "specification_not_running",
    "title": "Provenance and source curator",
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

- [[sector-education]]: assigned_reviewer_specification — planned (edge-01abb573ecd4d8676476)
- [[sector-financial]]: assigned_reviewer_specification — planned (edge-07ebb848eaef8775fa6a)
- [[sector-construction]]: assigned_reviewer_specification — planned (edge-0f9e1b4520a1a67db168)
- [[sector-tax]]: assigned_reviewer_specification — planned (edge-103bb9ea38b8d6810935)
- [[sector-veterans]]: assigned_reviewer_specification — planned (edge-14f6d0199ad9811d22b5)
- [[sector-unemployment]]: assigned_reviewer_specification — planned (edge-1bb8ac03bee087af3525)
- [[sector-housing]]: assigned_reviewer_specification — planned (edge-2b4f65eaaa9b6ada9da6)
- [[sector-defense-spares]]: assigned_reviewer_specification — planned (edge-322898914d953cc766a7)
- [[sector-pandemic-loans]]: assigned_reviewer_specification — planned (edge-3e629aca44512311c125)
- [[sector-pharma-labs]]: assigned_reviewer_specification — planned (edge-4fc510d52f21189b14d2)
- [[sector-childcare-social]]: assigned_reviewer_specification — planned (edge-62cc63527ca67f96e993)
- [[sector-justice-detention]]: assigned_reviewer_specification — planned (edge-633e831d4ebcee1dbb3a)
- [[sector-tribal-local]]: assigned_reviewer_specification — planned (edge-63981d116f83f9531845)
- [[sector-foreign-aid]]: assigned_reviewer_specification — planned (edge-7306bbaa410a602ce7b5)
- [[sector-energy-environment]]: assigned_reviewer_specification — planned (edge-77ee17c7d7e4d22d3b50)
- [[sector-medicaid-behavioral]]: assigned_reviewer_specification — planned (edge-84acd213f75e1b4a05ad)
- [[sector-healthcare-dme]]: assigned_reviewer_specification — planned (edge-98bb7cf5cd811b886611)
- [[sector-agriculture-food]]: assigned_reviewer_specification — planned (edge-98e55917afd8e7dc4b6d)
- [[sector-it-services]]: assigned_reviewer_specification — planned (edge-ac3edf6b4802611c7488)
- [[sector-healthcare-services]]: assigned_reviewer_specification — planned (edge-bd31b151bc3513e2197d)
- [[sector-pensions-benefits]]: assigned_reviewer_specification — planned (edge-bf7f3a310d85e582f90e)
- [[sector-grants-research]]: assigned_reviewer_specification — planned (edge-c36da2f0d2226f588eff)
- [[sector-customs-trade]]: assigned_reviewer_specification — planned (edge-cd7992315df9f9fe603a)
- [[sector-disaster]]: assigned_reviewer_specification — planned (edge-d8fdd838365a43d75458)
- [[sector-defense-systems]]: assigned_reviewer_specification — planned (edge-e5253c3a78c6d8e60b6b)
- [[sector-logistics]]: assigned_reviewer_specification — planned (edge-e6e03c366ffc3730dc59)
- [[sector-small-business]]: assigned_reviewer_specification — planned (edge-f19efa1c00d0ab22d4e2)
