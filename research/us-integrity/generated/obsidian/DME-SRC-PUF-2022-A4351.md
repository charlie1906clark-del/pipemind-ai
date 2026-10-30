---
id: "DME-SRC-PUF-2022-A4351"
type: "source"
title: "CMS supplier detail: 2022 A4351"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2022 A4351

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "1efd4c53de117089f7f47ec43ead51e272634b5810223c78effb516d56ea0860",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2022_A4351.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/dad703df-2e52-4ac6-a26f-51ecbf463d77/data?filter%5BHCPCS_Cd%5D=A4351&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-COHORT-2022-A4351-money-standardized_payment]]: cites — documented_fact (edge-13e1ca9f045efa1103ef)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-214e715486c0fbab5c4a)
- [[DME-CHANGE-2022-2023-A4351]]: cites — documented_fact (edge-28e131bb99e8340c2ea6)
- [[DME-NATIONAL-CHECK-2022-A4351]]: cites — documented_fact (edge-3e6994c9da10b76d34e7)
- [[DME-COHORT-2022-A4351-money-submitted]]: cites — documented_fact (edge-4044e97760f6bedcbdff)
- [[DME-REVOCATION-CROSSCHECK-2022-ALL_THREE_CODES]]: cites — documented_fact (edge-41fe9797b1f5f60ac59c)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-64343aeebf64c53b2b47)
- [[DME-FALS-17]]: cites — documented_fact (edge-69041bb0e3c94aa22cf7)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-7b1d04f0670d62bfa9c7)
- [[DME-INV-20261029]]: cites — documented_fact (edge-8e2d0e0fa40622fe83bb)
- [[DME-COHORT-2022-A4351-money-allowed]]: cites — documented_fact (edge-a8bab3e669419ca43f5f)
- [[DME-REVOCATION-CROSSCHECK-2022-A4351]]: cites — documented_fact (edge-b6330071da12c79bede8)
- [[DME-FALS-20]]: cites — documented_fact (edge-ba2630cd8c3589c46a91)
- [[DME-ENTRY-CONTROL-2022-2023]]: cites — documented_fact (edge-e5510d6500d5d5797c5a)
- [[DME-COHORT-2022-A4351-money-puf_payment]]: cites — documented_fact (edge-e5fc8cae7c6eba1d6d8c)
- [[DME-COHORT-2022-A4351]]: cites — documented_fact (edge-ee3ef3765380f96bac60)
- [[DME-FALS-18]]: cites — documented_fact (edge-fddcac9dc4562b53511d)
