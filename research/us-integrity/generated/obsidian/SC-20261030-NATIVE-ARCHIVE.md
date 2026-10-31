---
id: "SC-20261030-NATIVE-ARCHIVE"
type: "source_access_observation"
title: "Native archive schema acquired; exact NIIN rows remain absent"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Native archive schema acquired; exact NIIN rows remain absent

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "base_catalog_absence_inferred": false,
  "base_tables_acquired": false,
  "change_scan_limit": "Add/delete byte scans and nested directory only; large change member not decompressed",
  "exact_niin_rows_acquired": 0,
  "executable_extracted_or_run": false,
  "http_206_range_requests": 4,
  "native_characteristic_reply_length": 3144,
  "native_part_number_field_length": 60,
  "native_tables": [
    "V_FLIS_PART",
    "V_CHARACTERISTICS"
  ],
  "older_csv_layout_interchangeability": false,
  "received_range_bytes": 10412003,
  "visibility": "public"
}
```

## Sources

- [[SC-20261030-SRC-PUBLOG-1]]
- [[SC-20261030-SRC-PUBLOG-2]]
- [[SC-20261030-SRC-PUBLOG-3]]
- [[SC-20261030-SRC-PUBLOG-CHANGE-RECEIPT]]

## Outgoing relationships

- retains_unresolved_specification: [[BOLT-SPEC-EXACT-ROW-GAP]] — documented_fact (SC-20261030-E-da9f1f4fe953658f8d0a); sources: [[SC-20261030-SRC-PUBLOG-1]], [[SC-20261030-SRC-PUBLOG-2]], [[SC-20261030-SRC-PUBLOG-3]], [[SC-20261030-SRC-PUBLOG-CHANGE-RECEIPT]]
- cites: [[SC-20261030-SRC-PUBLOG-2]] — documented_fact (edge-2ea92d5587955af195b1); sources: [[SC-20261030-SRC-PUBLOG-2]]
- cites: [[SC-20261030-SRC-PUBLOG-3]] — documented_fact (edge-4e03fbbd0c3e271c0836); sources: [[SC-20261030-SRC-PUBLOG-3]]
- cites: [[SC-20261030-SRC-PUBLOG-1]] — documented_fact (edge-6ed8b2a057cfaf8f8f7b); sources: [[SC-20261030-SRC-PUBLOG-1]]
- cites: [[SC-20261030-SRC-PUBLOG-CHANGE-RECEIPT]] — documented_fact (edge-c75944d794119c6449d8); sources: [[SC-20261030-SRC-PUBLOG-CHANGE-RECEIPT]]

## Backlinks

- [[SC-20261030-CASE]]: includes_observation — documented_fact (SC-20261030-E-22fb336315bce28c2c09)
- [[SC-20261030-NATIONWIDE-OFFER]]: requires_exact_specification — documented_fact (SC-20261030-E-683b5ee36a52ba565c93)
