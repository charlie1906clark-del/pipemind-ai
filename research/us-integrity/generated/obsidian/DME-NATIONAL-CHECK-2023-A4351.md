---
id: "DME-NATIONAL-CHECK-2023-A4351"
type: "finding"
title: "2023 A4351: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4351: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4351",
    "detail_payment_coverage_pct": "99.11",
    "detail_service_coverage_pct": "99.03",
    "national_amounts_usd_reconstructed": {
      "allowed": "180999829.65",
      "puf_payment": "136673833.72",
      "standardized_payment": "144910340.55",
      "submitted": "446344427.30"
    },
    "national_beneficiaries_sum_across_rental": 87545,
    "national_claims": 400212,
    "national_less_detail_payment_usd": "1218612.80",
    "national_services": "79525705",
    "national_suppliers_sum_across_rental": 2374,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2023
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2023-A4351]]
- [[DME-SRC-PUF-2023-A4351]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2023-A4351-money-national-puf-payment]] — documented_fact (DME-E-2072f1fd20af5b54b320); sources: [[DME-SRC-NATIONAL-2023-A4351]]
- cites: [[DME-SRC-NATIONAL-2023-A4351]] — documented_fact (edge-568e49f722027519085e); sources: [[DME-SRC-NATIONAL-2023-A4351]]
- cites: [[DME-SRC-PUF-2023-A4351]] — documented_fact (edge-a705b19bf0d577057663); sources: [[DME-SRC-PUF-2023-A4351]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-ce3b60f345d83122ef08)
