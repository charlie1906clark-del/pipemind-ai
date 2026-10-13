"""Bounded synthetic least-cost corridor ranking; never an approved construction route."""
from __future__ import annotations
from dataclasses import dataclass
from heapq import heappop, heappush
from math import isfinite
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Segment:
    start: str
    end: str
    length_m: float
    ground_risk: float = 0
    protected_area: bool = False
    trenchless_crossings: int = 0
    infrastructure_parallel: bool = False


def best_route(nodes: Sequence[str], segments: Sequence[Segment], source: str, destination: str,
               *, risk_weight: float = 2.0, crossing_cost_m: float = 500.0) -> dict:
    if len(nodes)>500 or len(segments)>5000:
        raise ValueError("graph size limit exceeded")
    valid=set(nodes)
    if source not in valid or destination not in valid or not source or not destination:
        raise ValueError("invalid terminals")
    graph: dict[str,list[tuple[str,float,float,Segment]]] = {n:[] for n in valid}
    for s in segments:
        if s.start not in graph or s.end not in graph:
            raise ValueError("segment refers to unknown node")
        if s.protected_area:
            continue  # hard exclusion in this synthetic example
        if any(type(v) not in (int,float) or not isfinite(v) or v<0 for v in (s.length_m,s.ground_risk,s.trenchless_crossings)):
            raise ValueError("invalid edge")
        weight=s.length_m*(1+risk_weight*s.ground_risk)+s.trenchless_crossings*crossing_cost_m
        if s.infrastructure_parallel:
            weight*=.9
        graph[s.start].append((s.end,weight,s.length_m,s))
        graph[s.end].append((s.start,weight,s.length_m,s))
    queue=[(0.0,source,(),0.)]
    best={source:0.}
    while queue:
        cost,node,path,length=heappop(queue)
        if cost>best[node]:
            continue
        if node==destination:
            return {"status":"SYNTHETIC_ROUTING_SCREENING","nodes":list(path)+[node],
                    "proxy_cost":cost,"length_m":length,
                    "limitations":["No real geospatial datasets, permits, protective provisions or constructability validation",
                                   "Protected areas are hard-excluded only for a synthetic example"]}
        for target,w,l,seg in graph[node]:
            proposed=cost+w
            if proposed<best.get(target,float("inf")):
                best[target]=proposed
                heappush(queue,(proposed,target,(*path,node),length+l))
    return {"status":"NO_FEASIBLE_ROUTE","nodes":[],"limitations":["Synthetic graph disconnected after exclusions"]}
