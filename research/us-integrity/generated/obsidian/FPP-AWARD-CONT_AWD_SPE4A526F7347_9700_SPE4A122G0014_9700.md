---
id: "FPP-AWARD-CONT_AWD_SPE4A526F7347_9700_SPE4A122G0014_9700"
type: "award_observation"
title: "SPE4A526F7347"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A526F7347

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "amount_interpretation": "award_obligations_are_not_unit_prices",
  "no_adverse_inference": true,
  "observation": {
    "amount_basis": "cumulative_award_obligation_not_unit_price_or_cash_payment",
    "api_detail_url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE4A526F7347_9700_SPE4A122G0014_9700/",
    "award_obligation_usd": "91284.75",
    "award_url": "https://www.usaspending.gov/award/CONT_AWD_SPE4A526F7347_9700_SPE4A122G0014_9700",
    "awarding_office": null,
    "awarding_subtier": "Defense Logistics Agency",
    "awarding_toptier": "Department of Defense",
    "base_obligation_date": "2026-07-16",
    "date_signed": null,
    "description": "8512198871!BOLT,CLOSE TOLERANC",
    "estimated_loss_usd": null,
    "express_report_in_description": false,
    "funding_office": null,
    "funding_subtier": "Defense Logistics Agency",
    "funding_toptier": "Department of Defense",
    "generated_award_id": "CONT_AWD_SPE4A526F7347_9700_SPE4A122G0014_9700",
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
    "naics": "336413",
    "observation_id": "award-SPE4A526F7347",
    "parent_generated_award_id": null,
    "parent_piid": null,
    "performance_end": "2027-12-14",
    "performance_start": "2026-07-16",
    "performance_state": "AZ",
    "piid": "SPE4A526F7347",
    "pricing_type": null,
    "professional_officer_role_excerpt": null,
    "psc": "5306",
    "recipient_name": "HONEYWELL INTERNATIONAL INC.",
    "recipient_uei": "ZLHMCNLMEYK1",
    "reported_number_offers": null,
    "sample_page_rank": 8,
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
  "original_projection_id": "award:CONT_AWD_SPE4A526F7347_9700_SPE4A122G0014_9700",
  "public_record": true,
  "visibility": "public"
}
```

## Sources

- [[FPP-SRC-usaspending-search-dla-bolts]]

## Outgoing relationships

- reports_cumulative_obligation: [[FPP-OBLIGATION-CONT_AWD_SPE4A526F7347_9700_SPE4A122G0014_9700]] — documented_fact (PA-E-a25d4e3aee6efec51e602b4f); sources: [[FPP-SRC-usaspending-search-dla-bolts]]
- reported_award_recipient: [[FPP-UEI-ZLHMCNLMEYK1]] — documented_fact (PA-E-c6623fb91d7ea9b1f1f56b9e); sources: [[FPP-SRC-usaspending-search-dla-bolts]]
- cites: [[FPP-SRC-usaspending-search-dla-bolts]] — documented_fact (edge-82d8a2e2ff58471e99b8); sources: [[FPP-SRC-usaspending-search-dla-bolts]]

## Backlinks

- [[FPP-COHORT-20261030]]: includes_award_observation — documented_fact (PA-E-38dcf8018713cdc8bb6229d4)
