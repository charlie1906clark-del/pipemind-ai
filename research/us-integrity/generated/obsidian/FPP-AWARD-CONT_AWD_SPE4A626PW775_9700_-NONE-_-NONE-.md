---
id: "FPP-AWARD-CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-"
type: "award_observation"
title: "SPE4A626PW775"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626PW775

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "amount_interpretation": "award_obligations_are_not_unit_prices",
  "no_adverse_inference": true,
  "observation": {
    "amount_basis": "cumulative_award_obligation_not_unit_price_or_cash_payment",
    "api_detail_url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-/",
    "award_obligation_usd": "615816.57",
    "award_url": "https://www.usaspending.gov/award/CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-",
    "awarding_office": "DLA AVIATION",
    "awarding_subtier": "Defense Logistics Agency",
    "awarding_toptier": "Department of Defense",
    "base_obligation_date": "2026-07-09",
    "date_signed": "2026-07-09",
    "description": "8512215906!BOLT,EXTERNALLY REL",
    "estimated_loss_usd": null,
    "express_report_in_description": false,
    "funding_office": "DLA AVIATION",
    "funding_subtier": "Defense Logistics Agency",
    "funding_toptier": "Department of Defense",
    "generated_award_id": "CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-",
    "line_observation_ids": [
      "SPE4A626PW775-0001",
      "SPE4A626PW775-0002"
    ],
    "missingness": {
      "awarding_office": "observed",
      "buyer_benefit_or_kickback": "not_acquired",
      "cash_payment_or_invoice": "not_acquired",
      "date_signed": "observed",
      "delivery_acceptance": "not_acquired",
      "exact_production_item_and_unit": "observed_on_original_award",
      "independent_like_for_like_price": "not_acquired",
      "individual_price_selection_decision_maker": "not_established_by_professional_officer_role",
      "original_order_lines": "acquired_two_clins",
      "parent_award": "null_in_detail_response",
      "solicitation": "observed",
      "supplier_cost_or_markup": "not_acquired"
    },
    "naics": "332722",
    "observation_id": "award-SPE4A626PW775",
    "parent_generated_award_id": null,
    "parent_piid": null,
    "performance_end": "2028-04-10",
    "performance_start": "2026-07-09",
    "performance_state": "TX",
    "piid": "SPE4A626PW775",
    "pricing_type": "FIRM FIXED PRICE",
    "professional_officer_role_excerpt": "selected/dla-award-page1-role-selected.txt",
    "psc": "5306",
    "recipient_name": "DON INDUSTRIAL GROUP LLC",
    "recipient_uei": "XN9HKU6LUM59",
    "reported_number_offers": "4",
    "sample_page_rank": 1,
    "solicitation_id": "SPE4A626Q0688",
    "source_ids": [
      "usaspending-search-dla-bolts",
      "usaspending-detail-SPE4A626PW775"
    ],
    "stratum": "dla-bolts",
    "total_outlays_usd": null,
    "undiscovered_status": "not_established",
    "unit_price_note": "Use separately typed CLIN records; heterogeneous award has no single unit price.",
    "unit_price_usd": null
  },
  "original_projection_id": "award:CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-",
  "public_record": true,
  "visibility": "public"
}
```

## Sources

- [[FPP-SRC-usaspending-detail-SPE4A626PW775]]
- [[FPP-SRC-usaspending-search-dla-bolts]]

## Outgoing relationships

- awarding_office: [[FPP-OFFICE-8f80f4e4a25e58cb]] — documented_fact (PA-E-3facc9167fc96f95da1f418f); sources: [[FPP-SRC-usaspending-detail-SPE4A626PW775]]
- awarded_clin: [[FPP-LINE-SPE4A626PW775-0002]] — documented_fact (PA-E-4be292661a33459f4a7e4745); sources: [[FPP-SRC-dla-original-SPE4A626PW775]]
- reports_cumulative_obligation: [[FPP-OBLIGATION-CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-]] — documented_fact (PA-E-58e0e9f96b4827a8dae75247); sources: [[FPP-SRC-usaspending-detail-SPE4A626PW775]], [[FPP-SRC-usaspending-search-dla-bolts]]
- awarded_clin: [[FPP-LINE-SPE4A626PW775-0001]] — documented_fact (PA-E-7ec7baa4ef4c5a4b6586470c); sources: [[FPP-SRC-dla-original-SPE4A626PW775]]
- funding_office: [[FPP-OFFICE-8f80f4e4a25e58cb]] — documented_fact (PA-E-866f1f01c819d809da4370e5); sources: [[FPP-SRC-usaspending-detail-SPE4A626PW775]]
- reported_award_recipient: [[FPP-UEI-XN9HKU6LUM59]] — documented_fact (PA-E-ee6c1257aa0d4512d6e3fbf2); sources: [[FPP-SRC-usaspending-detail-SPE4A626PW775]], [[FPP-SRC-usaspending-search-dla-bolts]]
- cites: [[FPP-SRC-usaspending-detail-SPE4A626PW775]] — documented_fact (edge-153acfd89452da2dccfc); sources: [[FPP-SRC-usaspending-detail-SPE4A626PW775]]
- cites: [[FPP-SRC-usaspending-search-dla-bolts]] — documented_fact (edge-a0fe488fb716cc1d362f); sources: [[FPP-SRC-usaspending-search-dla-bolts]]

## Backlinks

- [[FPP-TP-AWARD-W775]]: same_exact_award_identifier — documented_fact (PA-E-53edf5af721bef1a7e85179b)
- [[FPP-DLA-LINE-RECONCILIATION]]: reconciles_selected_award — documented_fact (PA-E-dc9639a486ef441ee68aca5d)
- [[FPP-COHORT-20261030]]: includes_award_observation — documented_fact (PA-E-ebfe5d056a03da154e842540)
