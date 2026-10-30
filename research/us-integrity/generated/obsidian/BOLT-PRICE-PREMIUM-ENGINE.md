---
id: "BOLT-PRICE-PREMIUM-ENGINE"
type: "analytical_method"
title: "Offline price-comparison calculator preserves eligibility gates and amount bases"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Offline price-comparison calculator preserves eligibility gates and amount bases

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "automatic_reviewer_authentication": false,
  "automatic_source_authentication": false,
  "implementation_path": "investigations/dla-bolt-trace-2026-10-30/price-controls/premium_audit.py",
  "implementation_sha256": "7aed71b71b47c0940b0c07fd1239c64bb70817be506204b3ac3de366d9dcfde2",
  "method_origin": "Custom research code; cited official sources supply methodological context, not software certification",
  "official_fraud_detector": false,
  "real_cohort_loss_established": false,
  "source_role": "Methodological background; execution evidence is in the pinned local inputs, outputs and independent review",
  "test_artifact_sha256": "c65a73a210deb2446e5dbbff5ad83bf5f7eee30755cb4ab96db3522e2baae97c",
  "visibility": "public"
}
```

## Sources

- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]

## Outgoing relationships

- has_synthetic_calibration: [[BOLT-SYNTHETIC-ANNUAL-ILLUSTRATION]] — documented_fact (BOLT-E-03d90462d200c650c9e1); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]]
- records_actual_gate_result: [[BOLT-PRICE-ACTUAL-BLOCKED]] — documented_fact (BOLT-E-4691c0b444867e0f845e); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]]
- has_synthetic_calibration: [[BOLT-SYNTHETIC-uniform-12-percent]] — documented_fact (BOLT-E-868176ea9776b26a31c9); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]]
- has_synthetic_calibration: [[BOLT-SYNTHETIC-weighted-mix]] — documented_fact (BOLT-E-8a0b699210517d599d24); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-324c98f6aa6bac29c035); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-f8332702fdf3bede96f8); sources: [[BOLT-PC-METHOD-S02]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-586a5cdb32d18ce182a5)
- [[BOLT-PCR-F08]]: assesses_evidence — documented_fact (BOLT-E-ef8cd573a0dd16cfe8c2)
