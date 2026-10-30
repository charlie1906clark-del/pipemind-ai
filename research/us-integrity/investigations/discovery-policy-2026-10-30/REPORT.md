# Public procurement discovery and reward-policy review

Research cutoff: **30 October 2026**. Five specialist workstreams examined executive statements, congressional authority, supplier-name matching, procurement prices and independent challenge. They produced two executed public-data pilots and a reproducible evidence bank. **Neither pilot establishes a new fraud case, recoverable loss or entitlement to a reward.** The strongest next investigation is a bounded set of simple-item purchases, followed into original award/order lines and the terms necessary for a valid comparison.

This report covers the sources and queries recorded in the component registers. It does not claim every presidential or congressional statement, every sector, buyer, supplier, owner, invoice or payment has been examined. Acquired records, unsuccessful retrievals and unverified routes remain distinguishable.

## What Trump said and what DOJ implemented

The White House confirms a **20 October 2026 Oval Office announcement**. Exact speech excerpts below come from **Roll Call Factba.se**, a non-government transcript. The official video page was found, but its audio was not independently checked and no government-issued transcript was located. These are attributed statements with timestamps, not a certified transcript. The four excerpts total 18 quoted words. [Executive sources EX-S01–03](executive/sources.json)

| Speaker and transcript interval | Short exact excerpt | Proposition attributed in the transcript |
|---|---|---|
| Trump, 00:55:57–00:56:02 | “There's no limit.” | An uncapped one-percent commission |
| Trump, 00:56:24–00:56:35 | “if we recover the money” | Recovery, rather than a projected saving, as the stated basis |
| Trump, 00:14:19–00:15:16 | “binding arbitration” | Presidential involvement in resolving reward disputes |
| Vance, 00:56:35–00:56:46 | “not to limit this just to criminal prosecutions” | A broader scope than criminal cases |

The operative written WHIP material differs. DOJ's detailed terms and FAQ, updated 20 October, describe a three-year pilot with **discretionary $10,000–$30,000 awards**. The FAQ ordinarily connects payment to unsealed criminal charges and does not require conviction, recovery or a minimum loss. The landing page, updated **28 October**, still requires original written information, voluntariness, cooperation and criminal charges. DOJ makes the award determination. The announced $25 million Treasury commitment is not evidence of individual payments. [Executive sources EX-S04–07](executive/sources.json)

The inconsistency must remain visible: speech does not establish an unlimited implemented payment formula, and identified waste cannot be multiplied by 1% to create earnings. The terms' introduction omits the Department of War while eligibility section 6 includes it; other current DOJ pages also include it. This unresolved wording does not establish coverage of every defense purchase. Directive 26-12 and Executive Order 14395 support broader enforcement and prevention work, but no universal one-percent entitlement was located in them. Full portal wording was unavailable on two America.gov routes. See [executive findings and statements](executive/REPORT.md).

## What Congress has actually done

The authority DOJ cites, **28 USC530C(b)(1)(L)**, contains no percentage formula. Its ordinary ceiling is $3 million, subject to stated exceptions; awards of $250,000 or more require personal Attorney General or presidential approval and subsequent committee notification. Approval alone does not eliminate the ceiling. The full text retrieved was a GPO 2024 edition, corroborated by current House indexing; direct current-code retrieval failed. That edition limitation remains attached. No enacted general 1% entitlement or identifiable general 1% bill was located in the bounded searches. [Congress C01](congress/sources.json)

| Record | Status actually established |
|---|---|
| FY2026 NDAA, S1071 | Enacted 18 December 2025 as PL119-60 |
| S1473, Stop Stealing our Chips Act | Senate-passed; held at House desk in latest captured action, 21 May 2026 |
| HR4646, Whistleblower Protection Act of 2025 | Received in Senate and referred to Banking, 16 September 2026 |
| HR10792, FTC Whistleblower Act of 2026 | Committee referrals, 9 October 2026 |
| HR7725 / HR7726 | Union Calendar / Senate HELP referral respectively in captured records; no enactment recorded |
| Cline's 29 October benefits-fraud announcement | Member-hosted draft located; bill-number and official action crosswalk unresolved |

The October Warren/Grassley/Slotkin/Ernst supplier-pricing letter is an oversight request, with answers due **3 November**, still future at this cutoff. The September 2025 price-increase proposal and its thresholds are not established binding fraud tests. A member's criticism is an attributed claim, not this project's independent loss calculation. The [congressional report](congress/REPORT.md), [source register](congress/sources.json) and captured XML preserve action dates and record-update dates separately.

One enacted change materially affects auditing: **PL119-60 §1804(c) amended 10 USC3702 to use a $10 million threshold for qualifying prime contracts entered into after 30 June 2026**. A universal $2.5 million certified-data rule would misclassify some contracts. Modifications, subcontracts, exceptions, applicable clauses and agency deviations require their own checks; full current deviation text was not retrieved. Missing public cost data is therefore not proof of unlawful withholding. FAR 15.404-1 also requires valid comparators and adjustments for material differences. [Congress C11–15](congress/sources.json)

FCA qui tam shares commonly range from 15–25% or 25–30% of proceeds depending on government participation, with exclusions and other conditions. Those percentages are not general waste-reporting rewards. Public-disclosure, related-action and original-source rules require case-specific treatment. Civil FCA knowledge can include deliberate ignorance or reckless disregard without specific intent to defraud; a high price alone still establishes none of the necessary claim elements. [Congress C02–04](congress/sources.json)

## Executed name test: Amazon and Amazon.

Nineteen public USAspending requests captured contract-recipient searches, prime-contract award searches for **1 October 2025–30 September 2026**, before/after counts, explicit empty terminal pages and six profiles. `Amazon` returned **150 awards**; `Amazon.` returned **12**, all contained within the 150. The union is 150, not 162. Completeness applies to those saved queries, not every federal transaction during the fiscal year. [Name report](names/REPORT.md), [sources](names/sources.json), [capture manifest](names/capture-2026-10-30/manifest.json).

The records contain three distinct UEIs: Amazon.com Services has 11 awards, AWS without a terminal period has one, and AWS with a terminal period has 138. The two AWS identifiers remain separate. The dot query includes the one no-period AWS award while excluding the 138 terminal-period records. It is therefore not a literal punctuation cohort.

Six recipient rows form three same-UEI `P`/`C` profile pairs, not six companies. All three child profiles report a common parent UEI; parent profiles report themselves. This supports a source-reported hierarchy, not independently verified beneficial ownership. No same-UEI/multiple-name variation appears in the captured award set, and no award lacks a UEI. No amounts were summed: profile amounts and award-level financial measures have different bases.

This real test demonstrates why punctuation alone fails. Names preserve their original strings; Unicode normalization supplies only a comparison key. Legal suffixes, DBA text and subsidiary words remain, and mixed-script lookalikes are not automatically merged. A useful impersonation lead would require a dated identifier, control or representation contradiction tied to an actual transaction. The pilot establishes no such contradiction and no fake company.

## Executed price test: an original DLA bolt solicitation

The public DLA RFQ **SPE4A6-26-U-3619**, issued 3 September 2026, was acquired through its ordinary notice/consent flow and archived with a hash. For NSN **5306016864912**, seven history rows print unit costs from **0.93000 to 1.92000**. Independent visual inspection confirmed the rows, including one 472-quantity entry that a secondary listing had split. The history table omits historical units, packaging and other comparison terms. [Price report](pricing/REPORT.md), [selected evidence](pricing/snapshots/selected_evidence.json), [source/access register](pricing/source_access_matrix.json).

The current quote's price cells are blank. Its $350,000 maximum and 2,221 estimated annual quantity cannot yield a purchased unit price. Current `EA` and pack information cannot silently populate historical records. All **21 possible pairs** remain blocked by the comparison gate: **zero eligible pairs**, no verified invoice/payment and no savings estimate. This proves a useful public acquisition route, not overpricing.

The route has limits. SAM award access can require a key and supplies award context rather than complete invoices. FLIS catalog history is not verified award-price history. FedMall files and medical schedules were identified but not acquired as evaluated comparison datasets. Whole weapons also combine configuration, development, support and rights; their headline totals are weak first comparators. Public records access should be tested document by document.

## From observations to a new lead

The next package is **30 recent machine-bolt RFQs within a fixed 90-day window**, then a bounded trace of original awards/orders and modifications. The [follow-up queue](FOLLOW-UP-QUEUE.json) defines finite acquisition, item/unit, pricing, identity, novelty and independent-review tasks. Only same-item comparisons with supported economic adjustments advance. Missing records create explicit unresolved tasks; they do not become assumed prices or misconduct.

Each surviving lead needs a precise question about billing, delivery, substitution or a representation, together with counterevidence. Quantity discounts, urgency, qualification, tooling, freight, allocation and legitimate corporate relationships must be tested. A null cohort completes the assignment. No agent is instructed to keep searching until it produces an accusation.

Novelty has three separate meanings: new to this analysis, not located in searched public disclosures, and unknown to government. Public sources can usually address only the first two. WHIP permits qualifying independent analysis, including public information, subject to further conditions; neither public-data origin nor an existing related investigation automatically resolves eligibility. The [earlier DME/catheter work](../dme-catheter-2026-10-29/REPORT.md) remains calibration and published-case tracing, not a newly discovered scheme.

The public bank retains methods, neutral source records, published findings, uncertainty and disconfirmed hypotheses. New named adverse theories do not enter it automatically. Independent review reproduced the name data, visually checked the price table, and verified identical offline extraction. Sixteen name tests and six pricing tests pass; capture-proof, parent-link, page-location and non-finite-number defects were corrected. A code gate cannot authenticate its own supplied evidence. [Review report](review/REPORT.md), [review record](review/review.json).

## Claude/Grok collaboration and completion boundary

The repository contains two concrete handoffs, **CLAUDE-PRICE-001** and **GROK-IDENTITY-001**, both **queued, not dispatched**. No live result from either provider has been received. Grok authorization was initiated and remains pending. Automatic approval review rejected the Claude administrator route for excessive organizational permissions and a separate inference gateway for unapproved routing/account/billing scope. No further authorization attempt or model execution is implied. [Connection status](../../collaboration/CONNECTION-STATUS.json), [queue](../../collaboration/QUEUE.json), [handoff protocol](../../collaboration/README.md).

A repository file does not invoke a model or share persistent provider memory. Actual dispatch needs a verified connection and receipt; returned evidence needs independent review before graph acceptance. The completed work is a sourced policy review, two tested discovery methods, preserved evidence and finite next assignments. The remaining objective is to test new transactions without confusing anomaly, unreasonable price, false claim, recovery and reward.
