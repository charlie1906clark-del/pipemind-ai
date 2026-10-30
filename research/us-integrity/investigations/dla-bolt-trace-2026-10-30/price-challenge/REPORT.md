# DLA bolt price and buyer-independence challenge

The buyer-supplier scenario is a valid gap in the earlier work. Verifying a supplier's legal identity and reconciling an order's arithmetic do not establish a fair market price, independent bids or absence of a corrupt benefit. This new lane tests those separate questions for NSN **5306016864912**. The earlier [document review](../review/REPORT.md) remains frozen.

The actual current order establishes **906 EA at USD 0.9100, totaling USD 824.46 ordered**. It does not establish payment, an independent benchmark, an excessive margin or a buyer's benefit. The seven earlier award summaries report three to five offers; they do not disclose the losing prices, bidder independence, evaluation rationale or actual invoices. Their USD 4,962.02 total is selected cumulative obligations, not a loss estimate. See [current](../current/REPORT.md) and [historical](../awards/REPORT.md) evidence.

## What a 12% pattern would mean

For the user's anonymous example, assume that 100,000 is the annual price increment and 12% is the markup on an equivalent baseline. Currency is unspecified.

| Quantity | Exact relationship | Rounded illustration |
|---|---|---:|
| Baseline annual value | 100,000 / 0.12 | 833,333.33 |
| Gross annual value | baseline + 100,000 | 933,333.33 |
| Increment / baseline | 100,000 / 833,333.333… | 12% |
| Increment / gross | 100,000 / 933,333.333… | 10.714286% |
| Buyer's alleged cut | requires separate evidence | Unknown |

This is algebra, not a government transaction, loss or established kickback. If 100,000 instead meant gross spend, the calculation would differ. A distributor's acquisition cost plus a margin also differs from an independently available, equivalent delivered price: handling, inventory, compliance and commercial risk can matter. A buyer's cut cannot be deduced from either margin or premium.

## Distinct conclusions and their proof

| Conclusion | Evidence needed |
|---|---|
| Ordinary commercial margin | Actual cost and sale terms, with services and risk understood |
| Poor purchase | A feasible equivalent lower-cost option at the relevant time, plus selection rationale |
| Unexplained premium | A difference surviving technical, quantity, date, freight and service controls |
| Corruption indicator | Supported improper influence or benefit linked to a documented decision |
| Established bribery/kickback | A dated authoritative finding or admission establishing the conduct |

These are separate categories rather than an automatic escalation ladder. An unexplained price difference can justify further inquiry without proving intent. Corruption can exist even when its unit-price effect is unquantified.

For simplified acquisitions, [FAR 13.106-3](https://www.acquisition.gov/far/13.106-3) requires a fair-and-reasonable-price determination and prefers competitive quotations where possible. A catalog entry alone does not establish reasonableness. Supporting records may identify suppliers, quoted prices, delivery and other terms. The exact governing clauses, version and any applicable deviations still need to be checked for an individual action. [FAR 15.404-1](https://www.acquisition.gov/far/15.404-1) supplies useful comparison methods: prior prices must be valid comparators and material differences require adjustments. This protocol does not assert that Part 15 procedures or certified cost or pricing data were mandatory for these purchase orders. Source details are in [method_sources.json](method_sources.json).

## Concrete price tests

For each qualified line, use quantity **q**, actual comparable landed unit price **p**, and independently supported adjusted benchmark **b**. Preserve a single amount basis: ordered, invoiced or paid.

- Baseline **B = Σ(q × b)**.
- Observed value **A = Σ(q × p)**.
- Signed difference **E = A − B**.
- Amount-weighted markup **E / B**, where B is positive.
- Difference as a share of gross **E / A**, where A is positive.

Do not average line percentages equally. Keep negative differences in the total; report a positive-only sum separately if useful. Publish eligible amount and line coverage, exclusions and benchmark intervals. If there is no qualified benchmark, these outputs remain null. Actual invoice, acceptance, credits and payment evidence are separate gates before upgrading an order comparison to a paid-value comparison; neither is automatically a recoverable-loss finding.

A recurring 12% hypothesis must be declared before inspecting outcomes. Define tolerance, independent solicitation and period requirements, complete eligible universe and a held-out period. For example, a one-percentage-point band around 12% could be an exploratory screen, **not an official fraud threshold**. Report every residual and how results change across plausible benchmark ranges. Several lines from one solicitation are not independent repetitions. Do not round prices into a pattern, select only expensive purchases or reverse-engineer a benchmark by dividing the observed price by 1.12.

Control product mix by matching the same item and revision, then compare a fixed basket using unchanged quantities. Match feasible quantity tiers and full packs. Align quote dates and delivery commitments; document any time adjustment with item-relevant evidence. Compare the same freight, packaging, certification, traceability, warranty and payment terms. Our eight observed order/history rows do not support a causal regression or a repeated-premium finding with these missing controls.

The [price calculator](../price-controls/premium_audit.py) applies declared comparison gates and amount weighting. It is an arithmetic validator, not a source-authentication or misconduct detector. Its invented scenarios must remain separate from actual DLA observations.

## Market work: useful leads, qualification still unresolved

The independent [market review](market_review.json) evaluates the [seller matrix](../market/benchmark_matrix.json), not just its conclusions.

| Seller reference | Narrow observation | Decision |
|---|---|---|
| Cox HB8F38.34 | Test-site header; displayed stock 62 against an order for 906 | Exclude from executable quote set |
| Fastener SuperStore 191377 | USD-displayed 342.62 per 1,100-piece carton; division gives about 0.311473 per piece | Retain provisional catalog candidate |
| MF Supply HH38FX3/4G8ZY | Displayed box and piece prices; explicit pack count missing | Retain provisional catalog candidate; normalized pack price unresolved |

The reviewer freshly reopened all three product pages and reconstructed the carton arithmetic. MF initially failed at its canonical URL, then succeeded through the recorded product-details request and redirect; its terms were also independently checked. The two latter sellers display the same upstream part reference, which does not establish independent manufacturers or collusion. No seller page establishes a compliant, available 906-unit government order.

A 1,100-piece carton also means buying a full carton if smaller quantities are unavailable; multiplying a prorated unit price by 906 would understate that purchase's outlay. Larger-carton discounts require their actual minimum quantities. No hypothetical catalog difference is booked as a government overcharge.

The decisive product gap is an unrestricted authoritative crosswalk from the NSN and applicable revision to all required characteristics. A secondary site's dimensions and an ASME B18.24 reference do not by themselves supply this crosswalk. Complete technical equivalence and accepted supply conditions must be established before qualifying any catalog benchmark.

## Test competition and the buyer's actual decisions

Acquire the actual bid/quote abstract, acceptability review, award rationale and price-reasonableness record for each named solicitation. Reconstruct offered prices, delivery, timestamps, withdrawals and exclusions. Three to five reported offers alone neither prove nor disprove independent competition.

[DOJ's collusion guidance](https://www.justice.gov/atr/red-flags-collusion) identifies proposal similarities, repeated winner patterns and losing-bidder subcontracting as possible investigative signals. Apply those as screens and test ordinary explanations: common templates, standardized goods, shared upstream supply, capacity and specialization. A shared manufacturer reference is not evidence that separate sellers coordinated bids.

Separate the requisitioner, purchasing staff, contracting officer, evaluator, inspector and payment official. A signature does not establish who selected the specification, supplier or price. Link a public professional role to an actual decision only through dated records. Then compare same-item outcomes before and after role changes, and against comparable offices, using a declared procurement universe. Report vendor win share and bid-exclusion patterns with their denominators. Staffing, mission and availability changes remain potential explanations.

Business filings may establish dated officers, ownership or employment where actually disclosed. Preserve effective dates and filing dates; current registrations do not establish historical ownership. This work does not assemble residential, contact, family or private financial profiles.

## What known corruption shows—and what it does not

The [known-case calibration](mechanism_sources.json) documents a USAID case using DOJ and OIG releases. DOJ reported individual guilty pleas and corporate admissions; its account describes concealed benefits and manipulated procurement decisions involving existing contractors. OIG says an allegation of procurement-information disclosure triggered its investigation. Status is dated to the releases, not asserted to be unchanged today.

This illustrates why real companies and correct arithmetic cannot clear a corruption hypothesis. It supplies no bolt price comparator, fixed 12% pattern or link to this DLA cohort. The announced contract volume is not established loss. Underlying bank exhibits were not inspected here; the official summaries are identified as such.

## Highest-value next records

1. **Authoritative unrestricted item characteristics and revision.** This decides whether the cheaper catalog products are the same product.
2. **Dated, accepted comparable supply terms.** Confirm pack size, quantity available, delivery, freight and required compliance for the actual order; public pages may support only part of this. No supplier contact was made.
3. **Actual bid abstract and price-reasonableness record.** These distinguish independent competitive quotes from an offer-count summary and explain selection.
4. **Historical CLINs and modifications.** Recover specification, unit, pack and delivery terms rather than copying current requirements backward.
5. **Dated official role and decision records.** Identify actual procurement influence before testing buyer-linked patterns.
6. **Receipts, invoices, credits and disbursements.** Required to determine net paid amounts.
7. **Specific benefit/influence evidence.** This may appear in released official records; nonpublic bank, payroll or communications records require a lawful investigative process and are not part of this public research.

[Evidence requirements](evidence_requirements.json) lists exact fields, tests and acquisition status. [The agent contract](agent_contract.json) assigns eight specialized roles, separates producer and reviewer, and defines bounded follow-up and Claude handoff requirements. Inaccessible or withheld records remain evidence gaps, not evidence of concealment. Absence of a public enforcement result does not prove that a hypothesis is new.

This lane's acceptable outcome is a supported conclusion—including an ordinary explanation or an unresolved result. It does not require discovering fraud.
