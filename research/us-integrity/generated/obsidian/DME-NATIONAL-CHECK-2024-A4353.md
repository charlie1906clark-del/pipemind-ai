---
id: "DME-NATIONAL-CHECK-2024-A4353"
type: "finding"
title: "2024 A4353: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4353: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4353",
    "detail_payment_coverage_pct": "99.85",
    "detail_service_coverage_pct": "99.84",
    "national_amounts_usd_reconstructed": {
      "allowed": "1486107942.53",
      "puf_payment": "1155271517.52",
      "standardized_payment": "1167002313.46",
      "submitted": "1562316579.58"
    },
    "national_beneficiaries_sum_across_rental": 244723,
    "national_claims": 271980,
    "national_less_detail_payment_usd": "1728254.60",
    "national_services": "157039228",
    "national_suppliers_sum_across_rental": 672,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2024
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2024-A4353]]
- [[DME-SRC-PUF-2024-A4353]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2024-A4353-money-national-puf-payment]] — documented_fact (DME-E-119fb8bcda16a4504705); sources: [[DME-SRC-NATIONAL-2024-A4353]]
- cites: [[DME-SRC-NATIONAL-2024-A4353]] — documented_fact (edge-33b4e59e0a3eab98223e); sources: [[DME-SRC-NATIONAL-2024-A4353]]
- cites: [[DME-SRC-PUF-2024-A4353]] — documented_fact (edge-469ed055bee00eb004b1); sources: [[DME-SRC-PUF-2024-A4353]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-2d8219afae98ec01b23d)
