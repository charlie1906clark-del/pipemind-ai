---
id: "DME-COHORT-2023-A4352"
type: "dataset_cohort"
title: "2023 A4352: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4352: published supplier rows

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
      "allowed": "905157651.27",
      "puf_payment": "705045365.12",
      "standardized_payment": "740387396.77",
      "submitted": "1130957574.16"
    },
    "claims": "304682",
    "code": "A4352",
    "description": [
      "Intermittent urinary catheter; coude (curved) tip, with or without coating (teflon, silicone, silicone elastomeric, or hydrophilic, etc.), each"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "159239",
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
      "Tot_Suplr_Benes": 405,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "1751.32",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "1.06",
    "payment_share_top10_pct": "90.51",
    "payment_share_top1_pct": "24.80",
    "payment_share_top5_pct": "84.13",
    "rental_indicators": [
      "N"
    ],
    "rows": 586,
    "rows_with_suppressed_beneficiaries": 405,
    "services": "111301088",
    "supplier_median_payment_per_service": "6.01",
    "supplier_median_services_per_known_beneficiary": "725.45",
    "supplier_payment_median_usd": "21722.93",
    "supplier_payment_p90_usd": "323167.12",
    "suppliers": 586,
    "weighted_payment_per_service": "6.33",
    "year": 2023
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2023-A4352]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2023-A4352-money-puf_payment]] — documented_fact (DME-E-23c5c706c4ce4a6b90a5); sources: [[DME-SRC-PUF-2023-A4352]]
- reports_amount: [[DME-COHORT-2023-A4352-money-standardized_payment]] — documented_fact (DME-E-3aae800ef2736c2d2dc1); sources: [[DME-SRC-PUF-2023-A4352]]
- reports_amount: [[DME-COHORT-2023-A4352-money-submitted]] — documented_fact (DME-E-d0958be63cce0ecf8cbf); sources: [[DME-SRC-PUF-2023-A4352]]
- reports_amount: [[DME-COHORT-2023-A4352-money-allowed]] — documented_fact (DME-E-e3f8bf721f7a54a23b6f); sources: [[DME-SRC-PUF-2023-A4352]]
- cites: [[DME-SRC-PUF-2023-A4352]] — documented_fact (edge-5de5bfc07c0f3a53dedb); sources: [[DME-SRC-PUF-2023-A4352]]

## Backlinks

- [[DME-CHANGE-2023-2024-A4352]]: compares_cohort — documented_fact (DME-E-3d8413cce590ef84461c)
- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-85b3da617d87c59b2016)
- [[DME-CHANGE-2022-2023-A4352]]: compares_cohort — documented_fact (DME-E-dccc8461a2da030e360e)
