---
id: "workstream-HC-05"
type: "workstream"
title: "Clinical laboratories, urine drug tests and genetic testing"
status: "planned"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Clinical laboratories, urine drug tests and genetic testing

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "agent": "Laboratory coding and CLIA auditor: require precise panel/code/date evidence and separate admitted facts from settlement allegations.",
  "blind_spots": [
    "Aggregate NPI/code totals cannot show same-patient same-day testing combinations.",
    "CLIA certificate quality status is not Medicare billing approval or fraud determination.",
    "Medical necessity and intent require additional records."
  ],
  "buyer_vs_payee": "An ordering physician is not automatically an owner or procurement buyer; an advertised test brand does not uniquely identify the billing laboratory.",
  "funds_path": [
    "CMS/MAC or Medicaid/MCO",
    "billing laboratory",
    "ordering practitioner and potential marketer/MSO",
    "reference lab or testing subcontractor"
  ],
  "hypotheses": [
    {
      "alternatives": [
        "specialist addiction/toxicology practice",
        "legitimate confirmatory testing",
        "reference-lab referrals"
      ],
      "needed": "Coverage policy, ordering data, actual test panel, medical record and patient-specific indication under lawful access.",
      "signal": "High same-family test intensity or spending concentration"
    },
    {
      "alternatives": [
        "bona fide investment returns",
        "actual services under compliant arrangement"
      ],
      "needed": "Contract/distribution/referral evidence and legal review; public association alone cannot establish a kickback.",
      "signal": "Ownership distributions correlated with referrals"
    }
  ],
  "join_plan": [
    "Resolve NPI and CLIA certificate separately, using explicit crosswalk or corroborated location/legal name and certificate dates.",
    "Compare CPT/HCPCS families with site-of-service and year-specific billing rules; preserve modifiers when available.",
    "Record marketers/MSOs only if documented; never convert a co-located company into a financial intermediary."
  ],
  "priority": "high",
  "visibility": "public"
}
```

## Sources

- [[src-HC-S01]]
- [[src-HC-S18]]
- [[src-HC-S19]]
- [[src-HC-S24]]
- [[src-HC-S26]]

## Outgoing relationships

- cites: [[src-HC-S18]] — documented_fact (edge-4b2a06d1ff46ab011009); sources: [[src-HC-S18]]
- has_research_hypothesis: [[workstream-HC-05-hyp-2]] — planned (edge-7c9b46c03e7b019ab723); sources: 
- cites: [[src-HC-S26]] — documented_fact (edge-7d3987fbefef9a852748); sources: [[src-HC-S26]]
- cites: [[src-HC-S19]] — documented_fact (edge-a5461d58c1f18d5bdd63); sources: [[src-HC-S19]]
- cites: [[src-HC-S01]] — documented_fact (edge-ad5ea246a9346454e8c6); sources: [[src-HC-S01]]
- has_research_hypothesis: [[workstream-HC-05-hyp-1]] — planned (edge-b8236a62ddecb24a9b9e); sources: 
- cites: [[src-HC-S24]] — documented_fact (edge-ea229b87c609d412ea5e); sources: [[src-HC-S24]]

## Backlinks

None recorded.
