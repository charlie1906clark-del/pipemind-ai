# Federal price pilot — observed 2026-10-30

This pilot acquired **30 official award records across DLA, VA and HHS**, traced three selected awards, and reached a new original DLA award with **two priced contract lines**. The DLA arithmetic reconciles exactly. It establishes an awarded line price and item scope for further comparison; it does not establish excessive pricing, a kickback, a cash payment, a loss, or a previously undiscovered fraud.

The strongest new price evidence is DLA purchase order **SPE4A626PW775**, signed 2026-07-09, awarded to the reported recipient DON INDUSTRIAL GROUP LLC, UEI `XN9HKU6LUM59`. [Official award record](https://www.usaspending.gov/award/CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-) · [Original DLA award](https://dibbs2.bsm.dla.mil/Downloads/Awards/09JUL26/SPE4A626PW775.PDF) · [Source page 4](selected/dla-award-page4.png) · [Source page 5 test line](selected/dla-award-page5-first-article.png).

| Original line | Exact scope | Quantity / unit | Awarded price | Extended amount |
|---|---|---:|---:|---:|
| 0001 | NSN `5306004457358`, part `39-8820-501`, special front-engine-mount bolt | 2,243 EA | $272.99 | $612,316.57 |
| 0002 | Government first-article test requirement | 1 EA test requirement | $3,500.00 | $3,500.00 |
| Reconciled award | Production plus separate testing | Quantities not combined | — | **$615,816.57** |

The $3,500 difference between production-line multiplication and the total award is explained by the separately priced testing line. It is not an unexplained excess. The first page's 2,244 quantity combines heterogeneous lines and must not be used to infer 2,244 production bolts. The contract's E08 provision explicitly defines the test line's EA as one first-article test and separates test costs from production costs. The inserted first-article clause specifies **two test articles**, due within 400 days, and a 180-day government response period. Those two test articles are not automatically added to production quantity; the clause permits accepted, undamaged articles to count toward contract quantity. [Selected E08](selected/dla-award-page7-e08-selected.txt) · [Selected first-article clause](selected/dla-award-page11-first-article-selected.txt).

The production delivery date is **2028-04-10**, while the test line is due **2027-08-13**. Production is firm fixed price, inspection and acceptance at origin, FOB origin with government freight payment, zero quantity variance, and specified packaging, drawing and quality requirements. The source describes a **critical application item**. The test line separately shows contractor freight payment. A generic hardware-store bolt or a mismatched quantity/quality/lead-time quote is not a valid comparison. No matched independent unit-price benchmark was obtained. [Item specification](selected/dla-award-page3.txt) · [Production terms](selected/dla-award-page5-selected.txt) · [Test schedule](selected/dla-award-page6.txt).

Page 2 identifies the dealer as CAGE `745V4` and says it will supply the exact part from approved manufacturer SPS TECHNOLOGIES, LLC, CAGE `27624`. This is a contractual supplier designation, not independent proof of actual origin, delivery, payment, beneficial ownership or a transfer to the manufacturer. A selected page-1 excerpt records the printed contracting/ordering officer role; it does not establish personal benefit or who made the underlying price-selection decision. [Dealer/manufacturer clause](selected/dla-award-page2.txt) · [Professional-role excerpt](selected/dla-award-page1-role-selected.txt).

## What the bounded cohort covers

The fixed window is 2026-07-03–2026-07-31 using USAspending's **base-obligation-date / new-awards-only** filter. Each row is an award-level obligation as observed on 2026-10-30, not a payment or unit price. Each stratum is only the first ten descending-obligation results. All three responses report another page. [Exact protocol](SELECTION_PROTOCOL.md) · [All 30 normalized records](observations.json) · [Coverage](coverage.json).

| Stratum | Captured awards | Sum of captured cumulative award obligations | Coverage |
|---|---:|---:|---|
| DLA, PSC 5306 bolts | 10 | $2,006,327.90 | First page; more results exist |
| VA, PSC 6515 medical supplies/equipment | 10 | $119,368,989.65 | First page; includes five express reports |
| HHS, PSC 6515 medical supplies/equipment | 10 | $11,768,165.65 | First page; mixed item and system descriptions |

These sums are **neither July spending nor population totals nor estimated exposure to fraud**. Five VA descriptions explicitly reference express reports; some performance periods predate July. The original common date window and all 30 rows remain intact. No sampling-completeness or fraud-prevalence inference is supported.

## Three targeted traces

| Candidate | Official path established | Price evidence and remaining records |
|---|---|---|
| DLA `SPE4A626PW775` | DLA Aviation → reported recipient UEI `XN9HKU6LUM59`; solicitation `SPE4A626Q0688`; original two-line award acquired | $272.99 production unit price and separate $3,500 first-article line. Need exact-item dated comparator, evaluated bids/price reasonableness, modifications and eventual invoice/acceptance evidence. |
| VA `36C79126F0030` | Commodities & Services Acquisition Service → First Nation Group; order → BPA `36C79123A0003` → FSS `36F79719D0027` | $10,601,525.70 award obligation; PAP devices/accessories. No order CLINs, quantities, exact models or purchased unit prices acquired. Indexed schedule PDF returned 404. |
| HHS/NIH `75N98026F00268` | NIH OLAO awarding office; NIH-CC funding office → TrillaMed UEI `GW9FLBWB5625`; RFQ `RFQ1821947`; VA FSS `36F79720D0041` | $1,928,503.77 award obligation; defibrillators. No exact order models, quantities, accessories or unit prices acquired. Exact RFQ search yielded no document; indexed schedule PDF failed. |

The VA and HHS records are selected for document tractability and economic size, not suspected misconduct. Agency buying and funding offices can differ. Reported offer counts—four, two and one respectively—are metadata and do not by themselves establish bid independence, collusion or a purchasing violation. The trace links are award/recipient/office/parent relationships, **not verified money movements**. [Graph](transaction_links.json) · [Field-level missingness](missingness.json).

The HHS FSS route did expose two official catalog entries: item `240031300` at $14,744.66/EA and item `P1806UD` at $2,012.06/EA. They are respectively a surgical-display package and a cardiac-laboratory server software upgrade. **Both were rejected as defibrillator comparisons.** Sharing a contractor and schedule contract does not establish an exact-item match. The displayed contract dates do not establish historical line-price validity. [Recorded exclusions and source URLs](rejected_comparators.json).

## Next work and stopping conditions

Eight specialized, dependency-aware tasks are defined in [follow_up_tasks.json](follow_up_tasks.json): independently reproduce DLA specifications; obtain exact-item benchmarks; trace bid/price/payment support; acquire VA order lines and governing prices; acquire NIH order/quote lines; independently review each medical price comparison; and run an adversarial evidence review. These are importable task definitions, not a claim that another model or an autonomous background process has executed them.

The immediate evidence requirement for the user's concealed-markup hypothesis is an independently supported comparable price or supplier cost **for the same item and terms**, followed by documents identifying the actual price decision and any benefit. Neither a high award total, a punctuation difference in a name, a shared schedule contract, nor an observed spread alone supplies those missing links. Supplier cost, markup, buyer benefit and kickbacks remain unestablished in this pilot. A null result is retained rather than converted into an accusation.

This pass used **12 search queries and 23 API/document retrieval operations**. Failed URLs, the SAM shell, excluded comparisons and unvisited PDF links remain visible in [request_ledger.json](request_ledger.json), [document_links.json](document_links.json), and the capture manifests. No accounts or protected payment systems were accessed. [Source registry](sources.json) distinguishes original-response hashes from selected snapshots; [selected_manifest.json](selected_manifest.json) pins public source selections.

Offline validation checks capture hashes, exact identifiers, agency/PSC filters, date bounds, finite values, duplicate exclusion, line arithmetic, positive original-award quantities, and separation of obligation, production, testing and catalog prices. See [VALIDATION.md](VALIDATION.md). The pilot observations feed the repository’s [canonical Obsidian output](../../generated/obsidian/); this package does not maintain duplicate per-award notes.
