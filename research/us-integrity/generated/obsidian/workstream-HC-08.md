---
id: "workstream-HC-08"
type: "workstream"
title: "Medicare Advantage risk adjustment and delegated vendor networks"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Medicare Advantage risk adjustment and delegated vendor networks

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Risk-adjustment evidence auditor: require correct model/version, supported diagnosis/deletion facts and legal-status precision.",
  "blind_spots": [
    "Public sources rarely expose complete enrollee diagnosis chains or HRA-vendor contracts.",
    "OIG HRA-only payment estimates include alternative care-quality explanations and are not fraud loss estimates."
  ],
  "buyer_vs_payee": "Capitation is an insurer payment, not reimbursement for one specific billed clinical service; chart review and care delivery can be performed by different entities.",
  "funds_path": [
    "CMS risk-adjusted capitation",
    "Medicare Advantage organization",
    "delegated provider group / HRA or coding vendor",
    "corporate parent"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "true morbidity increase",
        "benefit/coding/model change",
        "care underuse",
        "data incompleteness"
      ],
      "needed": "Validated diagnosis encounter histories, HCC model/year, deletion records and clinical documentation.",
      "signal": "Risk-adjustment payment rises without corresponding service pattern in authorized data"
    }
  ],
  "join_plan": [
    "Keep contract/plan/year and parent organization effective dates; do not infer plan ownership from brand alone.",
    "Preserve diagnosis submission/deletion, HRA and encounter origins if lawfully available.",
    "Use public audits/settlements as typology evidence; do not pretend public NPI aggregates include underlying risk adjustment records."
  ],
  "priority": "high_materiality_low_public_evidence_completeness",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S22]]
- [[src-HC-S25]]

## Outgoing relationships

- cites: [[src-HC-S25]] — documented_fact (edge-0488b64a7129f82dd9d6); sources: [[src-HC-S25]]
- has_research_hypothesis: [[workstream-HC-08-hyp-1]] — planned (edge-af6939830069fcb3f781); sources: 
- cites: [[src-HC-S22]] — documented_fact (edge-cdb67f18b9f94ac3f548); sources: [[src-HC-S22]]

## Backlinks

None recorded.
