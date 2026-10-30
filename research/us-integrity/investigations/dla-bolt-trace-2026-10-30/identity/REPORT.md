# Five-supplier identity trace for one DLA bolt

Checked **30 October 2026**. This lane complements the pricing work on machine bolt **NSN 5306016864912**. It resolves the five CAGE identifiers in seven historical rows of official DLA RFQ SPE4A626U3619 against **current official CAGE results**, **USAspending recipient profiles**, and **seven exact historical award records**. All five current identifier crosswalks agree with the historical award joins. This is a useful completed identity check; it establishes no impersonation, new fraud or beneficial-ownership chain.

## What the records support

| CAGE | Current official legal business name | UEI | Profile state | Historical awards in this fixed set |
|---|---|---|---|---:|
| 6ZF42 | BUTT FAREED AHMAD | GWEEKJ2PNL45 | TX | 2 |
| 0NFB8 | DIALOGIC CORP | JEJSN59MQVK3 | PA | 1 |
| 7W108 | SUBURBAN BOLT & SUPPLY CO | JE5NG1MWNU77 | MI | 1 |
| 8A1E8 | KAREN CARLISLE | KJGWN783BNB5 | TX | 2 |
| 51Y73 | CASCADE NUT & BOLT, INC | US4BABY42KV8 | OR | 1 |

Names, codes and current crosswalks come from DLA's public CAGE search. State information comes from the separate USAspending profile and is not an owner's residence. Source IDs `BI-S-CAGE-<code>` and `BI-S-PROFILE-<code>` resolve in [sources.json](sources.json). The selected registry responses each contain one detail-result link and the exact code, UEI and legal name. The source dates are current observations, not retroactive registration certificates.

The API classifies two records as sole proprietorships and three as corporate business records. A person's name in the legal-business-name field therefore does not by itself indicate a fabricated supplier. Only business structure relevant to interpreting the record is retained; demographic categories, street addresses and personal contacts are omitted.

The five recipient queries returned **nine profile rows**: four parent/child pairs and one child-only result for Cascade under the contract-recipient filter. Empty second pages and first-page totals establish completion for these five literal queries. The nine rows do not imply nine distinct companies. Each child profile was read separately, producing **15 USAspending requests** in total.

## The historical joins are separate from the current registry

The prior official solicitation supplies **PIID + CAGE + award date**. The newly acquired USAspending award response supplies **exact PIID + signed date + recipient UEI/name**. All seven PIIDs and dates match, and each resulting UEI agrees with the current CAGE lookup. This is an exact-record join, not a name-similarity match.

The seven keys are SPE4A626V138W, SPE4A626P5931, SPE4A625V346U, SPE4A625V252D, SPE4A625V208Q, SPE4A625PK654 and SPE4A625V4508. Dates range from **4 December 2024 to 26 May 2026**. Each join retains its own DLA page locator and award source; see [entity_records.json](entity_records.json). The CAGE field is provided by the distinct DLA history source, not asserted to exist in the captured USAspending award schema.

These matches support the identity of the **reported award recipient**. They do not prove historical SAM activation, eligibility for a particular certification, actual delivery, bank payee, invoice payment, a novation, or unchanged legal control. Current registration and historical award facts have separate time bases. The award lane retains competition, obligation and other procurement fields; this identity lane neither recalculates unit prices nor labels an obligation as cash paid.

## Punctuation and aliases have ordinary explanations here

The five official recipient profiles report **12 alternate-name strings**, including comma/spacing changes, `CORP.` versus `CORPORATION`, and `&` versus `AND`. The aliases are preserved verbatim with their source UEI. Their effective dates are not available in these responses, so they are not promoted into a dated legal-name-change history.

No entity is merged merely because names normalize to the same text. Conversely, the API's explicit alternate-name list is stronger evidence of a source-reported naming relationship than a punctuation heuristic. This small cohort supplies concrete controls for a future impersonation screen: the system should accept supported alias relationships without inferring either deception or legal identity from text alone.

## Ownership remains a different question

All five child profiles report the same UEI as their parent. This is **USAspending's current reporting hierarchy**, not authenticated beneficial ownership. A self-parent record does not prove that no external owner or holding company exists, and it is not evidence of concealed ownership.

One secondary discovery page lists Derry Enterprises as Cascade's parent awardee. That pointer is recorded in [query_log.json](query_log.json), but no primary corporate transaction or ownership filing was acquired here to authenticate it or establish its effective date. It is not inserted as a beneficial-owner relationship. The secondary assertion and an API self-parent field may concern different reporting structures or periods; their difference alone establishes no contradiction or wrongdoing. The next useful ownership step would be a dated primary corporate or acquisition record, followed by checking whether it affects the exact award-period representation being examined.

## Acquisition, reproducibility and limits

CAGE records were obtained through the site's ordinary public notice, cookie and search forms. No account, credential, CAPTCHA solving or access-control workaround was used. Form tokens and cookies were not retained. The bounded lane used **10 search queries** and **31 logical public-source reads**, within the coordinator-approved revised ceiling of 33. The extension from 25 reads permitted the four remaining exact CAGE lookups after the normal form route was established. Server redirects were followed normally within those reads.

The [capture manifest](capture_manifest.json) distinguishes original response hashes from hashes of selected/reformatted snapshots. Original API wire bytes and CAGE HTML are not archived here. The selected evidence omits addresses, contacts and demographics; its byte hashes are real, but they do not claim to be hashes of the full original pages. Search snippets served as discovery pointers and did not substitute for official identity confirmation. Corporate registries, exclusion histories, historical activation periods and financial accounts were not inspected in this lane.

The offline builder checks saved API hashes, query totals/terminal pages, profile bindings, exact registry code/UEI/name text and each award/date/UEI join before generating the records:

```sh
python research/us-integrity/investigations/dla-bolt-trace-2026-10-30/identity/build_records.py
```

Four negative-control/provenance tests pass, covering altered capture bytes, contradictory CAGE/award joins even after digest updates, and preservation of ownership/eligibility uncertainty.

The acquisition scripts perform explicit network reads and reject repeated capture labels or existing CAGE logs. They are not background workers or a nationwide scraper. Reacquisition requires a separate dated evidence directory and review; it must not silently overwrite these dated observations.

**Outcome:** five current official CAGE-to-UEI crosswalks, seven exact historical award joins, and 12 source-reported aliases. Zero identifier mismatches were observed within this fixed set. Beneficial ownership and historical registration eligibility remain unresolved; no fraud finding or money aggregation is made.
