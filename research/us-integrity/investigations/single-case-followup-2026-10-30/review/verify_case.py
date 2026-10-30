#!/usr/bin/env python3
"""Read-only independent consistency checks for this frozen single-case follow-up.

No remote calls, source acquisition, model invocation, graph approval or fraud
inference. Exact fractions independently check the hypothetical full-carton
arithmetic. Selected-artifact integrity is not authentication of original pages.
"""
import argparse
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
RESEARCH = CASE.parents[1]


def load(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pins(root, records):
    for row in records:
        # Producers declare either research-root or repository-root paths.
        # Interpret the explicit prefix; never guess a suffix match.
        base = RESEARCH.parents[1] if row['path'].startswith('research/us-integrity/') else root
        path = (base / row['path']).resolve()
        assert path.is_relative_to(RESEARCH), row['path']
        assert digest(path) == row['sha256'], row['path']
    return len(records)


def check_market(market):
    assert market['case_nsn'] == '5306016864912'
    assert market['qualified_comparators'] == 0
    assert market['fraud_established'] is False
    assert market['buyer_benefit_established'] is False
    prices = {'MF Supply': Fraction('328.91'), 'Nationwide Industrial Supply': Fraction('190.49')}
    rows = market['catalog_outlay_arithmetic']
    assert {(r['seller'], r['target_quantity']) for r in rows} == {(seller, q) for seller in prices for q in [906, 2221]}
    for row in rows:
        q = row['target_quantity']
        cartons = (q + 1099) // 1100
        assert row['minimum_full_cartons'] == cartons
        assert row['catalog_units_purchased'] == cartons * 1100
        assert row['surplus_units'] == cartons * 1100 - q
        assert Fraction(row['catalog_cash_outlay_before_unpriced_terms']) == prices[row['seller']] * cartons
        assert row['government_comparable'] is False
        assert all(row[k] is None for k in ['price_premium', 'overcharge', 'loss'])
        if q == 2221:
            assert row['target_quantity_context'] == 'parent_estimated_annual_demand_not_an_order'
    inventory = next(r for r in market['changed_findings'] if r['id'] == 'SCM-F02')
    assert inventory['seller_displayed_nominal_pieces'] == 7 * 1100
    assert inventory['actual_available_or_reserved_pieces'] is None
    assert inventory['delivery_promise_verified'] is False
    allowance = market['counterfactual_allowance']
    assert allowance['status'] == 'illustrative_only_not_a_qualified_price_comparison'
    assert allowance['scope_quantity'] == 906 and allowance['not_applied_to_annual_demand'] is True
    assert Fraction(allowance['actual_order_value_usd']) == Fraction(906) * Fraction('0.91')
    for row in allowance['rows']:
        assert Fraction(row['full_carton_outlay_assumed_usd']) == prices[row['seller']]
        assert Fraction(row['residual_budget_assumed_usd']) == Fraction('824.46') - prices[row['seller']]


def verify():
    counts = {}
    for name, manifest in [('bids', 'bundle-manifest.json'), ('market-terms', 'manifest.json'), ('spec', 'VALIDATION.json')]:
        counts[name] = pins(CASE / name, load(CASE / name / manifest)['artifacts'])
    selection = load(CASE / 'selection/VALIDATION.json')
    counts['selection'] = pins(CASE / 'selection', [{'path': p, 'sha256': sha} for p, sha in selection['artifact_hashes'].items()])
    prior_count = 0
    for name, filename in [('selection','inputs.json'),('spec','prior-inputs.json'),('bids','prior-inputs.json'),('market-terms','prior-inputs.json')]:
        prior_count += pins(RESEARCH, load(CASE / name / filename)['artifacts'])
    selected = load(CASE / 'bids/selected-manifest.json')['records']
    for source in selected:
        assert digest(CASE / 'bids' / source['artifact_path']) == source['sha256']
    rfq = load(CASE / 'bids/selected/current-rfq-record.json')
    award = load(CASE / 'bids/selected/current-award-record.json')
    assert (rfq['nsn'], rfq['solicitation'], rfq['contract']) == ('5306016864912','SPE4A626U3619','SPE4A626D61WS')
    assert rfq['rfq_quantity_as_displayed'] == '2221' and rfq['quantity_is_paid_or_ordered'] is False
    assert award['displayed_amount'] == '350000.00' and award['payment_verified'] is False
    assert 'ceiling' in award['amount_interpretation']
    assert award['competing_quote_prices_acquired'] == 0 and award['price_reasonableness_decision_acquired'] is False
    clause = re.sub(r'\s+', ' ', (CASE / 'bids/selected/parent-page3-h06.txt').read_text())
    assert 'Price evaluation will be based on the price quoted for the estimated annual demand in the schedule.' in clause
    assert 'The unit price for orders is based on the price for the quantity range that will cover the total quantity on the order, regardless of destination.' in clause
    spec = load(CASE / 'spec/qualification.json')
    assert spec['niin'] == '016864912'
    assert spec['primary_exact_niin_characteristics_rows_acquired'] == 0
    assert spec['primary_exact_niin_reference_rows_acquired'] == 0
    assert spec['qualified_price_benchmark'] is False and spec['fair_pricing_established'] is False
    shell = load(CASE / 'spec/tdmt-access.json')
    assert shell['http_status'] == 200 and shell['technical_record_acquired'] is False
    archive = load(CASE / 'spec/archive-static-inspection.json')
    for source in archive:
        assert source['status'] == 206
        assert digest(CASE / 'spec' / source['selected_artifact']) == source['selected_sha256']
    changes = load(CASE / 'spec/archive-change-inspection.json')
    total_range_bytes = sum(r['range_bytes'] for r in archive) + changes['range_bytes']
    assert total_range_bytes == 10412003
    assert changes['skipped_inner_members'][0]['declared_uncompressed_bytes'] == 53049953
    decision = load(CASE / 'selection/decision.json')
    assert decision['national_figure_interpretation']['measures_additive'] is False
    assert decision['national_figure_interpretation']['exact_user_reference_confirmed'] is False
    assert decision['selected_case']['fraud_probability'] is None
    assert decision['selected_case']['new_or_undiscovered_fraud_established'] is False
    market = load(CASE / 'market-terms/observations.json')
    check_market(market)
    mutations = [
        ('premature_qualified_comparator', lambda m: m.update(qualified_comparators=1)),
        ('premature_government_equivalence', lambda m: m['catalog_outlay_arithmetic'][0].update(government_comparable=True)),
        ('claimed_loss_from_catalog', lambda m: m['catalog_outlay_arithmetic'][0].update(loss='495.55')),
        ('fractional_carton_for_906', lambda m: m['catalog_outlay_arithmetic'][0].update(minimum_full_cartons=Fraction(906,1100))),
        ('round_down_annual_cartons', lambda m: m['catalog_outlay_arithmetic'][1].update(minimum_full_cartons=2)),
        ('nominal_stock_treated_reserved', lambda m: m['changed_findings'][1].update(actual_available_or_reserved_pieces=7700)),
    ]
    rejected = []
    for name, mutate in mutations:
        candidate = copy.deepcopy(market); mutate(candidate)
        try:
            check_market(candidate)
        except AssertionError:
            rejected.append(name)
        else:
            raise AssertionError('Negative control was accepted: ' + name)
    frozen_review = HERE / 'review.json'
    if frozen_review.exists():
        pins(RESEARCH.parents[1], load(frozen_review)['reviewed_input_artifacts'])
    return {'schema_version':'1.0','checked_on':'2026-10-30','status':'passed_scoped_consistency_checks',
            'producer_manifest_pin_counts':counts,'prior_input_pins_checked_with_repeats':prior_count,
            'bids_selected_artifact_hashes_verified':len(selected),'spec_selected_artifact_hashes_verified':len(archive),
            'declared_archive_range_bytes_reconciled':total_range_bytes,
            'independent_fraction_checks':{'full_carton_scenarios':4,'counterfactual_allowances':2},
            'negative_controls_rejected':rejected,'qualified_benchmarks':0,'network_requests':0,
            'scope_limit':'Checks retained records and exact arithmetic; does not reauthenticate original pages, independence, technical equivalence or source completeness.'}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); result=verify(); body=json.dumps(result,indent=2)+'\n'
    if args.output: args.output.write_text(body)
    print(body,end='')
