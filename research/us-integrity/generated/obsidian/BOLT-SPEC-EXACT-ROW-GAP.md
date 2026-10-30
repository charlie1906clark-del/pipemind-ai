---
id: "BOLT-SPEC-EXACT-ROW-GAP"
type: "research_question"
title: "The exact NIIN record remains unextracted; commercial equivalence is still unresolved"
status: "unknown"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# The exact NIIN record remains unextracted; commercial equivalence is still unresolved

Evidence status: **unknown**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "data_privacy_or_unavailability_inferred": false,
  "observation": {
    "acquisition_decision": "Do not download large opaque tables without a validated compatible parser. Preserve exact route and verify a selected NIIN export, then independently review the match. This is a technical evidence gap, not proof data is private or unavailable.",
    "archive_scope": "Directory metadata and file-format inspection only. A binary prefix is not an extracted row; no absence inference.",
    "as_of": "2026-10-30",
    "catalog_reader_route_verified": true,
    "exact_nsn_to_retail_specification_match": null,
    "market_comparability": "still_unresolved",
    "next_steps": [
      "Acquire the DLA CSV Characteristics and Reference products through actual published links, or use the documented official PUB LOG reader to export NIIN016864912.",
      "Capture export date, source release, exact original record and field definitions; review NSN, revisions and applicability dates.",
      "Reconcile dimensions, material grade, finish, traceability, packaging and all applicable order terms with seller offers."
    ],
    "niin": "016864912",
    "nsn": "5306016864912",
    "primary_current_document": "../current/observations.json",
    "primary_current_limit": "ASME B18.24 cited; exact part-piece number blank. Does not establish retail characteristics.",
    "reader_route": "Official archive TOOLS/README.TXT documents DECOMP SQL table extraction; archive contains V_CHARACTERISTICS.TAB and V_FLIS_PART.TAB. Compatible reader and complete necessary member data still required.",
    "selected_member_sizes": [
      {
        "compressed_bytes": 155515900,
        "compression_type": 8,
        "crc32": "4095fc3e",
        "header_offset": 1037570506,
        "name": "V_CHARACTERISTICS.TAB",
        "uncompressed_bytes": 306610192
      },
      {
        "compressed_bytes": 130989447,
        "compression_type": 8,
        "crc32": "897f6217",
        "header_offset": 1360534774,
        "name": "V_FLIS_PART.TAB",
        "uncompressed_bytes": 187203600
      }
    ],
    "status": "primary_item_characteristics_not_extracted",
    "verified_item_characteristics": null,
    "verified_part_number": null
  },
  "source_scope": "Public archive route and member format, not an authenticated item characteristic row",
  "technical_evidence_gap": true,
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-SPEC-DLA-ARCHIVE]]
- [[BOLT-SPEC-DLA-CSV-LAYOUT]]
- [[BOLT-SPEC-DLA-PUBLOG]]
- [[BOLT-SPEC-DLA-READINGROOM]]
- [[BOLT-SPEC-TOOLS-README]]

## Outgoing relationships

- investigates_specification_for: [[DISC-NSN-5306016864912]] — documented_fact (BOLT-E-63cd4af6e65875a2f1ff); sources: [[BOLT-CUR-S01]], [[BOLT-SPEC-DLA-ARCHIVE]], [[BOLT-SPEC-DLA-CSV-LAYOUT]], [[BOLT-SPEC-DLA-PUBLOG]], [[BOLT-SPEC-DLA-READINGROOM]], [[BOLT-SPEC-TOOLS-README]]
- blocks_qualified_comparison: [[BOLT-MARKET-BENCHMARK-MATRIX]] — planned (BOLT-E-e379c9a0ef9ebac17b3a); sources: [[BOLT-SPEC-DLA-ARCHIVE]], [[BOLT-SPEC-DLA-CSV-LAYOUT]], [[BOLT-SPEC-DLA-PUBLOG]], [[BOLT-SPEC-DLA-READINGROOM]], [[BOLT-SPEC-TOOLS-README]]
- continues_crosswalk_research: [[BOLT-NSN-SPEC-CROSSWALK-GAP]] — documented_fact (BOLT-E-ffdc3c2acf9f0e72696d); sources: [[BOLT-SPEC-DLA-ARCHIVE]], [[BOLT-SPEC-DLA-CSV-LAYOUT]], [[BOLT-SPEC-DLA-PUBLOG]], [[BOLT-SPEC-DLA-READINGROOM]], [[BOLT-SPEC-TOOLS-README]]
- cites: [[BOLT-SPEC-DLA-PUBLOG]] — documented_fact (edge-06edbee18e7d7199d139); sources: [[BOLT-SPEC-DLA-PUBLOG]]
- cites: [[BOLT-SPEC-DLA-ARCHIVE]] — documented_fact (edge-0914e4310bb2a2fdd6ff); sources: [[BOLT-SPEC-DLA-ARCHIVE]]
- cites: [[BOLT-SPEC-DLA-READINGROOM]] — documented_fact (edge-139c0db1f539822309c3); sources: [[BOLT-SPEC-DLA-READINGROOM]]
- cites: [[BOLT-SPEC-DLA-CSV-LAYOUT]] — documented_fact (edge-a17c9432dc06af6a26d3); sources: [[BOLT-SPEC-DLA-CSV-LAYOUT]]
- cites: [[BOLT-SPEC-TOOLS-README]] — documented_fact (edge-e0c8c7baff1d6414201d); sources: [[BOLT-SPEC-TOOLS-README]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-ef70c1e7c661f7bbd5f5); sources: [[BOLT-CUR-S01]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — unknown (BOLT-E-e8bd95851bcc640ad3d3)
