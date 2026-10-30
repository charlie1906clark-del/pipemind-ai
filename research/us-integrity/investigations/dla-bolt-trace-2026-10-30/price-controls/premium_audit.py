#!/usr/bin/env python3
"""Offline price comparisons, not a misconduct detector. Standard library only."""
from __future__ import annotations

import argparse
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


TERMS = (
    'item_identifier', 'revision', 'unit_of_issue', 'pack_size', 'quantity',
    'price_date', 'delivery', 'condition', 'quality', 'traceability', 'freight',
    'warranty', 'included_scope',
)
ADJUSTABLE = {'quantity', 'price_date', 'delivery', 'freight', 'warranty', 'included_scope'}
BASES = {'ordered_value': 'ordered_unit_price',
         'invoiced_value': 'invoiced_unit_price', 'paid_cash': 'paid_unit_price'}
CONTRACT_KINDS = {'ordered_value': {'agency_award_line', 'order_line'},
                  'invoiced_value': {'invoice_line'},
                  'paid_cash': {'invoice_line', 'payment_record'}}
REFERENCE_KINDS = {'manufacturer_listing', 'distributor_listing', 'agency_award_line',
                   'independent_quote', 'supplier_invoice', 'catalog_reference'}
UNKNOWN_TERMS = {'unknown', 'unverified', 'unresolved', 'not known', 'not stated',
                 'not_verified', 'not_known', 'not_provided', 'tbd', 'n/a', 'none', 'null'}
DECIMAL = re.compile(r'-?(?:0|[1-9][0-9]{0,17})(?:\.[0-9]{1,12})?\Z')


class EvidenceError(ValueError):
    pass


def decimal(value, name, positive=False):
    if not isinstance(value, str) or not DECIMAL.fullmatch(value):
        raise EvidenceError(name + ': require a finite plain decimal string, max 18 integer/12 fraction digits')
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise EvidenceError(name + ': invalid decimal') from exc
    if not result.is_finite() or (positive and result <= 0):
        raise EvidenceError(name + ': must be finite and greater than zero')
    return result


def text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise EvidenceError(name + ': missing nonempty text')
    return value


def day(value, name):
    try:
        return date.fromisoformat(text(value, name))
    except ValueError as exc:
        raise EvidenceError(name + ': invalid ISO date') from exc


def source(value, name, origin, kinds):
    if not isinstance(value, dict):
        raise EvidenceError(name + ': missing source provenance')
    for field in ('source_id', 'url', 'locator', 'scope', 'source_kind'):
        text(value.get(field), name + '.' + field)
    try:
        parsed = urlsplit(value['url'])
    except ValueError as exc:
        raise EvidenceError(name + ': invalid source URL') from exc
    if parsed.scheme not in {'http', 'https'} or not parsed.hostname or parsed.username or parsed.password:
        raise EvidenceError(name + ': require a source HTTP(S) URL')
    day(value.get('observed_on'), name + '.observed_on')
    if origin == 'illustrative':
        if value['source_kind'] != 'illustrative':
            raise EvidenceError(name + ': synthetic input must be labeled illustrative')
    elif value['source_kind'] not in kinds or parsed.hostname.endswith('.invalid'):
        raise EvidenceError(name + ': unsupported real-evidence source kind or placeholder URL')


def terms(value, name):
    if not isinstance(value, dict):
        raise EvidenceError(name + ': missing comparison terms')
    for field in TERMS:
        text(value.get(field), name + '.' + field)
        if value[field].strip().lower() in UNKNOWN_TERMS:
            raise EvidenceError(name + '.' + field + ': unresolved term cannot establish equivalence')
    for field in ('pack_size', 'quantity'):
        decimal(value[field], name + '.' + field, positive=True)
    day(value['price_date'], name + '.price_date')
    return value


def same_term(key, left, right):
    if key in {'pack_size', 'quantity'}:
        return decimal(left, key, True) == decimal(right, key, True)
    return left == right


def canonical_key(line):
    # Namespace is explicit: no merging by supplier name or similar award strings.
    fields = ('agency_code', 'piid', 'order_id', 'clin')
    value = line.get('key')
    if not isinstance(value, dict):
        raise EvidenceError('missing award/order/CLIN identity')
    parts = []
    for field in fields:
        raw = text(value.get(field), 'key.' + field)
        if raw != raw.strip():
            raise EvidenceError('key fields may not contain surrounding whitespace')
        parts.append(raw.upper())
    return tuple(parts)


def amount(value, places=2):
    with localcontext() as ctx:
        ctx.prec = 80
        return format(value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP), 'f')


def exact(value):
    return format(value, 'f')


def check_line(line, origin):
    basis = line.get('value_basis')
    if basis not in BASES:
        raise EvidenceError('value_basis: only ordered_value, invoiced_value or paid_cash')
    contract = line.get('contract')
    if not isinstance(contract, dict):
        raise EvidenceError('missing contract evidence')
    if contract.get('price_measure') != BASES[basis]:
        raise EvidenceError('contract price measure does not match declared value basis; ceilings prohibited')
    if contract.get('quantity_measure') != {
        'ordered_value': 'ordered_quantity', 'invoiced_value': 'invoiced_quantity',
        'paid_cash': 'paid_line_quantity'}[basis]:
        raise EvidenceError('quantity measure does not match value basis; estimates prohibited')
    qty = decimal(line.get('quantity'), 'quantity', True)
    unit = decimal(contract.get('unit_price'), 'contract.unit_price')
    if unit < 0:
        raise EvidenceError('contract.unit_price: negative price unsupported')
    if not re.fullmatch(r'[A-Z]{3}', str(line.get('currency', ''))):
        raise EvidenceError('currency: require one explicit three-letter code')
    source(contract.get('source'), 'contract.source', origin, CONTRACT_KINDS[basis])
    ct = terms(contract.get('terms'), 'contract.terms')
    if decimal(ct['quantity'], 'contract.terms.quantity', True) != qty:
        raise EvidenceError('contract term quantity differs from line quantity')
    if basis == 'paid_cash':
        payment = contract.get('payment_evidence')
        source(payment, 'contract.payment_evidence', origin, {'payment_record'})
        if contract.get('payment_to_line_reconciled') is not True:
            raise EvidenceError('paid_cash requires a documented line-level payment reconciliation')
    if contract.get('line_total') is not None:
        total = decimal(contract['line_total'], 'contract.line_total')
        if total != qty * unit:
            raise EvidenceError('line_total does not equal quantity × unit price')
    reference = line.get('reference')
    if not isinstance(reference, dict):
        raise EvidenceError('No qualified reference supplied; recorded contract price alone is not a fairness test')
    if reference.get('currency') != line['currency']:
        raise EvidenceError('currency mismatch: no automatic foreign-exchange conversion')
    ref_unit = decimal(reference.get('unit_price'), 'reference.unit_price', True)
    if (reference.get('price_measure') == 'inferred_from_assumed_markup' or
            (isinstance(reference.get('source'), dict) and
             reference['source'].get('source_kind') == 'inferred_from_assumed_markup')):
        raise EvidenceError('circular reference inferred from an assumed markup cannot establish a premium')
    if reference.get('price_measure') not in {'offered_unit_price', 'awarded_unit_price', 'catalog_unit_price', 'invoice_unit_price'}:
        raise EvidenceError('reference must be an actual unit/reference-unit price, not a ceiling ratio')
    source(reference.get('source'), 'reference.source', origin, REFERENCE_KINDS)
    if reference.get('availability_for_quantity') != 'confirmed':
        raise EvidenceError('reference availability for the tested quantity is not confirmed')
    rt = terms(reference.get('terms'), 'reference.terms')
    independence = reference.get('independence')
    if not isinstance(independence, dict) or independence.get('status') != 'reviewed_independent':
        raise EvidenceError('reference independence remains unverified')
    if independence.get('claimant_independence_status') != 'reviewed_independent':
        raise EvidenceError('claimant independence from the price-setting parties remains unverified')
    source(independence.get('evidence'), 'reference.independence.evidence', origin,
           REFERENCE_KINDS | {'primary_corporate_filing', 'primary_official_registry'})
    review = line.get('comparison_review')
    if not isinstance(review, dict) or review.get('decision') != 'comparable':
        raise EvidenceError('independent comparison review has not approved equivalence')
    analyst = text(line.get('analyst_id'), 'analyst_id')
    reviewer = text(review.get('reviewer_id'), 'comparison_review.reviewer_id')
    if analyst.strip().casefold() == reviewer.strip().casefold():
        raise EvidenceError('comparison self-review is not independent')
    day(review.get('reviewed_on'), 'comparison_review.reviewed_on')
    text(review.get('evidence_note'), 'comparison_review.evidence_note')
    adjustments = reference.get('adjustments', [])
    if not isinstance(adjustments, list):
        raise EvidenceError('reference.adjustments must be a list')
    mapped = {}
    for adjustment in adjustments:
        if not isinstance(adjustment, dict):
            raise EvidenceError('adjustment must be an evidence object')
        field = adjustment.get('term')
        if field not in ADJUSTABLE or field in mapped:
            raise EvidenceError('unsupported or duplicate adjustment term')
        if adjustment.get('reviewer_id') != reviewer:
            raise EvidenceError('adjustment has not been checked by the separate reviewer')
        source(adjustment.get('source'), 'adjustment.source', origin, REFERENCE_KINDS)
        text(adjustment.get('reason'), 'adjustment.reason')
        mapped[field] = decimal(adjustment.get('per_unit_amount'), 'adjustment.per_unit_amount')
    for field in TERMS:
        if not same_term(field, ct[field], rt[field]) and field not in mapped:
            raise EvidenceError('unresolved term mismatch: ' + field)
    adjusted = ref_unit + sum(mapped.values(), Decimal(0))
    if adjusted <= 0:
        raise EvidenceError('adjusted reference price must be greater than zero')
    baseline = qty * adjusted
    actual = qty * unit
    diff = actual - baseline
    return {'line_id': line['line_id'], 'status': 'eligible_as_declared',
            'data_origin': origin, 'key': line['key'], 'currency': line['currency'],
            'value_basis': basis, 'quantity': exact(qty),
            'contract_unit_price': exact(unit), 'raw_reference_unit_price': exact(ref_unit),
            'reference_adjustment_per_unit': exact(sum(mapped.values(), Decimal(0))),
            'adjusted_reference_unit_price': exact(adjusted),
            'reference_basis_exact': exact(baseline), 'observed_basis_exact': exact(actual),
            'difference_exact': exact(diff), 'difference_rounded': amount(diff),
            'premium_against_reference_percent': amount(diff / baseline * 100, 6),
            'difference_as_percent_of_observed_value': None if actual == 0 else amount(diff / actual * 100, 6),
            'source_ids': [contract['source']['source_id'], reference['source']['source_id']],
            'reference_kind': reference['source']['source_kind'],
            'reviewer_id_as_declared': reviewer}


def audit(payload):
    if not isinstance(payload, dict):
        raise EvidenceError('input must be a JSON object')
    if payload.get('schema_version') != '1.0':
        raise EvidenceError('unsupported schema version')
    origin = payload.get('data_origin')
    if origin not in {'public_observation', 'illustrative'}:
        raise EvidenceError('data_origin must explicitly distinguish public evidence from illustration')
    evidence_kind = text(payload.get('evidence_kind'), 'evidence_kind')
    dataset_scope = text(payload.get('dataset_scope'), 'dataset_scope')
    records = payload.get('lines')
    if not isinstance(records, list) or not records:
        raise EvidenceError('nonempty lines list required')
    if len(records) > 10000:
        raise EvidenceError('finite offline batch limit: 10000 lines')
    seen_keys, seen_ids, results = set(), set(), []
    with localcontext() as context:
        # Products need up to 60 digits; summing 10000 bounded lines needs more.
        context.prec = 80
        for line in records:
            if not isinstance(line, dict):
                raise EvidenceError('each line must be an evidence object')
            ident = text(line.get('line_id'), 'line_id')
            key = canonical_key(line)
            if key in seen_keys or ident in seen_ids:
                raise EvidenceError('duplicate award/order/CLIN or line_id; reconcile modifications before summing')
            seen_keys.add(key)
            seen_ids.add(ident)
            try:
                results.append(check_line(line, origin))
            except EvidenceError as exc:
                results.append({'line_id': ident, 'key': line['key'], 'status': 'blocked',
                                'data_origin': origin, 'reason': str(exc),
                                'reference_status': 'not_supplied' if line.get('reference') is None else 'not_qualified',
                                'adjusted_reference_unit_price': None,
                                'premium_against_reference_percent': None,
                                'difference_exact': None})
        groups = {}
        for row in results:
            if row['status'] != 'eligible_as_declared':
                continue
            key = (row['currency'], row['value_basis'])
            group = groups.setdefault(key, {'reference': Decimal(0), 'observed': Decimal(0), 'line_ids': [], 'rates': []})
            group['reference'] += Decimal(row['reference_basis_exact'])
            group['observed'] += Decimal(row['observed_basis_exact'])
            group['line_ids'].append(row['line_id'])
            group['rates'].append(Decimal(row['difference_exact']) / Decimal(row['reference_basis_exact']))
        aggregates = []
        for (currency, basis), group in sorted(groups.items()):
            ref, observed = group['reference'], group['observed']
            difference = observed - ref
            aggregates.append({'currency': currency, 'value_basis': basis,
                               'eligible_line_ids': group['line_ids'],
                               'reference_basis_exact': exact(ref), 'observed_basis_exact': exact(observed),
                               'difference_exact': exact(difference), 'difference_rounded': amount(difference),
                               'weighted_premium_against_reference_percent': amount(difference / ref * 100, 6),
                               'difference_as_percent_of_observed_value': None if observed == 0 else amount(difference / observed * 100, 6),
                               'minimum_line_premium_percent': amount(min(group['rates']) * 100, 6),
                               'maximum_line_premium_percent': amount(max(group['rates']) * 100, 6)})
    return {'schema_version': '1.0', 'data_origin': origin,
            'evidence_kind': evidence_kind, 'dataset_scope': dataset_scope,
            'submitted_lines': len(records), 'lines': results,
            'eligible_lines': sum(r['status'] == 'eligible_as_declared' for r in results),
            'blocked_lines': sum(r['status'] == 'blocked' for r in results),
            'coverage_complete_for_submitted_lines': not any(r['status'] == 'blocked' for r in results),
            'aggregates': aggregates,
            'interpretation': 'Differences against supplied reviewed references, not a misconduct or recoverability finding.',
            'authentication_limit': 'This calculator validates declared fields and arithmetic. It cannot authenticate sources, reviewer identity, availability, independence, payments or concealed benefits. Inspect the underlying evidence.',
            'rounding': 'Decimal precision 80; totals aggregate unrounded values; display uses half-up 2 decimal amounts and 6 decimal percentage points. No FX or automatic unit conversion.'}


def annual_illustration():
    with localcontext() as context:
        context.prec = 80
        extra, rate = Decimal('100000'), Decimal('0.12')
        baseline = extra / rate
        gross = baseline + extra
        return {'schema_version': '1.0', 'data_origin': 'illustrative_user_scenario',
                'evidence_kind': 'synthetic_calibration',
                'dataset_scope': 'Algebraic illustration of the user-described 12% and 100000 example; no actual transaction evidence',
                'currency': 'unspecified',
                'assumptions': ['100000 is the total price increment, not gross annual purchasing',
                                '12% is a uniform markup on the comparable underlying cost',
                                'No legitimate extra costs or tax differences are modeled',
                                'No government transaction or personal benefit is established'],
                'increment': '100000.00', 'markup_against_reference_percent': '12.000000',
                'implied_reference_annual_cost_rounded': amount(baseline),
                'implied_gross_annual_value_rounded': amount(gross),
                'increment_as_percent_of_gross': amount(extra / gross * 100, 6),
                'rounding_note': 'Exact underlying divisions repeat; monetary illustrations are rounded to 2 places only.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=Path)
    parser.add_argument('--annual-illustration', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if bool(args.input) == args.annual_illustration:
        parser.error('Choose one input JSON or --annual-illustration')
    try:
        if args.annual_illustration:
            result = annual_illustration()
        else:
            raw = args.input.read_bytes()
            result = audit(json.loads(raw))
            result['input_snapshot'] = {'file_name': args.input.name,
                                        'sha256': hashlib.sha256(raw).hexdigest()}
    except (EvidenceError, json.JSONDecodeError) as exc:
        parser.exit(2, str(exc) + '\n')
    body = json.dumps(result, indent=2, allow_nan=False) + '\n'
    if args.output:
        with args.output.open('x') as handle:
            handle.write(body)
    else:
        print(body, end='')


if __name__ == '__main__':
    main()
