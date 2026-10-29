---
id: "DME-NATIONAL-CHECK-2022-A4351"
type: "finding"
title: "2022 A4351: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4351: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4351",
    "detail_payment_coverage_pct": "99.06",
    "detail_service_coverage_pct": "98.98",
    "national_amounts_usd_reconstructed": {
      "allowed": "153573912.12",
      "puf_payment": "115914393.40",
      "standardized_payment": "122405250.64",
      "submitted": "334709185.45"
    },
    "national_beneficiaries_sum_across_rental": 76307,
    "national_claims": 404259,
    "national_less_detail_payment_usd": "1091089.38",
    "national_services": "73429961",
    "national_suppliers_sum_across_rental": 2499,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2022
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2022-A4351]]
- [[DME-SRC-PUF-2022-A4351]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2022-A4351-money-national-puf-payment]] — documented_fact (DME-E-7434e54bad94a709ad98); sources: [[DME-SRC-NATIONAL-2022-A4351]]
- cites: [[DME-SRC-PUF-2022-A4351]] — documented_fact (edge-3e6994c9da10b76d34e7); sources: [[DME-SRC-PUF-2022-A4351]]
- cites: [[DME-SRC-NATIONAL-2022-A4351]] — documented_fact (edge-5361b4d0c4870ce47a75); sources: [[DME-SRC-NATIONAL-2022-A4351]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-4c057c15f40f20453540)
