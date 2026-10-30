# Public procurement price discovery — 30 October 2026

**Outcome:** one official DLA solicitation was acquired successfully, with seven genuine procurement-history price rows for a common bolt. This demonstrates a public acquisition path for a new investigation. It does **not** establish a new fraud case, an overpayment, a payment at all, or recoverable savings. No supplier is identified here as suspicious.

The strongest feasible next work package is a bounded cohort of **30 recent public DLA machine-bolt solicitations**, followed by original award/order verification for the same NSN and truly comparable terms. Starting with whole weapons or comparing contract ceilings would add substantial ambiguity before any reliable unit-price baseline exists.

## What was acquired

The original [DLA RFQ SPE4A6-26-U-3619](https://dibbs2.bsm.dla.mil/Downloads/RFQ/9/SPE4A626U3619.PDF), issued 3 September 2026, concerns machine bolt NSN **5306-01-686-4912**. Its public download first presents a DoD notice and consent form. The observed form was submitted normally in the same session, without an account, credentials, proxy, or access-control workaround. The returned 423,468-byte PDF is archived with SHA-256 `4a3996d9aca0fac0b32ea1cebfe8833fdbb144de33dc0af2739d0269b037ac51`.

Pages 7–8 contain these procurement-history entries. This is a faithful **history-table transcription**, not a reconstructed invoice:

| Award date | Quantity printed | Unit cost printed | Source page |
|---|---:|---:|---:|
| 2026-05-26 | 1,212.000 | 0.93000 | 7 |
| 2025-11-14 | 706.000 | 1.00000 | 7 |
| 2025-06-16 | 448.000 | 1.05000 | 8 |
| 2025-05-16 | 665.000 | 1.10000 | 8 |
| 2025-04-30 | 472.000 | 1.17000 | 8 |
| 2025-03-24 | 240.000 | 1.44000 | 8 |
| 2024-12-04 | 536.000 | 1.92000 | 8 |

All seven surplus-material flags are `N`. Contract numbers and CAGE identifiers are preserved in [selected evidence](snapshots/selected_evidence.json) solely as neutral source keys. Historical unit of issue, pack quantity, technical revision, delivery terms, nonrecurring costs, and currency labeling are absent from this particular history table. They remain **null**, rather than being filled from the current solicitation. There are **zero verified comparable price pairs** and no savings calculation.

The current solicitation specifies `EA`, QUP `001`, 78-day delivery, FOB origin, destination inspection and acceptance, and packaging requirements. It provides an estimated annual quantity of 2,221, a minimum order of 555, and a guaranteed minimum of 222 only after the unilateral IDC becomes binding. Its maximum contract value is $350,000. **Its current unit-price and total-price cells are blank.** Dividing $350,000 by 2,221 would manufacture a price from a ceiling and an estimate. It cannot support an overpricing claim.

The source also exposed an important granularity discrepancy: a secondary discovery listing displayed the 30 April 2025 quantity as three entries totaling 472. The original RFQ history has one 472-unit row. This does not establish that the mirror's components are false; it establishes that they cannot be counted as three separate rows of this primary history table. That mirror supplied a document lead; it was not used as authoritative transaction evidence. Pages 7–8 were rendered and visually checked against extraction.

## Available public routes and their limits

| Route | What it can contribute | Access actually established | Critical limitation |
|---|---|---|---|
| DIBBS public RFQ PDFs | NSN, current technical/delivery/pack terms; sometimes historical contract, quantity and unit-cost table | One official PDF acquired and archived | A solicitation is not a paid invoice; prior terms require prior documents |
| DIBBS awards and original orders | Potential bridge from history contract to priced award/CLIN | Discovery path identified; original historical award documents not acquired in this run | Do not assert every historical award is public or contains invoice-level detail |
| DLA FLIS/PUB LOG reading room | NSN identification, reference/part information, management and packaging reference files | Official page search index read; direct site returned 403 | `History.zip` concerns inactive NSN catalog history; it is not verified award-price history. Catalog prices are not necessarily negotiated net prices |
| DLA FedMall sales file | Potential transactional cross-check | Monthly XLSX files identified in official page index; none downloaded | Column structure, unit prices, sales meaning and completeness remain unverified |
| SAM Contract Awards API | Award/action identifiers, agencies, recipients and contract context | Official documentation read; no authenticated API call made | Requires API key. Revealed DoD data are delayed; public response omits immediate/domestic parent fields. Not an invoice-price feed |
| USAspending | Obligations, outlays and award context, cohort selection | Existing repository connector already available; official documentation read | Award/action financial totals cannot supply a missing CLIN quantity or unit price |
| VA FSS / National Acquisition Center | Public line-item prices and contract terms for medical/pharmaceutical comparison | Current official pages located; no catalog dataset downloaded in this run | Schedule/list ceiling and national-contract concessions differ from actual paid price; match NDC, strength, package and dates |
| Original agency records / FOIA | Missing orders, CLIN schedules, modifications, accepted-delivery or payment evidence where releasable | Public FOIA route identified; no requests submitted | Not all records are releasable; a public-data premise does not remove exemptions or create absent records |

The [access matrix](source_access_matrix.json) distinguishes an acquired dataset from a documentation read or search-index discovery. A failed request is recorded as a session access result, not proof that the underlying record is unavailable to everyone. No speculative endpoint or API stub is presented as a working price feed.

## What a defensible price comparison requires

[FAR 15.404-1](https://www.acquisition.gov/far/15.404-1) expressly requires evaluating the validity of historical prices and adjusting for materially different terms, quantities, markets and items. It also distinguishes price analysis from cost analysis and addresses unit-price allocation. The novelty-seeking workflow should implement those requirements before ranking a supplier.

1. **Resolve the item:** exact NSN, manufacturer/part and revision where applicable; approved-source constraints; new versus repaired/surplus condition; inspect ambiguous or superseded item identifiers.
2. **Resolve the purchased unit:** preserve the original unit of issue, unit of purchase, QUP and pack count; normalize only with an evidenced conversion. An `EA` current solicitation cannot silently define a prior row's unit.
3. **Resolve the instrument and amount:** distinguish an IDV/IDC ceiling, obligated action, delivery-order CLIN, optional quantity, invoice, credit and payment. Keep amendments and order relationships so neither IDV plus child order nor old plus modified price is counted twice.
4. **Resolve economics:** quantity tier, award/order date, lead time and urgency, freight/FOB, inspection, warranty, qualification, tooling, nonrecurring engineering, minimum lots and sole-source constraints. A large premium can be legitimate, wasteful, or incorrectly recorded without being deceptive.
5. **Verify the suspicious proposition:** seek a demonstrably false representation or duplicate/non-delivered/substituted billing, alongside the purchase/payment evidence. High cost alone is a price-review lead; intent or knowledge cannot be inferred from the price gap.
6. **Search prior disclosures:** compare NSN, contracts, CAGE/UEI and mechanism against DOJ, DoD/DLA OIG, GAO, agency reports and public court material. “Not found in our search” is bounded novelty status, never proof that a case is undiscovered.

Retail-marketplace screenshots and vaguely similar materials are weak comparators. For weapons, configuration, integration, sustainment, data rights, testing and delivery schedules often dominate the price. Use a separately documented cost-analysis path rather than extrapolating bolt economics to a weapon system. Proprietary cost data that have not been released remain a missing input.

## Next work package and stopping rules

**WP-DLA-BOLTS-001** targets 30 RFQs issued within a documented 90-day window, collected from an official public listing or an explicitly supplied list of official URLs. The sample is purposive, not representative of all federal procurement. Record every included, excluded, duplicate, inaccessible and empty-history document. A discovery mirror can identify a URL, but every price record must be verified against the primary document.

The acquisition agent produces a hashed source registry and raw documents. A second agent independently checks table extraction and units. The item specialist groups only verified equivalent products. The price analyst releases a comparison only when the term gates pass; otherwise it creates a missing-record task. A separate challenger enumerates ordinary explanations and attempts to disprove the lead. A novelty reviewer searches previous disclosures. A human reviewer decides whether a private evidence package warrants further records work or referral.

This pilot ends with **feasibility established, no scored suspect and no savings estimate**. Do not search indefinitely until a positive result appears. A completed cohort with no supported lead is a valid result. Do not submit reports, contact procurement staff, accuse entities, or expose private candidate dossiers merely because an automated threshold fires. The current public history sample is deliberately retained as a neutral source demonstration.

The precise reviewable agent instructions are in [agent_contract.json](agent_contract.json). This is an execution contract for future work, not a claim that Claude, Grok or any external model has performed these checks. The Python eligibility gate checks completeness and declared comparability mechanically; it cannot authenticate arbitrary source hashes, descriptive strings or review flags. Independent source and adjustment review remains mandatory even when the gate passes.

## Reproduce and validate

From this directory, offline extraction uses the archived primary source:

```bash
python reproduce.py --pdf snapshots/SPE4A626U3619.pdf --output /tmp/dla-offline-new
```

To request the same public document anew through its ordinary consent flow:

```bash
python reproduce.py --output /tmp/dla-live-new
```

Python 3 and Poppler `pdftotext` are required. Output paths must be new. The downloader has a bounded response size, 20-second request timeout, expected-host/form checks and no bypass/retry fallback. A changed PDF hash requires review. It does not retain cookies or hidden form values. The raw acquisition, packaged live reacquisition and offline replay succeeded; both replays produced the identical selected JSON and original PDF hash; [manifest](acquisition_manifest.json) records the exact coverage and verification status. Published selected evidence is a subset and must not be mistaken for a complete award history.
