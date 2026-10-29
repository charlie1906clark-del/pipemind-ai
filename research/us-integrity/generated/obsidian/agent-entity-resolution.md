---
id: "agent-entity-resolution"
type: "agent_specification"
title: "Entity and ownership resolver"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Entity and ownership resolver

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Identity decision log, candidate matches, contrary evidence and unresolved owner edges",
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
    "id": "agent-entity-resolution",
    "join_keys": "UEI; CAGE; NPI; CCN; state registry ID; CIK; LEI; effective dates",
    "kind": "cross_cutting",
    "method": "Test DBA, registered agent, same-name businesses, acquisitions and shared service addresses before any merge.",
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
    "scope": "Resolve legal entities, public business roles and corporate relationships using dated identifiers; maintain reversible candidate matches.",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "SAM; NPPES/PECOS public files; state registries; SEC; primary case documents",
    "status": "specification_not_running",
    "title": "Entity and ownership resolver",
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

- [[sector-medicaid-behavioral]]: assigned_reviewer_specification — planned (edge-126f4f2839aea2b42dfd)
- [[sector-logistics]]: assigned_reviewer_specification — planned (edge-1483661c358ffd5e0c10)
- [[sector-healthcare-dme]]: assigned_reviewer_specification — planned (edge-21e49d297a982f6d1141)
- [[sector-education]]: assigned_reviewer_specification — planned (edge-2307437c5ef320785d96)
- [[sector-pensions-benefits]]: assigned_reviewer_specification — planned (edge-27f248738ac070d00ba6)
- [[sector-pandemic-loans]]: assigned_reviewer_specification — planned (edge-444eddbc9deb07cd0149)
- [[sector-defense-systems]]: assigned_reviewer_specification — planned (edge-508ae69bf67190b104f2)
- [[sector-tax]]: assigned_reviewer_specification — planned (edge-510591cf575fbb97b0bb)
- [[sector-tribal-local]]: assigned_reviewer_specification — planned (edge-541dfadb4ebfa555e38e)
- [[sector-energy-environment]]: assigned_reviewer_specification — planned (edge-5f49f0af9ab4f67992f4)
- [[sector-unemployment]]: assigned_reviewer_specification — planned (edge-6150b1afaf7b315a3160)
- [[sector-healthcare-services]]: assigned_reviewer_specification — planned (edge-6e6a72ed5270d8cd822a)
- [[sector-financial]]: assigned_reviewer_specification — planned (edge-74a7e8651fe8795b11b4)
- [[sector-it-services]]: assigned_reviewer_specification — planned (edge-78b7cfbb3b11e648b332)
- [[sector-pharma-labs]]: assigned_reviewer_specification — planned (edge-7a837f0349a2dbad3889)
- [[sector-housing]]: assigned_reviewer_specification — planned (edge-8c71e052c1751f78e3c5)
- [[sector-customs-trade]]: assigned_reviewer_specification — planned (edge-90d52c0676a632481028)
- [[sector-veterans]]: assigned_reviewer_specification — planned (edge-930fd09247afee2f5507)
- [[sector-childcare-social]]: assigned_reviewer_specification — planned (edge-9bfda98cab4f04ee85a4)
- [[sector-foreign-aid]]: assigned_reviewer_specification — planned (edge-9ef016e18e2699cfd943)
- [[sector-defense-spares]]: assigned_reviewer_specification — planned (edge-a625164d7c1bea9d834a)
- [[sector-justice-detention]]: assigned_reviewer_specification — planned (edge-a715408e155710cb169c)
- [[sector-agriculture-food]]: assigned_reviewer_specification — planned (edge-c4d472c4bab59aa3c929)
- [[sector-grants-research]]: assigned_reviewer_specification — planned (edge-d634eeab1bb956c41211)
- [[sector-construction]]: assigned_reviewer_specification — planned (edge-daa1005ced850e3546af)
- [[sector-disaster]]: assigned_reviewer_specification — planned (edge-f6ca98c756d8df243d78)
- [[sector-small-business]]: assigned_reviewer_specification — planned (edge-fd656cc48ed113123989)
