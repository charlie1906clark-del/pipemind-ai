---
id: "BOLT-BREV-F04"
type: "review_assessment"
title: "Secondary 157.5867 unit-price alarm is unsupported"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Secondary 157.5867 unit-price alarm is unsupported

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "evidence_limits": "The site internal calculation is uninspected. Reject that unit-price inference; do not attribute misrepresentation to the vendor.",
  "locator": "Secondary price table; original RFQ p2, parent p5, child p2",
  "new_named_adverse_allegation": false,
  "review_decision": "reject_inference",
  "review_input_paths": [
    "review/pdf_review.json",
    "review/current_order_review.json"
  ],
  "statement": "The secondary displayed unit price equals350000/2221, but primary records distinguish a350000ceiling from estimated quantity and establish0.91/EA.",
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-SRC-BR-S02]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- assesses_evidence: [[BOLT-CURRENT-UNIT-PRICE]] — documented_fact (BOLT-E-7e13f06cf380a7506331); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-SRC-BR-S02]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-0e1fa8d666a2ef445349); sources: [[BOLT-CUR-S01]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-50e70c072231d8f61346); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-BR-S02]] — documented_fact (edge-6c0af380b436c5d612a4); sources: [[BOLT-SRC-BR-S02]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-e56b342ee3b30b4a6247); sources: [[BOLT-CUR-S02]]

## Backlinks

- [[BOLT-INDEPENDENT-REVIEW]]: records_review_assessment — documented_fact (BOLT-E-3e7cdad77ad1f331cac8)
- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-a0ef2e459c6031b8094f)
