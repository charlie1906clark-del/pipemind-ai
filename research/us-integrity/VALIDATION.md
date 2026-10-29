# Validation and remaining limits

Verified 29 October 2026 against the files in this branch. This record concerns the research software and supplied evidence, not a forensic conclusion about the sampled recipients.

| Check | Result |
|---|---|
| Graph validator with public-export checks | Passed: 829 nodes, 1,861 edges, 212 source records |
| Obsidian generation | 829 generated node notes plus a navigation note; all wiki links checked |
| Task definitions/import | 24 dependency-ordered work packages |
| Engine tests | 35 passed |
| Public-source connector tests | 8 passed, offline |
| Assembly semantic regression tests | 9 passed |
| Investigation extension/provenance tests | 11 passed |
| Catheter acquisition and analytical contract tests | 6 passed |
| Total tests | **69 passed** |
| Reassembly | Same canonical graph bytes on repeated frozen input |
| Captured USAspending responses | 3 successful HTTP 200 requests; 65 rows; request/response hashes verified |
| Cohort completeness | All three responses have further pages; incomplete samples explicitly retained |
| Catheter acquisition | All 6,870 published rows across nine code/year cohorts; filtered counts and terminal empty pages verified |
| National catheter comparator | Nine geography/service rows; suppression undercoverage quantified |
| Independent calculation review | Nine aggregates, six decompositions, two cross-code checks and nine national reconciliations passed |
| Revoked-enrollment acquisition | 8,620 main rows plus 94 companion NPI rows; counts, hashes, joins and date boundaries checked |
| Investigation approval boundary | Explicit extension and 34 input-artifact digests checked; no unlisted automatic ingestion |
| Registry/court evidence | Exact NPI matches, corporate roles, exclusion/revocation events and source-specific legal dates preserved |
| Search | SQLite full-text search returned source-linked results |
| Task concurrency | Exclusive claims, expiry/fencing, dependencies and completion preservation tested |
| Source spot checks | Official CMS, DOJ, VA OIG and SEC records re-opened during independent review |
| New fraud proved / submissions made | None / none |
| Autonomous agents or inter-chat connection | Not activated |

The independent review corrected legal-status parsing that could confuse negated convictions or unverified sentencing with completed legal events; person-versus-company typing; lost amount qualifiers; future snapshot collisions; and missing request-digest/success checks. The regression suite preserves these distinctions.

Six specialist workers executed the catheter research pass in this session. Its [validation record](investigations/dme-catheter-2026-10-29/VALIDATION.json) and [independent calculation check](investigations/dme-catheter-2026-10-29/falsification/data_review.json) record the completed work. Two anonymous historical-enrollment questions remain unresolved after bounded follow-up. No fraud determination or cash-loss calculation is inferred from those joins. The source-capture hashes distinguish original responses, selected/normalized snapshots and canonical graph serialization.

Current graph content digest: see `generated/manifest.json`. This digest hashes the supplied canonical JSON, not every consulted webpage. Only sources explicitly marked as byte-archived have captured content hashes. Most web research sources retain consultation metadata and relevant summaries, not original webpage bytes.

Identity scope remains explicit: award recipients use source-reported UEIs; corporate filing relationships are dated; case name mentions remain scoped and unresolved until corroborated. Public healthcare aggregates cannot establish medical necessity, exact patient transactions or direct referral relationships. Award sums are cumulative, not FY2026 spending. Lower bounds and conditional payments remain qualified, and overlapping case amounts are nonadditive.

The current code does not perform nationwide ingestion, score new fraud, identify all owners, query private records, independently update every court docket, submit reward claims, or run a live LLM agent service. Agent contracts and shared-task architecture prepare that work; they do not prove it is running. The local task ledger only coordinates workers using the same database; separate sessions require a coordinator or a later shared transactional service.
