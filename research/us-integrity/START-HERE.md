# US public-funds integrity research — start here

Built and researched on **29 October 2026**, in a separate domain of PipeMind. This is a source-led research bank with real data captures, a completed catheter investigation and executable local tools. It does not identify a newly proved fraud case or promise a reward.

## Latest completed investigation

Read the [catheter supplier investigation](investigations/dme-catheter-2026-10-29/REPORT.md). Six specialist workers acquired all **6,870 published supplier rows** for three catheter codes in 2022–2024, independently checked the calculations, traced original Gold Rush case documents, and matched public company, NPI, exclusion and revocation records. The case focus is Centennial's secondary-payer and intercompany trail; the public data test measures historical concentration and its limitations. The evidence supports a more precise existing-case map and unresolved questions, not a newly established fraud or loss.

The [execution ledger](investigations/dme-catheter-2026-10-29/RUN-LEDGER.md) records actual assignments. Findings, source records, temporal events and monetary measures enter Obsidian through a reviewed, digest-pinned graph extension. The follow-up queue contains finite research questions and disconfirmation conditions. No unattended worker or external submission was activated.

## Read this first: the reward claim

Trump's 20 October remarks described 1% of recovered money. DOJ's written WHIP programme instead currently describes discretionary $10,000–$30,000 payments for qualifying original tips leading to criminal charges. This is not a general entitlement to 1% of estimated savings. The programme's detailed terms also contain inconsistent defence-scope wording. Other statutory/pilot routes have different conditions, originality requirements, thresholds, exclusions and procedures. See [the verified reward memo](reports/reward/reward_verification.md) and its source register before building a business model around rewards.

Public cases and government-wide estimates are calibration material, not new discoveries or a recoverable pot of money. Publishing novel named theories in this public repository could affect potential claim procedures and originality; restricted evidence and case-specific legal review need a separate workspace. No tips, claims, messages to targets or external reports have been submitted.

## What is included

- **27 sector scopes**: military systems/spares/logistics; Medicare/DME/home health/hospice; pharmaceuticals/labs/PBMs; Medicaid/autism; VA; construction/infrastructure; IT/cyber/services; set-asides; foreign aid; research grants; education; PPP/EIDL; unemployment; disasters; housing; agriculture/food; childcare/social services; energy/environment; tax; customs/trade; finance; pensions/benefits; detention; tribal/local funding.
- The **foundation's 148 source records**, covering 145 deduplicated research URLs plus three separately captured award-query responses, are supplemented by the catheter investigation. Sources distinguish official records, issuer disclosures, reporting and retrieval depth. Most consulted web sources have not been byte-archived; captured API extracts have actual checksums with explicit scope.
- The **foundation's 28 published enforcement/audit benchmarks**, supplemented by dated case events in the investigation, preserve source-stated legal status. Charges, pleas, sentences, settlements, audit findings and administrative actions stay distinct. Later docket developments require rechecking.
- **65 captured public award rows**: 25 medical-supplies awards, 20 defence-parts awards and 20 NIH grant awards. Each is a largest-cumulative-amount first-page sample; every response reports more pages. These are neither complete cohorts nor fraud rankings. The NIH filter is a research-focused proxy, not a verified research-only population.
- **32 specialist/reviewer contracts**, mapping every sector to an assigned role, plus **24 dependency-ordered foundation work packages**. Six specialist workers executed the catheter investigation in this session; the specifications do not constitute deployed autonomous services.
- A canonical JSON evidence graph, one Obsidian note per node, CSV graph/financial views, local SQLite search, validation and an atomic leased task queue. Exact current counts are in [coverage-summary.json](data/coverage-summary.json).

## Open the evidence bank in Obsidian

Open `research/us-integrity/generated/obsidian` as a vault and begin at [00-START-HERE.md](generated/obsidian/00-START-HERE.md). No community plugin is required. The built-in graph shows source, entity, award, case, hypothesis, agent and task links. Each note has a stable ID, status, sources and relationships. The vault is a generated view: edit the reviewed registries or canonical assembly inputs and rebuild it, rather than editing generated findings directly.

An Obsidian-ready folder is included in GitHub; it has not been installed into a vault on your computer. Never add confidential tips, patient information, bank records or novel named allegations to this public folder.

## Research reading order

1. [System architecture](architecture/SYSTEM-DESIGN.md), [operations/security](architecture/OPERATIONS-AND-SECURITY.md), and [build roadmap](architecture/BUILD-ROADMAP.md).
2. [Healthcare](reports/healthcare/healthcare_research.md), [procurement](reports/procurement/research.md), and [other sectors](reports/cross_sector/PLAYBOOK.md). These contain buyer/payer paths, datasets, join keys, hypotheses, benign alternatives and missing evidence.
3. [Ownership, sales and trading](OWNERSHIP-AND-COMMERCE.md), with dated public corporate examples. Registered agents are not assumed to own companies, and securities holdings are not automatically control relationships.
4. [Agent registry](agents/AGENT-REGISTRY.md), [full sector coverage mapping](agents/coverage-map.json), and [collaboration protocol](architecture/MULTI-AGENT-PROTOCOL.md).
5. [Validation record](VALIDATION.md) and [connector capture instructions](connectors/README.md).

## Run the local foundation

Python 3.11+; standard library only. From repository root:

```bash
python research/us-integrity/tools/assemble.py
python research/us-integrity/engine/integrity.py validate research/us-integrity/data/graph.json --public
python research/us-integrity/engine/integrity.py build research/us-integrity/data/graph.json --output /tmp/us-integrity-work --tasks research/us-integrity/architecture/tasks.json
python research/us-integrity/engine/integrity.py search --db /tmp/us-integrity-work/graph.sqlite "medical"
python -m unittest discover -s research/us-integrity/engine -p 'test_*.py'
python -m unittest discover -s research/us-integrity/connectors -p 'test_*.py'
python -m unittest discover -s research/us-integrity/tools -p 'test_*.py'
```

Reassembly makes no remote requests. New acquisition is explicit, finite and documented. Award captures enter through `data/approved-snapshots.json`. Reviewed investigation extensions enter through `data/approved-investigations.json`, with extension/input digests, collision rejection and the same provenance/public-export validator. An unlisted directory never enters automatically. Keep dated evidence instead of silently replacing earlier observations.

## Work with the other ChatGPT session

Give it [SECOND-MODEL-HANDOFF.md](agents/SECOND-MODEL-HANDOFF.md), this branch, and a specific work package. A coordinator should assign separate tasks when sessions cannot share one live task database. Two copies of SQLite do not share locks. A shared transactional task service is a later build, and this work does not establish a live connection to a separate chat or select its model.

## Next discriminating evidence

The [catheter follow-up queue](investigations/dme-catheter-2026-10-29/FOLLOW-UP-QUEUE.json) prioritizes payer-specific cash reconciliation, the two unnamed intercompany transactions in the public complaint, historical enrollment scope and implementation of suspension notifications. Each task defines the evidence needed and an outcome that would close or downgrade the lead. Other sector pilots remain in the foundation queue. Expand only after reproducible tests, including valid findings of no fraud.

Tracing every buyer, invoice, supplier, owner and bank transfer nationwide is not possible from current public sources. Unknown relationships remain explicit. This repository does not claim comprehensive buyer coverage, private financial access, a completed forensic audit, reward eligibility, or agents running in the background.
