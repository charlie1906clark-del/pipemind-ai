---
id: "DME-SRC-PUF-2022-A4353"
type: "source"
title: "CMS supplier detail: 2022 A4353"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2022 A4353

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "dd7d5cedfa9d160dde10ac5bfc999af01c540cb06e9e5d9d15c79a3b3afd44b1",
  "dataset_uuid": "dad703df-2e52-4ac6-a26f-51ecbf463d77",
  "hash_scope": "Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response",
  "period": "2022",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2022_A4353.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/dad703df-2e52-4ac6-a26f-51ecbf463d77/data?filter%5BHCPCS_Cd%5D=A4353&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-INV-20261029]]: cites — documented_fact (edge-0ed81f5d48b9e4b8dc94)
- [[DME-COHORT-2022-A4353-money-puf_payment]]: cites — documented_fact (edge-17e7418db9b736ed25cd)
- [[DME-ENTRY-CONTROL-2022-2023]]: cites — documented_fact (edge-18d19fa6a252bc74cd81)
- [[DME-COHORT-2022-A4353-money-standardized_payment]]: cites — documented_fact (edge-27d64915ef4b14cdd95d)
- [[DME-COHORT-2022-A4353-money-submitted]]: cites — documented_fact (edge-29df03576ed98c646584)
- [[DME-FALS-18]]: cites — documented_fact (edge-2c98ef96aa03b05ff5d7)
- [[DME-COHORT-2022-A4353]]: cites — documented_fact (edge-4b907d1f3ed3d8d52ca3)
- [[DME-REVOCATION-CROSSCHECK-2022-A4353]]: cites — documented_fact (edge-55e6ad12bbe403447bed)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-5ae604c949d8bd0d3929)
- [[DME-COHORT-2022-A4353-money-allowed]]: cites — documented_fact (edge-672a33e8d275d8292a62)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-78e3fb37a87510109425)
- [[DME-FALS-20]]: cites — documented_fact (edge-7ed091eef29df9d8d283)
- [[DME-REVOCATION-CROSSCHECK-2022-ALL_THREE_CODES]]: cites — documented_fact (edge-b066335e54cc21197f8f)
- [[DME-FALS-17]]: cites — documented_fact (edge-c866fdc345c68b94dbcc)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-cfe408e13532334c4569)
- [[DME-NATIONAL-CHECK-2022-A4353]]: cites — documented_fact (edge-d3af21232d500fdec81f)
- [[DME-CHANGE-2022-2023-A4353]]: cites — documented_fact (edge-de55c3c8ec9fca433d21)
