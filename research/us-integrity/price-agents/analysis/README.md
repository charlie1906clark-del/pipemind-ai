# Repeated premium screen

`recurrence.py` runs the existing qualification and weighted-price calculator before screening repeated differences. The program is an exploratory arithmetic aid used by an analyst; it does not run a language model, authenticate a review, prove an excessive price or identify corruption.

```bash
python research/us-integrity/price-agents/analysis/recurrence.py research/us-integrity/price-agents/analysis/examples/synthetic-input.json research/us-integrity/price-agents/analysis/examples/exploratory-plan.json research/us-integrity/price-agents/analysis/examples/synthetic-metadata.json
python -m unittest discover -s research/us-integrity/price-agents/analysis -p 'test_*.py'
```

The plan specifies a target percentage, tolerance in percentage points, observation period, minimum share of eligible lines in that band, maximum blocked-line fraction, and minimum counts of distinct in-band solicitations, months and benchmark families. This initial version supports only `exploratory_retrospective`; a user-supplied date cannot establish advance registration. Preserve a committed plan before a future held-out acquisition, then independently review its timing and any changes before calling a test prospective.

Grouping uses supplier identifier, purchasing-office identifier, item stratum, currency and ordered/invoiced/paid basis. Metadata must cover every submitted line exactly once and bind the input and plan by canonical JSON SHA256. Exact transaction-key duplicates are rejected by the existing calculator. Distinct solicitation/family IDs and review identities are declared evidence, not proof of independence. Do not invent IDs to pass minimum counts or split one solicitation into several apparent repetitions.

Band membership uses unrounded cross-products. All eligible lines, including cheaper lines and differences outside the target band, remain in the weighted total. Minimum distinct-source counts use only in-band lines. Blocked coverage is a line-count measure for the submitted group, not a value-coverage percentage or a nationwide completeness claim. Separate currencies and value bases never aggregate. A candidate pattern is a request for independent investigation, with no fraud probability, personal-benefit amount or recoverable loss.

The four-line synthetic example gives a12% repeated pattern under its declared controls. The negative-line test preserves three12% lines and one−10% line, making the overall weighted premium6.5%; selecting only the expensive lines would mislead. Boundary tests distinguish an actual13.000000000001% rate from its rounded13% display. Other tests cover same-solicitation repetitions, shared upstream families, dates, duplicate keys, circular benchmarks and missing comparisons.

The actual example reuses the frozen DLA order input and remains blocked. `PIID-prefix:SPE4A6` is only a source-key grouping label; it does not identify an individual buyer or prove office independence. No real repeated premium is established. Synthetic outputs must not enter actual money totals or real-entity allegation nodes.

An independent reviewer must inspect item equivalence, feasible quantity/pack, date, freight, compliance, benchmark provenance, case selection and source relationships. A fixed markup can persist while nominal prices fall; a repeated rate can also arise from ordinary catalog multipliers or service costs. Price-pattern evidence and any actual benefit/influence evidence remain separate.

A repeated line-count pattern can coexist with a **negative aggregate difference** if a large cheaper purchase outweighs several small premiums. The output therefore reports net-difference sign and the fraction of eligible reference value represented by in-band lines. A candidate pattern must never be described as overall overpayment. Independent adversarial tests reproduce this counterexample.
