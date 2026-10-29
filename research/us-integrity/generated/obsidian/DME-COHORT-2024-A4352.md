---
id: "DME-COHORT-2024-A4352"
type: "dataset_cohort"
title: "2024 A4352: published supplier rows"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 2024 A4352: published supplier rows

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
      "allowed": "245161152.62",
      "puf_payment": "188687884.04",
      "standardized_payment": "200514032.30",
      "submitted": "356666512.85"
    },
    "claims": "180680",
    "code": "A4352",
    "description": [
      "Intermittent urinary catheter; coude (curved) tip, with or without coating (teflon, silicone, silicone elastomeric, or hydrophilic, etc.), each"
    ],
    "known_supplier_beneficiary_sum_not_unique_people": "35046",
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
      "Tot_Suplr_Benes": 376,
      "Tot_Suplr_Clms": 0,
      "Tot_Suplr_Srvcs": 0
    },
    "payment_hhi_0_to_10000": "1554.97",
    "payment_share_rows_with_suppressed_beneficiaries_pct": "3.82",
    "payment_share_top10_pct": "68.28",
    "payment_share_top1_pct": "36.90",
    "payment_share_top5_pct": "59.77",
    "rental_indicators": [
      "N"
    ],
    "rows": 569,
    "rows_with_suppressed_beneficiaries": 376,
    "services": "29730699",
    "supplier_median_payment_per_service": "6.17",
    "supplier_median_services_per_known_beneficiary": "732.33",
    "supplier_payment_median_usd": "25248.94",
    "supplier_payment_p90_usd": "326879.57",
    "suppliers": 569,
    "weighted_payment_per_service": "6.35",
    "year": 2024
  },
  "national_unique_beneficiaries": "not_calculable_from_supplier_sums",
  "no_fraud_determination": true,
  "scope": "All publicly returned supplier/service rows for each HCPCS, all locations and rental indicators; not all Medicare claims or all suppliers.",
  "visibility": "public"
}
```

## Sources

- [[DME-SRC-PUF-2024-A4352]]

## Outgoing relationships

- reports_amount: [[DME-COHORT-2024-A4352-money-submitted]] — documented_fact (DME-E-2e7f1796bd867937e5dd); sources: [[DME-SRC-PUF-2024-A4352]]
- reports_amount: [[DME-COHORT-2024-A4352-money-puf_payment]] — documented_fact (DME-E-3d97dfef63ddf8ff83cf); sources: [[DME-SRC-PUF-2024-A4352]]
- reports_amount: [[DME-COHORT-2024-A4352-money-allowed]] — documented_fact (DME-E-9836a7e12b73c40c6ed4); sources: [[DME-SRC-PUF-2024-A4352]]
- reports_amount: [[DME-COHORT-2024-A4352-money-standardized_payment]] — documented_fact (DME-E-f41b2d8153574438153a); sources: [[DME-SRC-PUF-2024-A4352]]
- cites: [[DME-SRC-PUF-2024-A4352]] — documented_fact (edge-5d2821f0686787b691c3); sources: [[DME-SRC-PUF-2024-A4352]]

## Backlinks

- [[DME-CHANGE-2023-2024-A4352]]: compares_cohort — documented_fact (DME-E-4e39a8f6c5392223ec8b)
- [[DME-INV-20261029]]: examines_cohort — documented_fact (DME-E-61baf447290937fccab7)
