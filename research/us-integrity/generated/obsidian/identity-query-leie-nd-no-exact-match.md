---
id: "identity-query-leie-nd-no-exact-match"
type: "query_result"
title: "ND Medical exact NPI absent from retrieved LEIE snapshot"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# ND Medical exact NPI absent from retrieved LEIE snapshot

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "coverage_through": "2026-09-30",
  "interpretation": "No exact-NPI row found. Not a clearance: identifiers may be absent and later changes are outside this snapshot.",
  "match_count": 0,
  "public_record": true,
  "rows_scanned": 84093,
  "searched_npi": "1790533503",
  "visibility": "public"
}
```

## Sources

- [[identity-src-oig-leie-2026-09]]
- [[identity-src-oig-leie-method]]

## Outgoing relationships

- cites: [[identity-src-oig-leie-2026-09]] — documented_fact (edge-9328461d5676b4f6cd1d); sources: [[identity-src-oig-leie-2026-09]]
- cites: [[identity-src-oig-leie-method]] — documented_fact (edge-c0a9bb3865e4351e067a); sources: [[identity-src-oig-leie-method]]

## Backlinks

- [[DME-INV-20261029]]: includes_identity_record — documented_fact (DME-E-28d910db024c68b5379f)
- [[identity-org-nd-medical-solutions]]: has_exact_npi_query_result — documented_fact (DME-E-b96c903707e012a0413e)
