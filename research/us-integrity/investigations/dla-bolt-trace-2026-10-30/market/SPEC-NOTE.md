---
type: evidence-gap
date: 2026-10-30
nsn: "5306016864912"
status: primary-crosswalk-not-acquired
tags: [procurement, price-audit, primary-source-gap]
---

# Exact specification remains unverified

The original DLA contract proves that NSN **5306016864912**, described as a machine bolt, is priced at **USD 0.91000 per EA**. Its page 5 cites **ASMEB18.24**, revision date **10/16/2023**, with **TDP Rev A Gen 1**. The **PART PIECE NUMBER field is blank**. It does not supply the diameter, pitch, length, material grade or finish needed to certify an exact retail equivalent.

The secondary lead associates this NSN with **AEB02F375750WA6DG1**, nominal **3/8-24 UNF × 3/4 inch**, **Grade 8 steel**, and a **zinc** treatment. That lead is useful for choosing provisional market products. It is not an acquired primary specification. In particular, “zinc” alone does not establish a yellow coating specification, thickness, manufacturing source or acceptance requirements. ASME's appearance beside a standard is not evidence that it manufactured the bolt or is an approved supply source.

## Evidence and access result

| Source | Observed result | What it establishes |
| --- | --- | --- |
| [Original DLA contract](https://dibbs2.bsm.dla.mil/Downloads/Awards/17SEP26/SPE4A626D61WS.PDF), page 5 | Existing selected text read locally | NSN, item name, standard reference, blank part field, USD0.91/EA |
| [PUB LOG overview/manuals](https://www.dla.mil/Information-Operations/Services/Applications/PUB-LOG/ProceduresManuals/) | Official search-index text returned; document open returned 403 | A route lead for public characteristics and reference data, not the exact record |
| [DLA PUB LOG search training](https://www.dla.mil/Small-Business/Resource-Center/Training-Resources/Details/Article/4179917/how-to-use-pub-log-to-find-national-stock-number-information/) | Official search-index text returned; document open returned 403 | A described installed application workflow; no lookup performed here |
| [WebFLIS overview](https://www.dla.mil/Information-Operations/Services/Applications/WebFLIS/) | Official search-index text returned; document open returned 403 | Related PUB LOG route only |
| [PUB LOG main page](https://www.dla.mil/Information-Operations/Services/Applications/PUB-LOG/) | Document open returned 403 | Retrieval failure only |
| [DLA PUB LOG brochure](https://www.dla.mil/Portals/104/Documents/J3LogisticOperations/Brochures/J3_PUB%20LOG%20Brochure_240126.pdf?ver=bDUUFfog-GHv1aHQtgaQGA%3D%3D) | Official search-index text returned; document open returned 403 | No exact NSN association acquired |

These are failures of the retrieval path used in this run. They do **not** prove that the record is absent, restricted or unavailable to the public. No access controls were bypassed. No login, large archive download or restricted technical-data retrieval was attempted.

The exact source, query and status ledger is in [spec-crosswalk.json](spec-crosswalk.json). This subtask used four search queries, five web document-open attempts, and two local document reads. The first two search responses were lost to output/context truncation and are explicitly excluded as evidence. No search-negative claim relies on them.

## Consequence for the price audit

Record retail prices as **provisional dimensional comparators**, with their pack quantities, stock, grade, finish, dates and terms. An observed spread may justify a follow-up inquiry, but cannot yet be called an equivalent-item overcharge or recovered saving. The gap does not imply the government price is fair either. The supplier's invoice arithmetic and identity can both be correct while buyer independence or price fairness remains unresolved.

The next narrow evidence target is the publicly releasable **CHAR** and **MCRD/reference** records for **NIIN 016864912**, from a dated official PUB LOG snapshot. Retain field labels, units, reference qualification codes and an extract hash, then reconcile them to the contract's packaging, quality, traceability and acceptance requirements. Neither public catalog availability nor this suggested extraction is a claim that the actual record has already been acquired.

## Local provenance

Verified selected primary text: `../current/snapshots/parent-page5.txt`.

SHA-256: `e551d347f7dc7abe51e52351b6ea4dbaa70d97c88ebbeeb447e71f42aa26d9dd`.

The primary PDF was already captured by the current-contract agent; it was not redownloaded in this subtask. Existing `../current/observations.json` was read to align the notation and keep the parent contract unit price distinct from ordered quantities and unverified payments.
