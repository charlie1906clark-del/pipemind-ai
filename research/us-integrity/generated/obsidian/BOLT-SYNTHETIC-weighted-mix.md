---
id: "BOLT-SYNTHETIC-weighted-mix"
type: "synthetic_calibration"
title: "Synthetic calculator example: weighted-mix"
status: "hypothesis"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Synthetic calculator example: weighted-mix

Evidence status: **hypothesis**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "aggregates": [
    {
      "currency": "XXX",
      "difference_as_percent_of_observed_value": "1.960784",
      "difference_exact": "20",
      "difference_rounded": "20.00",
      "eligible_line_ids": [
        "C",
        "D"
      ],
      "maximum_line_premium_percent": "20.000000",
      "minimum_line_premium_percent": "0.000000",
      "observed_basis_exact": "1020",
      "reference_basis_exact": "1000",
      "value_basis": "ordered_value",
      "weighted_premium_against_reference_percent": "2.000000"
    }
  ],
  "authentication_limit": "This calculator validates declared fields and arithmetic. It cannot authenticate sources, reviewer identity, availability, independence, payments or concealed benefits. Inspect the underlying evidence.",
  "data_origin": "illustrative",
  "dataset_scope": "Two invented order lines illustrating value weighting",
  "declared_input_only": true,
  "evidence_kind": "synthetic_calibration",
  "government_transaction": false,
  "input_sha256": "ea40415a73b259211b1ffce5a4d54b9e97188c90b49e6e02c05f78fe0923ee2e",
  "line_rates": [
    {
      "difference_exact": "20",
      "line_id": "C",
      "premium_percent": "20.000000",
      "quantity": "1",
      "reference_basis_exact": "100"
    },
    {
      "difference_exact": "0",
      "line_id": "D",
      "premium_percent": "0.000000",
      "quantity": "9",
      "reference_basis_exact": "900"
    }
  ],
  "monetary_finding": false,
  "no_money_export": true,
  "output_path": "investigations/dla-bolt-trace-2026-10-30/price-controls/outputs/weighted-mix.json",
  "synthetic": true,
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[BOLT-PRICE-PREMIUM-ENGINE]]: has_synthetic_calibration — documented_fact (BOLT-E-8a0b699210517d599d24)
