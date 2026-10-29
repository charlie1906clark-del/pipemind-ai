---
id: "DME-COHORT-2023-A4353"
type: "dataset_cohort"
title: "2023 A4353: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2023 A4353: published supplier rows

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
      "allowed": "3904854765.10",
      "puf_payment": "3057362798.24",
      "standardized_payment": "3131912968.00",
      "submitted": "4082795910.61"
    },
    "claims": "569453",
    "code": "A4353",
    "description": [
      "Intermittent urinary catheter, with insertion supplies"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "523496",
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
      "Tot_Suplr_Benes": 230,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "1069.15",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "0.21",
    "payment_share_top10_pct": "92.65",
    "payment_share_top1_pct": "18.02",
    "payment_share_top5_pct": "62.80",
    "rental_indicators": [
      "N"
    ],
    "rows": 332,
    "rows_with_suppressed_beneficiaries": 230,
    "services": "429227298",
    "supplier_median_payment_per_service": "7.21",
    "supplier_median_services_per_known_beneficiary": "1033.45",
    "supplier_payment_median_usd": "31997.54",
    "supplier_payment_p90_usd": "380566.04",
    "suppliers": 332,
    "weighted_payment_per_service": "7.12",
    "year": 2023
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2023-A4353]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2023-A4353-money-standardized_payment]] — documented_fact (DME-E-2a35a11dd07d706b6797); sources: [[DME-SRC-PUF-2023-A4353]]
- reports_amount: [[DME-COHORT-2023-A4353-money-allowed]] — documented_fact (DME-E-59233aea63320db7e2e3); sources: [[DME-SRC-PUF-2023-A4353]]
- reports_amount: [[DME-COHORT-2023-A4353-money-submitted]] — documented_fact (DME-E-9afcc24154f811c8d991); sources: [[DME-SRC-PUF-2023-A4353]]
- reports_amount: [[DME-COHORT-2023-A4353-money-puf_payment]] — documented_fact (DME-E-c3db385d5d849948e20a); sources: [[DME-SRC-PUF-2023-A4353]]
- cites: [[DME-SRC-PUF-2023-A4353]] — documented_fact (edge-4e6bb87411a1d4cee342); sources: [[DME-SRC-PUF-2023-A4353]]

## Backlinks

- [[DME-CHANGE-2023-2024-A4353]]: compares_cohort — documented_fact (DME-E-143f2aaff5d2472eb07d)
- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-8c17b72bfe69decb0eb6)
- [[DME-CHANGE-2022-2023-A4353]]: compares_cohort — documented_fact (DME-E-d663abe9c2fa94e6f60e)
