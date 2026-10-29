---
id: "agent-healthcare-pharma-labs"
type: "agent_specification"
title: "Pharmaceuticals, PBMs and laboratories"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Pharmaceuticals, PBMs and laboratories

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "runtime_active": false,
  "specification": {
    "acceptance": "Drug/test-specific comparable measures and a reviewed distinction between transfers, allegations and adjudicated conduct",
    "benign_alternatives": "Specialist referral patterns; rebates hidden from gross figures; branded/generic and package differences",
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
    "hypotheses": "Unusual test/prescribing concentration; publicly documented payment links; possible duplicate product units",
    "id": "agent-healthcare-pharma-labs",
    "join_keys": "NPI; NDC; HCPCS; manufacturer; service year; organisation IDs",
    "kind": "sector_specialist",
    "method": "Separate manufacturer transfers from kickbacks; do not infer net prices from gross reimbursement; require service/contract context",
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
    "scope": "healthcare-pharma-labs",
    "source_tiers": [
      "primary official record with exact locator",
      "official explanatory/data documentation",
      "secondary reporting only as a lead to primary evidence"
    ],
    "sources": "CMS Part D and Open Payments; Medicaid drug public files; FDA drug data; HHS OIG; DOJ published cases",
    "status": "specification_not_running",
    "title": "Pharmaceuticals, PBMs and laboratories",
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

- [[sector-pharma-labs]]: assigned_primary_specification — planned (edge-42219980193e30cce2de)
