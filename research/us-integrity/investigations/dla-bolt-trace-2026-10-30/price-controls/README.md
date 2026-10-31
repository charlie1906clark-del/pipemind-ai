# Reviewed price comparisons

This offline, standard-library calculator tests declared comparable prices. It implements the user's concern that correct procurement arithmetic and a real supplier do not establish a fair price. A recurring percentage difference is a research lead; this program does not establish intent, a concealed payment, an unlawful benefit, recoverable loss, or a reward entitlement.

The comparator, reviewer identity, claimant independence, availability, and payment reconciliation are **declared inputs that this program cannot authenticate**. `eligible_as_declared` means that the schema gates passed. A researcher must inspect the cited evidence and a separate reviewer must assess the match. The program makes no network requests and never derives an independent benchmark by assuming the answer.

## Reproduce

Run these commands from this directory with Python 3.10 or newer:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
python premium_audit.py scenarios/uniform-12-percent.json
python premium_audit.py scenarios/weighted-mix.json
python premium_audit.py scenarios/dla-current-no-qualified-benchmark.json
python premium_audit.py --annual-illustration
```

Add `--output /path/to/new-result.json` to create a result file. Existing output files are never overwritten by the CLI. Invalid batches exit with code 2; individual comparisons lacking evidence appear as `blocked`. A zero eligible-line count is not a finding of fair pricing. The checked-in `outputs/` files reproduce those four commands. Each file-based result includes the exact input SHA-256. The current-order fixture separately hashes the inspected `../current/observations.json` snapshot.

## Formulas and denominators

For each eligible line, let `q` be its stated ordered, invoiced, or reconciled paid quantity; `p` the price on that basis; and `r` the independently reviewed reference unit price plus documented per-unit adjustments.

| Measure | Formula |
| --- | --- |
| Line price premium | `(p − r) / r` |
| Comparable reference value | `q × r` |
| Observed value on the stated basis | `q × p` |
| Difference against the reference | `q × (p − r)` |
| Weighted aggregate premium | `sum(q × (p − r)) / sum(q × r)` |
| Difference as a share of gross observed value | `sum(q × (p − r)) / sum(q × p)` |

Negative differences are preserved. Rates are not averaged across lines. Currency and value basis form separate aggregation groups; ordered values, invoices, and paid cash are never summed together. Values are decimal strings, calculated at precision 80; input bounds and the 10000-line limit leave enough precision for exact products and aggregate sums. Amounts display to two decimal places and percentages to six, using half-up rounding after aggregation. Per-line `*_exact` fields preserve unrounded decimal products; percentages involving repeating division are rounded. A zero observed value makes its gross-share percentage null.

The illustrative two-line fixture has reference value `200000`, ordered value `224000`, and difference `24000`: 12% of the reference and 10.714286% of gross. The unequal-weight fixture has a 20% difference on one unit and no difference on nine equal-value units: its aggregate is 2%, not the unweighted 10% average of its two line rates. Both use fictional parties and declared inputs, with `XXX` explicitly representing unspecified currency.

The user's separate annual illustration assumes that `100000` is the total price increment at a uniform 12% markup. Algebra then gives an implied reference annual cost of `100000 / 0.12 = 833333.333…` and gross value `933333.333…`, displayed as `833333.33` and `933333.33`. It does not establish a personal benefit or any government transaction. The currency was not specified. Do not insert these illustrative amounts into actual money totals or actual source/evidence nodes.

## Input gates

The JSON fixtures are complete schema examples. `schema_version`, `data_origin`, `evidence_kind`, `dataset_scope`, and a nonempty `lines` array are required. Public observations and synthetic calibration must use separate files. Illustrative source URLs end in `.invalid` and do not represent evidence.

Each line must provide an explicit agency namespace, PIID, order ID, and CLIN. `NO_SEPARATE_ORDER` is permitted when an independently verified standalone award genuinely lacks a separate order. Keys are case-insensitive; surrounding whitespace is rejected. Any duplicate key or line ID rejects the whole batch. Reconcile amendments, cancellations, returns, and replacement snapshots before submission. The program cannot decide which modification supersedes another.

Both sides require item identifier, revision, unit of issue, pack size, quantity, price date, delivery terms, condition, quality, traceability, freight, warranty, and included scope. Missing terms and common unknown placeholders block comparison even if a reviewer flag says `comparable`.

| Evidence gate | Rule |
| --- | --- |
| Item identity and specification | Item, revision, unit, pack, condition, quality, and traceability must match exactly. No implicit NSN crosswalk, pack conversion, or historical unit assumption. |
| Quantity and timing | Each price must apply to the tested quantity and date. Reference availability must be declared confirmed. |
| Documented adjustments | Quantity, date, delivery, freight, warranty, or scope differences require a separate adjustment with signed per-unit amount, reason, source, and the comparison reviewer's ID. Zero adjustments still need evidence. |
| Provenance | Every source requires HTTP(S) URL, source ID, observed date, source kind, locator, and scope. Public observations reject illustrative source kinds and `.invalid` URLs. |
| Independence | Reference and claimant independence must both be declared `reviewed_independent`, with supporting evidence. Neither field proves the declaration true. |
| Review | The comparison requires decision `comparable`, review date, evidence note, and a reviewer ID different from the analyst ID. |
| Ordered value | Requires an award/order line, ordered unit price, and ordered quantity. |
| Invoiced value | Requires an invoice line, invoiced unit price, and invoiced quantity. Relabeling an order source is rejected. |
| Paid cash | Requires invoice/payment evidence, a separate payment record, paid quantity/unit-price basis, and explicit line-level reconciliation. Ordered value alone is not paid cash. |
| Numeric controls | No floats, exponent notation, nonfinite numbers, negative observed prices, nonpositive reference/adjusted reference prices, or zero/negative quantities. Documented reference adjustments may be negative. |
| Misclassified values | Contract ceilings, estimated annual quantities, and a ceiling divided by an estimate are not accepted as ordered unit-price observations. |
| Circular baseline | A reference labeled `inferred_from_assumed_markup` is blocked. Dividing `0.91` by `1.12` to get `0.8125` does not independently establish a 12% premium. |

The accepted public reference source kinds are manufacturer/distributor listings, independent quotes, supplier invoices, catalogs, and agency award lines. Admitting an agency award line is only a schema capability: award history may share the same pricing problem and must not be asserted independent without evidence. An observed public offer also does not prove quantity availability, date alignment, NSN equivalence, or applicable compliance requirements. Source kind and reviewer flags cannot make a commercially similar item an established benchmark.

## Current DLA line

The public-observation fixture records the inspected line for order `SPE4A627F0588`, linked to parent `SPE4A626D61WS`: `906 EA × USD 0.9100 = USD 824.46` in ordered value. Source `BOLT-CUR-S02` is the official award PDF; its page and scope are recorded in the fixture. The local source snapshot and selected public excerpts are maintained in `../current/`.

Its price comparison remains **blocked**. No qualified reference is supplied; several condition, traceability, warranty, and landed-cost terms remain unresolved. The result has null comparison amounts and no aggregate. It is neither a finding of fair pricing nor evidence of a 12% premium. Current commercial offers require the separate market research and comparison review before they could be supplied here. Nothing in this fixture asserts that USD 824.46 was paid.

## Repeated-percentage research

The output includes minimum and maximum eligible line rates to aid inspection. It does not automatically label a recurring 12% pattern. Before a pattern screen, predeclare the tolerance, dates, eligible population, strata, rounding treatment, exclusions, and minimum independent solicitations or periods. Review the full eligible population, preserve cheaper lines, disclose blocked coverage, and test whether freight, discounts, taxes, quality or delivery terms explain the pattern. Avoid selecting a reference or time window because it produces the suspected percentage. See `../price-challenge/` for the separate research and review playbook.

## Output contract for graph integration

Every result contains `data_origin`, `evidence_kind`, and `dataset_scope`. Line states are `eligible_as_declared` or `blocked`; blocked lines have null adjusted reference, premium, and difference. `submitted_lines`, `eligible_lines`, `blocked_lines`, and `coverage_complete_for_submitted_lines` describe only the submitted set, not the completeness of procurement records. The CLI's `input_snapshot` hashes the input but does not authenticate it.

Synthetic files must enter only synthetic calibration nodes, with `synthetic=true` and no actual `money` property. Their `.invalid` URLs and fictional source IDs must not become real source nodes. The DLA result belongs to a separate public-observation, blocked-comparison node. Neither result provides a buyer benefit or a misconduct conclusion.

The 12 unittest cases cover weighted and gross denominators, negative differences, duplicate rejection, unresolved terms, immutable specifications, independence/provenance/reviewer gates, ceiling/estimate confusion, numerical edge cases, freight adjustments, invalid adjustments, invoice/payment/currency separation, and the actual-order/circular-reference controls. The program is an offline research aid, not an automated adjudicator.
