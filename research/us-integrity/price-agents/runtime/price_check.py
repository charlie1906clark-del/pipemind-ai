#!/usr/bin/env python3
"""Use the existing reviewed premium engine without changing its evidence gates."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CALCULATOR=ROOT/'investigations/dla-bolt-trace-2026-10-30/price-controls/premium_audit.py'
EXPECTED='7aed71b71b47c0940b0c07fd1239c64bb70817be506204b3ac3de366d9dcfde2'


def run(path):
    code=CALCULATOR.read_bytes()
    if hashlib.sha256(code).hexdigest()!=EXPECTED:raise ValueError('Calculator changed; review and repin before executing')
    raw=Path(path).read_bytes()
    if len(raw)>8*1024*1024:raise ValueError('Input exceeds8MiB')
    spec=importlib.util.spec_from_file_location('reviewed_premium_audit',CALCULATOR)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    result=module.audit(json.loads(raw))
    return {'calculator':{'path':str(CALCULATOR.relative_to(ROOT)),'sha256':EXPECTED},'input_snapshot':{'file_name':Path(path).name,'sha256':hashlib.sha256(raw).hexdigest()},'result':result,'automatic_task_completion':False,'automatic_graph_promotion':False,'source_authentication':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');p.add_argument('--output');a=p.parse_args()
    try:encoded=json.dumps(run(a.input),indent=2,allow_nan=False)+'\n'
    except (ValueError,OSError) as exc:p.exit(2,str(exc)+'\n')
    if a.output:
        with open(a.output,'x') as f:f.write(encoded)
    else:print(encoded,end='')


if __name__=='__main__':main()
