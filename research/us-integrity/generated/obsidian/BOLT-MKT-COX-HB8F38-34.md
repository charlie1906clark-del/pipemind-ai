---
id: "BOLT-MKT-COX-HB8F38-34"
type: "market_product_observation"
title: "Cox Hardware and Lumber: HB8F38.34"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Cox Hardware and Lumber: HB8F38.34

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
      "available_units": 62,
      "item_specific": true,
      "on_order_units": 0,
      "units_906_available": false
    },
    "limitations": [
      "Header identifies site as a test site.",
      "Opened page shows 62 units; search-index version showed18, so neither is an executable906-unit quote.",
      "500+ price must not be applied as an executable906-unit offer.",
      "The full-box discount note does not explicitly establish pack size.",
      "No primary NSN match; no accepted government terms."
    ],
    "manufacturer_part_as_displayed": "COX-111449",
    "offer_status": "test_site_catalog_reference_only",
    "price": {
      "currency_display": "$",
      "currency_interpretation": "USD inferred from US merchant; ISO currency not explicit",
      "freight_included": null,
      "pack_quantity": null,
      "price_as_of": "2026-10-30",
      "publication_date": null,
      "selling_uom": "EA",
      "tax_included": null,
      "tiers": [
        {
          "maximum_units": 99,
          "minimum_units": 1,
          "price_per_unit": "0.590"
        },
        {
          "maximum_units": 499,
          "minimum_units": 100,
          "price_per_unit": "0.413"
        },
        {
          "maximum_units": null,
          "minimum_units": 500,
          "price_per_unit": "0.384"
        }
      ]
    },
    "qualification_status": "excluded_from_transactable_quote_set",
    "seller": "Cox Hardware and Lumber",
    "sku": "HB8F38.34",
    "specifications": {
      "certification_included": null,
      "country_of_manufacture": null,
      "diameter_in": 0.375,
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

- [[BOLT-MKT-SRC-COX]]

## Outgoing relationships

- screened_as_possible_comparator_for: [[DISC-NSN-5306016864912]] — documented_fact (BOLT-E-f4ecb5c8a4497c84586b); sources: [[BOLT-CUR-S01]], [[BOLT-MKT-SRC-COX]]
- cites: [[BOLT-MKT-SRC-COX]] — documented_fact (edge-ad985211f234556cd77b); sources: [[BOLT-MKT-SRC-COX]]

## Backlinks

- [[BOLT-PCR-F02]]: assesses_evidence — documented_fact (BOLT-E-9a492a484be20e200a6c)
- [[BOLT-MARKET-BENCHMARK-MATRIX]]: screens_candidate — documented_fact (BOLT-E-d34bee7117c86978c06c)
