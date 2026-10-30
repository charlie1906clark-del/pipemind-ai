#!/usr/bin/env python3
"""Read-only review of this graph projection against its exact committed baseline.

Requires the baseline Git object, as a normal history-bearing checkout provides.
Does not mutate approval, assemble the graph, make remote calls or infer fraud.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
CASE=HERE.parent
ROOT=CASE.parents[1]
REPO=ROOT.parents[1]
BASE='9238fe6743be83e731cfb40f6481a096bc7208ca'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path):return json.loads(path.read_text())


def verify():
    path=CASE/'graph-extension.json'; graph=load(path)
    assert sha(path)=='dc6d0bb0ce2d2b764c3d8331c577cc8a0a9687c27338680fc4b92de1819796ed'
    for artifact in graph['input_artifacts']:
        assert sha(ROOT/artifact['path'])==artifact['sha256'],artifact['path']
    review=load(HERE/'review.json')
    for artifact in review['reviewed_input_artifacts']:
        assert sha(REPO/artifact['path'])==artifact['sha256'],artifact['path']
    prior=json.loads(subprocess.check_output(['git','show',BASE+':research/us-integrity/data/graph.json'],cwd=REPO,text=True))
    old_ids={row['id'] for row in prior['nodes']+prior['edges']}
    new_ids={row['id'] for row in graph['nodes']+graph['edges']}
    assert not old_ids & new_ids
    nodes={n['id']:n for n in graph['nodes']}
    assert len(nodes)==42 and len(graph['edges'])==27
    assert sum(n['type']=='source' for n in graph['nodes'])==24
    assert not any(n['type']=='money_measure' or 'money' in n.get('properties',{}) for n in graph['nodes'])
    assert not any(v in json.dumps(graph) for v in ['495.55','633.97'])
    for n in graph['nodes']:
        props=n.get('properties',{})
        for key in ['price_excess','buyer_benefit','recoverable_loss','fraud_probability']:
            if key in props:assert props[key] is None,(n['id'],key)
        if n['type']=='source' and props.get('source_bytes_archived'):
            assert sha(ROOT/props['snapshot_path'])==props['content_sha256'],n['id']
    def props(ident):return nodes['SC-20261030-'+ident]['properties']
    market=load(CASE/'market-terms/observations.json')
    assert props('NATIONWIDE-OFFER')['advertised_case_price_1_to_4']=='190.49'
    assert props('NATIONWIDE-OFFER')['advertised_carton_quantity']==1100
    assert props('NATIONWIDE-OFFER')['government_equivalence'] is False
    assert props('MF-PACK')['advertised_pack_quantity']==1100 and props('MF-PACK')['nominal_displayed_pieces']==7700
    assert props('UPSTREAM-LOT-GAP')['disclosed_distributor_role']=='master_distributor'
    assert props('UPSTREAM-LOT-GAP')['actual_manufacturer_identified'] is False
    assert props('UPSTREAM-LOT-GAP')['delivered_lot_origin_verified'] is False
    assert props('TDMT-GATE')['technical_record_acquired'] is False
    assert props('TDMT-GATE')['http_success_is_document_success'] is False
    assert props('NATIVE-ARCHIVE')['exact_niin_rows_acquired']==0
    assert props('NATIVE-ARCHIVE')['received_range_bytes']==10412003
    assert props('RELEASE-LABEL')['publication_timestamp_verified'] is False
    assert props('H06')['evaluation_quantity_basis'] != props('H06')['individual_order_price_basis']
    assert props('H06')['estimated_annual_demand_is_order'] is False
    assert props('AWARD-RECORD')['payment_verified'] is False
    assert props('RFQ-RECORD')['quantity_is_ordered_or_paid'] is False
    assert props('HISTORICAL-ROUTES')['awards_missing_or_concealed_inferred'] is False
    assert props('SBA-POTENTIAL')['amounts_additive'] is False
    for ident in ['SBA-POTENTIAL','GAO-IMPROPER','GAO-FRAUD-RANGE']:
        assert props(ident)['allocation_to_selected_purchase'] is False
    assert props('COMPARISON-BOUNDARY')['qualified_benchmarks']==market['qualified_comparators']==0
    assert props('COMPARISON-BOUNDARY')['actual_competing_quote_prices']==0
    assert props('COMPARISON-BOUNDARY')['fair_pricing_established'] is False
    spec=importlib.util.spec_from_file_location('single_case_graph_review',ROOT/'engine/integrity.py')
    engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
    combined={'version':graph['version'],'as_of':graph['as_of'],'nodes':prior['nodes']+graph['nodes'],'edges':prior['edges']+graph['edges']}
    counts=engine.validate_graph(combined,public=True)
    return {'schema_version':'1.0','checked_on':'2026-10-30','status':'accepted_for_exact_public_projection',
        'graph_extension_sha256':sha(path),'baseline_commit':BASE,'input_pins_verified':len(graph['input_artifacts']),
        'producer_review_pins_verified':len(review['reviewed_input_artifacts']),
        'extension_nodes':len(graph['nodes']),'extension_explicit_edges':len(graph['edges']),
        'extension_sources':24,'combined_before_assembly_source_links':counts,
        'prior_id_collisions':0,'new_actual_money_measures':0,'counterfactual_residuals_exported':False,
        'source_snapshot_hashes':'passed','semantic_mappings':'passed',
        'standalone_scope':'Extension intentionally has links to committed baseline nodes; public validation uses the combined graph.',
        'omitted_direct_pin':graph['omitted_review_dependencies'],
        'omission_check':'The root case overview is excluded from direct extension inputs but remains pinned and verified through the producer review; it must not be treated as freely mutable.',
        'network_requests':0,'canonical_approval_or_assembly_performed':False}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);args=p.parse_args()
    result=verify();text=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')
