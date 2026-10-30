---
id: "DME-NATIONAL-CHECK-2022-A4352"
type: "finding"
title: "2022 A4352: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4352: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4352",
    "detail_payment_coverage_pct": "99.22",
    "detail_service_coverage_pct": "99.15",
    "national_amounts_usd_reconstructed": {
      "allowed": "343877250.55",
      "puf_payment": "267662167.65",
      "standardized_payment": "284010505.29",
      "submitted": "482227273.41"
    },
    "national_beneficiaries_sum_across_rental": 45961,
    "national_claims": 185500,
    "national_less_detail_payment_usd": "2077342.81",
    "national_services": "46664007",
    "national_suppliers_sum_across_rental": 1215,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2022
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2022-A4352]]
- [[DME-SRC-PUF-2022-A4352]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2022-A4352-money-national-puf-payment]] — documented_fact (DME-E-5d3188cf35d5311f566e); sources: [[DME-SRC-NATIONAL-2022-A4352]]
- cites: [[DME-SRC-PUF-2022-A4352]] — documented_fact (edge-6f1b209a00d9d8fb9ca0); sources: [[DME-SRC-PUF-2022-A4352]]
- cites: [[DME-SRC-NATIONAL-2022-A4352]] — documented_fact (edge-fc6bfec9daff46c6d5a4); sources: [[DME-SRC-NATIONAL-2022-A4352]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-aabed5b7bfebdeaf3c72)
