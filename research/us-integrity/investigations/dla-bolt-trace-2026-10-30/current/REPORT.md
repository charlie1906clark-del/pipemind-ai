# Original current contract and delivery-order trace

Checked 30 October 2026. The original DLA contract and its inspected delivery order specify **USD 0.91 per EA** for NSN 5306016864912. The delivery order specifies **906 EA and $824.46**. This is a verified ordered line value; delivery, acceptance and payment remain unverified. The $350,000 parent figure is a ceiling. No fraud, overpayment or recoverable loss is established.

## Primary documents acquired

| Document | Original date | Exact evidence |
|---|---|---|
| SPE4A6-26-D-61WS | 17 September 2026 | Page2: $350,000 maximum; 2,221 EA estimated annual quantity; conditional 222 EA guaranteed minimum; minimum delivery order 1 EA. Page5: CLIN 0001, USD 0.91000/EA, QUP 001,76 delivery days. |
| SPE4A6-27-F-0588 under that contract | 19 October 2026 | Page1: parent/order identifiers, CAGE 8A1E8 and $824.46 total. Page2: NSN, CLIN 0001/basicCLIN 0001,906 EA,0.9100 unit price,824.46 line value, delivery 4 January 2027. |

Both were downloaded from the official DLA public document route after its normal notice/consent form. The original hashes are in [selected_manifest.json](selected_manifest.json). The first-page business name and CAGE agree across the documents. The parent uses an indefinite-delivery quantity of0.000 on its base line: this is not a purchased quantity or evidence of free goods. Its instructions make orders and acceptable performance relevant to when the unilateral arrangement becomes binding. We have not verified that performance.

The child line points explicitly to the parent's basic CLIN and uses the same 0.91 price. Decimal arithmetic confirms 906×0.91=824.46. Its dollar-value heading and linked parent's explicitUSD currency provide the currency basis. Page1's receipt, acceptance and payment certification blocks are blank. The delivery date was future at retrieval. Neither the ordered amount nor the blank blocks prove what was ultimately paid.

## What this resolves

A third-party display reviewed separately shows a 157.5867 unit-price figure. That value arithmetically matches 350,000÷2,221. The two operands are the ceiling and estimated annual quantity, so this calculation is ineligible as a purchased unit price. The acquired original priced lines now supply direct evidence of 0.91 per EA. We do not infer the website's internal algorithm or intentional wrongdoing from numerical agreement. See the [independent review](../review/REPORT.md).

The RFQ required 78 delivery days and a 555 EA minimum delivery order; the resulting parent shows 76 days and 1 EA. These differences demonstrate why the RFQ cannot automatically supply awarded terms. They do not independently establish an improper contract change. Older historical prices still lack their original line terms, so this current contract does not make all historical comparisons valid.

## Empty public-database searches

Five USAspending query attempts were retained. Three completed with HTTP 200 and zero rows: one keyword search and separate unquoted award-ID searches for the parent and child. Two quoted exact-ID requests returnedHTTP 503. Failed requests are not empty datasets. Unquoted ID filters may match fuzzily, so any future response needs an exact-identifier check.

USAspending's official About the Data document, updated 6 October 2026, describes a 90-day delay for DoD/USACE procurement data, including contracts and IDVs, affecting Files C/D1. The parent and child were 43 and 11 days old at retrieval. Normal publication delay is a plausible explanation for absence from these query results, not proof of the cause for either particular record. The successful original DLA downloads illustrate why an empty aggregate-data search must not be classified as a nonexistent contract. Sources and precise locators are in [sources.json](sources.json).

## Retention and reproduction

The public repository retains selected term/line text and rendered pages, without supplier street/contact fields. Full original PDFs remain local and are excluded from Git. Their download hashes are distinct from the hashes of selected artifacts; no selected excerpt is labeled a complete original document. The public source URLs permit a new ordinary acquisition attempt.

From this directory, with original PDFs in an explicitly supplied local directory:

```sh
python reproduce_selected.py --source-dir /path/to/originals --output /tmp/bolt-selected-replay
```

For two new bounded public-document attempts:

```sh
python reproduce_selected.py --acquire --output /tmp/bolt-public-reacquisition
```

Output directories must be new. The latter retains original PDFs locally in a folder labeled not to publish. A source hash change or failed acquisition stops replay; no account, access-control workaround or automatic retry is used. Poppler's `pdftotext` is required. The recorded offline replay reproduced all three selected text pages. Independent visual review covers the original source pages; the archived images preserve the priced lines for inspection.
