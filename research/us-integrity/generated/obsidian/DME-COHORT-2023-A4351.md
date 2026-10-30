---
id: "DME-COHORT-2023-A4351"
type: "dataset_cohort"
title: "2023 A4351: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4351: published supplier rows

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
      "allowed": "179360364.65",
      "puf_payment": "135455220.92",
      "standardized_payment": "143518395.22",
      "submitted": "443455530.08"
    },
    "claims": "395328",
    "code": "A4351",
    "description": [
      "Intermittent urinary catheter; straight tip, with or without coating (teflon, silicone, silicone elastomer, or hydrophilic, etc.), each"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "86348",
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
      "Tot_Suplr_Benes": 997,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "856.28",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "4.55",
    "payment_share_top10_pct": "63.35",
    "payment_share_top1_pct": "24.17",
    "payment_share_top5_pct": "52.47",
    "rental_indicators": [
      "N"
    ],
    "rows": 1382,
    "rows_with_suppressed_beneficiaries": 997,
    "services": "78751615",
    "supplier_median_payment_per_service": "1.71",
    "supplier_median_services_per_known_beneficiary": "827.40",
    "supplier_payment_median_usd": "7099.09",
    "supplier_payment_p90_usd": "57135.19",
    "suppliers": 1382,
    "weighted_payment_per_service": "1.72",
    "year": 2023
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2023-A4351]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2023-A4351-money-standardized_payment]] — documented_fact (DME-E-53d082107d8678cdcbf0); sources: [[DME-SRC-PUF-2023-A4351]]
- reports_amount: [[DME-COHORT-2023-A4351-money-puf_payment]] — documented_fact (DME-E-9951248050dbaa7cefd8); sources: [[DME-SRC-PUF-2023-A4351]]
- reports_amount: [[DME-COHORT-2023-A4351-money-allowed]] — documented_fact (DME-E-c09a3646fe37c76ee7e7); sources: [[DME-SRC-PUF-2023-A4351]]
- reports_amount: [[DME-COHORT-2023-A4351-money-submitted]] — documented_fact (DME-E-e3d00f96aa6067145b4f); sources: [[DME-SRC-PUF-2023-A4351]]
- cites: [[DME-SRC-PUF-2023-A4351]] — documented_fact (edge-a8201b857e09ca52c38b); sources: [[DME-SRC-PUF-2023-A4351]]

## Backlinks

- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-31b7a92b5b28ccb0424d)
- [[DME-CHANGE-2023-2024-A4351]]: compares_cohort — documented_fact (DME-E-db7c93af9481c58fd05c)
- [[DME-CHANGE-2022-2023-A4351]]: compares_cohort — documented_fact (DME-E-f4ca83bf8309eae2f012)
