---
id: "BOLT-PCR-F08"
type: "review_assessment"
title: "The offline calculator reproduces the declared arithmetic and blocks the actual DLA comparison; its flags cannot authenticate the evidence."
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# The offline calculator reproduces the declared arithmetic and blocks the actual DLA comparison; its flags cannot authenticate the evidence.

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "evidence_paths": [
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-controls/premium_audit.py",
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-controls/test_premium_audit.py",
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-controls/README.md",
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-controls/outputs/dla-current-no-qualified-benchmark.json"
  ],
  "limits": [
    "Independent review identified order-to-invoice source relabeling; producer corrected the source-kind gate and regression coverage passed.",
    "Public source URLs, availability, independence and reviewer identities remain declared evidence requiring human/source review."
  ],
  "new_named_adverse_inference": false,
  "provenance_note": "External source links provide source facts or methodology; code execution and synthetic arithmetic are supported by the separately pinned local artifacts",
  "review_decision": "accept",
  "synthetic_numeric_claim": false,
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]

## Outgoing relationships

- assesses_evidence: [[BOLT-PRICE-PREMIUM-ENGINE]] — documented_fact (BOLT-E-ef8cd573a0dd16cfe8c2); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-0f80b7ee742bc1f5ffcb); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-450944a5156fb64e773f); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-b8a579e3dfe24fea3742); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-bbf72509089ff975f340); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-f35fd255503193e81f17); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-PRICE-CHALLENGE-REVIEW]]: records_review_assessment — documented_fact (BOLT-E-33a0121e8aa691e9ed17)
- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-3f1a1308b1355c587cec)
