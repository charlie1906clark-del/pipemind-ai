---
id: "DME-SRC-PUF-2023-A4353"
type: "source"
title: "CMS supplier detail: 2023 A4353"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2023 A4353

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "16b75bd7d611dbb3c067ad2dde56d27027ad179bd27b758323d44c584d069d1e",
  "dataset_uuid": "44235fd3-6cf9-487f-928d-12998cd84071",
  "hash_scope": "Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response",
  "period": "2023",
  "request_manifest": "investigations/dme-catheter-2026-10-29/data-audit/acquisition_manifest.json",
  "selected_columns": [
    "Suplr_NPI",
    "Suplr_Prvdr_Ent_Cd",
    "Suplr_Prvdr_State_Abrvtn",
    "Suplr_Prvdr_Spclty_Cd",
    "Suplr_Prvdr_Spclty_Desc",
    "HCPCS_Cd",
    "HCPCS_Desc",
    "Suplr_Rentl_Ind",
    "Tot_Suplr_Benes",
    "Tot_Suplr_Clms",
    "Tot_Suplr_Srvcs",
    "Avg_Suplr_Sbmtd_Chrg",
    "Avg_Suplr_Mdcr_Alowd_Amt",
    "Avg_Suplr_Mdcr_Pymt_Amt",
    "Avg_Suplr_Mdcr_Stdzd_Amt"
  ],
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2023_A4353.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/44235fd3-6cf9-487f-928d-12998cd84071/data?filter%5BHCPCS_Cd%5D=A4353&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-NATIONAL-CHECK-2023-A4353]]: cites — documented_fact (edge-03b95e0c6530469458f4)
- [[DME-FALS-20]]: cites — documented_fact (edge-0ff2a81834174ba5424f)
- [[DME-COHORT-2023-A4353]]: cites — documented_fact (edge-4e6bb87411a1d4cee342)
- [[DME-REVOCATION-CROSSCHECK-2023-A4353]]: cites — documented_fact (edge-4ebdab1c52845de55434)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-507fcdd625ff25b4c70a)
- [[DME-INV-20261029]]: cites — documented_fact (edge-58976ff8141d6821cdef)
- [[DME-COHORT-2023-A4353-money-allowed]]: cites — documented_fact (edge-59123ca19eae89fac56c)
- [[DME-CHANGE-2023-2024-A4353]]: cites — documented_fact (edge-6246c8285f2931d7cd60)
- [[DME-COHORT-2023-A4353-money-puf_payment]]: cites — documented_fact (edge-6dc0fb12bf520e05a78b)
- [[DME-CHANGE-2022-2023-A4353]]: cites — documented_fact (edge-78fb6ade710408253b13)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-79786b8199877b9b9186)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-94c29a072e89479acc4c)
- [[DME-COHORT-2023-A4353-money-submitted]]: cites — documented_fact (edge-a1508e260068bd5283e0)
- [[DME-COHORT-2023-A4353-money-standardized_payment]]: cites — documented_fact (edge-a261e5ec7b0d65554577)
- [[DME-ENTRY-CONTROL-2022-2023]]: cites — documented_fact (edge-ae10f9c392aaa4c73107)
- [[DME-REVOCATION-CROSSCHECK-2023-ALL_THREE_CODES]]: cites — documented_fact (edge-b84ed8f0cf36bef5af2d)
- [[DME-ENTRY-CONTROL-2023-2024]]: cites — documented_fact (edge-b936fd2c39f24dd816ed)
- [[DME-FALS-18]]: cites — documented_fact (edge-cc7d104b84bc20e65b47)
- [[DME-FALS-17]]: cites — documented_fact (edge-f46b2006ab3545f82a35)
