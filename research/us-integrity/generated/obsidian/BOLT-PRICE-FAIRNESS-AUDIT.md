---
id: "BOLT-PRICE-FAIRNESS-AUDIT"
type: "audit_framework"
title: "Price fairness and buyer independence require separate evidence beyond document arithmetic"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Price fairness and buyer independence require separate evidence beyond document arithmetic

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "actual_cohort_buyer_independence": "unknown",
  "actual_cohort_price_fairness": "unknown",
  "benchmark_relative_difference": null,
  "buyer_benefit": null,
  "framework_origin": "Research design informed by the cited official methodology and known-case mechanisms",
  "fraud_finding": false,
  "normalization_rules": [
    "Require documented pack and price units. Dividing box price by a claimed per-piece display can check arithmetic but cannot prove pack count.",
    "Keep item price and government-paid freight distinct, then compare like landed-cost bases. FOB origin does not mean free shipping.",
    "Use quantities actually ordered/invoiced/paid for the chosen basis; an annual estimate, ceiling or cancelled balance is not volume purchased.",
    "Require actual revision/grade/thread/finish/traceability equivalence or a documented technical adjustment; do not use ASME B18.24 alone as a complete product specification.",
    "Preserve the source's monetary precision and round only at declared reporting stages; do not select a tier whose minimum order exceeds feasible demand without accounting for all packs purchased.",
    "Do not infer dated availability from today's stock, or a historical comparable from a current page. Preserve quote validity and delivery capacity.",
    "Maintain business identity and beneficial ownership as different relations. A current CAGE/UEI match, self-parent record, shared upstream manufacturer or punctuation alias does not prove historical ownership or bid coordination.",
    "Do not merge awards, invoice lines and cash disbursements; use unique parent/order/modification/CLIN keys and deduplicate cumulative obligations."
  ],
  "scope": {
    "nsn": "5306016864912",
    "office": "DLA purchasing office identified by action documents; individual decision roles not established",
    "period": "Initial cohort: seven historical actions plus current parent and child; expanding requires a declared universe and coverage"
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-PC-MECH-S01]]
- [[BOLT-PC-MECH-S02]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]

## Outgoing relationships

- requires_evidence: [[BOLT-PC-R01]] — planned (BOLT-E-06985405da53612055c7); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- defines_finding_class: [[BOLT-PRICE-CLASS-unexplained_premium]] — planned (BOLT-E-165d588fcb7e3dfbf7cd); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- separately_tests: [[BOLT-BUYER-INDEPENDENCE-UNKNOWN]] — documented_fact (BOLT-E-18414b5cbfc43f020d9e); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T06]] — planned (BOLT-E-1e304448fa02bd85863c); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R04]] — planned (BOLT-E-1ee8799e8fc504b048ec); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T04]] — planned (BOLT-E-237740da95bd21818d4d); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T02]] — planned (BOLT-E-3e4fa97e8d2bec26d7ba); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- defines_finding_class: [[BOLT-PRICE-CLASS-poor_purchase]] — planned (BOLT-E-4ca511e8b319da23e10d); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R06]] — planned (BOLT-E-4f03d8dc2563136e3119); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R07]] — planned (BOLT-E-54c76220271c411a30aa); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R05]] — planned (BOLT-E-5500569b8a17e749f097); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T01]] — planned (BOLT-E-65b102723c7e3c6314f0); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T07]] — planned (BOLT-E-6f06306703374b76a7f5); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T09]] — planned (BOLT-E-725451f0dc468d5bbe98); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- defines_finding_class: [[BOLT-PRICE-CLASS-corroborated_corruption_indicator]] — planned (BOLT-E-77ccb09c9d85db197520); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R08]] — planned (BOLT-E-7a08a4aeca75ac6cbea8); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T05]] — planned (BOLT-E-80132cf00a7a2d5058ec); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R02]] — planned (BOLT-E-99adcfe12c41724d964b); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- requires_evidence: [[BOLT-PC-R03]] — planned (BOLT-E-9d4c8af94b8bd8f09cc0); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- separately_tests: [[BOLT-PRICE-FAIRNESS-UNKNOWN]] — documented_fact (BOLT-E-b135dabcc69bbf613a69); sources: [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- defines_finding_class: [[BOLT-PRICE-CLASS-established_kickback_or_bribery]] — planned (BOLT-E-c2cdb395953551284ed9); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- tests_hypothesis: [[BOLT-REPEATED-PREMIUM-HYPOTHESIS]] — planned (BOLT-E-c8483b1bfe430b0c9fb6); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- calibrates_control_questions: [[BOLT-PC-MECH-C01]] — documented_fact (BOLT-E-c84b2389d272a5451620); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]]
- specifies_test: [[BOLT-PC-T03]] — planned (BOLT-E-f10328458bf320359c0f); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- specifies_test: [[BOLT-PC-T08]] — planned (BOLT-E-f1b0fc0e17b4a865f619); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- defines_finding_class: [[BOLT-PRICE-CLASS-ordinary_margin]] — planned (BOLT-E-f30a86e647c15b0c2d3f); sources: [[BOLT-PC-MECH-S01]], [[BOLT-PC-MECH-S02]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]], [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-04df79fdf0aad91c0d39); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-12220d1cd79cbec37339); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-39a5057ffac97dd29e91); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-98736b5e1b9c4b2a1610); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-c10cef1837a65a6a6290); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-d4cf3ade9579ed6f036b); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-dc8a9cb142d66ba235bc); sources: [[BOLT-CUR-S02]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-4d0af4a2394c4a500d84)
- [[BOLT-PCR-F11]]: assesses_evidence — documented_fact (BOLT-E-77162b38c175e451f2fe)
