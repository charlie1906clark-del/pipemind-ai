# Independent review of the DLA bolt trace

Checked 30 October 2026. **The original current contract and delivery order establish a USD 0.91 price per EA, with 906 EA ordered for $824.46.** They disprove use of the secondary listing's 157.5867 as this order's unit price. The original RFQ and seven retained award summaries also support a traceable historical example, but not yet a fully comparable historical price series, payment, delivery, or fraud. A separate standards reference does not establish an exclusive supplier list.

## Original document and independent extraction

The original DLA RFQ SPE4A6-26-U-3619 was checked against SHA-256 `4a3996d9aca0fac0b32ea1cebfe8833fdbb144de33dc0af2739d0269b037ac51`. Pages 7–10 were rendered and visually inspected. A separate `pdftotext` extraction checked the history rows, current line and page 2 terms. The parser emits a form-field warning, but the displayed pages and independently matched text rows are intact. This is a read-only evidence review; no form fields were edited. [BR-S01](sources.json)

The seven CAGE/contract/quantity/cost/date combinations match the earlier selected evidence exactly. Current CLIN 0001 has unit `EA` and an estimated 2,221 quantity, but its unit-price and total-price cells are blank. Page 2 distinguishes a $350,000 maximum, a non-firm annual estimate, a conditional 222-unit minimum and 555-unit minimum order. These fields serve different purposes. No division of the ceiling by an estimate establishes a paid unit price.

[verify_pdf.py](verify_pdf.py) imports no producer module. [pdf_review.json](pdf_review.json) preserves its result and the separate manual visual check. All seven printed historical costs decrease in chronological order, from 1.92000 to 0.93000. That descriptive pattern does not support a simple claim of steadily increasing prices, but it also does not prove that earlier prices were unreasonable or later ones reasonable.

The two repeated-CAGE pairs combine larger later quantities with lower printed costs. For 6ZF42, quantity rises 156.78% and printed cost falls 20.51%; for 8A1E8, the corresponding changes are +24.07% and −42.71%. These are unadjusted arithmetic observations, not a causal discount estimate. Different dates, lead times, quantities, freight, qualification and production costs remain possible explanations.

## Terms that remain unresolved

[comparability_matrix.json](comparability_matrix.json) distinguishes current solicitation terms from historical evidence. Current pages specify 78-day delivery, FOB origin, destination inspection/acceptance, quantity-per-unit-pack 1, packaging requirements, sampling rules and a standard reference. None can simply be copied backward into the seven historical rows.

Historical records still need the actual awarded unit, pack, technical reference/version, condition, freight/delivery, inspection, warranty basis and nonrecurring cost treatment. The history's `N` surplus indicator does not supply all those fields. A missing warranty term is unknown, not proof that there was no warranty. A period-of-performance endpoint in an award API is not automatically the required physical delivery date.

All 21 possible historical pairs remain blocked for a definitive like-for-like price comparison. General FAR price-analysis guidance requires prior prices to be valid comparators and material quantity, terms and market differences to be addressed. The cited page provides methodology; applicability of particular clauses still depends on the actual contract and acquisition route. [BR-S03](sources.json)

## Secondary-display alarms

The inspected secondary NSN listing presents 157.5867 as a current unit price. `350000 / 2221`, rounded to four decimal places, yields exactly that number. The original RFQ identifies those inputs as a maximum and a non-firm estimate; its current price cells are blank. The original awarded contract and order now establish the actual document unit price as USD 0.91. The displayed number is therefore unsuitable as this transaction's unit-price comparator. The site's internal calculation has not been inspected, and the error is not evidence that the contracting party made a false claim. [BR-S01–02, BR-S06–07](sources.json)

The listing also displays ASME as a manufacturer/listed source and flags another awardee as not listed. In contrast, the primary RFQ explicitly classifies `ASMEB18.24` as a basic non-government standard. ASME's own listing identifies B18.24–2023 as a part-identifying-number standard for fasteners. These sources support a standards-reference interpretation, not an exclusive approved-manufacturer inference. The actual historical source-approval restrictions, if any, still require the applicable solicitation/award and official catalog-reference qualifiers. A catalog cross-reference alone does not prove that a distributor, reseller or manufacturer was unauthorized. [BR-S01, BR-S04–05](sources.json)

The secondary page remains a discovery aid. Its identifiers lead to primary records; its labels and computed prices are not imported as verified government findings. No technical manufacturing dimensions, restricted drawing or controlled data package was acquired to resolve this issue.

## Current original award and order

The coordinator acquired parent SPE4A6-26-D-61WS and child SPE4A6-27-F-0588 through the normal public DLA notice/consent flow. I independently rendered parent pages 2 and 5 and child pages 1 and 2, then checked the text and Decimal arithmetic. The parent p5 records CLIN 0001, unit EA, USD 0.91000, with $350,000 as the maximum. Its quantity 0.000 is part of an indefinite-delivery arrangement; the p2 estimate is not purchased by the parent alone. [BR-S06](sources.json)

Child p2 references basic CLIN 0001 and orders **906.000 EA × 0.9100 = 824.46**, with required delivery **4 January 2027**. Child p1 identifies the parent and order, order date 19 October 2026, and the same total. Receipt, inspection/acceptance and payment-certification blocks are blank in the inspected form. This establishes an ordered line and amount, not paid cash or completed delivery. [BR-S07](sources.json)

The award changes two visible RFQ terms: minimum delivery order quantity is **1 EA rather than 555 EA**, and delivery is **76 rather than 78 days**. These differences are not themselves adverse findings. They demonstrate why a solicitation must not be treated as the final awarded terms. Full subsequent-modification coverage is not established. The current line is verified; historical comparability remains separately unresolved. [current_order_review.json](current_order_review.json)

Original current-document hashes are retained as acquisition/verification metadata. Full PDFs are not republished in the public repository because they include unnecessary sole-proprietor street/contact fields. The coordinator's selected neutral pages/text support offline public review; optional original-document verification requires the acquired originals or a fresh ordinary public download.

## Seven official award-summary joins

[verify_awards.py](verify_awards.py) independently checks the nine retained response snapshots and request hashes, the same seven exact contract keys, an empty terminal page, signed dates, recipient UEIs and award amounts. It uses Decimal arithmetic and no producer modules. Every printed history quantity multiplied by printed cost matches the respective API total obligation; every history award date matches the signed date. [award_review.json](award_review.json)

This strengthens record linkage and arithmetic consistency. It does not promote the history row to an authenticated awarded CLIN or an invoice. The selected API records report competed simplified acquisitions, firm-fixed pricing and three to five offers. Those are useful counterevidence to an unsupported sole-source narrative, but the underlying bids and eligibility determinations have not been examined. Null outlay fields do not mean no payment occurred; payment remains unverified.

Independent live spot checks of the newest and oldest exact award keys are recorded in [spotchecks/manifest.json](spotchecks/manifest.json). Their selected award, recipient and procurement fields are compared with the producer capture. The original response digests and selected snapshot digests have distinct scopes; omitted addresses and contact details are not silently called byte-archived.

Empty USAspending searches for current September/October keys are not proof that the contracts do not exist: the original PDFs are now available. USAspending's official notice describes a 90-day delay in displaying DoD contract data. That is a plausible explanation for timing differences, not a verified cause for any particular empty response. [BR-S08](sources.json)

## Independent supplier-identity review

All five retained CAGE registry result rows agree with their respective USAspending UEIs and legal business names. The seven historical award links match exact contract keys and signed dates; the earlier RFQ supplies the historical CAGE field. Nine recipient profiles are not nine firms: parent/child reporting levels must remain separate. Twelve alternate-name strings are source-reported aliases, with no independently established effective dates. [identity_review.json](identity_review.json)

The independent checker verifies each retained request/snapshot digest and derivation input, extracts the CAGE/UEI/name sequence, and checks it against the profile and exact award record. It also verifies that self-parent relationships have not been promoted to beneficial ownership or historical eligibility. This reviewer did not repeat all five live CAGE queries; the retained selected records and producer request logs were examined. No identifier contradiction was found in that bounded evidence. [verify_identity.py](verify_identity.py)

Seven independent current-order regression tests pass. They reject a ceiling-derived price, changed amount, assumed payment, missing page, an altered line even after its manifest is repinned, and a non-finite price. The default current check uses selected public snapshots and works without the full PDFs. Optional original replay is `python verify_current.py --source-dir /path/to/originals`; the earlier original visual/hash inspection is separately recorded in [current_original_inspection.json](current_original_inspection.json).

## Decision boundary

Accept the verified USD 0.91 current order price, exact-key historical joins, reproduced arithmetic, dated source-reported procurement attributes and explicit missing terms. Reject an inference of a 157.5867 purchased unit price from the ceiling/estimate calculation. Reject an unauthorized-source inference based only on the secondary ASME label. Leave historical pricing fairness, delivered conformity, disbursement and legal wrongdoing unresolved until transaction-specific evidence supports them.

The most discriminating next records are the original priced award/CLIN and modifications for any proposed comparison, followed by acceptance/delivery and payment evidence where a concrete billing question survives. Source-registry qualifiers and the actual governing source-approval text would resolve the separate manufacturer-list question. Public-case searches can show a match or no match in the searched sources; they cannot certify that investigators have never seen a matter.
