---
id: "BOLT-PRICE-ACTUAL-BLOCKED"
type: "analytical_result"
title: "Actual DLA price calculation is blocked; no benchmark premium or loss is emitted"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Actual DLA price calculation is blocked; no benchmark premium or loss is emitted

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "buyer_benefit": null,
  "data_origin": "public_observation",
  "dataset_scope": "One inspected DLA ordered line, not a payment, independent market benchmark or complete award population",
  "evidence_kind": "documented_contract_observation_with_unresolved_comparison",
  "gate_behavior": "Fail-fast validation; the first missing field is not an exhaustive gap list",
  "price_premium": null,
  "qualified_benchmark": null,
  "recoverable_loss": null,
  "result": {
    "aggregates": [],
    "authentication_limit": "This calculator validates declared fields and arithmetic. It cannot authenticate sources, reviewer identity, availability, independence, payments or concealed benefits. Inspect the underlying evidence.",
    "blocked_lines": 1,
    "coverage_complete_for_submitted_lines": false,
    "data_origin": "public_observation",
    "dataset_scope": "One inspected DLA ordered line, not a payment, independent market benchmark or complete award population",
    "eligible_lines": 0,
    "evidence_kind": "documented_contract_observation_with_unresolved_comparison",
    "input_snapshot": {
      "file_name": "dla-current-no-qualified-benchmark.json",
      "sha256": "87b32320d35bae4381de252a4f05f7c57d35539235491cc29f85827a31e3304d"
    },
    "interpretation": "Differences against supplied reviewed references, not a misconduct or recoverability finding.",
    "lines": [
      {
        "adjusted_reference_unit_price": null,
        "data_origin": "public_observation",
        "difference_exact": null,
        "key": {
          "agency_code": "DLA",
          "clin": "0001",
          "order_id": "SPE4A627F0588",
          "piid": "SPE4A626D61WS"
        },
        "line_id": "DLA-SPE4A627F0588-0001",
        "premium_against_reference_percent": null,
        "reason": "contract.terms.condition: missing nonempty text",
        "reference_status": "not_supplied",
        "status": "blocked"
      }
    ],
    "rounding": "Decimal precision 80; totals aggregate unrounded values; display uses half-up 2 decimal amounts and 6 decimal percentage points. No FX or automatic unit conversion.",
    "schema_version": "1.0",
    "submitted_lines": 1
  },
  "source_authentication_by_calculator": false,
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]

## Outgoing relationships

- keeps_fairness_question_open: [[BOLT-PRICE-FAIRNESS-UNKNOWN]] — documented_fact (BOLT-E-3a8d7071b7711a9ef161); sources: [[BOLT-CUR-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]]
- evaluates_ordered_line: [[BOLT-ORDER-SPE4A627F0588]] — documented_fact (BOLT-E-c44e23f022fb915dcceb); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-1727bfee386d9242cf49); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-265f36762582a0523bd7); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-4c5e2f8d14300d63a549); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-eea70fceb12a1611c638); sources: [[BOLT-PC-METHOD-S02]]

## Backlinks

- [[BOLT-PRICE-PREMIUM-ENGINE]]: records_actual_gate_result — documented_fact (BOLT-E-4691c0b444867e0f845e)
- [[BOLT-PCR-F06]]: assesses_evidence — documented_fact (BOLT-E-64f12d6f45f568786796)
- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-6f527323b367abb5be3d)
