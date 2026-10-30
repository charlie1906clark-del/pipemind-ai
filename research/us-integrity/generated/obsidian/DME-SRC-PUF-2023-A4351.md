---
id: "DME-SRC-PUF-2023-A4351"
type: "source"
title: "CMS supplier detail: 2023 A4351"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2023 A4351

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "09bacddc9472e38934f3c81787b51c9bf515b5fe56d559516efa55626b403063",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2023_A4351.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/44235fd3-6cf9-487f-928d-12998cd84071/data?filter%5BHCPCS_Cd%5D=A4351&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-REVOCATION-CROSSCHECK-2023-ALL_THREE_CODES]]: cites — documented_fact (edge-08a5e9b9e74b072b07b5)
- [[DME-CHANGE-2023-2024-A4351]]: cites — documented_fact (edge-4a9408551d675fc65a75)
- [[DME-FALS-17]]: cites — documented_fact (edge-4d1736ff470cec7d3af2)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-4d2cb13e2cd990ec775b)
- [[DME-ENTRY-CONTROL-2023-2024]]: cites — documented_fact (edge-53a305e874411a6f6960)
- [[DME-COHORT-2023-A4351-money-puf_payment]]: cites — documented_fact (edge-55c4e64c6084000176c7)
- [[DME-COHORT-2023-A4351-money-standardized_payment]]: cites — documented_fact (edge-5c239da17fb453b4433f)
- [[DME-COHORT-2023-A4351-money-allowed]]: cites — documented_fact (edge-7554588bb43e160d6f2e)
- [[DME-CHANGE-2022-2023-A4351]]: cites — documented_fact (edge-7d222ef0142934df8afd)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-838ff1ef6510f95b7417)
- [[DME-COHORT-2023-A4351-money-submitted]]: cites — documented_fact (edge-95b80d2debadcda54e76)
- [[DME-REVOCATION-CROSSCHECK-2023-A4351]]: cites — documented_fact (edge-a1e20d56466fb529a057)
- [[DME-FALS-20]]: cites — documented_fact (edge-a2dd2bb271b222c243bd)
- [[DME-NATIONAL-CHECK-2023-A4351]]: cites — documented_fact (edge-a705b19bf0d577057663)
- [[DME-COHORT-2023-A4351]]: cites — documented_fact (edge-a8201b857e09ca52c38b)
- [[DME-FALS-18]]: cites — documented_fact (edge-b33a856c0f129d7771f6)
- [[DME-INV-20261029]]: cites — documented_fact (edge-bfde2fb3cbf06cd7eada)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-f5bdd66b56d551793248)
