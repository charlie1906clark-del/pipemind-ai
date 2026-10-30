---
id: "agent-falsification-reviewer"
type: "agent_specification"
title: "Independent falsification reviewer"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Independent falsification reviewer

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Supported, narrowed, unsupported, contradicted or needs-more-evidence verdict with reasons",
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
    "id": "agent-falsification-reviewer",
    "join_keys": "Claim ID; input manifest; entity/period/measure",
    "kind": "cross_cutting",
    "method": "Receive evidence before conclusions when feasible; do not count repeated official press-release copies as independent corroboration.",
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
    "scope": "Attempt to disprove the lead using fresh reading, matched controls, data-quality explanations and contradictory evidence.",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "Original sources plus independent primary corroboration",
    "status": "specification_not_running",
    "title": "Independent falsification reviewer",
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

- [[sector-foreign-aid]]: assigned_reviewer_specification — planned (edge-03f06df9d49f66915a4e)
- [[sector-logistics]]: assigned_reviewer_specification — planned (edge-0f87cfcd0ac1eb9a8b3e)
- [[sector-medicaid-behavioral]]: assigned_reviewer_specification — planned (edge-0f9366c4168b2e06082b)
- [[sector-it-services]]: assigned_reviewer_specification — planned (edge-16d26f75c34c6d9fd64f)
- [[sector-education]]: assigned_reviewer_specification — planned (edge-1c0864c586d87aa6f50a)
- [[sector-defense-systems]]: assigned_reviewer_specification — planned (edge-2a4cb08a918bea4605a9)
- [[sector-financial]]: assigned_reviewer_specification — planned (edge-2c68b48915342fe8948c)
- [[sector-pandemic-loans]]: assigned_reviewer_specification — planned (edge-2de483d7925ebe236bbf)
- [[sector-veterans]]: assigned_reviewer_specification — planned (edge-37418d22a9693ea3fee0)
- [[sector-healthcare-dme]]: assigned_reviewer_specification — planned (edge-400320ed57d55989b711)
- [[sector-grants-research]]: assigned_reviewer_specification — planned (edge-42b2c92a4ca20a6477ed)
- [[sector-customs-trade]]: assigned_reviewer_specification — planned (edge-43e0ab3aeab9bd4819b6)
- [[sector-justice-detention]]: assigned_reviewer_specification — planned (edge-457aed17b213958d5ebb)
- [[sector-small-business]]: assigned_reviewer_specification — planned (edge-4df893d1666ed20de857)
- [[sector-housing]]: assigned_reviewer_specification — planned (edge-4e275ffd3714aa3c4bbb)
- [[sector-pharma-labs]]: assigned_reviewer_specification — planned (edge-503bb6421e4a3852a365)
- [[sector-disaster]]: assigned_reviewer_specification — planned (edge-57f809271cd18deb62ef)
- [[sector-defense-spares]]: assigned_reviewer_specification — planned (edge-811921947e4a26ffcc52)
- [[sector-construction]]: assigned_reviewer_specification — planned (edge-89bcaf5129b11266d3cb)
- [[sector-pensions-benefits]]: assigned_reviewer_specification — planned (edge-8a3214f4eec7f8b8a082)
- [[sector-childcare-social]]: assigned_reviewer_specification — planned (edge-923d63149d7733a1207f)
- [[sector-tax]]: assigned_reviewer_specification — planned (edge-cfa85c1e5b15b507e65b)
- [[sector-energy-environment]]: assigned_reviewer_specification — planned (edge-dfb4a1e7a80a0aaaf4f6)
- [[sector-tribal-local]]: assigned_reviewer_specification — planned (edge-e37b3aaa107633ae97ba)
- [[sector-agriculture-food]]: assigned_reviewer_specification — planned (edge-f169e048e75cf9fc1c02)
- [[sector-unemployment]]: assigned_reviewer_specification — planned (edge-f2198f7d4e7645537b84)
- [[sector-healthcare-services]]: assigned_reviewer_specification — planned (edge-f447cbc7f7beab871362)
