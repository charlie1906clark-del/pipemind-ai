---
id: "PA-RECURRENCE-ACTUAL-BLOCKED"
type: "arithmetic_screen_observation"
title: "No real repeated premium established: actual comparison is blocked"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# No real repeated premium established: actual comparison is blocked

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "actual_repeated_premium": null,
  "purchasing_office_label_is_only_piid_prefix": true,
  "real_buyer_benefit": null,
  "real_loss": null,
  "result": {
    "calculator_sha256": "7aed71b71b47c0940b0c07fd1239c64bb70817be506204b3ac3de366d9dcfde2",
    "data_origin": "public_observation",
    "dataset_scope": "One inspected DLA ordered line, not a payment, independent market benchmark or complete award population",
    "design_status": "exploratory_retrospective",
    "evidence_kind": "documented_contract_observation_with_unresolved_comparison",
    "groups": [
      {
        "blocked_line_ids": [
          "DLA-SPE4A627F0588-0001"
        ],
        "buyer_benefit": null,
        "coverage_basis": "Line counts for submitted group; blocked value and nationwide coverage are not established",
        "currency": "USD",
        "distinct_in_band_as_declared": {
          "benchmark_families": 0,
          "months": 0,
          "solicitations": 0
        },
        "eligible_lines": 0,
        "fraud_probability": null,
        "in_band_lines": 0,
        "in_band_reference_share_percent_display": null,
        "in_band_reference_value_exact": null,
        "item_stratum_as_declared": "NSN:5306016864912",
        "line_details": [],
        "net_difference_positive": null,
        "observed_value_exact": null,
        "purchasing_office_identifier_as_declared": "PIID-prefix:SPE4A6",
        "reasons": [
          "no qualified comparison as declared",
          "blocked-line fraction exceeds plan limit",
          "insufficient distinct in-band solicitations",
          "insufficient distinct in-band months",
          "insufficient distinct in-band benchmark_families"
        ],
        "recoverable_loss": null,
        "reference_value_exact": null,
        "screen_status": "insufficient_pattern_support",
        "signed_difference_exact": null,
        "submitted_lines": 1,
        "supplier_identifier_as_declared": "CAGE:8A1E8",
        "value_basis": "ordered_value",
        "weighted_premium_percent_display": null
      }
    ],
    "input_canonical_sha256": "90994c9f78408c10718c002b5cbee295a2ad5c6a294ce1a5b1a151ca49748e3d",
    "limitations": [
      "Labels, independence, scope completeness and comparison review are supplied declarations, not authenticated by this tool.",
      "No automatic supplier ranking, accusation, publication, payment inference or personal-benefit conclusion.",
      "Repeated target-band rates are an exploratory lead, not a causal or statistical significance test.",
      "A repeated line-count pattern can coexist with a negative aggregate difference; it does not establish overall overpayment.",
      "Negative differences and all eligible lines remain in weighted totals; multiple lines of one solicitation do not count as separate solicitations.",
      "A supplied plan date does not establish preregistration. Preserve this plan before a future held-out acquisition for prospective testing."
    ],
    "metadata_canonical_sha256": "494427354ed65f3226e29a20ebfbab4e7e88687e5240379b888a0e1ae0a67582",
    "plan": {
      "analysis_scope": "One retained current order; PIID prefix is a grouping key, not verified individual buyer identity",
      "design_status": "exploratory_retrospective",
      "maximum_blocked_fraction": "0.25",
      "minimum_benchmark_families": 2,
      "minimum_in_band_fraction": "0.75",
      "minimum_months": 2,
      "minimum_solicitations": 3,
      "period_end": "2026-10-30",
      "period_start": "2026-01-01",
      "plan_id": "ACTUAL-BOLT-BLOCKED-SCREEN",
      "schema_version": "1.0",
      "scope_kind": "declared_sample",
      "target_percent": "12",
      "tolerance_percentage_points": "1"
    },
    "plan_canonical_sha256": "8ec5bdbd0fbc1d5f40cefe6481f952fbc39888ec2d235fde4e761497ba704f0b",
    "schema_version": "1.0"
  },
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-RECURRENCE-ACTUAL]]

## Outgoing relationships

- cites: [[PA-SRC-RECURRENCE-ACTUAL]] — documented_fact (edge-7f59ad1872cea0a4a038); sources: [[PA-SRC-RECURRENCE-ACTUAL]]

## Backlinks

- [[PA-SYSTEM-20261030]]: records_blocked_actual_screen — documented_fact (PA-E-fd0409d804e79fbb2cfe61a7)
