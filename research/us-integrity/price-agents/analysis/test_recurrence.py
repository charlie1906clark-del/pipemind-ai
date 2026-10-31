import copy
import json
from pathlib import Path
import unittest

import recurrence as r


def fixtures():
    prior = r.ROOT / 'investigations/dla-bolt-trace-2026-10-30/price-controls/scenarios/uniform-12-percent.json'
    example = json.loads(prior.read_text())
    example['dataset_scope'] = 'Four synthetic purchases; no real government transaction'
    lines, metadata = [], []
    for i in range(4):
        line = copy.deepcopy(example['lines'][0])
        ident = 'SYN-' + str(i)
        line['line_id'] = ident
        line['key']['piid'] = ident
        line['quantity'] = '1'
        for side in ('contract', 'reference'):
            line[side]['terms']['quantity'] = '1'
            line[side]['terms']['price_date'] = f'2026-0{6+i}-01'
            line[side]['source']['source_id'] = side + ident
        lines.append(line)
        metadata.append({'line_id': ident, 'supplier_identifier': 'ILL-SUPPLIER',
                         'purchasing_office_identifier': 'ILL-OFFICE', 'item_stratum': 'ILL-MATCHED-ITEM',
                         'solicitation_identifier': 'ILL-SOL-' + str(i),
                         'benchmark_family': 'ILL-FAMILY-' + str(i % 2), 'grouping_review_id': 'ILL-REVIEW'})
    example['lines'] = lines
    plan = {'schema_version': '1.0', 'plan_id': 'ILL-REPEATED-PREMIUM-001',
            'design_status': 'exploratory_retrospective', 'analysis_scope': 'Four invented purchases',
            'scope_kind': 'declared_sample', 'period_start': '2026-01-01', 'period_end': '2026-10-30',
            'target_percent': '12', 'tolerance_percentage_points': '1',
            'minimum_in_band_fraction': '0.75', 'maximum_blocked_fraction': '0.25',
            'minimum_solicitations': 3, 'minimum_months': 2, 'minimum_benchmark_families': 2}
    meta = {'schema_version': '1.0', 'data_origin': 'illustrative', 'lines': metadata}
    bind(example, plan, meta)
    return example, plan, meta


def bind(x, p, m):
    m['input_canonical_sha256'] = r.digest(x)
    m['plan_canonical_sha256'] = r.digest(p)


class RepeatedPremiumTests(unittest.TestCase):
    def test_uniform_pattern_and_no_fraud_claim(self):
        out = r.screen(*fixtures())
        group = out['groups'][0]
        self.assertEqual(group['screen_status'], 'candidate_pattern_for_review')
        self.assertEqual(group['signed_difference_exact'], '48')
        self.assertEqual(group['weighted_premium_percent_display'], '12.000000000')
        self.assertIsNone(group['buyer_benefit'])
        self.assertIsNone(group['fraud_probability'])
        self.assertEqual(out['data_origin'], 'illustrative')

    def test_negative_lines_remain_in_weighted_total(self):
        x, p, m = fixtures(); x['lines'][3]['contract']['unit_price'] = '90'; bind(x, p, m)
        group = r.screen(x, p, m)['groups'][0]
        self.assertEqual(group['in_band_lines'], 3)
        self.assertEqual(group['signed_difference_exact'], '26')
        self.assertEqual(group['weighted_premium_percent_display'], '6.500000000')

    def test_repeated_clins_do_not_create_independent_solicitations(self):
        x, p, m = fixtures()
        for line in m['lines']: line['solicitation_identifier'] = 'ONE-SOLICITATION'
        group = r.screen(x, p, m)['groups'][0]
        self.assertEqual(group['distinct_in_band_as_declared']['solicitations'], 1)
        self.assertEqual(group['screen_status'], 'insufficient_pattern_support')

    def test_shared_benchmark_and_one_month_do_not_suffice(self):
        x, p, m = fixtures()
        for raw, meta in zip(x['lines'], m['lines']):
            meta['benchmark_family'] = 'SHARED-UPSTREAM'
            for side in ('contract', 'reference'): raw[side]['terms']['price_date'] = '2026-06-01'
        bind(x, p, m); group = r.screen(x, p, m)['groups'][0]
        self.assertEqual(group['distinct_in_band_as_declared']['months'], 1)
        self.assertEqual(group['distinct_in_band_as_declared']['benchmark_families'], 1)
        self.assertEqual(group['screen_status'], 'insufficient_pattern_support')

    def test_rounded_boundary_cannot_force_band_membership(self):
        x, p, m = fixtures(); p['minimum_in_band_fraction'] = '1'
        x['lines'][0]['contract']['unit_price'] = '113.000000000001'; bind(x, p, m)
        group = r.screen(x, p, m)['groups'][0]
        self.assertFalse(group['line_details'][0]['in_band'])
        self.assertEqual(group['screen_status'], 'insufficient_pattern_support')

    def test_blocked_coverage_is_visible_and_limits_screen(self):
        x, p, m = fixtures()
        for line in x['lines'][:2]: line['reference'] = None
        bind(x, p, m); group = r.screen(x, p, m)['groups'][0]
        self.assertEqual(group['blocked_line_ids'], ['SYN-0', 'SYN-1'])
        self.assertIn('blocked-line fraction exceeds plan limit', group['reasons'])

    def test_circular_benchmark_never_qualifies(self):
        x, p, m = fixtures()
        for line in x['lines']:
            line['reference']['price_measure'] = 'inferred_from_assumed_markup'
        bind(x, p, m); group = r.screen(x, p, m)['groups'][0]
        self.assertEqual(group['eligible_lines'], 0)
        self.assertIsNone(group['signed_difference_exact'])

    def test_duplicate_transaction_is_rejected(self):
        x, p, m = fixtures(); x['lines'][1]['key'] = copy.deepcopy(x['lines'][0]['key']); bind(x, p, m)
        with self.assertRaises(r.premium.EvidenceError): r.screen(x, p, m)

    def test_metadata_must_cover_bound_input_and_plan(self):
        x, p, m = fixtures(); p['target_percent'] = '15'
        with self.assertRaises(r.ScreenError): r.screen(x, p, m)
        x, p, m = fixtures(); m['lines'].pop()
        with self.assertRaises(r.ScreenError): r.screen(x, p, m)

    def test_origins_and_preregistration_cannot_be_relabelled(self):
        x, p, m = fixtures(); m['data_origin'] = 'public_observation'
        with self.assertRaises(r.ScreenError): r.screen(x, p, m)
        x, p, m = fixtures(); p['design_status'] = 'preregistered'; bind(x, p, m)
        with self.assertRaises(r.ScreenError): r.screen(x, p, m)

    def test_dates_and_threshold_bounds(self):
        x, p, m = fixtures(); p['period_end'] = '2026-06-30'; bind(x, p, m)
        with self.assertRaises(r.ScreenError): r.screen(x, p, m)
        for value in ('NaN', 'Infinity', '-1', '1.1'):
            x, p, m = fixtures(); p['minimum_in_band_fraction'] = value; bind(x, p, m)
            with self.assertRaises((r.ScreenError, r.premium.EvidenceError)): r.screen(x, p, m)

    def test_currency_and_office_are_separate_groups(self):
        x, p, m = fixtures(); m['lines'][0]['purchasing_office_identifier'] = 'OTHER-OFFICE'
        group = r.screen(x, p, m)['groups']
        self.assertEqual(len(group), 2)
        self.assertEqual(sum(g['submitted_lines'] for g in group), 4)


if __name__ == '__main__':
    unittest.main()
