# Exact identity and corporate-role audit

As of 29 October 2026. Two already published enforcement matters were checked. This work establishes identifiers and separates administrative records from allegations; it does not establish a new fraud case or a conviction.

## Resolved identifiers

| Business | Official NPI | Practice state | State corporate record | Outcome |
|---|---|---|---|---|
| ND Medical Solutions LLC | `1790533503` | PA | Unresolved | Exact official NPPES result; official DOJ business and public-role corroboration |
| Centennial Med Supply, LLC | `1609626167` | CO | Colorado `20241008944` | Exact NPPES result plus official state entity record |

The live [ND NPPES API](https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1790533503) returns an organizational DME record, enumerated 7 May 2024, last updated and certified 18 February 2025, with Erekle Gugava reported as authorized official, title President. The live [Centennial NPPES API](https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1609626167) returns an organizational DME record, enumerated 26 March 2024 and updated/certified 20 August 2025, with the reported name **KAHKA BENDELIANI**, title Owner. Both return NPPES status `A`. These are registry assertions; they do not independently prove beneficial ownership or current Medicare billing eligibility.

Centennial is a Colorado business. New Hampshire is the prosecution venue, not the company's practice state. The [official Colorado dataset](https://data.colorado.gov/resource/4ykn-tg5h.json?entityid=20241008944) reports formation on 2 January 2024, current status Delinquent and registered agent Kakha Bendeliani. A registered agent is a different role from an owner. The exact query is saved in `colorado_snapshot.json`.

## An independently reproducible administrative-status result

The [official OIG full LEIE download](https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv) contained 84,093 rows. An exact NPI comparison found Centennial's business row: `1609626167`, CO, exclusion code `1128Aa`, exclusion date **11 July 2026**. The [download page](https://www.oig.hhs.gov/exclusions/leie-database-supplement-downloads/) identifies this as the September 2026 active-exclusion snapshot, posted 9 October. It covers actions through September, not every later event through retrieval day.

No row with ND's exact NPI was found. That result is not clearance: identifiers can be missing and the snapshot has a time boundary. Both original-response hashes and a sanitized matched row are retained in `leie_snapshot.json`; the complete file containing unrelated individual records was not saved.

An active NPI and an OIG exclusion are different administrative predicates. Their coexistence is not a database contradiction. Medicare enrollment/revocation and MA/Part D preclusion are separate checks, handled by the companion enrollment audit; this identity report does not substitute for them.

## Ownership dates and roles remain source-specific

| Record | Assertion | Classification |
|---|---|---|
| ND NPPES | Erekle Gugava, President/authorized official | Reported professional role |
| ND indictment announcement | Gugava purportedly owned ND during February–July 2025 | Criminal allegation |
| ND court-copy paragraph 14 | Alleged sale around 18 February; purported ownership through around 9 July 2025 | Allegation in mirrored filing |
| Centennial Colorado record | Kakha Bendeliani, registered agent | Registry role |
| Centennial NPPES | **KAHKA** Bendeliani, authorized official/title Owner | Reported professional role, spelling retained |
| Bendeliani indictment, page 10 | Purported sole officer/manager from around 20 June 2025 | Criminal allegation |
| Danelia complaint and DOJ announcement | Driving, translation and assistance with financial transactions | Criminal allegation; ownership not established |

The ND date comes from [a court-stamped indictment copy on Universal Hub](https://images.universalhub.com/files/attachments/2026/gugava-indictment.pdf), case `1:26-cr-10243-NMG`, Document 1, filed 3 September 2026, paragraph 14. The [official DOJ announcement](https://www.justice.gov/opa/pr/illegal-alien-georgia-charged-conspiracy-launder-proceeds-13b-health-care-fraud-scheme) corroborates the case and general period. The exact alleged sale date equals NPPES's last-update date, but that alignment does not reveal what changed or prove an ownership transfer. No independently certified docket copy was obtained.

The [Danelia affidavit](https://www.justice.gov/criminal/media/1446881/dl), paragraphs 51–53, describes separate milestones: agreement 15 May 2025, closing 12 June, bank-signatory change 18 June and new accounts 20 June. Paragraph 18 describes the corporate amendment around 20 June. The [Bendeliani indictment](https://www.justice.gov/criminal/media/1446896/dl), page 10, was downloaded and rendered to verify **2025**. Different milestones must not be collapsed into one date. The affidavit's anonymized CC-1 is not de-anonymized from that document alone.

The NPPES spelling KAHKA versus DOJ/Colorado Kakha is retained as a candidate person correspondence. Same company, state and surname support review, but no silent person merge was made. Ultimate beneficial ownership remains unresolved for both companies. The [DOJ announcement](https://www.justice.gov/usao-nh/pr/district-new-hampshire-and-new-england-strike-force-charges-money-laundering-operation) describes nominee arrangements; it does not turn registry roles into proof of the underlying controllers.

## Negative results and access limits

- The initial Colorado exact-name query missed the comma in “Centennial Med Supply, LLC.” A bounded broader search located the record; the final saved query uses the exact state identifier. Other similarly named businesses were not merged or published as leads.
- The affidavit's approximate 1 January 2024 formation date and the state record's exact 2 January date are retained. A one-day approximate-date difference is not evidence of fraud.
- [Pennsylvania's official guidance](https://www.pa.gov/agencies/dos/programs/business/information-services/record-searches) identifies the public business search, but its unauthenticated HTTP request returned 403. ND's state identifier, original filings and prior owner remain unverified. Colorado's detailed filing-history request also returned 403; the official open dataset succeeded. Neither failure establishes absence of registration.
- No primary evidence here identifies every manufacturer, seller, procurement contract, retail customer or ultimate overseas counterparty. No such entity or trade edge was invented. Public reimbursement records should not be treated as an exhaustive procurement ledger.

## Reproduction and graph delivery

`evidence_records.json` contains the task contract, 12 source nodes and eight evidence records. `entities.json` and `relationships.json` contain 12 proposed nodes and 14 source-backed edges in the repository graph shape. Authorized official, registered agent, alleged nominee owner and unresolved beneficial controller are separate relationships. Claims remain allegations; the administrative listing is labeled separately. No complete docket-status search is claimed.

Run `python acquire_identity.py /path/to/new-directory` to repeat the bounded official registry and LEIE checks. It creates a new destination, retains original-byte hashes, and saves only selected business fields. It does not preserve beneficiary information, street addresses, personal contacts or unrelated exclusion rows. Retrieval dates and snapshot coverage must be re-evaluated on every run.

Validation: the acquisition script completed a second live run; both NPPES response hashes matched the initial retrieval, and the LEIE scan again returned one exact match across 84,093 rows. JSON and graph reference checks passed. The dedicated schema library was unavailable in this interpreter; the repository integrator should run its standard graph validation.
