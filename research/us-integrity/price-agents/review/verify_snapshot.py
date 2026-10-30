#!/usr/bin/env python3
"""Independent offline reconciliation of the retained public pilot and demo receipts.

No network use, source authentication, or producer-file writes. Run after a freeze.
"""
from datetime import date
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

HERE = Path(__file__).resolve().parent
AGENTS = HERE.parent
INTEGRITY = AGENTS.parent
PILOT = INTEGRITY / 'investigations/federal-price-pilot-2026-10-30'


def read(path):
    return json.loads(path.read_text(), parse_float=Decimal)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def without_run_times(value):
    # The tracer uses the actual run clock; remove only declared clock fields.
    if isinstance(value, dict):
        return {k: without_run_times(v) for k, v in value.items()
                if k not in {'started_at', 'finished_at', 'observed_at', 'completed_at'}}
    if isinstance(value, list):
        return [without_run_times(v) for v in value]
    return value


def main():
    results = {'schema_version': '1.0', 'checked_on': '2026-10-30',
               'network_requests': 0, 'scope': 'Offline retained-byte and arithmetic checks; not source authentication'}
    coverage = read(PILOT / 'coverage.json')
    rows, amounts, checked = [], {}, []
    for manifest in read(PILOT / 'capture/manifest.json'):
        name = manifest['id']
        source = PILOT / 'capture' / manifest['snapshot_path']
        assert sha(source) == manifest['snapshot_sha256']
        assert sha(PILOT / 'capture' / manifest['request_path']) == manifest['request_sha256']
        page = read(source)
        assert len(page['results']) == 10
        assert page['page_metadata']['hasNext'] is True
        values = page['results']
        assert all(date(2026, 7, 3) <= date.fromisoformat(r['Base Obligation Date']) <= date(2026, 7, 31) for r in values)
        amount = sum((Decimal(str(r['Award Amount'])) for r in values), Decimal(0))
        assert amount.is_finite()
        amounts[name] = str(amount.quantize(Decimal('.01')))
        summary = next(s for s in coverage['strata'] if s['stratum'] == name)
        assert Decimal(summary['sum_cumulative_sample_award_obligations_usd']) == amount
        rows.extend(values)
        checked.append({'stratum': name, 'rows': 10, 'has_next_page': True,
                        'sum_cumulative_obligations_usd': amounts[name]})
    ids = [r['generated_internal_id'] for r in rows]
    assert len(set(ids)) == len(ids) == 30
    observations = read(PILOT / 'observations.json')['observations']
    assert set(ids) == {r['generated_award_id'] for r in observations}
    assert all(r['unit_price_usd'] is None and r['estimated_loss_usd'] is None for r in observations)
    line_data = read(PILOT / 'line_observations.json')
    lines = line_data['observations']
    assert len(lines) == 2
    total = Decimal(0)
    for line in lines:
        q, p, extended = (Decimal(line[key]) for key in ('quantity', 'unit_price_usd', 'extended_amount_usd'))
        assert q > 0 and p >= 0 and q * p == extended
        total += extended
        assert line['markup_percent'] is None and line['excess_amount_usd'] is None
    assert total == Decimal('615816.57')
    assert {r['line_type'] for r in lines} == {'production_item', 'first_article_test_requirement'}
    assert next(r for r in lines if r['line_type'] == 'production_item')['item_id'] == '5306004457358'
    selected = read(PILOT / 'selected_manifest.json')
    for entry in selected['selected_artifacts']:
        assert sha(PILOT / entry['path']) == entry['sha256']
    checks = read(HERE / 'official-rechecks/manifest.json')
    assert len(checks) == 2
    for check in checks:
        assert check['success'] and check['http_status'] == 200
        assert len(check['field_matches']) == 10 and all(check['field_matches'].values())
        assert sha(HERE / 'official-rechecks' / check['selected_file']) == check['selected_sha256']
    results['pilot'] = {'unique_sample_rows': 30, 'strata': checked, 'population_complete': False,
                        'selected_source_files_hash_checked': len(selected['selected_artifacts']),
                        'line_sum_usd': str(total), 'qualified_benchmarks': 0,
                        'actual_payment_verified': False, 'fraud_established': False}
    results['independent_official_rechecks'] = {'requests': 2, 'successes': 2, 'fields_per_record': 10, 'all_match': True}
    assert sha(HERE / 'runtime-demo-replay.json') == sha(AGENTS / 'runtime/demo-output.json')
    synthetic = read(HERE / 'tracer-demo-replay.json')
    assert without_run_times(synthetic) == without_run_times(read(AGENTS / 'tracing/runs/synthetic-link-trace-final.json'))
    assert synthetic['synthetic'] is True and synthetic['network_used'] is False
    results['demonstrations'] = {'runtime_byte_exact_replay': True, 'tracer_semantic_replay': True,
                                 'tracer_excluded_dynamic_fields': ['started_at', 'finished_at', 'observed_at', 'completed_at'],
                                 'real_network_or_model_calls_in_replays': 0}
    spec = importlib.util.spec_from_file_location('snapshot_review_runtime', AGENTS / 'runtime/agent_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = runtime
    spec.loader.exec_module(runtime)
    plan = read(AGENTS / 'plans/current-wave.json')
    with tempfile.TemporaryDirectory() as directory:
        db = runtime.connect(Path(directory) / 'review.sqlite')
        runtime.import_plan(db, plan, now=1)
        runtime.import_plan(db, plan, now=2)
        actual_tasks = db.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
        assert actual_tasks == len(plan['tasks']) == 20
        db.close()
    results['current_wave'] = {'tasks': actual_tasks, 'fresh_import_and_identical_reimport': True,
                               'sha256': sha(AGENTS / 'plans/current-wave.json')}
    bundle = read(PILOT / 'bundle_manifest.json')
    for entry in bundle['artifacts']:
        assert sha(PILOT / entry['path']) == entry['sha256'], entry['path']
    results['pilot']['bundle_artifact_hashes_checked'] = len(bundle['artifacts'])
    final_path = AGENTS / 'runs/current-run/export-state.json'
    final = json.loads(final_path.read_text())
    counts = {s: sum(t['status'] == s for t in final['status']['tasks'])
              for s in ('accepted', 'blocked', 'queued', 'claimed', 'awaiting_review')}
    assert counts == {'accepted': 4, 'blocked': 5, 'queued': 11, 'claimed': 0, 'awaiting_review': 0}
    assert len(final['tables']['attempts']) == len(final['tables']['evidence']) == 6
    for collection in final['tables'].values():
        for entry in collection:
            if 'sha256' in entry and 'payload' in entry:
                assert runtime.digest(entry['payload']) == entry['sha256']
    for entry in final['tables']['attempts']:
        assert entry['payload']['method'] == 'LOCAL_CAPTURE_REUSE'
        assert entry['payload']['new_network_requests'] == 0
    for entry in final['tables']['attempt_finishes']:
        assert entry['payload']['new_network_requests'] == 0
    for entry in final['tables']['evidence']:
        assert sha(INTEGRITY.parents[1] / entry['payload']['artifact_path']) == entry['payload']['sha256']
    expected_reviews = {r['review_id']: r for filename in ('cohort-receipts.json', 'line-receipts.json')
                        for r in read(HERE / filename)['receipts']}
    assert len(expected_reviews) == len(final['tables']['reviews']) == 4
    for entry in final['tables']['reviews']:
        assert entry['payload'] == expected_reviews[entry['id']]
    for entry in final['tables']['results']:
        assert entry['payload']['pricing_eligibility']['status'] == 'unqualified'
        assert entry['payload']['benefit_evidence']['status'] == 'unresolved'
    assert not any(t['lease_active'] for t in final['status']['tasks'])
    assert 'lease_token' not in final_path.read_text()
    results['actual_retained_evidence_run'] = {'state_counts': counts, 'local_reuse_attempts': 6,
        'new_network_requests': 0, 'exact_review_receipts_ingested': 4,
        'all_accepted_packets_price_unqualified': True, 'active_leases': 0,
        'reopens_in_actual_run': 0, 'resume_reopen_proof_scope': 'Separate synthetic runtime demonstration',
        'export_sha256': sha(final_path)}
    (HERE / 'snapshot-verification.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
