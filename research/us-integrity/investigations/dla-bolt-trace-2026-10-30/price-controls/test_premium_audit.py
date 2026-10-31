"""Evidence gates and economic counterexamples, using synthetic inputs only."""
import copy
import hashlib
import json
from pathlib import Path
import unittest

from premium_audit import EvidenceError, annual_illustration, audit


ROOT = Path(__file__).resolve().parent


def fixture(name='uniform-12-percent'):
    return json.loads((ROOT / 'scenarios' / (name + '.json')).read_text())


def single():
    data = fixture()
    data['lines'] = data['lines'][:1]
    return data


class PriceAuditTests(unittest.TestCase):
    def assert_blocked(self, data, contains=None):
        result = audit(data)
        self.assertEqual(result['eligible_lines'], 0)
        self.assertFalse(result['coverage_complete_for_submitted_lines'])
        self.assertEqual(result['aggregates'], [])
        self.assertIsNone(result['lines'][0]['premium_against_reference_percent'])
        if contains:
            self.assertIn(contains, result['lines'][0]['reason'])

    def test_uniform_markup_and_distinct_gross_denominator(self):
        result = audit(fixture())
        group = result['aggregates'][0]
        self.assertEqual(result['eligible_lines'], 2)
        self.assertEqual(group['reference_basis_exact'], '200000')
        self.assertEqual(group['observed_basis_exact'], '224000')
        self.assertEqual(group['difference_exact'], '24000')
        self.assertEqual(group['weighted_premium_against_reference_percent'], '12.000000')
        self.assertEqual(group['difference_as_percent_of_observed_value'], '10.714286')
        example = annual_illustration()
        self.assertEqual(example['implied_reference_annual_cost_rounded'], '833333.33')
        self.assertEqual(example['implied_gross_annual_value_rounded'], '933333.33')
        self.assertEqual(example['currency'], 'unspecified')
        self.assertEqual(example['evidence_kind'], 'synthetic_calibration')

    def test_weighting_and_negative_differences_are_not_cherry_picked(self):
        data = fixture('weighted-mix')
        group = audit(data)['aggregates'][0]
        self.assertEqual(group['weighted_premium_against_reference_percent'], '2.000000')
        # One line at +20%, nine equal-value units at -10%: net -7%, not +20%.
        data['lines'][1]['contract']['unit_price'] = '90'
        group = audit(data)['aggregates'][0]
        self.assertEqual(group['difference_exact'], '-70')
        self.assertEqual(group['weighted_premium_against_reference_percent'], '-7.000000')

    def test_duplicate_identity_rejects_entire_batch(self):
        data = fixture()
        data['lines'][1]['key'] = {k: v.lower() for k, v in data['lines'][0]['key'].items()}
        with self.assertRaisesRegex(EvidenceError, 'duplicate'):
            audit(data)
        data = fixture()
        data['lines'][1]['line_id'] = data['lines'][0]['line_id']
        with self.assertRaisesRegex(EvidenceError, 'duplicate'):
            audit(data)

    def test_unknown_or_missing_terms_override_review_flags(self):
        for field in ('price_date', 'quality', 'traceability', 'freight', 'warranty'):
            for value in (None, 'unknown'):
                with self.subTest(field=field, value=value):
                    data = single()
                    for part in ('contract', 'reference'):
                        data['lines'][0][part]['terms'][field] = value
                    self.assert_blocked(data)

    def test_identity_units_pack_and_specification_cannot_be_adjusted_away(self):
        for field, value in (('item_identifier', 'OTHER'), ('unit_of_issue', 'BOX'),
                             ('pack_size', '100'), ('revision', 'OTHER'),
                             ('condition', 'used'), ('quality', 'OTHER'),
                             ('traceability', 'untraceable')):
            with self.subTest(field=field):
                data = single()
                data['lines'][0]['reference']['terms'][field] = value
                self.assert_blocked(data, 'term mismatch')

    def test_provenance_independence_and_separate_reviewer_are_required(self):
        changes = (
            ('source', 'url', ''), ('source', 'observed_on', 'invalid'),
            ('source', 'scope', ''), ('source', 'locator', ''),
            ('independence', 'status', 'unknown'),
            ('independence', 'claimant_independence_status', 'unknown'),
        )
        for section, field, value in changes:
            with self.subTest(section=section, field=field):
                data = single()
                data['lines'][0]['reference'][section][field] = value
                self.assert_blocked(data)
        data = single()
        data['lines'][0]['comparison_review']['reviewer_id'] = data['lines'][0]['analyst_id']
        self.assert_blocked(data, 'self-review')
        data = single()
        data['data_origin'] = 'public_observation'
        self.assert_blocked(data, 'source kind or placeholder URL')

    def test_ceiling_ratios_and_estimated_quantities_are_not_unit_observations(self):
        for field, value in (('price_measure', 'ceiling_divided_by_estimated_quantity'),
                             ('quantity_measure', 'estimated_annual_quantity')):
            data = single()
            data['lines'][0]['contract'][field] = value
            self.assert_blocked(data)
        data = single()
        data['lines'][0]['contract']['line_total'] = '112001'
        self.assert_blocked(data, 'line_total')

    def test_nonfinite_negative_zero_and_float_inputs_do_not_escape_controls(self):
        for value in ('NaN', 'Infinity', '-Infinity', '-1', '0', '1e3', 100.0):
            with self.subTest(reference=value):
                data = single()
                data['lines'][0]['reference']['unit_price'] = value
                self.assert_blocked(data)
        for value in ('-1', 'NaN'):
            data = single()
            data['lines'][0]['contract']['unit_price'] = value
            self.assert_blocked(data)
        data = single()
        data['lines'][0]['contract']['unit_price'] = '0'
        group = audit(data)['aggregates'][0]
        self.assertEqual(group['weighted_premium_against_reference_percent'], '-100.000000')
        self.assertIsNone(group['difference_as_percent_of_observed_value'])

    def test_documented_freight_adjustment_changes_the_denominator(self):
        data = single()
        row = data['lines'][0]
        row['reference']['terms']['freight'] = 'Freight excluded'
        self.assert_blocked(data, 'freight')
        row['reference']['adjustments'] = [{
            'term': 'freight', 'per_unit_amount': '10',
            'reviewer_id': row['comparison_review']['reviewer_id'],
            'source': copy.deepcopy(row['reference']['source']),
            'reason': 'Synthetic documented 10000 delivery charge allocated to 1000 units'}]
        result = audit(data)['lines'][0]
        self.assertEqual(result['adjusted_reference_unit_price'], '110')
        self.assertEqual(result['premium_against_reference_percent'], '1.818182')
        # An asserted adjustment without its independent documentation is blocked.
        row['reference']['adjustments'][0]['source'] = None
        self.assert_blocked(data, 'source provenance')

    def test_adjustment_duplicates_and_nonpositive_adjusted_reference_block(self):
        data = single()
        row = data['lines'][0]
        adjustment = {'term': 'freight', 'per_unit_amount': '-100',
                      'reviewer_id': row['comparison_review']['reviewer_id'],
                      'source': copy.deepcopy(row['reference']['source']),
                      'reason': 'Synthetic adjustment reducing the reference to zero'}
        row['reference']['adjustments'] = [adjustment]
        self.assert_blocked(data, 'greater than zero')
        adjustment['per_unit_amount'] = '1'
        row['reference']['adjustments'] = [adjustment, copy.deepcopy(adjustment)]
        self.assert_blocked(data, 'duplicate adjustment')

    def test_cash_requires_reconciliation_and_currencies_or_bases_never_merge(self):
        data = fixture()
        second = data['lines'][1]
        second['value_basis'] = 'paid_cash'
        second['contract']['price_measure'] = 'paid_unit_price'
        second['contract']['quantity_measure'] = 'paid_line_quantity'
        result = audit(data)
        self.assertEqual(result['eligible_lines'], 1)
        self.assertEqual(result['blocked_lines'], 1)
        self.assertFalse(result['coverage_complete_for_submitted_lines'])
        second['contract']['payment_evidence'] = copy.deepcopy(second['contract']['source'])
        second['contract']['payment_to_line_reconciled'] = True
        self.assertEqual(len(audit(data)['aggregates']), 2)
        data = fixture()
        data['lines'][1]['currency'] = 'USD'
        data['lines'][1]['reference']['currency'] = 'USD'
        self.assertEqual(len(audit(data)['aggregates']), 2)
        # Public-source type matters: relabeling an order cannot manufacture an invoice.
        data = single()
        data['data_origin'] = 'public_observation'
        row = data['lines'][0]
        for source, kind in ((row['contract']['source'], 'order_line'),
                             (row['reference']['source'], 'independent_quote'),
                             (row['reference']['independence']['evidence'], 'primary_official_registry')):
            source.update(url='https://example.org/test-evidence', source_kind=kind)
        row['value_basis'] = 'invoiced_value'
        row['contract'].update(price_measure='invoiced_unit_price', quantity_measure='invoiced_quantity')
        self.assert_blocked(data, 'source kind')
        row['contract']['source']['source_kind'] = 'invoice_line'
        self.assertEqual(audit(data)['eligible_lines'], 1)

    def test_actual_order_has_no_benchmark_and_assumed_markup_is_circular(self):
        actual = fixture('dla-current-no-qualified-benchmark')
        path = ROOT / actual['input_source']['path']
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), actual['input_source']['sha256'])
        self.assertEqual(actual['lines'][0]['contract']['line_total'], '824.46')
        self.assert_blocked(actual)
        data = single()
        data['lines'][0]['contract']['unit_price'] = '0.91'
        data['lines'][0]['reference']['unit_price'] = '0.8125'
        data['lines'][0]['reference']['price_measure'] = 'inferred_from_assumed_markup'
        self.assert_blocked(data, 'circular reference')
        data['lines'][0]['reference']['price_measure'] = 'offered_unit_price'
        data['lines'][0]['reference']['source']['source_kind'] = 'inferred_from_assumed_markup'
        self.assert_blocked(data, 'circular reference')


if __name__ == '__main__':
    unittest.main()
