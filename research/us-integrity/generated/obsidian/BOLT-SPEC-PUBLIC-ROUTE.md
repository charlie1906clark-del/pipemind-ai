---
id: "BOLT-SPEC-PUBLIC-ROUTE"
type: "acquisition_observation"
title: "The public catalog archive is accessible; its member inventory and reader instructions were inspected"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# The public catalog archive is accessible; its member inventory and reader instructions were inspected

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "archive_bytes": 1617404308,
  "archive_entry_count": 493,
  "exact_niin_record_extracted": false,
  "executable_run": false,
  "full_archive_downloaded": false,
  "member_inspection": [
    {
      "complete_member": true,
      "compressed_bytes_read": 3153,
      "name": "TOOLS/README.TXT",
      "uncompressed_bytes_read": 9185
    },
    {
      "complete_member": false,
      "compressed_bytes_read": 16384,
      "name": "V_CHARACTERISTICS.TAB",
      "uncompressed_bytes_read": 56407
    }
  ],
  "metadata_bytes_received": 43604,
  "restriction_or_absence_inferred": false,
  "visibility": "public"
}
```

## Sources

- [[BOLT-SPEC-DLA-ARCHIVE]]
- [[BOLT-SPEC-DLA-CSV-LAYOUT]]
- [[BOLT-SPEC-DLA-PUBLOG]]
- [[BOLT-SPEC-DLA-READINGROOM]]
- [[BOLT-SPEC-TOOLS-README]]

## Outgoing relationships

- cites: [[BOLT-SPEC-DLA-CSV-LAYOUT]] — documented_fact (edge-4dd0e63f4fa96d3fbc6e); sources: [[BOLT-SPEC-DLA-CSV-LAYOUT]]
- cites: [[BOLT-SPEC-TOOLS-README]] — documented_fact (edge-59bfa02dcb91a166842f); sources: [[BOLT-SPEC-TOOLS-README]]
- cites: [[BOLT-SPEC-DLA-ARCHIVE]] — documented_fact (edge-add62a77b98e35ffdef0); sources: [[BOLT-SPEC-DLA-ARCHIVE]]
- cites: [[BOLT-SPEC-DLA-PUBLOG]] — documented_fact (edge-ef5a587ea1dd535f1dcf); sources: [[BOLT-SPEC-DLA-PUBLOG]]
- cites: [[BOLT-SPEC-DLA-READINGROOM]] — documented_fact (edge-f5039719dadec35cc6cb); sources: [[BOLT-SPEC-DLA-READINGROOM]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-ea34a56ff5c92720dd84)
