#!/usr/bin/env python3
"""Parse an explicitly supplied PUB LOG export; never authenticate or infer equivalence."""
from __future__ import annotations

import argparse
import csv
from datetime import date
import hashlib
import io
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, unquote, urlsplit

CHAR_FIELDS = ('NIIN', 'MRC', 'REQUIREMENTS_STATEMENT', 'CLEAR_TEXT_REPLY')
REF_FIELDS = ('NIIN', 'PART_NUMBER', 'CAGE_CODE', 'CAGE_STATUS', 'RNCC', 'RNVC',
              'DAC', 'RNAAC', 'RNFC', 'RNSC', 'RNJC', 'SADC', 'HCC', 'MSDS', 'MEDALS')
SCHEMAS = {'characteristics': CHAR_FIELDS, 'reference': REF_FIELDS}
MAX_BYTES = 50_000_000
MAX_ROWS = 250_000


class ExportError(ValueError):
    pass


def require_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ExportError(field + ': nonempty text required')
    return value


def iso_day(value, field):
    try:
        return date.fromisoformat(require_text(value, field))
    except ValueError as exc:
        raise ExportError(field + ': ISO date required') from exc


def public_receipt_url(value):
    """Reject secrets before preserving a URL in a public receipt; never fetch it."""
    original = require_text(value, 'source_url')
    decoded = original
    for _ in range(8):
        if any(c.isspace() or ord(c) < 32 or ord(c) == 127 or c == '\\' for c in decoded):
            raise ExportError('source URL contains disallowed whitespace, controls or backslash')
        try:
            parsed = urlsplit(decoded)
            # Empty userinfo is still userinfo; truthiness would miss https://@host/.
            if (parsed.scheme != 'https' or not parsed.hostname or
                    parsed.username is not None or parsed.password is not None or parsed.fragment):
                raise ExportError('source URL must be HTTPS without userinfo or fragment')
            for key, _value in parse_qsl(parsed.query, keep_blank_values=True):
                normalized = re.sub(r'[^a-z0-9]', '', key.casefold())
                if (any(word in normalized for word in ('token', 'password', 'passwd', 'secret',
                        'credential', 'signature', 'session', 'authorization', 'apikey', 'accesskey')) or
                        normalized in {'auth', 'key', 'sig', 'sid', 'code', 'jwt'} or
                        normalized.startswith(('xamz', 'xgoog'))):
                    raise ExportError('source URL contains a sensitive query key')
        except ValueError as exc:
            if isinstance(exc, ExportError):
                raise
            raise ExportError('invalid source URL') from exc
        try:
            next_decoded = unquote(decoded, errors='strict')
        except UnicodeError as exc:
            raise ExportError('source URL has invalid encoded text') from exc
        if next_decoded == decoded:
            return urlsplit(original)
        decoded = next_decoded
    raise ExportError('source URL uses excessive nested encoding')


def validate_receipt(receipt, raw, table):
    if not isinstance(receipt, dict):
        raise ExportError('receipt object required')
    for name in ('source_id', 'release_label', 'retrieval_method', 'export_query', 'source_scope'):
        require_text(receipt.get(name), name)
    if receipt.get('table') != table:
        raise ExportError('receipt table does not match parser mode')
    retrieved = iso_day(receipt.get('retrieved_on'), 'retrieved_on')
    released = iso_day(receipt.get('release_date'), 'release_date')
    if released > retrieved:
        raise ExportError('release date is later than retrieval')
    if receipt.get('scope') not in {'selected_export', 'full_table'}:
        raise ExportError('scope must be selected_export or full_table')
    if receipt.get('origin') not in {'public_observation', 'synthetic'}:
        raise ExportError('origin must be public_observation or synthetic')
    url = public_receipt_url(receipt.get('source_url'))
    host = url.hostname.lower()
    if receipt['origin'] == 'public_observation':
        if not (host == 'dla.mil' or host.endswith('.dla.mil') or
                host == 'publogstorage.blob.core.windows.net'):
            raise ExportError('public observation requires the stated official DLA source route')
        if receipt.get('source_kind') not in {'official_publog_csv', 'official_publog_decomp_export'}:
            raise ExportError('unsupported real source kind')
    elif not host.endswith('.invalid') or receipt.get('source_kind') != 'synthetic_fixture':
        raise ExportError('synthetic data requires a reserved .invalid URL and fixture label')
    expected = receipt.get('file_sha256')
    if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
        raise ExportError('file_sha256 must be a lowercase SHA256 digest')
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ExportError('export bytes do not match the supplied receipt')
    return receipt


def parse_export(raw, receipt, table, niin, delimiter=',', max_rows=MAX_ROWS):
    if table not in SCHEMAS:
        raise ExportError('unknown table')
    if not isinstance(niin, str) or not re.fullmatch(r'[0-9]{9}', niin):
        raise ExportError('NIIN must retain exactly nine decimal digits, including leading zeroes')
    if delimiter not in {',', '|'}:
        raise ExportError('only explicit comma or pipe delimiters are supported')
    if not isinstance(max_rows, int) or isinstance(max_rows, bool) or not 1 <= max_rows <= MAX_ROWS:
        raise ExportError('invalid row budget')
    if not isinstance(raw, bytes) or len(raw) > MAX_BYTES:
        raise ExportError('input must be bytes within the 50 MB selected-export limit')
    validate_receipt(receipt, raw, table)
    try:
        stream = io.StringIO(raw.decode('utf-8-sig'), newline='')
    except UnicodeDecodeError as exc:
        raise ExportError('UTF-8 text required; native .TAB files are not CSV exports') from exc
    reader = csv.reader(stream, delimiter=delimiter, strict=True)
    try:
        headers = next(reader)
    except (StopIteration, csv.Error) as exc:
        raise ExportError('header row required') from exc
    # Header normalization only; source values are never trimmed, decoded, or filled.
    headers = [h.strip().upper() for h in headers]
    if len(headers) != len(set(headers)):
        raise ExportError('duplicate columns are ambiguous')
    if any(h not in headers for h in SCHEMAS[table]):
        raise ExportError('missing required columns: ' + ','.join(h for h in SCHEMAS[table] if h not in headers))
    if any(not h for h in headers):
        raise ExportError('blank column name')
    selected, count, exact_seen, duplicates = [], 0, set(), 0
    try:
        for values in reader:
            if not values:
                raise ExportError('blank data row prevents a complete structured parse')
            count += 1
            if count > max_rows:
                raise ExportError('row budget exceeded; no partial-completeness result emitted')
            if len(values) != len(headers):
                raise ExportError('column-count mismatch at data row ' + str(count))
            record = dict(zip(headers, values))
            if not re.fullmatch(r'[0-9]{9}', record['NIIN']):
                raise ExportError('invalid NIIN at data row ' + str(count))
            if record['NIIN'] != niin:
                continue
            if table == 'characteristics':
                if not re.fullmatch(r'[A-Z0-9]{1,4}', record['MRC']):
                    raise ExportError('invalid selected MRC')
            else:
                if not record['PART_NUMBER'] or not re.fullmatch(r'[A-Z0-9]{5}', record['CAGE_CODE']):
                    raise ExportError('selected reference needs exact part number and five-character CAGE')
            identity = tuple(values)
            if identity in exact_seen:
                duplicates += 1
            exact_seen.add(identity)
            selected.append({'data_row': count, 'source_values': record})
    except csv.Error as exc:
        raise ExportError('malformed delimited text') from exc
    return {
        'schema_version': '1.0', 'niin': niin, 'table': table,
        'origin': receipt['origin'], 'synthetic': receipt['origin'] == 'synthetic',
        'source_receipt': receipt, 'input_file_sha256': receipt['file_sha256'],
        'status': 'parsed_pending_source_and_applicability_review' if selected else 'no_target_rows_in_supplied_export',
        'input_rows_scanned': count, 'selected_rows': selected,
        'selected_row_count': len(selected), 'exact_duplicate_selected_rows': duplicates,
        'complete_scan_of_supplied_file': True,
        'full_public_catalog_coverage_established': False,
        'source_authenticity_verified_by_parser': False,
        'nsn_equivalence_verified': False, 'manufacturer_or_approved_source_inferred': False,
        'revision_applicability_verified': False, 'price_comparison_qualified': False,
        'government_loss': None, 'buyer_benefit': None,
        'limitations': [
            'The digest binds supplied bytes to a supplied receipt; it does not authenticate provenance.',
            'No row in a selected export is not proof of absence from the public catalog.',
            'Reference codes and original values are preserved without decoding their meaning.',
            'A part/CAGE reference is not by itself an actual manufacturer or exclusive approved-source assertion.',
            'Release date is not proof that characteristics applied on the historical order date.',
            'Technical equivalence and procurement terms need independent review before a price comparison.'
        ]
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--table', choices=sorted(SCHEMAS), required=True)
    parser.add_argument('--niin', required=True)
    parser.add_argument('--delimiter', choices=['comma', 'pipe'], default='comma')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.input.is_symlink() or args.receipt.is_symlink():
            raise ExportError('symlink inputs are not accepted')
        if args.input.stat().st_size > MAX_BYTES:
            raise ExportError('input exceeds selected-export byte budget')
        result = parse_export(args.input.read_bytes(), json.loads(args.receipt.read_text()),
                              args.table, args.niin, ',' if args.delimiter == 'comma' else '|')
        # Exclusive create also prevents overwriting the inputs or a prior result.
        with args.output.open('x', encoding='utf-8') as output:
            output.write(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    except (ExportError, OSError, json.JSONDecodeError) as exc:
        parser.exit(2, str(exc) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
