---
id: "DME-COHORT-2024-A4351"
type: "dataset_cohort"
title: "2024 A4351: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4351: published supplier rows

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "cash_reconciliation": "not_performed",
  "complete_public_filtered_rows": true,
  "complete_underlying_claims": false,
  "metrics": {
    "amounts_usd_reconstructed": {
      "allowed": "160149565.31",
      "puf_payment": "120819435.24",
      "standardized_payment": "128281352.44",
      "submitted": "426309700.81"
    },
    "claims": "373474",
    "code": "A4351",
    "description": [
      "Intermittent urinary catheter; straight tip, with or without coating (teflon, silicone, silicone elastomer, or hydrophilic, etc.), each"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "69798",
    "minimum_claim_count": "11",
    "missing_fields": {
      "Avg_Suplr_Mdcr_Alowd_Amt": 0,
      "Avg_Suplr_Mdcr_Pymt_Amt": 0,
      "Avg_Suplr_Mdcr_Stdzd_Amt": 0,
      "Avg_Suplr_Sbmtd_Chrg": 0,
      "HCPCS_Cd": 0,
      "HCPCS_Desc": 0,
      "Suplr_NPI": 0,
      "Suplr_Prvdr_Ent_Cd": 0,
      "Suplr_Prvdr_Spclty_Cd": 0,
      "Suplr_Prvdr_Spclty_Desc": 0,
      "Suplr_Prvdr_State_Abrvtn": 0,
      "Suplr_Rentl_Ind": 0,
      "Tot_Suplr_Benes": 899,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "1062.92",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "4.77",
    "payment_share_top10_pct": "61.80",
    "payment_share_top1_pct": "28.93",
    "payment_share_top5_pct": "52.83",
    "rental_indicators": [
      "N"
    ],
    "rows": 1297,
    "rows_with_suppressed_beneficiaries": 899,
    "services": "68738868",
    "supplier_median_payment_per_service": "1.76",
    "supplier_median_services_per_known_beneficiary": "851.09",
    "supplier_payment_median_usd": "7797.89",
    "supplier_payment_p90_usd": "65212.36",
    "suppliers": 1297,
    "weighted_payment_per_service": "1.76",
    "year": 2024
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2024-A4351]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2024-A4351-money-submitted]] — documented_fact (DME-E-05d906b70d30fed0ecbe); sources: [[DME-SRC-PUF-2024-A4351]]
- reports_amount: [[DME-COHORT-2024-A4351-money-allowed]] — documented_fact (DME-E-46cbf2c09fc7ab33c2c8); sources: [[DME-SRC-PUF-2024-A4351]]
- reports_amount: [[DME-COHORT-2024-A4351-money-puf_payment]] — documented_fact (DME-E-d90319a58376043d3462); sources: [[DME-SRC-PUF-2024-A4351]]
- reports_amount: [[DME-COHORT-2024-A4351-money-standardized_payment]] — documented_fact (DME-E-e6d7fa432505df418418); sources: [[DME-SRC-PUF-2024-A4351]]
- cites: [[DME-SRC-PUF-2024-A4351]] — documented_fact (edge-9d557e0e987fbdda14ed); sources: [[DME-SRC-PUF-2024-A4351]]

## Backlinks

- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-3d6a5da5d35a1d45907e)
- [[DME-CHANGE-2023-2024-A4351]]: compares_cohort — documented_fact (DME-E-f8b49025b427af6a0726)
