#!/usr/bin/env python3
"""Read-only integration check against the committed preintegration graph.

Writes only this review folder. Does not approve, assemble, or publish a graph.
"""
from collections import Counter
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parents[1]
CASE = ROOT / 'investigations/price-agent-system-2026-10-30'
PILOT = ROOT / 'investigations/federal-price-pilot-2026-10-30'
BASE = 'd535e545adf362c17e43337e1147a0b2f6c7c18a'
ORIGINAL_REVIEW_SHA = '9dd1c94239e77725da5ba1ce453a31a0d0cc072dacf151fb36cf97292c28ca35'


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    original = read(HERE / 'review.json')
    assert sha(HERE / 'review.json') == ORIGINAL_REVIEW_SHA
    for pin in original['reviewed_input_artifacts']:
        assert sha(REPO / pin['path']) == pin['sha256'], pin['path']
    graph_path = CASE / 'graph-extension.json'
    graph = read(graph_path)
    nodes = {n['id']: n for n in graph['nodes']}
    edges = graph['edges']
    pins = graph['input_artifacts']
    assert len({p['path'] for p in pins}) == len(pins)
    for pin in pins:
        path = (ROOT / pin['path']).resolve()
        assert any(path.is_relative_to(ROOT / folder) for folder in ('investigations', 'price-agents'))
        assert sha(path) == pin['sha256'], pin['path']
    source_count = 0
    for node in nodes.values():
        if node['type'] != 'source':
            continue
        source_count += 1
        p = node['properties']
        if p.get('source_bytes_archived'):
            path = (ROOT / p['snapshot_path']).resolve()
            assert path.is_relative_to(ROOT)
            assert sha(path) == p['content_sha256']
        if p.get('artifact_origin') == 'locally_produced_repository_artifact':
            assert p['network_retrieval_inferred'] is False

    # Validate no earlier ID can be silently overwritten, even after assembly.
    prior_raw = subprocess.check_output(['git', 'show', BASE + ':research/us-integrity/data/graph.json'], cwd=REPO)
    prior = json.loads(prior_raw)
    previous_ids = {n['id'] for n in prior['nodes'] + prior['edges']}
    incoming_ids = {n['id'] for n in graph['nodes'] + edges}
    assert not previous_ids.intersection(incoming_ids)
    assert len(incoming_ids) == len(graph['nodes']) + len(edges)
    spec = importlib.util.spec_from_file_location('graph_review_integrity', ROOT / 'engine/integrity.py')
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    standalone = engine.validate_graph(graph, public=True)
    combined = engine.validate_graph({'version': '1.0', 'as_of': graph['as_of'],
        'nodes': prior['nodes'] + graph['nodes'], 'edges': prior['edges'] + edges}, public=True)

    observations = read(PILOT / 'observations.json')['observations']
    lines = read(PILOT / 'line_observations.json')['observations']
    money = [n for n in nodes.values() if n['type'] == 'money_measure']
    assert len(money) == 32
    assert Counter(n['type'] for n in nodes.values())['award_observation'] == 30
    assert Counter(n['type'] for n in nodes.values())['reported_parent_award_reference'] == 3
    for ob in observations:
        node = nodes['FPP-AWARD-' + ob['generated_award_id']]
        assert node['properties']['observation'] == ob
        value = nodes['FPP-OBLIGATION-' + ob['generated_award_id']]['properties']
        assert Decimal(value['money']['amount']) == Decimal(ob['award_obligation_usd'])
        assert value['money']['kind'] == 'cumulative_award_obligation'
    for line in lines:
        assert nodes['FPP-LINE-' + line['observation_id']]['properties']['observation'] == line
        value = nodes['FPP-ORDERED-VALUE-' + line['observation_id']]['properties']
        assert Decimal(value['money']['amount']) == Decimal(line['extended_amount_usd'])
        assert value['money']['kind'] == 'awarded_contract_line_ordered_value'
    for node in money:
        p = node['properties']
        assert p['aggregation_permitted'] is False and p['paid_cash_verified'] is False
        assert p['recoverable_loss'] is None and p['buyer_benefit'] is None
    assert sum(Decimal(line['extended_amount_usd']) for line in lines) == Decimal('615816.57')
    rejected = read(PILOT / 'rejected_comparators.json')['observations']
    for row in rejected:
        p = nodes['FPP-REJECTED-' + row['id']]['properties']
        assert p['observation'] == row and p['benchmark_status'] == 'excluded_wrong_product'
        assert p['paid_price'] is False and p['purchased_line'] is False

    parties = read(PILOT / 'parties/graph.json')
    for row in parties['nodes']:
        mapped = nodes['FPP-' + row['id']]
        assert mapped['type'] == row['type'] and mapped['status'] == row['status']
        assert set(mapped['source_ids']) == {'FPP-' + s for s in row['source_ids']}
        if row['type'] != 'source':
            assert all(mapped['properties'][k] == v for k, v in row['properties'].items())
    for row in parties['edges']:
        mapped = next(e for e in edges if e['properties'].get('original_projection_id') == row['id'])
        assert (mapped['source'], mapped['target'], mapped['type']) == ('FPP-' + row['source'], 'FPP-' + row['target'], row['type'])
        assert set(mapped['source_ids']) == {'FPP-' + s for s in row['source_ids']}
        assert all(mapped['properties'][k] == v for k, v in row['properties'].items())
    assert len([n for n in nodes.values() if n['type'] == 'person']) == 1
    assert not any('L10000120053' in json.dumps(n) for n in nodes.values())

    plan = read(ROOT / 'price-agents/plans/current-wave.json')
    for task in plan['tasks']:
        assert nodes[task['id']]['status'] == 'planned'
        assert nodes[task['id']]['properties']['definition'] == task
    roles = read(ROOT / 'price-agents/plans/role-contracts.json')['roles']
    for role in roles:
        assert nodes[role['id']]['properties']['contract'] == role
        assert nodes[role['id']]['properties']['deployed_model_instance'] is False
    run = read(ROOT / 'price-agents/runs/current-run/export-state.json')
    for task in run['status']['tasks']:
        assert nodes['PA-RUNSTATE-' + task['task_id']]['properties']['ledger_observation'] == task
    for packet in run['tables']['results']:
        p = nodes['PA-RUNRESULT-' + packet['id']]['properties']
        assert p['packet'] == packet['payload'] and p['result_sha256'] == packet['sha256']
        assert p['packet']['pricing_eligibility']['status'] == 'unqualified'
    summary = nodes['PA-RUN-LOCAL-20261030']['properties']
    assert summary['counts'] == {'queued': 11, 'blocked': 5, 'accepted': 4}
    assert summary['local_capture_reuse_attempts'] == 6 and summary['new_network_requests'] == 0
    assert nodes['PA-TRACER-LIVE-20261030']['properties']['coverage']['acquired_documents'] == 0
    synthetic = nodes['PA-RECURRENCE-SYNTHETIC']['properties']
    assert synthetic['real_transactions'] == 0 and synthetic['real_financial_totals_included'] is False
    assert 'money' not in synthetic
    actual = nodes['PA-RECURRENCE-ACTUAL-BLOCKED']['properties']
    assert actual['actual_repeated_premium'] is None and actual['real_loss'] is None and actual['real_buyer_benefit'] is None
    assert nodes['PA-SPEC-FOLLOWUP-20261030']['properties']['price_benchmark_qualified'] is False
    result = {'schema_version': '1.0', 'checked_on': '2026-10-30', 'scope': 'Read-only prepublication mapping and schema check',
        'graph_sha256': sha(graph_path), 'input_pins_verified': len(pins), 'source_nodes_checked': source_count,
        'original_review_sha256': ORIGINAL_REVIEW_SHA, 'original_review_input_pins_unchanged': len(original['reviewed_input_artifacts']),
        'baseline_commit': BASE, 'baseline_graph_sha256': hashlib.sha256(prior_raw).hexdigest(),
        'prior_id_collisions': 0, 'standalone_schema': standalone, 'combined_schema': combined,
        'exact_mappings': {'sampled_awards': 30, 'parent_references_separately_typed': 3, 'original_priced_lines': 2,
            'cumulative_obligation_measures': 30, 'ordered_line_measures': 2, 'rejected_comparators': len(rejected),
            'party_nodes': 15, 'party_edges': 9, 'professional_person_nodes': 1, 'role_contracts': 14,
            'planned_task_definitions': 20, 'separate_actual_task_states': 20, 'accepted_packets': 4},
        'new_network_requests': 0, 'canonical_approval_or_assembly_performed': False}
    (HERE / 'graph-integration-checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
