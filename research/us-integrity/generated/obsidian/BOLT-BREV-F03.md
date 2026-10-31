---
id: "BOLT-BREV-F03"
type: "review_assessment"
title: "Current original order establishes USD0.91 per EA"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Current original order establishes USD0.91 per EA

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "evidence_limits": "Ordered amount is not verified delivery, acceptance or payment; original full PDFs are not published.",
  "locator": "Parent pp2,5–6; child pp1–2",
  "new_named_adverse_allegation": false,
  "review_decision": "accept",
  "review_input_paths": [
    "current/selected_manifest.json",
    "current/observations.json",
    "review/current_order_review.json",
    "review/current_original_inspection.json"
  ],
  "statement": "Original parent CLIN0001 is USD0.91000/EA; child CLIN0001 orders906EA at0.9100 for824.46, due2027-01-04.",
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]

## Outgoing relationships

- assesses_evidence: [[BOLT-CURRENT-LINE-RECONCILIATION]] — documented_fact (BOLT-E-827e8cccbfefdb5e3ff8); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-276c502ff8ec551625ec); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-aca2f73e1862ce68468e); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-31c374bdff4c2982991c)
- [[BOLT-INDEPENDENT-REVIEW]]: records_review_assessment — documented_fact (BOLT-E-46b439ea6902ea46b0ab)
