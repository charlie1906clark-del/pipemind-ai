---
id: "BOLT-MKT-MF-HH38FX3-4G8ZY"
type: "market_product_observation"
title: "MF Supply: HH38FX3/4G8ZY"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# MF Supply: HH38FX3/4G8ZY

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "eligible_for_price_premium": false,
  "exact_nsn_equivalence_verified": false,
  "no_money_export": true,
  "no_suspect_classification": true,
  "observation": {
    "availability": {
      "available_boxes": 7,
      "item_specific": true,
      "units_906_available": null
    },
    "limitations": [
      "Box quantity is not explicit in opened page. Do not infer it from price or weight ratios.",
      "Displayed per-piece price is not proof that a single unit or906 units can be ordered.",
      "Seven available boxes are not proof of906 units until pack size is verified.",
      "Orders and pricing subject to acceptance; stock may change.",
      "Certifications, testing, inspection and QA conditions require disclosure and written acceptance under merchant terms.",
      "Shared3812CH8O reference with FSS means upstream independence is not established.",
      "No primary NSN crosswalk or accepted government-compliant quote."
    ],
    "manufacturer_part_as_displayed": "3812CH8O",
    "offer_status": "posted_catalog_offer_subject_to_seller_acceptance",
    "price": {
      "currency_display": "$",
      "currency_interpretation": "USD inferred from US merchant and US-only online shipping; ISO currency not explicit",
      "displayed_box_price": "328.91",
      "displayed_piece_price": "0.29901",
      "freight_included": null,
      "normalized_unit_price": null,
      "pack_quantity": null,
      "price_as_of": "2026-10-30",
      "publication_date": null,
      "selling_uom": "box",
      "tax_included": null
    },
    "qualification_status": "provisional_product_comparator",
    "seller": "MF Supply",
    "sku": "HH38FX3/4G8ZY",
    "specifications": {
      "certification_included": null,
      "country_of_manufacture": null,
      "diameter_in": 0.375,
      "dimensional_standard": "ASME B18.2.1",
      "finish": "yellow zinc",
      "finish_standard": null,
      "finish_thickness": null,
      "full_thread": null,
      "government_packaging_compliance": null,
      "grade": "8",
      "head_style": "hex",
      "length_in": 0.75,
      "lot_traceability_included": null,
      "material": "steel",
      "material_standard": "SAE J429",
      "nsn_crosswalk_primary": false,
      "thread_class": null,
      "thread_direction": null,
      "thread_series": "fine/UNF suggested by 3/8-24; not universally explicit",
      "threads_per_inch": 24
    },
    "upstream_manufacturer_unverified": null
  },
  "observation_kind": "Posted catalog data, not an accepted government-compliant quote",
  "visibility": "public"
}
```

## Sources

- [[BOLT-MKT-SRC-MF]]
- [[BOLT-MKT-SRC-MF-SHIPPING]]
- [[BOLT-MKT-SRC-MF-TERMS]]

## Outgoing relationships

- screened_as_possible_comparator_for: [[DISC-NSN-5306016864912]] — documented_fact (BOLT-E-9a04532dd8d12fed03d2); sources: [[BOLT-CUR-S01]], [[BOLT-MKT-SRC-MF]], [[BOLT-MKT-SRC-MF-SHIPPING]], [[BOLT-MKT-SRC-MF-TERMS]]
- cites: [[BOLT-MKT-SRC-MF-SHIPPING]] — documented_fact (edge-0859d8c1473fa141613c); sources: [[BOLT-MKT-SRC-MF-SHIPPING]]
- cites: [[BOLT-MKT-SRC-MF]] — documented_fact (edge-848579d341c5889269e0); sources: [[BOLT-MKT-SRC-MF]]
- cites: [[BOLT-MKT-SRC-MF-TERMS]] — documented_fact (edge-cce54139029b07b5a37b); sources: [[BOLT-MKT-SRC-MF-TERMS]]

## Backlinks

- [[BOLT-MARKET-BENCHMARK-MATRIX]]: screens_candidate — documented_fact (BOLT-E-1a372d4813fdb776149f)
- [[BOLT-PCR-F04]]: assesses_evidence — documented_fact (BOLT-E-1d22e6aed7605323d5b7)
