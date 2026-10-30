---
id: "DME-NATIONAL-CHECK-2024-A4352"
type: "finding"
title: "2024 A4352: supplier detail versus national aggregate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4352: supplier detail versus national aggregate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "not_additive_with_supplier_detail": true,
  "reconciliation": {
    "code": "A4352",
    "detail_payment_coverage_pct": "98.82",
    "detail_service_coverage_pct": "98.74",
    "national_amounts_usd_reconstructed": {
      "allowed": "248088072.12",
      "puf_payment": "190933171.56",
      "standardized_payment": "203051659.24",
      "submitted": "360459690.77"
    },
    "national_beneficiaries_sum_across_rental": 35414,
    "national_claims": 183132,
    "national_less_detail_payment_usd": "2245287.52",
    "national_services": "30110190",
    "national_suppliers_sum_across_rental": 1127,
    "note": "National table includes underlying claims hidden from supplier detail; totals reconstructed from rounded averages. Beneficiaries overlap across codes; do not sum them.",
    "year": 2024
  },
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-NATIONAL-2024-A4352]]
- [[DME-SRC-PUF-2024-A4352]]

## Outgoing relationships

- reports_amount: [[DME-NATIONAL-CHECK-2024-A4352-money-national-puf-payment]] — documented_fact (DME-E-344d9612b07d366d2ff9); sources: [[DME-SRC-NATIONAL-2024-A4352]]
- cites: [[DME-SRC-PUF-2024-A4352]] — documented_fact (edge-60df2bdeb566a7e06b92); sources: [[DME-SRC-PUF-2024-A4352]]
- cites: [[DME-SRC-NATIONAL-2024-A4352]] — documented_fact (edge-98287cd6623006b0409d); sources: [[DME-SRC-NATIONAL-2024-A4352]]

## Backlinks

- [[DME-INV-20261029]]: records_finding — documented_fact (DME-E-2a406b391dd5e60e0ede)
