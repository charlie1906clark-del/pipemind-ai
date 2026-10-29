# Validation and remaining limits

Verified 29 October 2026 against the files in this branch. This record concerns the research software and supplied evidence, not a forensic conclusion about the sampled recipients.

| Check | Result |
|---|---|
| Graph validator with public-export checks | Passed: 532 nodes, 1,180 edges, 148 source records |
| Obsidian generation | 532 generated node notes plus a navigation note |
| Task definitions/import | 24 dependency-ordered work packages |
| Engine tests | 35 passed |
| Public-source connector tests | 8 passed, offline |
| Assembly semantic regression tests | 9 passed |
| Total tests | **52 passed** |
| Reassembly | Same canonical graph bytes on repeated frozen input |
| Captured USAspending responses | 3 successful HTTP 200 requests; 65 rows; request/response hashes verified |
| Cohort completeness | All three responses have further pages; incomplete samples explicitly retained |
| Search | SQLite full-text search returned source-linked results |
| Task concurrency | Exclusive claims, expiry/fencing, dependencies and completion preservation tested |
| Source spot checks | Official CMS, DOJ, VA OIG and SEC records re-opened during independent review |
| New fraud proved / submissions made | None / none |
| Autonomous agents or inter-chat connection | Not activated |

The independent review corrected legal-status parsing that could confuse negated convictions or unverified sentencing with completed legal events; person-versus-company typing; lost amount qualifiers; future snapshot collisions; and missing request-digest/success checks. The regression suite preserves these distinctions.

Current graph content digest: see `generated/manifest.json`. This digest hashes the supplied canonical JSON, not every consulted webpage. Only sources explicitly marked as byte-archived have captured content hashes. Most web research sources retain consultation metadata and relevant summaries, not original webpage bytes.

Identity scope remains explicit: award recipients use source-reported UEIs; corporate filing relationships are dated; case name mentions remain scoped and unresolved until corroborated. Public healthcare aggregates cannot establish medical necessity, exact patient transactions or direct referral relationships. Award sums are cumulative, not FY2026 spending. Lower bounds and conditional payments remain qualified, and overlapping case amounts are nonadditive.

The current code does not perform nationwide ingestion, score new fraud, identify all owners, query private records, independently update every court docket, submit reward claims, or run a live LLM agent service. Agent contracts and shared-task architecture prepare that work; they do not prove it is running. The local task ledger only coordinates workers using the same database; separate sessions require a coordinator or a later shared transactional service.
