---
id: "BOLT-MARKET-COMPARABILITY-REQUIREMENTS"
type: "audit_gate_set"
title: "Market comparisons require item, quantity and accepted supply-term reconciliation"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Market comparisons require item, quantity and accepted supply-term reconciliation

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_scope": "Requirements for this research workflow; legal applicability must be checked separately",
  "required_gates": [
    "Official exact NSN-to-characteristics and accepted reference-part relationship",
    "Same dimensions, thread series/class/hand, grade, finish/thickness and head form",
    "Same country-of-origin restrictions and authorized supply chain where applicable",
    "Unit/pack/tier and order quantity reconciliation",
    "Item-specific stock, delivery date, quote validity and currency",
    "Freight allocation and taxes",
    "QUP001 packaging, bare marking, sampling, inspection, testing/certificates and traceability requirements",
    "Comparable date, contract terms and documented additional services/cost adjustments where material; seller margin itself is not a mandatory input to price analysis.",
    "Actual invoice, acceptance, payment and refunds/credits before loss quantification"
  ],
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-MKT-SRC-COX]]
- [[BOLT-MKT-SRC-FSS]]
- [[BOLT-MKT-SRC-FSS-FAQ]]
- [[BOLT-MKT-SRC-FSS-FINISH]]
- [[BOLT-MKT-SRC-FSS-STYLE]]
- [[BOLT-MKT-SRC-FSS-TERMS]]
- [[BOLT-MKT-SRC-MF]]
- [[BOLT-MKT-SRC-MF-SHIPPING]]
- [[BOLT-MKT-SRC-MF-TERMS]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]

## Outgoing relationships

- cites: [[BOLT-MKT-SRC-COX]] — documented_fact (edge-0019222f77134c172e10); sources: [[BOLT-MKT-SRC-COX]]
- cites: [[BOLT-MKT-SRC-MF-TERMS]] — documented_fact (edge-2c2a47a77a972127c61a); sources: [[BOLT-MKT-SRC-MF-TERMS]]
- cites: [[BOLT-MKT-SRC-MF-SHIPPING]] — documented_fact (edge-325915fbc4a0b6d7c524); sources: [[BOLT-MKT-SRC-MF-SHIPPING]]
- cites: [[BOLT-MKT-SRC-FSS-TERMS]] — documented_fact (edge-54c03d19855739e8308f); sources: [[BOLT-MKT-SRC-FSS-TERMS]]
- cites: [[BOLT-MKT-SRC-FSS-STYLE]] — documented_fact (edge-6d8594362598f14dba07); sources: [[BOLT-MKT-SRC-FSS-STYLE]]
- cites: [[BOLT-MKT-SRC-MF]] — documented_fact (edge-9eba261f9d1ebd514743); sources: [[BOLT-MKT-SRC-MF]]
- cites: [[BOLT-MKT-SRC-FSS-FAQ]] — documented_fact (edge-aaaadbfa055477141c9f); sources: [[BOLT-MKT-SRC-FSS-FAQ]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-b7c8310ecf3e595099f9); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-MKT-SRC-FSS-FINISH]] — documented_fact (edge-c480c9f8e1ad2dcac8fb); sources: [[BOLT-MKT-SRC-FSS-FINISH]]
- cites: [[BOLT-MKT-SRC-FSS]] — documented_fact (edge-caf76f926bfb334af2c5); sources: [[BOLT-MKT-SRC-FSS]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-ed9d3c38ffd43b48348a); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-f7090e5d45f56214c86b); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-fa70b2f0cbaf3968e3df); sources: [[BOLT-PC-METHOD-S01]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — planned (BOLT-E-6994a316f07e4897b8c7)
- [[BOLT-PCR-F12]]: assesses_evidence — documented_fact (BOLT-E-dbea16ee160ddaf02265)
