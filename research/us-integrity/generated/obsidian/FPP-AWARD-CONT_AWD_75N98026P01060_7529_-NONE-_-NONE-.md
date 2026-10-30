---
id: "FPP-AWARD-CONT_AWD_75N98026P01060_7529_-NONE-_-NONE-"
type: "award_observation"
title: "75N98026P01060"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 75N98026P01060

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "amount_interpretation": "award_obligations_are_not_unit_prices",
  "no_adverse_inference": true,
  "observation": {
    "amount_basis": "cumulative_award_obligation_not_unit_price_or_cash_payment",
    "api_detail_url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_75N98026P01060_7529_-NONE-_-NONE-/",
    "award_obligation_usd": "399800.00",
    "award_url": "https://www.usaspending.gov/award/CONT_AWD_75N98026P01060_7529_-NONE-_-NONE-",
    "awarding_office": null,
    "awarding_subtier": "National Institutes of Health",
    "awarding_toptier": "Department of Health and Human Services",
    "base_obligation_date": "2026-07-20",
    "date_signed": null,
    "description": "NHLBI: SUPPLY: COMET PACKAGE: AUTOMATED SEQIF STAINER AND IMAGING SYSTEM FOR SPATIAL MULTIOMICS ANALYSIS",
    "estimated_loss_usd": null,
    "express_report_in_description": false,
    "funding_office": null,
    "funding_subtier": "National Institutes of Health",
    "funding_toptier": "Department of Health and Human Services",
    "generated_award_id": "CONT_AWD_75N98026P01060_7529_-NONE-_-NONE-",
    "line_observation_ids": [],
    "missingness": {
      "awarding_office": "detail_not_requested",
      "buyer_benefit_or_kickback": "not_acquired",
      "cash_payment_or_invoice": "not_acquired",
      "date_signed": "detail_not_requested",
      "delivery_acceptance": "not_acquired",
      "exact_production_item_and_unit": "not_acquired",
      "independent_like_for_like_price": "not_acquired",
      "individual_price_selection_decision_maker": "not_identified",
      "original_order_lines": "not_acquired",
      "parent_award": "detail_not_requested",
      "solicitation": "detail_not_requested",
      "supplier_cost_or_markup": "not_acquired"
    },
    "naics": "334516",
    "observation_id": "award-75N98026P01060",
    "parent_generated_award_id": null,
    "parent_piid": null,
    "performance_end": "2027-01-20",
    "performance_start": "2026-07-20",
    "performance_state": "CA",
    "piid": "75N98026P01060",
    "pricing_type": null,
    "professional_officer_role_excerpt": null,
    "psc": "6515",
    "recipient_name": "ADVANCED CELL DIAGNOSTICS, INC.",
    "recipient_uei": "UD6XW8DAGLK6",
    "reported_number_offers": null,
    "sample_page_rank": 6,
    "solicitation_id": null,
    "source_ids": [
      "usaspending-search-hhs-medical"
    ],
    "stratum": "hhs-medical",
    "total_outlays_usd": "0.00",
    "undiscovered_status": "not_established",
    "unit_price_note": "Use separately typed CLIN records; heterogeneous award has no single unit price.",
    "unit_price_usd": null
  },
  "original_projection_id": "award:CONT_AWD_75N98026P01060_7529_-NONE-_-NONE-",
  "public_record": true,
  "visibility": "public"
}
```

## Sources

- [[FPP-SRC-usaspending-search-hhs-medical]]

## Outgoing relationships

- reports_cumulative_obligation: [[FPP-OBLIGATION-CONT_AWD_75N98026P01060_7529_-NONE-_-NONE-]] — documented_fact (PA-E-50089af4def12ae3e4867fd6); sources: [[FPP-SRC-usaspending-search-hhs-medical]]
- reported_award_recipient: [[FPP-UEI-UD6XW8DAGLK6]] — documented_fact (PA-E-9694ff241e70d2737f6b910a); sources: [[FPP-SRC-usaspending-search-hhs-medical]]
- cites: [[FPP-SRC-usaspending-search-hhs-medical]] — documented_fact (edge-458c07629c4088f361df); sources: [[FPP-SRC-usaspending-search-hhs-medical]]

## Backlinks

- [[FPP-COHORT-20261030]]: includes_award_observation — documented_fact (PA-E-7a000a03071f6181be0ae74b)
