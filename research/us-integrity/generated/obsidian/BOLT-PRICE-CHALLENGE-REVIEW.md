---
id: "BOLT-PRICE-CHALLENGE-REVIEW"
type: "review_record"
title: "Independent market and buyer-independence review leaves fairness and benefit questions open"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Independent market and buyer-independence review leaves fairness and benefit questions open

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "conclusions": {
    "buyer_benefit": "unresolved_no_cohort_specific_evidence",
    "buyer_independence": "unresolved",
    "document_arithmetic": "verified_with_scope",
    "kickback_amount": null,
    "loss_amount": null,
    "market_fairness": "unresolved",
    "new_fraud_finding_established": false,
    "paid_amount": null,
    "premium_amount": null,
    "qualified_comparator_count": 0
  },
  "next_discriminating_records": [
    "Unrestricted primary NSN characteristics and relevant revision/reference qualifiers.",
    "Dated accepted equivalent offer at feasible quantity with freight, certificates and delivery.",
    "Actual quote abstract, evaluation rationale and price-reasonableness record.",
    "Dated role-to-decision evidence and, separately, actual evidence of improper benefit if it exists in lawfully available records."
  ],
  "prior_document_review_unchanged": true,
  "review_receipt_path": "investigations/dla-bolt-trace-2026-10-30/price-challenge/market_review.json",
  "reviewer_task": "bolt_comparison_reviewer",
  "verification": {
    "artifact_limit": "Digests of selected factual extractions prove retained-byte integrity, not authenticity of original website bytes. Full current PDFs remain unarchived in the public repository.",
    "independent_reconstruction": {
      "checks": [
        "Three derivative market captures match manifest byte counts and SHA256 hashes and matrix fields.",
        "All three FSS displayed unit prices agree with independent carton division to displayed precision; normalized values agree within 1e-15.",
        "Fresh Cox row confirms test-site/stock exclusion.",
        "Fresh MF redirected page confirms displayed prices, seven boxes and no explicit pack count; terms confirm acceptance condition.",
        "Uniform fixture independently reconstructed B=200000, A=224000, E=24000, markup 12 percent.",
        "Unequal-weight fixture independently reconstructed 20/1000=2 percent.",
        "Annual example independently reconstructed exact fractions 2500000/3, 2800000/3 and 75/7 percent.",
        "Actual DLA output has zero eligible lines, no aggregates and null comparison amount.",
        "Prior review.json SHA256 remains aa7274b257e7d01a4bdf6cfca16e6e556477ec8fb2b772e1f92a0f1a65109e44."
      ],
      "method": "Manual fresh-page checks and separate Python Fraction/Decimal arithmetic, without using the producer's formulas as the expected answer."
    },
    "producer_unit_tests": {
      "command": "python -m unittest discover -s . -p 'test_*.py' -v",
      "cwd": "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-controls",
      "passed": 12,
      "rerun_after_final_precision_update": true
    },
    "public_acquisition_budget": {
      "document_attempts": 12,
      "includes_delegated_known_case_work": true,
      "queries": 5,
      "successful_document_reads": 11
    },
    "saved_cli_output_replays": {
      "files": [
        "uniform-12-percent",
        "weighted-mix",
        "dla-current-no-qualified-benchmark",
        "annual-12-percent-illustration"
      ],
      "matched": 4
    }
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-MKT-SRC-COX]]
- [[BOLT-MKT-SRC-FSS]]
- [[BOLT-MKT-SRC-MF]]
- [[BOLT-PC-MECH-S01]]
- [[BOLT-PC-MECH-S02]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]
- [[BOLT-PC-MKT-S01]]
- [[BOLT-PC-MKT-S02]]
- [[BOLT-PC-MKT-S03]]
- [[BOLT-PC-MKT-S04]]
- [[BOLT-SRC-award-SPE4A625PK654]]
- [[BOLT-SRC-award-SPE4A625V208Q]]
- [[BOLT-SRC-award-SPE4A625V252D]]
- [[BOLT-SRC-award-SPE4A625V346U]]
- [[BOLT-SRC-award-SPE4A625V4508]]
- [[BOLT-SRC-award-SPE4A626P5931]]
- [[BOLT-SRC-award-SPE4A626V138W]]

## Outgoing relationships

- records_review_assessment: [[BOLT-PCR-F05]] — documented_fact (BOLT-E-0587a91dda22081c7818); sources: [[BOLT-CUR-S01]], [[BOLT-SPEC-R01]], [[BOLT-SPEC-R02]]
- records_review_assessment: [[BOLT-PCR-F04]] — documented_fact (BOLT-E-2073b6a4d551683bc2ce); sources: [[BOLT-CUR-S02]], [[BOLT-PC-MKT-S03]], [[BOLT-PC-MKT-S04]]
- records_review_assessment: [[BOLT-PCR-F08]] — documented_fact (BOLT-E-33a0121e8aa691e9ed17); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- records_review_assessment: [[BOLT-PCR-F12]] — documented_fact (BOLT-E-4e113e164a00f8840cc4); sources: [[BOLT-PC-METHOD-S02]]
- records_review_assessment: [[BOLT-PCR-F03]] — documented_fact (BOLT-E-55333801226d8d90e532); sources: [[BOLT-CUR-S02]], [[BOLT-MKT-SRC-FSS-FAQ]], [[BOLT-MKT-SRC-FSS-TERMS]], [[BOLT-PC-MKT-S02]]
- records_review_assessment: [[BOLT-PCR-F02]] — documented_fact (BOLT-E-5572325e418882c25f26); sources: [[BOLT-CUR-S02]], [[BOLT-MKT-SRC-COX]], [[BOLT-PC-MKT-S01]]
- records_review_assessment: [[BOLT-PCR-F06]] — documented_fact (BOLT-E-63bedbcfcd1ab8ddf670); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-MKT-SRC-COX]], [[BOLT-MKT-SRC-FSS]], [[BOLT-MKT-SRC-MF]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- records_review_assessment: [[BOLT-PCR-F10]] — documented_fact (BOLT-E-653e1821ca71099da8e8); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]]
- records_review_assessment: [[BOLT-PCR-F09]] — documented_fact (BOLT-E-671986103d1ba49d8e57); sources: [[BOLT-PC-METHOD-S02]]
- records_review_assessment: [[BOLT-PCR-F07]] — documented_fact (BOLT-E-7f594bb5fc0ed45f80ea); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S03]], [[BOLT-SRC-award-SPE4A625PK654]], [[BOLT-SRC-award-SPE4A625V208Q]], [[BOLT-SRC-award-SPE4A625V252D]], [[BOLT-SRC-award-SPE4A625V346U]], [[BOLT-SRC-award-SPE4A625V4508]], [[BOLT-SRC-award-SPE4A626P5931]], [[BOLT-SRC-award-SPE4A626V138W]]
- records_review_assessment: [[BOLT-PCR-F01]] — documented_fact (BOLT-E-80b88a7a13f756e57d98); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- records_review_assessment: [[BOLT-PCR-F11]] — documented_fact (BOLT-E-a3cdf619e4d701b76f0a); sources: [[BOLT-MKT-SRC-COX]], [[BOLT-MKT-SRC-FSS]], [[BOLT-MKT-SRC-MF]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-SRC-award-SPE4A625V252D]] — documented_fact (edge-16a8868879766bbe432f); sources: [[BOLT-SRC-award-SPE4A625V252D]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-1940c975d5492db71df6); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-MKT-S01]] — documented_fact (edge-28709f7342773957cbf6); sources: [[BOLT-PC-MKT-S01]]
- cites: [[BOLT-SRC-award-SPE4A626V138W]] — documented_fact (edge-42711c3e21426e2c8c26); sources: [[BOLT-SRC-award-SPE4A626V138W]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-43c7c939a2ffe37a8176); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-SRC-award-SPE4A625V4508]] — documented_fact (edge-79bbb749ed6beff1adb7); sources: [[BOLT-SRC-award-SPE4A625V4508]]
- cites: [[BOLT-PC-MKT-S04]] — documented_fact (edge-7f34bc24d97d0d146650); sources: [[BOLT-PC-MKT-S04]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-847bc42ae7ec3b4a6b78); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-84d6bd0286af04c893f1); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-SRC-award-SPE4A625V346U]] — documented_fact (edge-8be101c313f77ba525ea); sources: [[BOLT-SRC-award-SPE4A625V346U]]
- cites: [[BOLT-SRC-award-SPE4A625V208Q]] — documented_fact (edge-908e73cd3dec76111566); sources: [[BOLT-SRC-award-SPE4A625V208Q]]
- cites: [[BOLT-SRC-award-SPE4A626P5931]] — documented_fact (edge-9966be58dd3c599bbb08); sources: [[BOLT-SRC-award-SPE4A626P5931]]
- cites: [[BOLT-MKT-SRC-COX]] — documented_fact (edge-9e5c54fe33d804702755); sources: [[BOLT-MKT-SRC-COX]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-bf977e9ab96567415489); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-SRC-award-SPE4A625PK654]] — documented_fact (edge-cbf2fdc22e45be3276e2); sources: [[BOLT-SRC-award-SPE4A625PK654]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-d1a079654e4915ec6a18); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MKT-S02]] — documented_fact (edge-e53fea17d6866f725d73); sources: [[BOLT-PC-MKT-S02]]
- cites: [[BOLT-PC-MKT-S03]] — documented_fact (edge-eb1c47ff5f8a3725d8c2); sources: [[BOLT-PC-MKT-S03]]
- cites: [[BOLT-MKT-SRC-FSS]] — documented_fact (edge-ef98923b1f4d36555b32); sources: [[BOLT-MKT-SRC-FSS]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-f77e0e11190bbf0402f5); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-MKT-SRC-MF]] — documented_fact (edge-f928b7e269f8aa0d0b6c); sources: [[BOLT-MKT-SRC-MF]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-493b0b562126b2eaa081)
