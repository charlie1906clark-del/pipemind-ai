---
id: "DME-SRC-PUF-2024-A4352"
type: "source"
title: "CMS supplier detail: 2024 A4352"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2024 A4352

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "daaff223e13d0a499a89dbce13fa9c971d5985b0c9df567b91f8cd2331c22625",
  "dataset_uuid": "1746a83e-bb65-4300-8e02-21edbab77c6b",
  "hash_scope": "Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response",
  "period": "2024",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2024_A4352.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data?filter%5BHCPCS_Cd%5D=A4352&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-0720289eef31793b4628)
- [[DME-FALS-17]]: cites — documented_fact (edge-0c16e8c2038e9e045e71)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-272dc479e1d3bda1eefc)
- [[DME-REVOCATION-CROSSCHECK-2024-ALL_THREE_CODES]]: cites — documented_fact (edge-2f3745bba6d6c4e490f5)
- [[DME-INV-20261029]]: cites — documented_fact (edge-4b8a9ab54670d8e51e6f)
- [[DME-COHORT-2024-A4352]]: cites — documented_fact (edge-5d2821f0686787b691c3)
- [[DME-NATIONAL-CHECK-2024-A4352]]: cites — documented_fact (edge-60df2bdeb566a7e06b92)
- [[DME-COHORT-2024-A4352-money-puf_payment]]: cites — documented_fact (edge-770bee77f714cd887744)
- [[DME-COHORT-2024-A4352-money-allowed]]: cites — documented_fact (edge-7d461dcc66cf6151a8c2)
- [[DME-CHANGE-2023-2024-A4352]]: cites — documented_fact (edge-90de3222f3f9d7cc32da)
- [[DME-FALS-18]]: cites — documented_fact (edge-9929c6136ca6e39bd70b)
- [[DME-COHORT-2024-A4352-money-submitted]]: cites — documented_fact (edge-ab7fe356b4d942871a57)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-b143553db631c4477df1)
- [[DME-COHORT-2024-A4352-money-standardized_payment]]: cites — documented_fact (edge-be9e75a6aa1ccbc921a8)
- [[DME-REVOCATION-CROSSCHECK-2024-A4352]]: cites — documented_fact (edge-cfe0c4d8cee3b7d5653b)
- [[DME-FALS-20]]: cites — documented_fact (edge-d9e6686c4c23e2034d23)
