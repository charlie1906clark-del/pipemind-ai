---
id: "DME-COHORT-2024-A4353"
type: "dataset_cohort"
title: "2024 A4353: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4353: published supplier rows

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
      "allowed": "1483828000.16",
      "puf_payment": "1153543262.92",
      "standardized_payment": "1165227698.80",
      "submitted": "1559220129.75"
    },
    "claims": "270631",
    "code": "A4353",
    "description": [
      "Intermittent urinary catheter, with insertion supplies"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "245150",
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
      "Tot_Suplr_Benes": 236,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "1525.41",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "0.57",
    "payment_share_top10_pct": "96.88",
    "payment_share_top1_pct": "29.21",
    "payment_share_top5_pct": "70.44",
    "rental_indicators": [
      "N"
    ],
    "rows": 332,
    "rows_with_suppressed_beneficiaries": 236,
    "services": "156793666",
    "supplier_median_payment_per_service": "7.41",
    "supplier_median_services_per_known_beneficiary": "1049.58",
    "supplier_payment_median_usd": "30382.05",
    "supplier_payment_p90_usd": "345689.78",
    "suppliers": 332,
    "weighted_payment_per_service": "7.36",
    "year": 2024
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2024-A4353]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2024-A4353-money-allowed]] — documented_fact (DME-E-35df0eb662f943c251de); sources: [[DME-SRC-PUF-2024-A4353]]
- reports_amount: [[DME-COHORT-2024-A4353-money-standardized_payment]] — documented_fact (DME-E-3b5212065a8cf57063e1); sources: [[DME-SRC-PUF-2024-A4353]]
- reports_amount: [[DME-COHORT-2024-A4353-money-submitted]] — documented_fact (DME-E-850baad777743cbf2dff); sources: [[DME-SRC-PUF-2024-A4353]]
- reports_amount: [[DME-COHORT-2024-A4353-money-puf_payment]] — documented_fact (DME-E-c5870b93a27f3d26e01f); sources: [[DME-SRC-PUF-2024-A4353]]
- cites: [[DME-SRC-PUF-2024-A4353]] — documented_fact (edge-8546efa121e3da448ce9); sources: [[DME-SRC-PUF-2024-A4353]]

## Backlinks

- [[DME-CHANGE-2023-2024-A4353]]: compares_cohort — documented_fact (DME-E-d4d0b535e0edc868bf5a)
- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-e207729d16db24c78b1c)
