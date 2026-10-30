#!/usr/bin/env python3
"""Exploratory repeated-premium screening of declared comparable purchases.

Calls the existing price-eligibility calculator first. Never authenticates
identities, predicts crime, or infers a buyer benefit from a price pattern.
"""
import argparse
from collections import defaultdict
from datetime import date
from decimal import Decimal, localcontext
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
CALCULATOR = ROOT / 'investigations/dla-bolt-trace-2026-10-30/price-controls/premium_audit.py'
spec = importlib.util.spec_from_file_location('price_agent_premium', CALCULATOR)
premium = importlib.util.module_from_spec(spec)
spec.loader.exec_module(premium)


class ScreenError(ValueError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def required(value, label):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ScreenError(label + ': require nonempty, trimmed text')
    if value.casefold() in {'unknown', 'null', 'none', 'tbd', 'unverified'}:
        raise ScreenError(label + ': unresolved grouping cannot establish repetition')
    return value


def integer(value, label, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ScreenError(label + ': outside supported integer bounds')
    return value


def screen(inputs, plan, metadata):
    if plan.get('schema_version') != '1.0' or metadata.get('schema_version') != '1.0':
        raise ScreenError('unsupported plan or metadata version')
    # A date supplied by the analyst cannot prove advance registration.
    if plan.get('design_status') != 'exploratory_retrospective':
        raise ScreenError('This version supports explicitly exploratory screening only')
    required(plan.get('plan_id'), 'plan_id')
    required(plan.get('analysis_scope'), 'analysis_scope')
    if plan.get('scope_kind') not in {'declared_sample', 'declared_complete_cohort'}:
        raise ScreenError('scope_kind must state sample or declared cohort')
    start, end = date.fromisoformat(plan['period_start']), date.fromisoformat(plan['period_end'])
    if start > end:
        raise ScreenError('reversed analysis period')
    target = premium.decimal(plan['target_percent'], 'target_percent')
    tolerance = premium.decimal(plan['tolerance_percentage_points'], 'tolerance', True)
    if not 0 < target <= 1000 or not tolerance < target:
        raise ScreenError('target/tolerance require a positive premium band')
    fraction = premium.decimal(plan['minimum_in_band_fraction'], 'minimum fraction', True)
    max_blocked = premium.decimal(plan['maximum_blocked_fraction'], 'maximum blocked fraction')
    if not 0 < fraction <= 1 or not 0 <= max_blocked <= 1:
        raise ScreenError('fractions must lie in [0,1], with positive minimum')
    mins = {key: integer(plan[key], key, low, 10000) for key, low in (
        ('minimum_solicitations', 3), ('minimum_months', 2), ('minimum_benchmark_families', 2))}
    if metadata.get('input_canonical_sha256') != digest(inputs) or metadata.get('plan_canonical_sha256') != digest(plan):
        raise ScreenError('metadata does not bind the exact input and plan')
    if metadata.get('data_origin') != inputs.get('data_origin'):
        raise ScreenError('synthetic/public origin mismatch')
    if len(inputs.get('lines', [])) > 10000:
        raise ScreenError('batch exceeds 10000 submitted lines')
    calculated = premium.audit(inputs)
    line_ids = {r['line_id'] for r in calculated['lines']}
    rows = metadata.get('lines')
    if not isinstance(rows, list) or len(rows) != len(line_ids):
        raise ScreenError('metadata must cover every submitted line exactly once')
    by_id = {}
    for row in rows:
        ident = required(row.get('line_id'), 'line_id')
        if ident in by_id or ident not in line_ids:
            raise ScreenError('duplicate or unknown metadata line')
        for key in ('supplier_identifier', 'purchasing_office_identifier', 'item_stratum'):
            required(row.get(key), key)
        by_id[ident] = row
    raw_by_id = {r['line_id']: r for r in inputs['lines']}
    groups = defaultdict(list)
    for row in calculated['lines']:
        m = by_id[row['line_id']]
        raw = raw_by_id[row['line_id']]
        currency = raw.get('currency')
        if not isinstance(currency, str) or not re.fullmatch('[A-Z]{3}', currency):
            currency = 'UNVERIFIED_CURRENCY'
        basis = raw.get('value_basis')
        if basis not in {'ordered_value', 'invoiced_value', 'paid_cash'}:
            basis = 'UNVERIFIED_BASIS'
        grouping = tuple(m[k] for k in ('supplier_identifier', 'purchasing_office_identifier', 'item_stratum'))
        groups[grouping + (currency, basis)].append((row, m))
    results = []
    with localcontext() as ctx:
        ctx.prec = 100
        for grouping, members in sorted(groups.items()):
            eligible = [(r, m) for r, m in members if r['status'] == 'eligible_as_declared']
            blocked = [r['line_id'] for r, _ in members if r['status'] != 'eligible_as_declared']
            in_band, details = [], []
            reference = observed = Decimal(0)
            in_band_reference = Decimal(0)
            for row, m in eligible:
                for key in ('solicitation_identifier', 'benchmark_family', 'grouping_review_id'):
                    required(m.get(key), key)
                raw = raw_by_id[row['line_id']]
                price_day = date.fromisoformat(raw['contract']['terms']['price_date'])
                if not start <= price_day <= end:
                    raise ScreenError('eligible line outside declared analysis period')
                # No reading rounded displayed rates to decide band membership.
                ref = Decimal(row['reference_basis_exact'])
                obs = Decimal(row['observed_basis_exact'])
                delta = obs - ref
                reference += ref
                observed += obs
                match = (target - tolerance) * ref <= delta * 100 <= (target + tolerance) * ref
                detail = {'line_id': row['line_id'], 'signed_difference_exact': format(delta, 'f'),
                          'rate_percent_display': premium.amount(delta / ref * 100, 9),
                          'in_band': match, 'price_date': price_day.isoformat(),
                          'solicitation_identifier': m['solicitation_identifier'],
                          'benchmark_family': m['benchmark_family'],
                          'grouping_review_id_as_declared': m['grouping_review_id']}
                details.append(detail)
                if match:
                    in_band.append(detail)
                    in_band_reference += ref
            distinct = {'solicitations': len({r['solicitation_identifier'].casefold() for r in in_band}),
                        'months': len({r['price_date'][:7] for r in in_band}),
                        'benchmark_families': len({r['benchmark_family'].casefold() for r in in_band})}
            gaps = []
            if not eligible:
                gaps.append('no qualified comparison as declared')
            if Decimal(len(blocked)) / len(members) > max_blocked:
                gaps.append('blocked-line fraction exceeds plan limit')
            for key in ('solicitations', 'months', 'benchmark_families'):
                if distinct[key] < mins['minimum_' + key]:
                    gaps.append('insufficient distinct in-band ' + key)
            fraction_pass = bool(eligible) and Decimal(len(in_band)) / len(eligible) >= fraction
            if eligible and not fraction_pass:
                gaps.append('in-band line fraction below plan threshold')
            results.append({
                'supplier_identifier_as_declared': grouping[0],
                'purchasing_office_identifier_as_declared': grouping[1],
                'item_stratum_as_declared': grouping[2], 'currency': grouping[3], 'value_basis': grouping[4],
                'submitted_lines': len(members), 'eligible_lines': len(eligible), 'blocked_line_ids': blocked,
                'in_band_lines': len(in_band), 'distinct_in_band_as_declared': distinct,
                'screen_status': 'candidate_pattern_for_review' if not gaps else 'insufficient_pattern_support',
                'reasons': gaps, 'line_details': details,
                'reference_value_exact': format(reference, 'f') if eligible else None,
                'observed_value_exact': format(observed, 'f') if eligible else None,
                'signed_difference_exact': format(observed-reference, 'f') if eligible else None,
                'net_difference_positive': observed > reference if eligible else None,
                'in_band_reference_value_exact': format(in_band_reference, 'f') if eligible else None,
                'in_band_reference_share_percent_display': premium.amount(in_band_reference/reference*100, 9) if eligible else None,
                'weighted_premium_percent_display': premium.amount((observed-reference)/reference*100, 9) if eligible else None,
                'fraud_probability': None, 'buyer_benefit': None, 'recoverable_loss': None,
                'coverage_basis': 'Line counts for submitted group; blocked value and nationwide coverage are not established',
            })
    return {'schema_version': '1.0', 'data_origin': calculated['data_origin'],
            'evidence_kind': calculated['evidence_kind'], 'dataset_scope': calculated['dataset_scope'],
            'design_status': 'exploratory_retrospective', 'plan': plan,
            'input_canonical_sha256': digest(inputs), 'plan_canonical_sha256': digest(plan),
            'metadata_canonical_sha256': digest(metadata),
            'calculator_sha256': hashlib.sha256(CALCULATOR.read_bytes()).hexdigest(),
            'groups': results,
            'limitations': [
                'Labels, independence, scope completeness and comparison review are supplied declarations, not authenticated by this tool.',
                'No automatic supplier ranking, accusation, publication, payment inference or personal-benefit conclusion.',
                'Repeated target-band rates are an exploratory lead, not a causal or statistical significance test.',
                'A repeated line-count pattern can coexist with a negative aggregate difference; it does not establish overall overpayment.',
                'Negative differences and all eligible lines remain in weighted totals; multiple lines of one solicitation do not count as separate solicitations.',
                'A supplied plan date does not establish preregistration. Preserve this plan before a future held-out acquisition for prospective testing.',
            ]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('plan', type=Path)
    parser.add_argument('metadata', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        output = screen(*(json.loads(p.read_text()) for p in (args.input, args.plan, args.metadata)))
        body = json.dumps(output, indent=2, ensure_ascii=False, allow_nan=False) + '\n'
        if args.output:
            with args.output.open('x') as f:
                f.write(body)
        else:
            print(body, end='')
    except (ScreenError, premium.EvidenceError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, 'Blocked: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
