# Exact bolt specification: acquisition and ingestion follow-up

The exact primary specification for **NSN 5306016864912 / NIIN 016864912 remains unacquired**. The current $0.91 order price still cannot be compared conclusively with the provisional commercial bolt listings. This follow-up does not turn a repeated access limitation into a finding of reasonable pricing or wrongdoing.

The new practical result is an exact two-record acquisition packet and a tested ingestion adapter. A researcher with an actual official export can now submit all of the characteristic and part-reference rows without losing the leading zero, reference qualifiers or source provenance. The adapter cannot authenticate a source merely because a receipt calls it official, and it never automatically qualifies a price comparison.

## What was established

The official DLA reading-room index describes separate Characteristics and Reference CSV products. Its dated layout documents identify `V_CHARACTERISTICS.CSV` with NIIN, MRC, requirement statement and clear-text reply. The Reference layout identifies `V_FLIS_PART.CSV`, preserving part number, CAGE and qualification fields including RNCC and RNVC. These source observations are recorded in [sources.json](sources.json); both direct layout-PDF opens returned HTTP 403, so their current evidence depth is indexed text.

Twelve bounded searches did not expose an actual published CSV file URL or an exact official row for this NIIN. Nonmatching results were excluded. No guessed ZIP URLs were used. This is a search outcome, not proof that the public record does not exist. The [query log](query_log.json) records the limits and failures.

The previously inspected public [PUB LOG archive](https://publogstorage.blob.core.windows.net/publog/PublogDVD.zip) contains native `V_CHARACTERISTICS.TAB` and `V_FLIS_PART.TAB` members. Its supplied DECOMP instructions document filtering a table with SQL and saving the result. The earlier archive metadata and selected instructions are reused with [exact hashes](prior-inputs.json). No new bulk download or executable run occurred. There is no installed Wine/Wine64 runtime in this environment, so the Windows reader path was not executed.

## The next acquisition is specific

[export-packet.json](export-packet.json) defines two work packages:

| Task | Needed source | Expected evidence |
| --- | --- | --- |
| BSF-CHAR-001 | Actual official characteristics export for NIIN 016864912 | All characteristic rows, field labels, release and retrieval metadata |
| BSF-REF-001 | Actual official part-reference export for the same NIIN | Every reference and its qualification codes, without assuming that CAGE means manufacturer |

The packet includes proposed SQL in the documented DECOMP form, derived from the dated CSV field layouts. These exact queries have **not** been run against the installed reader; a worker must verify its actual table and column names first. Alternatively, acquire the CSV products through their actual published reading-room links. The follow-up did not discover those file URLs and does not invent them.

Keep the source release label and date separate from the relevant order dates. A later catalog snapshot does not prove historical applicability. After the rows arrive, an independent reviewer must reconcile dimensions, thread, grade, material, finish, special requirements and reference qualifications, then separately compare quantity, availability, packaging, traceability, certificates, delivery and freight. A nominally similar bolt remains only a candidate until those checks pass.

## Executable adapter

[parse_publog_export.py](parse_publog_export.py) reads explicit comma- or pipe-delimited exports; it does not read native `.TAB` files, make network requests or run the supplied DLA executable. It checks source-receipt fields, exact byte hash, table schema, row width, NIIN format, row budgets and provenance labels. Public receipt URLs reject empty or populated userinfo, whitespace/control characters, backslashes and sensitive query keys after case-insensitive percent-decoding; ordinary public version parameters remain accepted. It preserves duplicate rows and source values rather than silently merging them. Missing records or malformed inputs never become a complete-catalog absence finding.

Example invocation from this directory, after obtaining an actual export and its receipt:

```bash
python parse_publog_export.py --input /path/to/characteristics.txt --receipt /path/to/receipt.json --table characteristics --niin 016864912 --delimiter pipe --output /path/to/new-selected-result.json
```

The CLI refuses to overwrite an existing output. The export byte limit is 50 MB and the row limit is 250,000; it is intended for selected exports, not direct parsing of an entire multi-gigabyte catalog. The full current catalog's completeness is never inferred from the supplied file. The parser reports `parsed_pending_source_and_applicability_review` only when matching rows exist.

Eleven tests cover exact keys and leading zeroes, quoted fields, receipt tampering, preserved qualifiers, missing/duplicate headers, malformed rows, absent-target semantics, binary rejection, exhausted budgets, synthetic/real labeling, date ordering, duplicates and exclusive output. Tests use fictional values; their NIIN is a parser-control key, not a technical finding. Run:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

The [validation record](VALIDATION.json) distinguishes these completed software checks from the still-open source acquisition. The only current result is an explicit evidence gap plus a reproducible way to ingest the missing records. No price premium, buyer benefit, loss or new fraud finding is established.
