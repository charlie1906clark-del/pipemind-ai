---
id: "FPP-LINE-SPE4A626PW775-0002"
type: "contract_line_observation"
title: "SPE4A626PW775-0002"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626PW775-0002

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "actual_payment_verified": false,
  "benchmark_qualified": false,
  "no_adverse_inference": true,
  "observation": {
    "actual_first_article_test_sample_quantity": "2",
    "actual_test_sample_quantity_source_page": 11,
    "additional_source_paths": [
      "selected/dla-award-page6.txt",
      "selected/dla-award-page7-e08-selected.txt",
      "selected/dla-award-page11-first-article-selected.txt"
    ],
    "clin": "0002",
    "delivery_date_source_page": 6,
    "delivery_due": "2027-08-13",
    "description": "Government First Article Test",
    "excess_amount_usd": null,
    "extended_amount_usd": "3500.00",
    "first_article_due_days_after_award": 400,
    "freight_payment": "CONTRACTOR",
    "government_notice_days_after_receipt": 180,
    "independent_comparator_unit_price_usd": null,
    "item_id": null,
    "item_id_type": null,
    "line_type": "first_article_test_requirement",
    "markup_percent": null,
    "observation_id": "SPE4A626PW775-0002",
    "page": 5,
    "piid": "SPE4A626PW775",
    "price_basis": "awarded_contract_line",
    "price_type": "Firm Fixed Price",
    "quantity": "1.000",
    "quantity_interpretation": "The number of units signifies the test requirement. Source directs actual test quantity to FAR clause 52.209-4. This is not one additional production bolt.",
    "source_paths": [
      "selected/dla-award-page5-selected.txt",
      "selected/dla-award-page5-first-article.png"
    ],
    "source_supplies_services_field": "0001 - S00000052",
    "test_article_quantity_not_added_to_production_quantity": true,
    "test_article_reuse_condition": "Clause(e) permits an approved first article to count toward contract quantity if it meets all acceptance requirements and was not consumed or destroyed in testing.",
    "unit": "EA",
    "unit_price_usd": "3500.00"
  },
  "original_projection_id": "line:SPE4A626PW775-0002",
  "public_record": true,
  "visibility": "public"
}
```

## Sources

- [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]]
- [[FPP-SRC-SELECTED-dla-award-page2-txt]]
- [[FPP-SRC-SELECTED-dla-award-page5-first-article-png]]
- [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]]
- [[FPP-SRC-SELECTED-dla-award-page6-txt]]
- [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]]
- [[FPP-SRC-dla-original-SPE4A626PW775]]

## Outgoing relationships

- reports_ordered_line_value: [[FPP-ORDERED-VALUE-SPE4A626PW775-0002]] — documented_fact (PA-E-406bb5fd0518ebadad9d98ab); sources: [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]], [[FPP-SRC-SELECTED-dla-award-page2-txt]], [[FPP-SRC-SELECTED-dla-award-page5-first-article-png]], [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]], [[FPP-SRC-SELECTED-dla-award-page6-txt]], [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]], [[FPP-SRC-dla-original-SPE4A626PW775]]
- cites: [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]] — documented_fact (edge-0dde71c86599bbc155a1); sources: [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page5-first-article-png]] — documented_fact (edge-418e70a43169b2bce51e); sources: [[FPP-SRC-SELECTED-dla-award-page5-first-article-png]]
- cites: [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]] — documented_fact (edge-59d5020f7aaf8b549f22); sources: [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page6-txt]] — documented_fact (edge-81263f3a35172565f223); sources: [[FPP-SRC-SELECTED-dla-award-page6-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]] — documented_fact (edge-ce8781578d2686351698); sources: [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page2-txt]] — documented_fact (edge-d25841d1debc918b1ae0); sources: [[FPP-SRC-SELECTED-dla-award-page2-txt]]
- cites: [[FPP-SRC-dla-original-SPE4A626PW775]] — documented_fact (edge-e39c958b5f6cf8a9d3d2); sources: [[FPP-SRC-dla-original-SPE4A626PW775]]

## Backlinks

- [[FPP-AWARD-CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-]]: awarded_clin — documented_fact (PA-E-4be292661a33459f4a7e4745)
