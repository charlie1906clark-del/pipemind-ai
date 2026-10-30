---
id: "DME-NATIONAL-CHECK-2023-A4352"
type: "finding"
title: "2023 A4352: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4352: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4352",
    "detail_payment_coverage_pct": "99.69",
    "detail_service_coverage_pct": "99.65",
    "national_amounts_usd_reconstructed": {
      "allowed": "908022416.35",
      "puf_payment": "707255528.31",
      "standardized_payment": "742916794.02",
      "submitted": "1134549546.44"
    },
    "national_beneficiaries_sum_across_rental": 157818,
    "national_claims": 307298,
    "national_less_detail_payment_usd": "2210163.19",
    "national_services": "111686945",
    "national_suppliers_sum_across_rental": 1165,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2023
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2023-A4352]]
- [[DME-SRC-PUF-2023-A4352]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2023-A4352-money-national-puf-payment]] — documented_fact (DME-E-76ce6045a763143ba177); sources: [[DME-SRC-NATIONAL-2023-A4352]]
- cites: [[DME-SRC-PUF-2023-A4352]] — documented_fact (edge-6c65526bbf88e88c31b5); sources: [[DME-SRC-PUF-2023-A4352]]
- cites: [[DME-SRC-NATIONAL-2023-A4352]] — documented_fact (edge-ddd687ce8489ac436969); sources: [[DME-SRC-NATIONAL-2023-A4352]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-740e6172944acd1a9557)
