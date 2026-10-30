---
id: "BOLT-MKT-FSS-191377"
type: "market_product_observation"
title: "Fastener SuperStore: 191377"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Fastener SuperStore: 191377

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
      "available_units": null,
      "generic_site_statement": "More than98% of listed items immediately available; not a stock confirmation for this SKU.",
      "item_specific": false
    },
    "limitations": [
      "Minimum advertised carton1100 exceeds observed906-unit government order; lower3+/5+ carton prices require3300+/5500+ units.",
      "Generic stock and shipping statements do not guarantee this item, quantity or delivery.",
      "Freight varies by weight/destination; FOB seller warehouses.",
      "No primary NSN match; generic spec PDFs are not lot certificates.",
      "RoHS status is on request, not confirmed.",
      "Shared3812CH8O reference with MF Supply means upstream independence is not established."
    ],
    "manufacturer_part_as_displayed": "Kanebridge3812CH8O",
    "offer_status": "posted_bulk_catalog_offer_not_accepted_quote",
    "price": {
      "currency_display": "$",
      "currency_interpretation": "USD inferred from US merchant; ISO currency not explicit",
      "freight_included": false,
      "pack_quantity": 1100,
      "price_as_of": "2026-10-30",
      "publication_date": null,
      "selling_uom": "carton",
      "tax_included": null,
      "tiers": [
        {
          "displayed_unit_price": "0.31147",
          "maximum_cartons": 2,
          "minimum_cartons": 1,
          "normalized_unit_price": "0.3114727272727273",
          "price_per_carton": "342.62"
        },
        {
          "displayed_unit_price": "0.29315",
          "maximum_cartons": 4,
          "minimum_cartons": 3,
          "normalized_unit_price": "0.2931545454545455",
          "price_per_carton": "322.47"
        },
        {
          "displayed_unit_price": "0.27686",
          "maximum_cartons": null,
          "minimum_cartons": 5,
          "normalized_unit_price": "0.2768636363636364",
          "price_per_carton": "304.55"
        }
      ]
    },
    "qualification_status": "provisional_product_comparator",
    "seller": "Fastener SuperStore",
    "sku": "191377",
    "specifications": {
      "certification_included": null,
      "country_of_manufacture": null,
      "diameter_in": 0.375,
      "dimensional_standard": "ASME B18.2.1-2012 via generic linked specification",
      "finish": "yellow zinc",
      "finish_standard": null,
      "finish_thickness": null,
      "full_thread": true,
      "government_packaging_compliance": null,
      "grade": "8",
      "head_style": "hex",
      "length_in": 0.75,
      "lot_traceability_included": null,
      "material": "steel",
      "nsn_crosswalk_primary": false,
      "thread_class": null,
      "thread_direction": null,
      "thread_series": "fine/UNF suggested by 3/8-24; not universally explicit",
      "threads_per_inch": 24,
      "width_across_flats_in": 0.5625
    },
    "upstream_manufacturer_unverified": "Kanebridge; seller cross-reference only"
  },
  "observation_kind": "Posted catalog data, not an accepted government-compliant quote",
  "visibility": "public"
}
```

## Sources

- [[BOLT-MKT-SRC-FSS]]
- [[BOLT-MKT-SRC-FSS-FAQ]]
- [[BOLT-MKT-SRC-FSS-TERMS]]

## Outgoing relationships

- screened_as_possible_comparator_for: [[DISC-NSN-5306016864912]] — documented_fact (BOLT-E-6e65f6e461500c3749fb); sources: [[BOLT-CUR-S01]], [[BOLT-MKT-SRC-FSS]], [[BOLT-MKT-SRC-FSS-FAQ]], [[BOLT-MKT-SRC-FSS-TERMS]]
- cites: [[BOLT-MKT-SRC-FSS]] — documented_fact (edge-37a6e60a8fd413a7f074); sources: [[BOLT-MKT-SRC-FSS]]
- cites: [[BOLT-MKT-SRC-FSS-TERMS]] — documented_fact (edge-3cb8ce5d3c7c0c989ff8); sources: [[BOLT-MKT-SRC-FSS-TERMS]]
- cites: [[BOLT-MKT-SRC-FSS-FAQ]] — documented_fact (edge-a5348754adeb5ad44ddd); sources: [[BOLT-MKT-SRC-FSS-FAQ]]

## Backlinks

- [[BOLT-MARKET-BENCHMARK-MATRIX]]: screens_candidate — documented_fact (BOLT-E-383e51b346d01bcdb21b)
- [[BOLT-PCR-F03]]: assesses_evidence — documented_fact (BOLT-E-57e83fb531ad6d7d7d74)
