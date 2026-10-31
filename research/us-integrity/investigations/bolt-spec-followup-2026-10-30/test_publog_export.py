import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from parse_publog_export import ExportError, parse_export, main


def receipt(raw, table='characteristics', origin='synthetic'):
    return {'source_id': 'SYNTHETIC-CONTROL', 'table': table, 'origin': origin,
            'release_label': 'Fictional parser fixture', 'release_date': '2026-10-01',
            'retrieved_on': '2026-10-30', 'retrieval_method': 'synthetic test fixture',
            'export_query': "NIIN='016864912'", 'source_scope': 'fictional rows only',
            'scope': 'selected_export', 'source_kind': 'synthetic_fixture',
            'source_url': 'https://fixture.invalid/example',
            'file_sha256': hashlib.sha256(raw).hexdigest()}


CHAR = b'NIIN,MRC,REQUIREMENTS_STATEMENT,CLEAR_TEXT_REPLY\n016864912,TEST,"Example, only",fictional\n000000001,TEST,Other,fictional\n'


class ExportTests(unittest.TestCase):
    def test_exact_niin_and_quoted_field_preserved(self):
        out = parse_export(CHAR, receipt(CHAR), 'characteristics', '016864912')
        self.assertEqual(out['input_rows_scanned'], 2)
        self.assertEqual(out['selected_row_count'], 1)
        self.assertEqual(out['selected_rows'][0]['source_values']['REQUIREMENTS_STATEMENT'], 'Example, only')
        self.assertFalse(out['nsn_equivalence_verified'])
        self.assertTrue(out['synthetic'])

    def test_leading_zero_loss_and_fuzzy_key_rejected(self):
        for key in ['16864912', '5306016864912', '016864912 ', 16864912]:
            with self.subTest(key=key), self.assertRaises(ExportError):
                parse_export(CHAR, receipt(CHAR), 'characteristics', key)

    def test_digest_mismatch_rejected(self):
        with self.assertRaises(ExportError):
            parse_export(CHAR + b'\n', receipt(CHAR), 'characteristics', '016864912')

    def test_reference_qualifiers_preserved_without_role_inference(self):
        raw = b'NIIN|PART_NUMBER|CAGE_CODE|CAGE_STATUS|RNCC|RNVC|DAC|RNAAC|RNFC|RNSC|RNJC|SADC|HCC|MSDS|MEDALS\n016864912|FICTIONAL-PART|00000|A|3|2|9|XX|4|5|6|AA|BB|CCCCC|Z\n'
        out = parse_export(raw, receipt(raw, 'reference'), 'reference', '016864912', '|')
        values = out['selected_rows'][0]['source_values']
        self.assertEqual(values['RNCC'], '3')
        self.assertEqual(values['RNVC'], '2')
        self.assertEqual(values['PART_NUMBER'], 'FICTIONAL-PART')
        self.assertFalse(out['manufacturer_or_approved_source_inferred'])

    def test_missing_or_duplicate_headers_and_wrong_row_width_rejected(self):
        samples = [b'NIIN,MRC\n016864912,TEST\n',
                   b'NIIN,MRC,MRC,REQUIREMENTS_STATEMENT,CLEAR_TEXT_REPLY\n016864912,TEST,TEST,a,b\n',
                   b'NIIN,MRC,REQUIREMENTS_STATEMENT,CLEAR_TEXT_REPLY\n016864912,TEST,a\n']
        for raw in samples:
            with self.subTest(raw=raw), self.assertRaises(ExportError):
                parse_export(raw, receipt(raw), 'characteristics', '016864912')

    def test_empty_result_does_not_claim_catalog_absence(self):
        out = parse_export(CHAR, receipt(CHAR), 'characteristics', '999999999')
        self.assertEqual(out['status'], 'no_target_rows_in_supplied_export')
        self.assertFalse(out['full_public_catalog_coverage_established'])

    def test_native_binary_or_truncated_budget_rejected(self):
        raw = b'\xa3\xff\x00binary'
        with self.assertRaises(ExportError):
            parse_export(raw, receipt(raw), 'characteristics', '016864912')
        with self.assertRaises(ExportError):
            parse_export(CHAR, receipt(CHAR), 'characteristics', '016864912', max_rows=1)

    def test_real_and_synthetic_provenance_cannot_be_mixed(self):
        real = receipt(CHAR, origin='public_observation')
        with self.assertRaises(ExportError):
            parse_export(CHAR, real, 'characteristics', '016864912')
        real.update(source_kind='official_publog_csv', source_url='https://www.dla.mil/example')
        out = parse_export(CHAR, real, 'characteristics', '016864912')
        self.assertFalse(out['source_authenticity_verified_by_parser'])
        self.assertFalse(out['price_comparison_qualified'])

    def test_invalid_release_order_and_duplicate_rows_handled(self):
        rc = receipt(CHAR)
        rc['release_date'] = '2026-10-31'
        with self.assertRaises(ExportError):
            parse_export(CHAR, rc, 'characteristics', '016864912')
        raw = CHAR + CHAR.splitlines()[1] + b'\n'
        out = parse_export(raw, receipt(raw), 'characteristics', '016864912')
        self.assertEqual(out['selected_row_count'], 2)
        self.assertEqual(out['exact_duplicate_selected_rows'], 1)

    def test_public_receipt_urls_exclude_credentials_and_obfuscated_controls(self):
        urls = [
            'https://@publogstorage.blob.core.windows.net/publog/PublogDVD.zip',
            'https://user:@publogstorage.blob.core.windows.net/publog/PublogDVD.zip',
            'https://www.dla.mil/example?token=private',
            'https://www.dla.mil/example?X-Amz-Signature=private',
            'https://www.dla.mil/example?sessionid=private',
            'https://www.dla.mil/example?%74%4f%6beN=private',
            'https://www.dla.mil/example?%2574oken=private',
            'https://www.dla.mil/exa\nmple',
            'https://www.dla.mil/example?ver=2026%250A10',
            'https://www.dla.mil/example\\record',
            'https://www.dla.mil/example%255crecord',
            'https://www.dla.mil/example?ver=%ff',
            ' https://www.dla.mil/example',
        ]
        for url in urls:
            rc = receipt(CHAR, origin='public_observation')
            rc.update(source_kind='official_publog_csv', source_url=url)
            with self.subTest(url=url), self.assertRaises(ExportError):
                parse_export(CHAR, rc, 'characteristics', '016864912')
        rc = receipt(CHAR, origin='public_observation')
        rc.update(source_kind='official_publog_csv', source_url='https://www.dla.mil/example?ver=202610')
        out = parse_export(CHAR, rc, 'characteristics', '016864912')
        self.assertEqual(out['source_receipt']['source_url'], rc['source_url'])
        self.assertFalse(out['source_authenticity_verified_by_parser'])

    def test_cli_exclusive_output_and_actual_file_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder)
            (p/'input.txt').write_bytes(CHAR)
            (p/'receipt.json').write_text(json.dumps(receipt(CHAR)))
            args = ['--input',str(p/'input.txt'),'--receipt',str(p/'receipt.json'),
                    '--table','characteristics','--niin','016864912','--output',str(p/'out.json')]
            self.assertEqual(main(args), 0)
            original = (p/'out.json').read_bytes()
            with self.assertRaises(SystemExit):
                main(args)
            self.assertEqual((p/'out.json').read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
