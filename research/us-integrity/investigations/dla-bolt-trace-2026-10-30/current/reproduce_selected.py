#!/usr/bin/env python3
"""Reproduce selected, neutral pages; original supplier-contact pages stay local.

Default: offline replay from supplied original PDFs. --acquire performs exactly
two public document attempts through the ordinary DLA consent flow.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--acquire', action='store_true')
    args = parser.parse_args()
    if bool(args.source_dir) == args.acquire:
        parser.error('Choose exactly one of --source-dir or --acquire')
    args.output.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((HERE / 'selected_manifest.json').read_text())
    source_dir = args.source_dir
    if args.acquire:
        source_dir = args.output / 'local-originals-do-not-publish'
        source_dir.mkdir()
        module_path = HERE.parent / 'awards/acquire_public_documents.py'
        spec = importlib.util.spec_from_file_location('dla_public_documents', module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        receipts = []
        for record in manifest['records']:
            receipts.append(module.one({
                'contract_number': record['file'].removesuffix('.pdf'),
                'award_date': record['date'],
            }, source_dir))
        (args.output / 'acquisition.json').write_text(json.dumps(receipts, indent=2) + '\n')
        if any(r['result'] != 'pdf_acquired' for r in receipts):
            raise ValueError('A public document attempt failed; no bypass or automatic retry')
    outputs = []
    for record in manifest['records']:
        pdf = source_dir / record['file']
        actual = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if actual != record['original_pdf_sha256']:
            raise ValueError('Original source changed; independent review required: ' + record['file'])
        raw = subprocess.check_output(['pdftotext', '-layout', str(pdf), '-']).decode()
        pages = raw.split('\f')
        is_parent = record['source_id'] == 'BOLT-CUR-S01'
        mapping = {'parent-page2.txt': 2, 'parent-page5.txt': 5} if is_parent else {'order-page2.txt': 2}
        for filename, page in mapping.items():
            body = pages[page - 1].encode()
            (args.output / filename).write_bytes(body)
            expected = next(x['sha256'] for x in record['selected_artifacts']
                            if Path(x['path']).name == filename)
            digest = hashlib.sha256(body).hexdigest()
            outputs.append({'file': filename, 'page': page, 'sha256': digest,
                            'matches_published_selection': digest == expected})
    (args.output / 'replay.json').write_text(json.dumps(outputs, indent=2) + '\n')
    if not all(x['matches_published_selection'] for x in outputs):
        raise ValueError('Selected text differs; check source and Poppler version before adoption')
    print(json.dumps({'verified_originals': len(manifest['records']),
                      'verified_selected_texts': len(outputs), 'payment_verified': False}))


if __name__ == '__main__':
    main()
