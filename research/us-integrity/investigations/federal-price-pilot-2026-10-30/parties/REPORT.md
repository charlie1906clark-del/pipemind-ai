# SPE4A626PW775: documented parties and unresolved money trail

The award names a dealer and an intended manufacturer. Exact DLA CAGE searches independently connect both to federal UEIs. This establishes who the public records identify; it does not establish a hidden markup, improper payment or personal benefit.

| Role | Documented entity | Identifier | Evidence and date |
|---|---|---|---|
| Named dealer | DON INDUSTRIAL GROUP LLC | CAGE 745V4; UEI XN9HKU6LUM59 | DLA order page 2, signed date 2026-07-09; exact CAGE search observed 2026-10-30 |
| Public award recipient | DON INDUSTRIAL GROUP LLC | Recipient 516cae19-6195-34c1-0e8f-71a1fd4f3702-C | Exact USAspending award and recipient profile |
| Contractually intended manufacturer | SPS TECHNOLOGIES LLC | CAGE 27624; UEI E6KFWWNKEQ49 | DLA order page 2 states source for P/N 39-8820-501; exact CAGE/UEI match |
| Reported parent of SPS recipient | BERKSHIRE HATHAWAY INC. | UEI UU26FKF1MML6 | USAspending child profile observed 2026-10-30; no historical ownership interval or percentage established |
| Awarding/funding office | DLA AVIATION | DLA 97AS; DoD 097 | Exact USAspending award |
| Actual government payee | Unknown | — | Obligation/recipient data is not a disbursement ledger |
| Actual invoice supplier | Unknown | — | Contractually intended manufacturer is not an invoice or delivery record |
| Printed contracting/ordering officer | Joseph Felhauer | Role limited to this instrument | DD1155 page 1 block 24 area; printed date 2026-07-09; signature execution not independently authenticated |
| Individual price selector, authenticated signer or payment approver | Unknown | — | Printed officer role does not establish these decisions or authorities |

Don's profile reports Don itself as parent. That does not identify an owner or demonstrate that no affiliates exist. SPS's reported-parent relationship is preserved with its source and observation date; it is not expanded into an unsupported beneficial-owner chain. The SPS comma/no-comma name variation is explicitly reported as an alias under the same UEI.

The Florida filing L10000120053 is an unmerged candidate. An official search-index extract identifies a manager, but the state document has no retained federal-identifier crosswalk and the manager's transaction-date role is unverified. The candidate stays outside the award graph. No residential addresses, personal contacts, family relationships or private financial profiles are retained.

The supplier-cost test still requires the dealer's actual supplier invoice, matching quantity and specifications, credits/rebates, packaging/freight and first-article obligations. Government invoice, receiving/acceptance and payment records would establish whether the scheduled supply became an actual payment. No price margin or benefit is computed from a corporate-parent field.

The machine-readable evidence is in [graph.json](graph.json), [sources.json](sources.json), [identity-decisions.json](identity-decisions.json), [timeline.json](timeline.json) and [unresolved.json](unresolved.json). [Context notes](context-notes.json) distinguish inspected company pages from search-index-only candidate observations. [Research budget](research-budget.json) records eight queries and fifteen public-read attempts, including consent and failed requests. [Acquisition log](acquisition_log.json) pins direct response hashes; retained selected extracts have separate hashes. Original source bytes are not claimed to be archived.

Reproduce local checks with `python3 validate_parties.py` from this directory. A fresh acquisition is deliberately blocked from overwriting evidence; a later authorized run should use a new dated output directory. The CAGE form requests follow ordinary public consent, without retaining cookies or form tokens.
