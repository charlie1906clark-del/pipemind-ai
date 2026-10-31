---
id: "BOLT-NSN-SPEC-CROSSWALK-GAP"
type: "research_question"
title: "An exact primary NSN-to-commercial-specification bridge has not been acquired"
status: "unknown"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# An exact primary NSN-to-commercial-specification bridge has not been acquired

Evidence status: **unknown**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "bounded_search": {
    "authentication_attempted": false,
    "bulk_archive_download_attempted": false,
    "cannot_infer_from_403": [
      "record absence",
      "record restriction",
      "supplier wrongdoing",
      "catalog accuracy"
    ],
    "contact_or_quote_request_sent": false,
    "document_read_limit": 8,
    "local_documents_read": 2,
    "restricted_data_acquired": false,
    "search_queries_used": 4,
    "search_query_limit": 4,
    "successful_web_document_opens": 0,
    "total_distinct_document_reads_or_attempts": 7,
    "web_document_open_attempts": 5
  },
  "candidate_part_reference": "AEB02F375750WA6DG1",
  "candidate_part_reference_primary_confirmation": false,
  "decision": {
    "fraud_established": false,
    "kickback_established": false,
    "market_products_may_be_reported_as": "Provisional dimensional comparators selected from a secondary catalog lead",
    "market_products_may_be_reported_as_exact_nsn_equivalents": false,
    "overcharge_established": false,
    "qualified_like_for_like_price_comparison": false,
    "reason": "No original public characteristic/reference record linking this NSN to the exact candidate specifications was acquired. Price comparisons also require quantities, availability, packaging, traceability, acceptance, freight and other terms."
  },
  "next_required_evidence": [
    "Acquire the publicly releasable PUB LOG CHAR record for NIIN 016864912 from a documented current snapshot, including field labels and units.",
    "Acquire its public MCRD/reference rows, including the AEB02F375750WA6DG1 reference if present, CAGE and reference qualification codes.",
    "Preserve source date, exact retrieved record and hash; reconcile it to the 2026 contract requirements before calling a retail product equivalent.",
    "If exact public characteristics remain unavailable, retain the provisional market screen and do not translate its price spread into loss, savings or fraud."
  ],
  "primary_verified": {
    "currency": "USD",
    "document": "SPE4A6-26-D-61WS",
    "item_name": "BOLT,MACHINE",
    "nsn": "5306016864912",
    "page": 5,
    "part_piece_number_field": "blank",
    "source_id": "SPEC-P01",
    "standard_reference": "ASMEB18.24",
    "standard_revision_date_as_printed": "10/16/2023",
    "tdp_reference": "TDP Rev A Gen 1",
    "unit_of_issue": "EA",
    "unit_price": "0.91000"
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-SPEC-R01]]
- [[BOLT-SPEC-R02]]
- [[BOLT-SPEC-R03]]
- [[BOLT-SPEC-R04]]
- [[BOLT-SPEC-R05]]
- [[BOLT-SRC-BR-S02]]

## Outgoing relationships

- cites: [[BOLT-SPEC-R05]] — documented_fact (edge-1e1074463523024b677b); sources: [[BOLT-SPEC-R05]]
- cites: [[BOLT-SPEC-R03]] — documented_fact (edge-649b6ad65c1c3537e566); sources: [[BOLT-SPEC-R03]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-6c81cb7a09a3573fa1c2); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-SPEC-R01]] — documented_fact (edge-76017b462adcd67f60b9); sources: [[BOLT-SPEC-R01]]
- cites: [[BOLT-SPEC-R04]] — documented_fact (edge-8fb615924d2268734db2); sources: [[BOLT-SPEC-R04]]
- cites: [[BOLT-SRC-BR-S02]] — documented_fact (edge-ab05243c541fb7fef184); sources: [[BOLT-SRC-BR-S02]]
- cites: [[BOLT-SPEC-R02]] — documented_fact (edge-f807946e4736232bc628); sources: [[BOLT-SPEC-R02]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — unknown (BOLT-E-98b68556bbc1f70f1f74)
- [[BOLT-PCR-F05]]: assesses_evidence — documented_fact (BOLT-E-cb5ccdc6032487d92b1a)
- [[BOLT-MARKET-BENCHMARK-MATRIX]]: requires_resolved_crosswalk — planned (BOLT-E-f54bffbe15b6d3b7d5fa)
- [[BOLT-SPEC-EXACT-ROW-GAP]]: continues_crosswalk_research — documented_fact (BOLT-E-ffdc3c2acf9f0e72696d)
