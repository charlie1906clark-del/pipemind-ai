# Independent review: discovery methods and false positives

Review date: 30 October 2026. This review tests the proposed research methods and the new public-data pilot. It does not determine anyone's guilt, prove that a matter is unknown to government, or establish reward eligibility.

## Decision

The strongest procurement research design is a **bounded comparison of repeated purchases of the same standardized item**, followed by an exact-identifier and dated-role check. Supplier-name normalization is useful as an inexpensive data-quality screen, but a full stop, legal suffix, abbreviation or Unicode variant alone is a weak fraud indicator. A price discrepancy can identify a poor buying outcome without establishing a false claim or unlawful conduct.

Start with commodity parts whose NSN or manufacturer part/revision, unit of issue, quantity and delivery terms can be verified. Large weapons-system totals combine configurations, support, development, options and quantities; they are usually a weaker first public-data comparison. This is a research prioritization judgment, not a finding that one sector has a measured higher incidence of fraud.

## Controls required by the evidence

| Proposed shortcut | Why it fails | Required discriminating test |
|---|---|---|
| “Amazon” and “Amazon.” must be separate entities | Search engines and databases normalize punctuation; the same entity can have aliases | Preserve literal names and compare exact UEI, CAGE, registry ID, profile level and date |
| Different UEIs with similar names prove impersonation | Subsidiaries, establishments, DBAs and unrelated businesses may share words | Resolve legal identity and dated relationship using independent records; leave unresolved matches separate |
| Same UEI proves ownership or valid registration | An identifier is not a complete ownership/enrollment history | Check the applicable registration status and public role evidence at the transaction date |
| Sum parent and child profile amounts | Profile populations can overlap | Keep recipient level and individual award/action grain; never aggregate overlapping profiles |
| Divide award value by a quantity found in a solicitation | A ceiling, estimated annual quantity and actual paid order may have different scopes | Match the same contract line, action, option period and amount/quantity basis |
| Compare the same noun in two descriptions | A bolt or valve can have different material, testing, configuration or certification | Match technical identifiers and specification revision before comparing |
| Use a retail listing as the fair government price | Packaging, quantity, delivery, warranty, qualification and timing differ | Adjust comparators explicitly and retain uncertainty; ask a technical specialist where material differences remain |
| Call a high ratio “fraud” | Waste, urgent procurement, market power, allocation, error and deception are different explanations | Identify a specific potentially false representation or contractual obligation and the evidence addressing it |
| No public case found means government does not know | Investigations can be nonpublic and searches incomplete | Record “no matching public action located in this bounded search,” with queries and date |
| Three models agree, therefore verified | Models may share a source or repeat each other's error | Require independently checked source records and calculations; record common provenance |

SAM distinguishes obtaining a UEI from completing entity registration; a UEI-only record is not proof of eligibility for a prime award. The official USAspending recipient contract defines P/C/R profile levels and describes the profile amount as a trailing-twelve-month transaction aggregate. That amount must not silently become a fiscal-year, lifetime, unit-price or loss figure. [RV-S01, RV-S02]

FAR 15.404-1(b)(2)(ii)(A–C) requires a valid historical comparison and adjustment for materially different terms, quantities, market/economic factors and item differences. Its unit-price provisions also address distortion from allocating costs across line items. These rules support the comparison controls above; a record that omits the adjustments cannot by itself prove unreasonable pricing. Agency deviations and the rule applicable on the actual contract date still need checking. [RV-S03]

## Novelty and legal-route discipline

Track three different questions: **what is new in our analysis**, **what is publicly reported already**, and **what government already knows**. Only the first two can ordinarily be investigated from this public repository. A new combination of public data can be analytically useful; it is not automatically an original, reward-eligible tip.

WHIP's written guidance allows independent analysis of public information, but imposes additional originality, material-addition, eligibility and charging requirements. It also states that an existing investigation does not automatically exclude genuinely new information. Thus the rule is neither “public data never qualifies” nor “every new spreadsheet qualifies.” Its discretion and the discrepancy with public remarks remain material. [RV-S04]

Do not use a universal requirement of specific intent to defraud as an automated filter. Civil FCA section 3729 defines knowing conduct to include actual knowledge, deliberate ignorance and reckless disregard, without requiring proof of specific intent. The relevant claim, falsity, materiality, state-of-mind and damages analysis is route-specific. This review does not decide that a price outlier satisfies any of those elements. The accessible GovInfo text cited here is the 2023 codified edition; the separate congressional workstream checks current authority. [RV-S05, RV-S06]

The prior catheter investigation is a calibration example and source of public mechanisms. Its existing charges, historical spike and named-company connections cannot be re-labelled newly discovered fraud. Likewise, an OIG finding quoted in a senator's letter is evidence of a published concern, not a new loss discovered by this project. GAO's fraud-risk work supports using data matching and prior adjudicated cases to design tests while distinguishing allegations from adjudications. [RV-S07]

## Acceptance conditions for a new candidate

1. Define one transaction population and confirm its grain, date coverage, exclusions and pagination.
2. Preserve the raw identifier and name alongside every normalization; normalization never authorizes a merge.
3. Match amounts and quantities at the same level. Label ceiling, obligation, unit price, invoice, payment and recovery separately.
4. Test at least two plausible alternatives, including the one most likely to explain the pattern.
5. Search exact identifiers and contract numbers against public enforcement, audits and litigation. Retain the search's scope and negative-result limits.
6. Have an independent reviewer reproduce the calculation and inspect the primary records.
7. Keep an unresolved candidate as a question. A publication or submission decision requires a separate review of the actual case and applicable process.

These are project research controls, not a claim that every data anomaly is legally confidential or that a tip must already prove an entire court case. The public repository should contain methods, neutral records and published facts; it should not become a public blacklist generated from a similarity score.

## Independent checks of this run

The name pilot was independently reconstructed from saved response pages, without importing its audit module. All 19 recorded requests have checked request/selected-response hashes. The two contract queries returned 150 and 12 award records respectively; the latter set is entirely contained in the former. Six recipient profiles represent three same-UEI parent/child pairs, not six independent companies. There are two normalized-name groups, including one group with two distinct UEIs. Those identifiers remain separate. The three child profiles report a common parent; this is source-reported linkage, not independently verified beneficial ownership.

The query `Amazon.` even returns the one AWS award whose name has no terminal full stop, while the 138 AWS records whose names do have it appear only in the `Amazon` result. This is an observed search-semantic difference, not a literal punctuation test or evidence of impersonation. These results concern the exact saved prime-contract query and dates; they do not cover every federal payment, buyer, subsidiary or trade. No monetary amounts were summed. [Local N1–N3]

This reviewer visually checked the original DLA PDF's pages 7–8 and independently reconstructed all seven history rows. Printed unit costs range from 0.93000 to 1.92000; historical units and material price-affecting terms remain unknown. Page 2 supplies a $350,000 maximum and an estimated 2,221 quantity, while page 9 has blank current price cells. Their quotient is not a unit price. The single 472-unit row is confirmed. None of the 21 possible historical pairs passes the project's comparability gate. This is a successful source-acquisition demonstration with no new fraud case, payment verification or savings estimate. [RV-S08, Local P1–P3]

Review found and the producers fixed: reliance on manifest claims instead of actual count/terminal pages; insufficient binding of derived parent fields to captured profiles; unused all-null nested parent selections; a pricing source-page mismatch; and acceptance of non-finite numeric values. The final name suite passes 16 tests and the price suite passes six. A separate offline extraction reproduces the published price selection byte-for-byte. The price gate remains a mechanical filter: it cannot authenticate a caller-supplied source hash or `reviewed` flag. Independent source review remains necessary.

The executive and congressional reports preserve the material distinctions: attributed non-government transcript versus independently checked official audio; public percentage remarks versus written reward terms; a member's proposal versus an enactment; and archived statutory editions versus a fully checked current consolidation. Full current deviation text, official audio comparison, reward-scope inconsistencies and some bill crosswalks remain open. Their bounded conclusions do not support a universal 1% entitlement. This review does not claim to have repeated every legal workstream search.

The next executable investigation should obtain a declared cohort of 30 recent DLA machine-bolt RFQs, then follow each historical contract key into the original award/order and modifications. Record inaccessible and noncomparable observations rather than filling missing values. Rank only verified comparable purchases for further records work; separately test a specific representation, delivery or billing proposition. A completed cohort with no supported candidate is an acceptable result. Public access to one PDF does not establish universal access to invoices, technical drawings, beneficiary records or ownership histories.

Reproducible checks are in [verify_names.py](verify_names.py) and [verify_price.py](verify_price.py); their output and input hashes are in [name_data_review.json](name_data_review.json) and [price_data_review.json](price_data_review.json). [review.json](review.json) records the final review decision and remaining gaps.

## Primary sources

- **RV-S01 — SAM.gov, Entity Registration:** https://sam.gov/entity-registration . Locators: “For a Unique Entity ID only” and registration/renewal sections. Current page inspected 2026-10-30.
- **RV-S02 — Treasury USAspending API recipient contract:** https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/recipient.md . Locators: RecipientListing `id`, `amount`, `recipient_level`, and request `keyword`. Contract reviewed 2026-10-30; an implementation discrepancy, if found, must be recorded.
- **RV-S03 — FAR 15.404-1:** https://www.acquisition.gov/far/15.404-1 . Locators: (b)(2)(ii)(A–C) and (f). Retrieved page shows FAC 2026-01, effective 2026-03-13; not a certification of every agency deviation.
- **RV-S04 — DOJ written Criminal Tip Rewards Pilot Program:** https://www.justice.gov/fraud/national-fraud-enforcement-division-criminal-tip-rewards-pilot-program . Locators: originality section 2, criminal-charge section 7, and discretion. Read 2026-10-30.
- **RV-S05 — GovInfo 2023 Code, 31 USC3729:** https://www.govinfo.gov/content/pkg/USCODE-2023-title31/html/USCODE-2023-title31-subtitleIII-chap37-subchapIII-sec3729.htm . Locators: (a)(1), (b)(1), (b)(4). Edition date preserved; current House endpoint was unavailable through this review's web retrieval.
- **RV-S06 — DOJ, The False Claims Act:** https://www.justice.gov/civil/false-claims-act . Current DOJ explainer read 2026-10-30; page updated 2025-01-15.
- **RV-S07 — GAO-24-105358, DOD Fraud Risk Management:** https://www.gao.gov/products/gao-24-105358 . Published 2024-02-27; findings on data matching, investigative-data limitations and alleged/adjudicated case distinctions. This historical report is not proof that every identified control gap remains open today.
- **RV-S08 — DLA RFQ SPE4A6-26-U-3619:** https://dibbs2.bsm.dla.mil/Downloads/RFQ/9/SPE4A626U3619.PDF . Issued 2026-09-03; original PDF independently read and pages 7–8 visually inspected. SHA-256 `4a3996d9aca0fac0b32ea1cebfe8833fdbb144de33dc0af2739d0269b037ac51`.
- **Local N1–N3 — captured name evidence:** [manifest](../names/capture-2026-10-30/manifest.json), [analysis](../names/analysis.json), [report](../names/REPORT.md). Exact request bodies, response selection, exclusions and query dates are retained there.
- **Local P1–P3 — captured price evidence:** [acquisition manifest](../pricing/acquisition_manifest.json), [selected evidence](../pricing/snapshots/selected_evidence.json), [report](../pricing/REPORT.md). This review verifies transcription, not prior award/payment authenticity.
