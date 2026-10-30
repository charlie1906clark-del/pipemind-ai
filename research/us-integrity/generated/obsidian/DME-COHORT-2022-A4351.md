---
id: "DME-COHORT-2022-A4351"
type: "dataset_cohort"
title: "2022 A4351: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4351: published supplier rows

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
      "allowed": "152106059.86",
      "puf_payment": "114823304.02",
      "standardized_payment": "121171483.67",
      "submitted": "332619729.56"
    },
    "claims": "399325",
    "code": "A4351",
    "description": [
      "Intermittent urinary catheter; straight tip, with or without coating (teflon, silicone, silicone elastomer, or hydrophilic, etc.), each"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "75767",
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
      "Tot_Suplr_Benes": 1092,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "953.00",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "5.35",
    "payment_share_top10_pct": "60.91",
    "payment_share_top1_pct": "25.54",
    "payment_share_top5_pct": "51.63",
    "rental_indicators": [
      "N"
    ],
    "rows": 1483,
    "rows_with_suppressed_beneficiaries": 1092,
    "services": "72681873",
    "supplier_median_payment_per_service": "1.58",
    "supplier_median_services_per_known_beneficiary": "833.05",
    "supplier_payment_median_usd": "6356.10",
    "supplier_payment_p90_usd": "43388.65",
    "suppliers": 1483,
    "weighted_payment_per_service": "1.58",
    "year": 2022
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2022-A4351]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2022-A4351-money-puf_payment]] — documented_fact (DME-E-1c57b4decd5391df5054); sources: [[DME-SRC-PUF-2022-A4351]]
- reports_amount: [[DME-COHORT-2022-A4351-money-allowed]] — documented_fact (DME-E-5ddd676eae7a4fe63084); sources: [[DME-SRC-PUF-2022-A4351]]
- reports_amount: [[DME-COHORT-2022-A4351-money-standardized_payment]] — documented_fact (DME-E-6d5e617631a186348423); sources: [[DME-SRC-PUF-2022-A4351]]
- reports_amount: [[DME-COHORT-2022-A4351-money-submitted]] — documented_fact (DME-E-81a66e0ced66287e83f0); sources: [[DME-SRC-PUF-2022-A4351]]
- cites: [[DME-SRC-PUF-2022-A4351]] — documented_fact (edge-ee3ef3765380f96bac60); sources: [[DME-SRC-PUF-2022-A4351]]

## Backlinks

- [[DME-CHANGE-2022-2023-A4351]]: compares_cohort — documented_fact (DME-E-71204872f9f36222a88e)
- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-c9af696ef610daf2fad8)
