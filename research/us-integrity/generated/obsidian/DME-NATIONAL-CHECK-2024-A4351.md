---
id: "DME-NATIONAL-CHECK-2024-A4351"
type: "finding"
title: "2024 A4351: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4351: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4351",
    "detail_payment_coverage_pct": "99.03",
    "detail_service_coverage_pct": "98.96",
    "national_amounts_usd_reconstructed": {
      "allowed": "161744723.80",
      "puf_payment": "121999530.80",
      "standardized_payment": "129612104.73",
      "submitted": "428531956.55"
    },
    "national_beneficiaries_sum_across_rental": 70376,
    "national_claims": 377854,
    "national_less_detail_payment_usd": "1180095.56",
    "national_services": "69464400",
    "national_suppliers_sum_across_rental": 2220,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2024
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2024-A4351]]
- [[DME-SRC-PUF-2024-A4351]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2024-A4351-money-national-puf-payment]] — documented_fact (DME-E-70e0370e66eeaa233e92); sources: [[DME-SRC-NATIONAL-2024-A4351]]
- cites: [[DME-SRC-PUF-2024-A4351]] — documented_fact (edge-7d42f78d8c2c86d4dde5); sources: [[DME-SRC-PUF-2024-A4351]]
- cites: [[DME-SRC-NATIONAL-2024-A4351]] — documented_fact (edge-c11a90b4694d6cb28b98); sources: [[DME-SRC-NATIONAL-2024-A4351]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-0251a75f149e545d9a5c)
