---
id: "DME-NATIONAL-CHECK-2022-A4353"
type: "finding"
title: "2022 A4353: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4353: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4353",
    "detail_payment_coverage_pct": "95.84",
    "detail_service_coverage_pct": "95.62",
    "national_amounts_usd_reconstructed": {
      "allowed": "53519355.06",
      "puf_payment": "40876216.24",
      "standardized_payment": "40776758.78",
      "submitted": "80424571.80"
    },
    "national_beneficiaries_sum_across_rental": 5731,
    "national_claims": 32754,
    "national_less_detail_payment_usd": "1699700.67",
    "national_services": "6279809",
    "national_suppliers_sum_across_rental": 720,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2022
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2022-A4353]]
- [[DME-SRC-PUF-2022-A4353]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2022-A4353-money-national-puf-payment]] — documented_fact (DME-E-a4be747d8fbea5018b4b); sources: [[DME-SRC-NATIONAL-2022-A4353]]
- cites: [[DME-SRC-NATIONAL-2022-A4353]] — documented_fact (edge-3ad9f63e49319ab72305); sources: [[DME-SRC-NATIONAL-2022-A4353]]
- cites: [[DME-SRC-PUF-2022-A4353]] — documented_fact (edge-d3af21232d500fdec81f); sources: [[DME-SRC-PUF-2022-A4353]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-5179384fbd8a1481c77e)
