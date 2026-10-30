---
id: "DME-COHORT-2022-A4352"
type: "dataset_cohort"
title: "2022 A4352: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2022 A4352: published supplier rows

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
      "allowed": "341168533.48",
      "puf_payment": "265584824.84",
      "standardized_payment": "281647763.93",
      "submitted": "478563968.49"
    },
    "claims": "182716",
    "code": "A4352",
    "description": [
      "Intermittent urinary catheter; coude (curved) tip, with or without coating (teflon, silicone, silicone elastomeric, or hydrophilic, etc.), each"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "45899",
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
      "Tot_Suplr_Benes": 398,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "2106.36",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "2.63",
    "payment_share_top10_pct": "80.03",
    "payment_share_top1_pct": "39.75",
    "payment_share_top5_pct": "73.21",
    "rental_indicators": [
      "N"
    ],
    "rows": 567,
    "rows_with_suppressed_beneficiaries": 398,
    "services": "46266852",
    "supplier_median_payment_per_service": "5.66",
    "supplier_median_services_per_known_beneficiary": "743.11",
    "supplier_payment_median_usd": "20300.19",
    "supplier_payment_p90_usd": "270061.05",
    "suppliers": 567,
    "weighted_payment_per_service": "5.74",
    "year": 2022
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2022-A4352]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2022-A4352-money-submitted]] — documented_fact (DME-E-0f763eb60203b5452cbc); sources: [[DME-SRC-PUF-2022-A4352]]
- reports_amount: [[DME-COHORT-2022-A4352-money-allowed]] — documented_fact (DME-E-39007662929f98050bb5); sources: [[DME-SRC-PUF-2022-A4352]]
- reports_amount: [[DME-COHORT-2022-A4352-money-standardized_payment]] — documented_fact (DME-E-73f6b8e720795e669da8); sources: [[DME-SRC-PUF-2022-A4352]]
- reports_amount: [[DME-COHORT-2022-A4352-money-puf_payment]] — documented_fact (DME-E-a95570cf05fac0fcb4da); sources: [[DME-SRC-PUF-2022-A4352]]
- cites: [[DME-SRC-PUF-2022-A4352]] — documented_fact (edge-0a37eeb3eff7156af076); sources: [[DME-SRC-PUF-2022-A4352]]

## Backlinks

- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-15ae241a0a8d2508fa42)
- [[DME-CHANGE-2022-2023-A4352]]: compares_cohort — documented_fact (DME-E-dfa0c2eccd9390ced9f9)
