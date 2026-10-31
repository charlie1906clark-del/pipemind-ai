---
id: "FPP-LINE-SPE4A626PW775-0001"
type: "contract_line_observation"
title: "SPE4A626PW775-0001"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626PW775-0001

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "actual_payment_verified": false,
  "benchmark_qualified": false,
  "no_adverse_inference": true,
  "observation": {
    "acceptance": "ORIGIN",
    "additional_source_paths": [
      "selected/dla-award-page3.txt",
      "selected/dla-award-page7-e08-selected.txt"
    ],
    "clin": "0001",
    "contractually_intended_manufacturer_cage": "27624",
    "critical_application_item": true,
    "dealer_cage": "745V4",
    "delivery_date_source_page": 5,
    "delivery_due": "2028-04-10",
    "description": "BOLT, EXTERNALLY REL",
    "description_source_page": 3,
    "drawing_reference": "81205 39-8820 revision A dated 1961-03-09; further referenced drawings/QAPs on page4",
    "excess_amount_usd": null,
    "extended_amount_usd": "612316.57",
    "fob": "ORIGIN",
    "freight_included_in_unit_price": null,
    "freight_note": "Contract states FOB origin and government freight payment; actual freight bill or allocation not acquired.",
    "freight_payment": "GOVERNMENT",
    "independent_comparator_unit_price_usd": null,
    "inspection": "ORIGIN",
    "item_description_page3": "BOLT-FRONT ENGINE MOUNT, SPECIAL",
    "item_id": "5306004457358",
    "item_id_type": "NSN",
    "line_type": "production_item",
    "manufacturer_part_number": "39-8820-501",
    "manufacturer_role_limit": "Contract states dealer will supply this approved manufacturer; actual production, delivery and manufacturer transfer not independently verified.",
    "manufacturer_source_page": 2,
    "markup_percent": null,
    "observation_id": "SPE4A626PW775-0001",
    "packaging": "QUP 001; ASTM D3951 subject to DLA technical/quality precedence; MIL-STD-129 labeling; RP001 palletization",
    "packaging_source_page": 5,
    "page": 4,
    "piid": "SPE4A626PW775",
    "price_basis": "awarded_contract_line",
    "price_type": "Firm Fixed Price",
    "quantity": "2243.000",
    "quantity_variance_percent": {
      "minus": 0,
      "plus": 0
    },
    "source_paths": [
      "selected/dla-award-page4.txt",
      "selected/dla-award-page4.png"
    ],
    "unit": "EA",
    "unit_price_usd": "272.99"
  },
  "original_projection_id": "line:SPE4A626PW775-0001",
  "public_record": true,
  "visibility": "public"
}
```

## Sources

- [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]]
- [[FPP-SRC-SELECTED-dla-award-page2-txt]]
- [[FPP-SRC-SELECTED-dla-award-page3-txt]]
- [[FPP-SRC-SELECTED-dla-award-page4-png]]
- [[FPP-SRC-SELECTED-dla-award-page4-txt]]
- [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]]
- [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]]
- [[FPP-SRC-dla-original-SPE4A626PW775]]

## Outgoing relationships

- contracted_production_item: [[FPP-NSN-5306004457358]] — documented_fact (PA-E-31869598c9a39d4c872b3446); sources: [[FPP-SRC-dla-original-SPE4A626PW775]]
- reports_ordered_line_value: [[FPP-ORDERED-VALUE-SPE4A626PW775-0001]] — documented_fact (PA-E-f4e68c10342c404af9b6cefb); sources: [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]], [[FPP-SRC-SELECTED-dla-award-page2-txt]], [[FPP-SRC-SELECTED-dla-award-page3-txt]], [[FPP-SRC-SELECTED-dla-award-page4-png]], [[FPP-SRC-SELECTED-dla-award-page4-txt]], [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]], [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]], [[FPP-SRC-dla-original-SPE4A626PW775]]
- cites: [[FPP-SRC-SELECTED-dla-award-page2-txt]] — documented_fact (edge-000682ca67b8185ae35c); sources: [[FPP-SRC-SELECTED-dla-award-page2-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page4-png]] — documented_fact (edge-52acbe8f4ef05f453d33); sources: [[FPP-SRC-SELECTED-dla-award-page4-png]]
- cites: [[FPP-SRC-SELECTED-dla-award-page3-txt]] — documented_fact (edge-6b7cebcb91b90c8d78b3); sources: [[FPP-SRC-SELECTED-dla-award-page3-txt]]
- cites: [[FPP-SRC-dla-original-SPE4A626PW775]] — documented_fact (edge-81868669815326d1c565); sources: [[FPP-SRC-dla-original-SPE4A626PW775]]
- cites: [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]] — documented_fact (edge-b8dd67b15acd9066fd59); sources: [[FPP-SRC-SELECTED-dla-award-page7-e08-selected-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]] — documented_fact (edge-dbb97f6c7fa594d9c309); sources: [[FPP-SRC-SELECTED-dla-award-page11-first-article-selected-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page4-txt]] — documented_fact (edge-facf9927d397798776da); sources: [[FPP-SRC-SELECTED-dla-award-page4-txt]]
- cites: [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]] — documented_fact (edge-fdcdd5b2abf104538db1); sources: [[FPP-SRC-SELECTED-dla-award-page5-selected-txt]]

## Backlinks

- [[FPP-AWARD-CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-]]: awarded_clin — documented_fact (PA-E-7ec7baa4ef4c5a4b6586470c)
