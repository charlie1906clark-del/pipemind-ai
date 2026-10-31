---
id: "FPP-AWARD-CONT_AWD_SPE4A626PX773_9700_-NONE-_-NONE-"
type: "award_observation"
title: "SPE4A626PX773"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626PX773

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "amount_interpretation": "award_obligations_are_not_unit_prices",
  "no_adverse_inference": true,
  "observation": {
    "amount_basis": "cumulative_award_obligation_not_unit_price_or_cash_payment",
    "api_detail_url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE4A626PX773_9700_-NONE-_-NONE-/",
    "award_obligation_usd": "213598.50",
    "award_url": "https://www.usaspending.gov/award/CONT_AWD_SPE4A626PX773_9700_-NONE-_-NONE-",
    "awarding_office": null,
    "awarding_subtier": "Defense Logistics Agency",
    "awarding_toptier": "Department of Defense",
    "base_obligation_date": "2026-07-14",
    "date_signed": null,
    "description": "8512235512!BOLT,SHOULDER",
    "estimated_loss_usd": null,
    "express_report_in_description": false,
    "funding_office": null,
    "funding_subtier": "Defense Logistics Agency",
    "funding_toptier": "Department of Defense",
    "generated_award_id": "CONT_AWD_SPE4A626PX773_9700_-NONE-_-NONE-",
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
    "naics": "332722",
    "observation_id": "award-SPE4A626PX773",
    "parent_generated_award_id": null,
    "parent_piid": null,
    "performance_end": "2026-09-02",
    "performance_start": "2026-07-14",
    "performance_state": "WA",
    "piid": "SPE4A626PX773",
    "pricing_type": null,
    "professional_officer_role_excerpt": null,
    "psc": "5306",
    "recipient_name": "ACTION MANUFACTURED PRODUCTS",
    "recipient_uei": "GMZLYNC8RMC7",
    "reported_number_offers": null,
    "sample_page_rank": 3,
    "solicitation_id": null,
    "source_ids": [
      "usaspending-search-dla-bolts"
    ],
    "stratum": "dla-bolts",
    "total_outlays_usd": null,
    "undiscovered_status": "not_established",
    "unit_price_note": "Use separately typed CLIN records; heterogeneous award has no single unit price.",
    "unit_price_usd": null
  },
  "original_projection_id": "award:CONT_AWD_SPE4A626PX773_9700_-NONE-_-NONE-",
  "public_record": true,
  "visibility": "public"
}
```

## Sources

- [[FPP-SRC-usaspending-search-dla-bolts]]

## Outgoing relationships

- reported_award_recipient: [[FPP-UEI-GMZLYNC8RMC7]] — documented_fact (PA-E-15c76024d73c9194f8ff5ec9); sources: [[FPP-SRC-usaspending-search-dla-bolts]]
- reports_cumulative_obligation: [[FPP-OBLIGATION-CONT_AWD_SPE4A626PX773_9700_-NONE-_-NONE-]] — documented_fact (PA-E-be6967e76e6a0d6a5a053bc2); sources: [[FPP-SRC-usaspending-search-dla-bolts]]
- cites: [[FPP-SRC-usaspending-search-dla-bolts]] — documented_fact (edge-58e4889f5b35bf8c9d73); sources: [[FPP-SRC-usaspending-search-dla-bolts]]

## Backlinks

- [[FPP-COHORT-20261030]]: includes_award_observation — documented_fact (PA-E-45c6adb62d934bd9f627cf69)
