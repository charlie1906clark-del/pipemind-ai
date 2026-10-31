---
id: "PA-SPEC-FOLLOWUP-20261030"
type: "source_access_observation"
title: "Original bolt technical comparison remains unresolved"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Original bolt technical comparison remains unresolved

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "authoritative_characteristics_rows": 0,
  "authoritative_reference_rows": 0,
  "observation": {
    "actual_primary_characteristic_rows_acquired": 0,
    "actual_primary_reference_rows_acquired": 0,
    "as_of": "2026-10-30",
    "buyer_benefit": null,
    "exact_specification_match": null,
    "new_fraud_established": false,
    "next_tasks": [
      "BSF-CHAR-001",
      "BSF-REF-001"
    ],
    "niin": "016864912",
    "nsn": "5306016864912",
    "observations": [
      {
        "fact": "Official dated CSV layouts identify the exact target table fields and reference qualifiers.",
        "id": "BSF-OBS-01",
        "limits": "Layout source is indexed text; original PDFs returned403. Schema is not an item record or proof of current release contents.",
        "sources": [
          "BSF-S02",
          "BSF-S03"
        ],
        "status": "source_reported_schema"
      },
      {
        "fact": "The prior public archive capture includes native V_CHARACTERISTICS.TAB and V_FLIS_PART.TAB and supplied DECOMP extraction instructions.",
        "id": "BSF-OBS-02",
        "limits": "No selected NIIN export performed; a compatible runtime is absent here.",
        "sources": [
          "BSF-S05"
        ],
        "status": "documented_prior_route"
      },
      {
        "artifact": "parse_publog_export.py",
        "fact": "Strict offline parser accepts authentic supplied CSV/pipe exports through hash-bound declared receipts, preserving exact NIIN and reference qualifiers.",
        "id": "BSF-OBS-03",
        "limits": "Parser validates syntax and declared provenance, not source authenticity, historical applicability or technical equivalence.",
        "status": "implemented_control"
      }
    ],
    "price_comparison_qualified": false,
    "price_premium": null
  },
  "parser_is_authentication": false,
  "price_benchmark_qualified": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SPEC-SRC-BSF-S01]]
- [[PA-SPEC-SRC-BSF-S02]]
- [[PA-SPEC-SRC-BSF-S03]]
- [[PA-SPEC-SRC-BSF-S04]]
- [[PA-SPEC-SRC-BSF-S05]]
- [[PA-SRC-SPEC-FOLLOWUP]]

## Outgoing relationships

- cites: [[PA-SPEC-SRC-BSF-S04]] — documented_fact (edge-020ffe070206e0f7d1ba); sources: [[PA-SPEC-SRC-BSF-S04]]
- cites: [[PA-SPEC-SRC-BSF-S03]] — documented_fact (edge-4be932843fdbf3e5b5df); sources: [[PA-SPEC-SRC-BSF-S03]]
- cites: [[PA-SPEC-SRC-BSF-S05]] — documented_fact (edge-a049106791846425739f); sources: [[PA-SPEC-SRC-BSF-S05]]
- cites: [[PA-SRC-SPEC-FOLLOWUP]] — documented_fact (edge-d72726338aa9b5bd73e6); sources: [[PA-SRC-SPEC-FOLLOWUP]]
- cites: [[PA-SPEC-SRC-BSF-S02]] — documented_fact (edge-e50eb09743ecdd783405); sources: [[PA-SPEC-SRC-BSF-S02]]
- cites: [[PA-SPEC-SRC-BSF-S01]] — documented_fact (edge-e59f162dbfdc73f727c0); sources: [[PA-SPEC-SRC-BSF-S01]]

## Backlinks

- [[PA-W1-SPEC-BOLT]]: documents_specification_gap — documented_fact (PA-E-e5dfb6dbb55dd8abf61693fd)
