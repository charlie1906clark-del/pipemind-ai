---
id: "PA-TRACER-LIVE-20261030"
type: "local_execution_observation"
title: "Direct tracer: 3 logical attempts, 0 HTTP requests and 0 acquired documents"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Direct tracer: 3 logical attempts, 0 HTTP requests and 0 acquired documents

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "attempts": [
    {
      "attempt_id": "TRACE-0001",
      "body_bytes_retained": false,
      "error": "dns_resolution_failed_or_timed_out",
      "finished_at": "2026-10-30T12:41:09.161948+00:00",
      "http_request_sent": false,
      "http_status": null,
      "method": "GET",
      "network_attempted": false,
      "parent_url": null,
      "relationship": "robots_policy",
      "started_at": "2026-10-30T12:41:09.133360+00:00",
      "status": "failed",
      "url": "https://www.usaspending.gov/robots.txt"
    },
    {
      "attempt_id": "TRACE-0002",
      "body_bytes_retained": false,
      "error": "dns_resolution_failed_or_timed_out",
      "finished_at": "2026-10-30T12:41:09.189508+00:00",
      "http_request_sent": false,
      "http_status": null,
      "method": "GET",
      "network_attempted": false,
      "parent_url": null,
      "relationship": "robots_policy",
      "started_at": "2026-10-30T12:41:09.161972+00:00",
      "status": "failed",
      "url": "https://dibbs2.bsm.dla.mil/robots.txt"
    },
    {
      "attempt_id": "TRACE-0003",
      "body_bytes_retained": false,
      "error": "dns_resolution_failed_or_timed_out",
      "finished_at": "2026-10-30T12:41:09.217009+00:00",
      "http_request_sent": false,
      "http_status": null,
      "method": "GET",
      "network_attempted": false,
      "parent_url": null,
      "relationship": "robots_policy",
      "started_at": "2026-10-30T12:41:09.189530+00:00",
      "status": "failed",
      "url": "https://raw.githubusercontent.com/robots.txt"
    }
  ],
  "coverage": {
    "acquired_documents": 0,
    "complete_procurement_universe": false,
    "declared_seed_count": 3,
    "failed_or_incomplete_attempts": 3,
    "frontier_complete": false,
    "http_requests_sent_confirmed": 0,
    "logical_attempts": 3,
    "network_attempts": 0,
    "received_body_bytes": 0
  },
  "other_research_tools_inferred_unavailable": false,
  "runtime_reservation_bridge_implemented": false,
  "scope": "Only selected request/link metadata retained. Body digests describe received bytes, not retained full documents. No prices, people, owners, misconduct or transaction facts authenticated.",
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-TRACER-LIVE]]

## Outgoing relationships

- cites: [[PA-SRC-TRACER-LIVE]] — documented_fact (edge-6af98a5a33fb030d0d16); sources: [[PA-SRC-TRACER-LIVE]]

## Backlinks

- [[PA-SYSTEM-20261030]]: records_tracer_scope — documented_fact (PA-E-e9b173fd8ff90a3206c9d207)
