# Targeted procurement price investigation

This system turns the concealed-markup question into separate, testable work: establish the exact purchase, qualify an independent price, measure a persistent difference, reconstruct the actual purchasing decision, and investigate a benefit only when relevant public records support that link. A legitimate supplier and correct invoice arithmetic do not resolve those questions.

The current implementation has **14 specialist role contracts, 20 dependency-aware tasks, an executable local durable queue, a bounded attachment tracer and an exploratory repeated-premium screen**. Actual workers acquired a **30-award DLA/VA/HHS pilot** and original DLA line evidence. Eight later sector waves are planned and gated. There is no unattended model service or nationwide ingestion running.

## Start with the actual evidence

The [pilot report](../investigations/federal-price-pilot-2026-10-30/REPORT.md) documents order **SPE4A626PW775**: **2,243 production bolts at $272.99 each**, plus a **$3,500 first-article test**, totaling **$615,816.57 ordered**. The item is NSN **5306004457358**, part **39-8820-501**, a special front-engine-mount item. The test requirement and production quantity are different deliverables. This is neither cash paid nor an independently established reasonable price.

The [party trace](../investigations/federal-price-pilot-2026-10-30/parties/REPORT.md) verifies the dealer's and intended manufacturer's identifiers and preserves a narrow printed professional role. It does not turn a reported parent into a beneficial owner, a recipient into an actual payee, or a contracting officer's name into evidence of improper influence. [Exact-part market research](research-market/REPORT.md) obtained no priced independent offer. The [earlier $0.91 bolt's primary-specification follow-up](../investigations/bolt-spec-followup-2026-10-30/REPORT.md) also remains open; the two NSNs must not be compared merely because both are bolts.

The [real retained-evidence run](runs/README.md) records how completed public acquisitions enter task state and independent review. The public exports retain original source dates and hashes. They explicitly count zero new network requests for local reuse. [Independent review](review/REPORT.md) checks the implementation, source selections, arithmetic and limitations.

## Roles and evidence gates

| Work | Required result |
|---|---|
| Cohort acquisition and transaction tracing | Declared population, original instrument, exact line, link lineage, dates, missing pages and failed routes |
| Specification and offer research | Same part/revision, unit and pack, quantity, date, quality, delivery, testing, warranty and applicable freight terms |
| Repeated-premium analysis | All eligible positive and negative differences, weighted values, distinct purchasing events and disclosed benchmark independence |
| Bids, business identity and professional roles | Actual competing bids/decision evidence; dated exact entity joins; the role supported by the record |
| Benefit and payment reconciliation | Source-supported influence/benefit, if any; orders, invoices, credits, receipt and cash kept distinct |
| Independent challenge, prior disclosure and graph curation | Rival explanations, reproduction, exact remaining record, disclosure status and reviewed facts |
| Coordinator | Finite budgets, exclusive local ownership, immutable inputs/results and explicit reopen rules |

See [architecture](ARCHITECTURE.md), [role contracts](plans/role-contracts.json), [current tasks](plans/current-wave.json), [record contracts](plans/record-contracts.json), [source access map](SOURCE-MAP.md) and [later waves](plans/later-waves.json).

## Running the implementation

Python 3.11 or newer; standard library. Run from the repository root. Keep operational databases outside the public research folder:

```bash
python research/us-integrity/price-agents/runtime/agent_runtime.py --db /tmp/price-tasks.sqlite --repository . init --plan research/us-integrity/price-agents/plans/current-wave.json
python research/us-integrity/price-agents/runtime/agent_runtime.py --db /tmp/price-tasks.sqlite --repository . status
python -m unittest discover -s research/us-integrity/price-agents/runtime -p 'test_*.py'
python -m unittest discover -s research/us-integrity/price-agents/tracing -p 'test_*.py'
python -m unittest discover -s research/us-integrity/price-agents/analysis -p 'test_*.py'
python -m unittest discover -s research/us-integrity/price-agents/review -p 'test_*.py'
```

The [runtime manual](runtime/README.md) documents claims, fenced leases, attempt reservation, evidence appends, review, block/reopen and export. The [tracer manual](tracing/README.md) documents URL admission, exact-identifier relevance, robots and redirect handling, budgets and failure receipts. [Recurrence analysis](analysis/README.md) reruns qualification before exploring repeated premiums. The 12% examples are synthetic; no real recurring 12% premium has been demonstrated. A line-count pattern can coexist with a negative overall price difference.

## Persistence and current operational limits

Persistence means retaining a failed path and resuming when a new record can discriminate between explanations. Tasks have finite attempts, bytes, time, evidence and reopen budgets. A supported ordinary explanation or unresolved result is a successful outcome. An accepted packet is not a qualified price benchmark; the downstream gate still applies.

The standalone tracer's live trial stopped at DNS resolution: **zero confirmed HTTP requests and zero acquired documents**. Other declared API/PDF acquisitions succeeded and are logged separately. The tracer is not yet integrated with the runtime's per-request reservation interface. Consequently this build cannot enforce a single global request budget across every script, browser or model session. Actor names distinguish records but do not authenticate independent people.

SQLite leases coordinate workers using one database. Separate chats or machines do not share those leases. A coordinator must assign disjoint tasks and verify input/result commits. The [Claude supplement](plans/claude-supplemental-assignment.json) assigns bid/decision work adjacent to this pilot; its existence is not a provider dispatch or result. No Claude/Grok API bridge, paid model setup, outbound contact, claim or agency submission was activated.

Only reviewed public business/professional evidence enters the canonical graph and generated Obsidian vault. Original documents containing unnecessary contact information remain outside the public artifacts; selected records retain locator and hash scope. Following links means following transaction-relevant, admitted public sources—not collecting unrelated personal lives or obeying instructions embedded in documents.
