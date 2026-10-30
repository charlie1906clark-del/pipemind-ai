---
id: "BOLT-SYNTHETIC-uniform-12-percent"
type: "synthetic_calibration"
title: "Synthetic calculator example: uniform-12-percent"
status: "hypothesis"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Synthetic calculator example: uniform-12-percent

Evidence status: **hypothesis**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "aggregates": [
    {
      "currency": "XXX",
      "difference_as_percent_of_observed_value": "10.714286",
      "difference_exact": "24000",
      "difference_rounded": "24000.00",
      "eligible_line_ids": [
        "A",
        "B"
      ],
      "maximum_line_premium_percent": "12.000000",
      "minimum_line_premium_percent": "12.000000",
      "observed_basis_exact": "224000",
      "reference_basis_exact": "200000",
      "value_basis": "ordered_value",
      "weighted_premium_against_reference_percent": "12.000000"
    }
  ],
  "authentication_limit": "This calculator validates declared fields and arithmetic. It cannot authenticate sources, reviewer identity, availability, independence, payments or concealed benefits. Inspect the underlying evidence.",
  "data_origin": "illustrative",
  "dataset_scope": "Two invented order lines; no named party or government transaction",
  "declared_input_only": true,
  "evidence_kind": "synthetic_calibration",
  "government_transaction": false,
  "input_sha256": "7b5e606c04e661fd9048bcc9688fe48f2f3a93c2f914c250f011a11722b1d641",
  "line_rates": [
    {
      "difference_exact": "12000",
      "line_id": "A",
      "premium_percent": "12.000000",
      "quantity": "1000",
      "reference_basis_exact": "100000"
    },
    {
      "difference_exact": "12000",
      "line_id": "B",
      "premium_percent": "12.000000",
      "quantity": "2000",
      "reference_basis_exact": "100000"
    }
  ],
  "monetary_finding": false,
  "no_money_export": true,
  "output_path": "investigations/dla-bolt-trace-2026-10-30/price-controls/outputs/uniform-12-percent.json",
  "synthetic": true,
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[BOLT-PRICE-PREMIUM-ENGINE]]: has_synthetic_calibration — documented_fact (BOLT-E-868176ea9776b26a31c9)
