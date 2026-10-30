---
id: "BOLT-SPEC-DLA-ARCHIVE"
type: "source"
title: "DLA public PUB LOG archive: partial metadata capture"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# DLA public PUB LOG archive: partial metadata capture

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-30T11:55:53.361532+00:00",
  "archive_bytes": 1617404308,
  "archive_complete": false,
  "content_sha256": "42652d47b841d5babe39bb6f4982e1a304c7328852098e7d53e436882d813114",
  "etag": "0x8DF35B01E6D741A",
  "last_modified": "Thu, 29 Oct 2026 11:31:05 GMT",
  "original_archive_sha256": null,
  "original_wire_archived": false,
  "range_reads": [
    {
      "bytes": 22,
      "content_range": "bytes 1617404286-1617404307/1617404308",
      "hash_scope": "retrieved range; not retained raw",
      "method": "GET",
      "range": "bytes=1617404286-1617404307",
      "sha256": "d2698bd7f4fa11ed18a687a64971e6e7e64376f4bd37874e1a60cf168aa9594a",
      "status": 206
    },
    {
      "bytes": 20,
      "content_range": "bytes 1617404266-1617404285/1617404308",
      "hash_scope": "retrieved range; not retained raw",
      "method": "GET",
      "range": "bytes=1617404266-1617404285",
      "sha256": "463bc9e1f52552232a4479b96001468b7de20f36acf033e5a56c7312e4410336",
      "status": 206
    },
    {
      "bytes": 43562,
      "content_range": "bytes 1617360724-1617404285/1617404308",
      "hash_scope": "retrieved range; not retained raw",
      "method": "GET",
      "range": "bytes=1617360724-1617404285",
      "sha256": "e1f0e38550252342f07a2e34afe946fc52c95b284240203076b9ad733cbdb04b",
      "status": 206
    }
  ],
  "retrieval": "HEAD200 and normal GET206 ranges; metadata, completeTOOLS/README.TXT and partialV_CHARACTERISTICS.TAB prefix",
  "snapshot_path": "investigations/dla-bolt-trace-2026-10-30/specification/archive-directory.json",
  "snapshot_scope": "Structured ZIP directory metadata extracted from HTTP ranges; not original archive or raw range bytes",
  "source_bytes_archived": true,
  "supports": "Actual archive member inventory and documented DECOMP extraction route; no NSN record acquired",
  "url": "https://publogstorage.blob.core.windows.net/publog/PublogDVD.zip",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[BOLT-SPEC-EXACT-ROW-GAP]]: cites — documented_fact (edge-0914e4310bb2a2fdd6ff)
- [[BOLT-SPEC-PUBLIC-ROUTE]]: cites — documented_fact (edge-add62a77b98e35ffdef0)
- [[BOLT-TRACE-20261030]]: cites — documented_fact (edge-ae11bbe7b60168ed4270)
