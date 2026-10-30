---
id: "DME-NATIONAL-CHECK-2023-A4353"
type: "finding"
title: "2023 A4353: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4353: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4353",
    "detail_payment_coverage_pct": "99.94",
    "detail_service_coverage_pct": "99.94",
    "national_amounts_usd_reconstructed": {
      "allowed": "3907243789.04",
      "puf_payment": "3059163823.61",
      "standardized_payment": "3133774694.55",
      "submitted": "4085976361.12"
    },
    "national_beneficiaries_sum_across_rental": 518185,
    "national_claims": 571072,
    "national_less_detail_payment_usd": "1801025.37",
    "national_services": "429493441",
    "national_suppliers_sum_across_rental": 703,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2023
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2023-A4353]]
- [[DME-SRC-PUF-2023-A4353]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2023-A4353-money-national-puf-payment]] — documented_fact (DME-E-2540f8f9e88b2322a5da); sources: [[DME-SRC-NATIONAL-2023-A4353]]
- cites: [[DME-SRC-PUF-2023-A4353]] — documented_fact (edge-03b95e0c6530469458f4); sources: [[DME-SRC-PUF-2023-A4353]]
- cites: [[DME-SRC-NATIONAL-2023-A4353]] — documented_fact (edge-f9f6a40d4127cfa1cb3a); sources: [[DME-SRC-NATIONAL-2023-A4353]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-3f10f7200d930bbf09c3)
