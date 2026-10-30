---
id: "DME-COHORT-2022-A4353"
type: "dataset_cohort"
title: "2022 A4353: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4353: published supplier rows

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
      "allowed": "51240498.68",
      "puf_payment": "39176515.57",
      "standardized_payment": "39037374.52",
      "submitted": "77286803.94"
    },
    "claims": "31093",
    "code": "A4353",
    "description": [
      "Intermittent urinary catheter, with insertion supplies"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "4725",
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
      "Tot_Suplr_Benes": 235,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "393.98",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "15.04",
    "payment_share_top10_pct": "46.88",
    "payment_share_top1_pct": "14.95",
    "payment_share_top5_pct": "35.13",
    "rental_indicators": [
      "N"
    ],
    "rows": 322,
    "rows_with_suppressed_beneficiaries": 235,
    "services": "6004669",
    "supplier_median_payment_per_service": "6.68",
    "supplier_median_services_per_known_beneficiary": "1075.98",
    "supplier_payment_median_usd": "24320.40",
    "supplier_payment_p90_usd": "220686.83",
    "suppliers": 322,
    "weighted_payment_per_service": "6.52",
    "year": 2022
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2022-A4353]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2022-A4353-money-allowed]] — documented_fact (DME-E-428d4af981a93abf5431); sources: [[DME-SRC-PUF-2022-A4353]]
- reports_amount: [[DME-COHORT-2022-A4353-money-puf_payment]] — documented_fact (DME-E-83c564a5a6c732b00cbe); sources: [[DME-SRC-PUF-2022-A4353]]
- reports_amount: [[DME-COHORT-2022-A4353-money-standardized_payment]] — documented_fact (DME-E-be061cff39c020c378db); sources: [[DME-SRC-PUF-2022-A4353]]
- reports_amount: [[DME-COHORT-2022-A4353-money-submitted]] — documented_fact (DME-E-d7419551f47851333cd2); sources: [[DME-SRC-PUF-2022-A4353]]
- cites: [[DME-SRC-PUF-2022-A4353]] — documented_fact (edge-4b907d1f3ed3d8d52ca3); sources: [[DME-SRC-PUF-2022-A4353]]

## Backlinks

- [[DME-CHANGE-2022-2023-A4353]]: compares_cohort — documented_fact (DME-E-6c1b6a91472ee7e9251a)
- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-bb0eeab9d490d51de0a8)
