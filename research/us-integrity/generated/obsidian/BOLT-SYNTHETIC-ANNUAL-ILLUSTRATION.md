---
id: "BOLT-SYNTHETIC-ANNUAL-ILLUSTRATION"
type: "synthetic_calibration"
title: "Synthetic annual algebra: 12% markup and a 100,000 total increment"
status: "hypothesis"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Synthetic annual algebra: 12% markup and a 100,000 total increment

Evidence status: **hypothesis**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "amount_is_buyer_benefit": false,
  "declared_input_only": true,
  "government_transaction": false,
  "illustration": {
    "assumptions": [
      "100000 is the total price increment, not gross annual purchasing",
      "12% is a uniform markup on the comparable underlying cost",
      "No legitimate extra costs or tax differences are modeled",
      "No government transaction or personal benefit is established"
    ],
    "currency": "unspecified",
    "data_origin": "illustrative_user_scenario",
    "dataset_scope": "Algebraic illustration of the user-described 12% and 100000 example; no actual transaction evidence",
    "evidence_kind": "synthetic_calibration",
    "implied_gross_annual_value_rounded": "933333.33",
    "implied_reference_annual_cost_rounded": "833333.33",
    "increment": "100000.00",
    "increment_as_percent_of_gross": "10.714286",
    "markup_against_reference_percent": "12.000000",
    "rounding_note": "Exact underlying divisions repeat; monetary illustrations are rounded to 2 places only.",
    "schema_version": "1.0"
  },
  "interpretation": "Assumes 100,000 is total price increment; it does not establish personal benefit or government loss",
  "no_money_export": true,
  "synthetic": true,
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[BOLT-PRICE-PREMIUM-ENGINE]]: has_synthetic_calibration — documented_fact (BOLT-E-03d90462d200c650c9e1)
- [[BOLT-PCR-F09]]: assesses_evidence — documented_fact (BOLT-E-41f68809c1f2ebd2d94c)
