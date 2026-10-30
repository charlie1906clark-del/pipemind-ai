# Adjacent Claude/Codex investigation: one DLA bolt procurement chain

Research cutoff: **30 October 2026**. This pass concentrates on DLA machine-bolt procurement, starting with **NSN 5306016864912**. It complements the pricing task the user reports assigning to Claude. Codex traced the historical awards and supplier identifiers, acquired the newer original contract and delivery order, and assigned an independent reviewer. No Claude result has yet been received or verified through the repository.

**The current question is whether the documented USD 0.91 unit price was reasonable and independently selected. Neither question is resolved.** The original newer contract specifies **USD 0.91 per EA**. Its inspected delivery order specifies **906 EA for $824.46**. A secondary site's $157.5867 unit-price display numerically matches a contract ceiling divided by estimated quantity. That calculation is not a purchased unit price. The acquired source lines resolve the ambiguity directly.

## What was actually traced

| Evidence chain | Completed result | What remains unproved |
|---|---|---|
| Original RFQ history → seven exact PIIDs → official award records | All seven dates match; each printed quantity × cost matches the corresponding cumulative obligation | Original historical CLIN terms, actual delivery and payment |
| Five historical CAGEs → current official CAGE registry → USAspending UEIs | Five exact crosswalks agree; all seven historical award joins agree | Historical activation/eligibility, bank payee and beneficial ownership |
| Newer parent contract → inspected delivery order | Both original documents acquired; same CAGE, NSN, basic CLIN and USD 0.91 price; 906 × 0.91 = 824.46 | Performance, acceptance, payment and all other orders/modifications |
| Independent challenge | Source rows, arithmetic, identifiers, terms and selected artifact hashes checked | Full forensic audit and case-specific legal conclusions |

The historical [award report](awards/REPORT.md) records **$4,962.02 in selected cumulative obligations**, three to five reported offers per award, and seven firm-fixed-price purchase-order records. These amounts are not cash paid or potential recoveries. Offer counts do not authenticate bidder independence. Those checks do not test market reasonableness or exclude collusion; no transaction-specific basis for alleging impersonation, collusion or false billing has yet been established.

The [identity report](identity/REPORT.md) resolves five CAGE/UEI crosswalks and preserves 12 source-reported aliases. Nine recipient-profile rows represent five identifiers, not nine independent companies. Sole-proprietor names and ordinary naming variants are recorded as business facts. The current source hierarchy reports each recipient as its own parent; this does not prove that beneficial ownership is unchanged or fully known.

## Original current documents change the interpretation

The parent **SPE4A6-26-D-61WS**, dated 17 September 2026, contains a **$350,000 maximum** and **2,221 EA estimated annual quantity** on page 2. Page 5 explicitly prices CLIN 0001 at **USD 0.91000 per EA**, with QUP 001 and 76 delivery days. Its base-line quantity of 0.000 is part of an indefinite-delivery instrument, not evidence that ordered bolts cost nothing.

The child **SPE4A6-27-F-0588**, dated 19 October 2026, explicitly references that parent and basic CLIN. Page 2 orders **906 EA at 0.9100**, totaling **$824.46**, with delivery shown as **4 January 2027**. The original receipt/payment certification blocks were blank when inspected. The evidence establishes an order and its price; it does not establish paid cash or completed performance. See [current document findings](current/REPORT.md), [structured observations](current/observations.json), and [selected source pages](current/selected_manifest.json).

Two detector errors are now concrete:

1. **Wrong amount basis:** 350,000 ÷ 2,221 is approximately 157.5867, the secondary display's figure. The original ceiling and non-firm estimate cannot support that unit-price label. This numerical agreement does not reveal the website's internal algorithm or intent. It does establish why a public-data detector must inspect original priced lines before escalating.
2. **Wrong role:** the original document labels ASME B18.24 as a basic nongovernment standard. A secondary page places ASME in a manufacturer/source list and describes the award recipient as unlisted. That display is insufficient evidence that an unauthorized manufacturer supplied the item. A standards reference, supplier role and approved-source restriction require separate evidence.

The RFQ and awarded terms also differ: minimum delivery order quantity changed from **555 to 1 EA**, and delivery changed from **78 to 76 days**. Those differences are not inherently improper. They show why a solicitation cannot automatically stand in for the final contract. Historical unit/pack/revision and other terms remain unresolved, so the new current line does not retroactively validate comparisons against every older price.

## Access gaps are evidence limitations

Seven historical award-document attempts produced six consent-flow timeouts and one HTML response, rather than the original priced PDFs. Their URL date components were derived from award dates, not verified posting dates. These failures are not evidence of deletion or concealment. A DLA newsletter's indexed official text describes 120-day PO/DO retention from posting, extended by modification; the complete newsletter was inaccessible, so this remains a qualified route-design input.

For the newer parent and child, three USAspending requests returned successful empty results and two returned HTTP 503. The official USAspending data guide describes a **90-day DoD procurement publication delay**. The inspected documents were only 43 and 11 days old. Delay is a plausible explanation for their absence from the acquired search results, not a verified cause in either case. Both original DLA documents were nevertheless acquired through the normal public notice/consent flow.

These observations improve the next acquisition design: preserve original documents while available, track actual posting/modification dates, and reconcile later aggregate publication. An approximate 91–119-day award-date screen may identify an overlap worth testing, but different date bases and processing delays mean it cannot guarantee availability.

## Price fairness and buyer–supplier collusion remain open

The user identified a failure mode that the first pass did not adequately test: a legitimate supplier can invoice an agreed price containing a repeated excess, with some benefit returned to a buyer. Reconciling records, verifying identifiers and observing declining historical prices do not rule this out. A constant percentage excess can persist even as the underlying market falls. There is currently no transaction-specific evidence of such a benefit in this DLA chain.

The [market audit](market/REPORT.md) opened seller-owned pages for the provisional description, 3/8-24 × 3/4-inch Grade 8 zinc-yellow hex cap screws. These are research candidates, not yet demonstrated substitutes for the exact NSN and government terms:

| Seller | Observed price | Material comparison limit |
|---|---|---|
| Fastener SuperStore, 191377 | $342.62 per 1,100 pieces; displayed $0.31147 each | Full-carton quantity differs from 906; historical offer validity, item-specific stock, government compliance and delivered costs unresolved |
| MF Supply, HH38FX3/4G8ZY | $328.91 per box; displayed $0.29901 per piece | Box quantity not explicit in acquired page; do not infer it as verified from arithmetic |
| Cox, HB8F38.34 | $0.384 at 500+ | Page explicitly says Test Site and lists only 62 available; exclude as a live906-piece benchmark |

These prices justify pursuing a more exact comparison with $0.91. They do **not** establish an overcharge percentage, recoverable amount or buyer payment. The [matrix](market/benchmark_matrix.json) preserves date, specification, quantity, stock and procurement-term gaps. The [primary specification trace](specification/REPORT.md) verified an accessible official DLA archive and its documented extraction route, but did not extract the exact NIIN record. The current contract cites ASME B18.24 but has a blank part-number field; generic catalog dimensions cannot fill that primary-source gap. The independent [price challenge](price-challenge/REPORT.md) specifies evidence needed to accept or reject the comparison and a separate test for buyer benefit.

The [price controls](price-controls/README.md) calculate quantity-weighted differences against an independently evidenced reference, including repeat purchases. They reject circular reasoning such as dividing $0.91 by 1.12 and then presenting the result as proof of a 12% excess. The user's 100,000 example is a currency-unspecified illustration: at 12% of the underlying cost, the base is approximately 833,333.33 and the total 933,333.33. That excess is 10.7142857% of the total. The engine marks this synthetic example separately; the real DLA reference price and excess remain null until the comparison passes review.

The [audit playbook](price-challenge/evidence_requirements.json) separates ordinary margin, poor value, an unexplained premium and evidence of collusion. Three to five reported offers do not establish independent competition. The needed records include the unrestricted item specification, compliant dated quotations, bid abstracts, the price-reasonableness determination, changes and approvals, and appropriately documented buyer/supplier benefit relationships. A person signing a form is not automatically the person who selected a price or benefited from it.

## Decision and adjacent work

Close only the disproved **$157.5867 purchased-unit-price interpretation**. Keep **$0.91 market reasonableness** and **buyer independence** unresolved, with finite evidence requests and explicit alternatives. This seed is both a useful detector control and an active specification/price-comparison question. No fraud inference follows from supplier naming, a price gap alone, or the inability to acquire a record.

Remain within DLA hardware. Rank a later cohort by repeat purchasing exposure, feasible independent benchmarks and source availability. The [next-cohort plan](NEXT-COHORT.json) preserves the first seed's open question and defines a finite extension; it has not run. Its price method must detect persistent excess as well as price increases. Annualization requires observed transactions in a stated period; neither a contract ceiling nor an estimated annual quantity can become paid spending.

Claude's complementary review should challenge the provisional market matches, the weighted-premium controls and the independence/benefit requirements. [CLAUDE-UPDATE.md](../../collaboration/CLAUDE-UPDATE.md) identifies exact paths and questions. Existing task specifications remain immutable. Supplemental evidence must retain the commit and hashes actually read. Separate branches prevent one worker overwriting another, and the coordinator reviews findings before graph acceptance.

The [independent review](review/REPORT.md) and [validation record](VALIDATION.json) distinguish verified observations, missing inputs and completed tests. The public bank retains selected evidence without supplier street/contact fields. Original download hashes are preserved, but selected excerpts are not labeled complete raw documents. **No new fraud, loss, recovery, reward eligibility, supplier contact or external submission is claimed.**
