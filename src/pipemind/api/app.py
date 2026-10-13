"""PipeMind management workbench HTTP API.

Safe by default: authenticated advisory simulations, validated imports, immutable
analysis history and NO actuation endpoints. No live OT/PLC connectivity.
"""
from __future__ import annotations

import json
import logging
import os
import time
from dataclasses import asdict
from pathlib import Path
from uuid import UUID

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, Field

from pipemind.api.auth import IdentityProvider
from pipemind.finance import CostInputs, compare_options, evaluate_cost
from pipemind.physics import CableInput, TankInput, PropertyDomainError, simulate_cable, simulate_tank
from pipemind.storage import Store
from pipemind.twin.telemetry import check_batch, METRICS
from pipemind.twin.forecast import forecast
from pipemind.brain import search as brain_search
from pipemind.evidence import load_evidence
from pipemind.agents import compose_review
from pipemind.optimization import OptimisationStudy, optimise
from pipemind.reports import draft_report
from pipemind.route import best_route, Segment

log=logging.getLogger("pipemind")
REPO_ROOT=Path(__file__).resolve().parents[3]
STATIC=REPO_ROOT/"web"


class StrictBody(BaseModel):
    model_config=ConfigDict(extra="forbid")


class TankBody(StrictBody):
    volume_m3: float=Field(default=100,gt=0,le=100000)
    fill_liquid_volume_fraction: float=Field(default=0.84,gt=0.03,lt=0.97)
    initial_pressure_pa: float=Field(default=101325,ge=30000,le=500000)
    heat_ingress_w: float=Field(default=700,ge=0,le=250000)
    cooling_duty_w: float=Field(default=0,ge=0,le=250000)
    cooling_cop: float=Field(default=0.04,ge=0.001,le=0.25)
    duration_hours: float=Field(default=12,gt=0,le=72)
    steps: int=Field(default=24,ge=1,le=144)
    spin: str=Field(default="para",pattern="^(para|normal|ortho)$")


class CableBody(StrictBody):
    length_m: float=Field(default=1000,gt=0,le=50000)
    inner_diameter_m: float=Field(default=0.12,ge=0.01,le=2)
    absolute_roughness_m: float=Field(default=1e-5,ge=0,le=0.01)
    mass_flow_kg_s: float=Field(default=0.8,gt=0,le=100)
    inlet_temperature_k: float=Field(default=19,ge=15,le=28)
    inlet_pressure_pa: float=Field(default=240000,ge=50000,le=600000)
    heat_ingress_w_per_m: float=Field(default=1,ge=0,le=50)
    residual_electrical_heat_w_per_m: float=Field(default=0,ge=0,le=100)
    elevation_gain_m: float=Field(default=0,ge=-1000,le=1000)
    steps: int=Field(default=40,ge=2,le=240)
    spin: str=Field(default="para",pattern="^(para|normal|ortho)$")


class CostBody(StrictBody):
    duration_hours: float=Field(default=24,ge=0,le=8760)
    heat_load_w: float=Field(default=1000,ge=0,le=1e7)
    recovered_vapour_fraction: float=Field(default=0,ge=0,le=1)
    cooling_fraction: float=Field(default=0,ge=0,le=1)
    cooling_cop: float=Field(default=0.04,gt=0,le=0.25)
    effective_latent_heat_j_kg: float=Field(default=445000,gt=0,le=5e6)
    electricity_gbp_kwh: float=Field(default=0.2,ge=0,le=1000)
    unrecovered_hydrogen_gbp_kg: float=Field(default=5,ge=0,le=10000)
    annualised_equipment_cost_gbp: float=Field(default=0,ge=0,le=1e12)


class ComparisonBody(StrictBody):
    baseline: CostBody
    candidates: list[CostBody]=Field(min_length=1,max_length=20)


class OptimisationBody(StrictBody):
    baseline: CostBody
    cooling_capital_annual_gbp: float | None = Field(default=None, ge=0, le=1e10)
    recovery_capital_annual_gbp: float | None = Field(default=None, ge=0, le=1e10)
    recovery_aux_electricity_kwh_per_kg: float | None = Field(default=None, ge=0, le=100000)


class ReviewBody(StrictBody):
    question: str = Field(default="", max_length=300)


class RouteSegment(StrictBody):
    start: str = Field(min_length=1, max_length=64)
    end: str = Field(min_length=1, max_length=64)
    length_m: float = Field(ge=0, le=1e9)
    ground_risk: float = Field(default=0, ge=0, le=10)
    protected_area: bool = False
    trenchless_crossings: int = Field(default=0, ge=0, le=1000)
    infrastructure_parallel: bool = False


class RouteBody(StrictBody):
    nodes: list[str] = Field(min_length=2, max_length=500)
    segments: list[RouteSegment] = Field(min_length=1, max_length=5000)
    source: str = Field(min_length=1, max_length=64)
    destination: str = Field(min_length=1, max_length=64)


class ObservationBody(StrictBody):
    asset_id: str=Field(min_length=1,max_length=64)
    measured_at: str=Field(min_length=10,max_length=40)
    metric: str=Field(min_length=1,max_length=64)
    value: float
    unit: str=Field(min_length=1,max_length=24)
    source: str=Field(default="simulated",max_length=64)
    lineage: str=Field(default="",max_length=200)


class BatchBody(StrictBody):
    observations: list[ObservationBody]=Field(min_length=1,max_length=500)


class TrendBody(StrictBody):
    values: list[float]=Field(min_length=1,max_length=2000)
    horizon_samples: int=Field(default=1,ge=1,le=24)


class ResearchBody(StrictBody):
    question: str=Field(min_length=2,max_length=300)
    limit: int=Field(default=8,ge=1,le=30)


def create_app() -> FastAPI:
    auth=IdentityProvider()
    store=Store(os.getenv("PIPEMIND_DB_PATH","/tmp/pipemind-research.sqlite"))
    app=FastAPI(title="PipeMind AI",version="0.2.0",description="Research-grade hydrogen decision-support platform; not OT control.")
    app.state.store=store
    app.state.auth=auth

    @app.middleware("http")
    async def guard(request: Request, call_next):
        if request.method not in ("GET","POST","HEAD","OPTIONS"):
            return JSONResponse({"error":"read-only platform; method not supported"},status_code=405)
        size=request.headers.get("content-length")
        if size and (not size.isdecimal() or int(size)>256_000):
            return JSONResponse({"error":"request too large"},status_code=413)
        try:
            response=await call_next(request)
        except Exception:
            log.exception("Unhandled server error")
            response=JSONResponse({"error":"internal failure"},status_code=500)
        response.headers["X-Content-Type-Options"]="nosniff"
        response.headers["Referrer-Policy"]="no-referrer"
        response.headers["X-Frame-Options"]="DENY"
        response.headers["Cache-Control"]="no-store"
        response.headers["Content-Security-Policy"]=(
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; "
            "connect-src 'self'; base-uri 'none'; object-src 'none'; frame-ancestors 'none'"
        )
        return response

    @app.exception_handler(PropertyDomainError)
    async def physics_error(request:Request,exc:PropertyDomainError):
        return JSONResponse({"error":"MODEL_DOMAIN_REJECTED","detail":str(exc)},status_code=422)

    @app.exception_handler(ValueError)
    async def input_error(request:Request,exc:ValueError):
        return JSONResponse({"error":"INVALID_MODEL_INPUT","detail":str(exc)},status_code=422)

    @app.get("/healthz")
    def health():
        return {"status":"alive","version":"0.2.0"}

    @app.get("/readyz")
    def ready():
        try:
            store.db.execute("SELECT 1")
            from pipemind.physics.properties import CoolProp
            return {"ready":CoolProp is not None,"database":"sqlite-single-node","eos":"CoolProp" if CoolProp is not None else "UNAVAILABLE"}
        except Exception:
            return JSONResponse({"ready":False},status_code=503)

    @app.get("/api/v1/status")
    def status(request:Request):
        person=auth.require(request,"viewer","analyst","ingest","auditor")
        from pipemind.physics.properties import CoolProp
        return {
            "product":"PipeMind AI","edition":"research / read-only pilot",
            "tenant":person.tenant,"roles":sorted(person.roles),
            "physics_backend":CoolProp.__version__ if CoolProp is not None else "UNAVAILABLE",
            "actuation_enabled":False,
            "wong_link":"CURATED_CONTRACT_ONLY","apex_connected":False,
            "capabilities":["tank-simulation","cable-screening","scenario-cost","telemetry-quality",
                            "trend-backtest","source-linked-research","audit-trail","advisory-review","report-drafts","synthetic-routing","scenario-optimisation"]
        }

    def save(person,kind,result):
        return {"run_id":store.save_run(person.tenant,person.subject,kind,result),**result}

    @app.post("/api/v1/simulations/tank")
    def tank(body:TankBody,request:Request):
        user=auth.require(request,"analyst")
        result=asdict(simulate_tank(TankInput(**body.model_dump())))
        return save(user,"tank",result)

    @app.post("/api/v1/simulations/cable")
    def cable(body:CableBody,request:Request):
        user=auth.require(request,"analyst")
        result=asdict(simulate_cable(CableInput(**body.model_dump())))
        return save(user,"cable",result)

    @app.post("/api/v1/cost/evaluate")
    def cost(body:CostBody,request:Request):
        user=auth.require(request,"analyst")
        return save(user,"cost",evaluate_cost(CostInputs(**body.model_dump())))

    @app.post("/api/v1/cost/compare")
    def compare(body:ComparisonBody,request:Request):
        user=auth.require(request,"analyst")
        baseline=CostInputs(**body.baseline.model_dump())
        variants=[CostInputs(**a.model_dump()) for a in body.candidates]
        return save(user,"comparison",{
            "baseline":evaluate_cost(baseline),
            "ranked_options":compare_options(baseline,variants),
            "approval_required":True,
            "no_equipment_control":True,
        })

    @app.post("/api/v1/optimization/screen")
    def optimization(body:OptimisationBody,request:Request):
        user=auth.require(request,"analyst")
        study=OptimisationStudy(
            baseline=CostInputs(**body.baseline.model_dump()),
            cooling_capital_annual_gbp=body.cooling_capital_annual_gbp,
            recovery_capital_annual_gbp=body.recovery_capital_annual_gbp,
            recovery_aux_electricity_kwh_per_kg=body.recovery_aux_electricity_kwh_per_kg
        )
        return save(user,"optimization",optimise(study))

    @app.post("/api/v1/routes/synthetic")
    def route(body:RouteBody,request:Request):
        user=auth.require(request,"analyst")
        result=best_route(
            body.nodes,[Segment(**s.model_dump()) for s in body.segments],
            body.source,body.destination
        )
        return save(user,"route",result)

    @app.post("/api/v1/twin/ingest")
    def ingest(body:BatchBody,request:Request):
        user=auth.require(request,"ingest")
        result=check_batch([item.model_dump() for item in body.observations])
        written=store.append_observations(user.tenant,user.subject,[x.to_dict() for x in result.accepted]) if result.accepted else 0
        return {"persisted":written,"quality":result.to_dict(),"source":"import/replay, not OT control"}

    @app.get("/api/v1/twin/observations/{asset_id}/{metric}")
    def observations(asset_id:str,metric:str,request:Request,limit:int=200):
        user=auth.require(request,"viewer","analyst")
        if not asset_id or len(asset_id)>64 or metric not in METRICS:
            raise HTTPException(422,"invalid asset or metric")
        if not 1 <= limit <= 2000:
            raise HTTPException(422,"limit out of bounds")
        return {"asset_id":asset_id,"metric":metric,"observations":store.read_observations(user.tenant,asset_id,metric,limit)}

    @app.post("/api/v1/twin/forecast")
    def trend(body:TrendBody,request:Request):
        user=auth.require(request,"analyst")
        return save(user,"trend",forecast(body.values,body.horizon_samples).to_dict())

    @app.post("/api/v1/research/search")
    def research(body:ResearchBody,request:Request):
        auth.require(request,"viewer","analyst")
        return {"question":body.question,"results":[x.to_dict() for x in brain_search(REPO_ROOT,body.question,body.limit)],
                "warning":"Retrieved text is not independently verified and must never override physics or safety gates."}

    @app.get("/api/v1/evidence")
    def evidence_manifest(request:Request):
        auth.require(request,"viewer","analyst","auditor")
        return {"cards":[e.to_dict() for e in load_evidence()],"warning":"Source verification is not a field test"}

    @app.post("/api/v1/agents/review/{run_id}")
    def review_run(run_id:str,body:ReviewBody,request:Request):
        user=auth.require(request,"analyst")
        try:
            UUID(run_id)
        except ValueError:
            raise HTTPException(404,"not found")
        record=store.get_run_record(user.tenant,run_id)
        if record is None:
            raise HTTPException(404,"not found")
        if record["kind"] not in {"tank","cable","cost","trend","comparison"}:
            raise HTTPException(422,"run type not eligible for review")
        result=compose_review(record["kind"],record["payload"],body.question)
        return save(user,"advisory-review",result)

    @app.get("/api/v1/reports/draft/{run_id}")
    def report_run(run_id:str,request:Request):
        user=auth.require(request,"analyst","viewer")
        try:
            UUID(run_id)
        except ValueError:
            raise HTTPException(404,"not found")
        record=store.get_run_record(user.tenant,run_id)
        if record is None:
            raise HTTPException(404,"not found")
        if record["kind"] not in {"tank","cable","cost","trend","comparison"}:
            raise HTTPException(422,"run type not eligible for report")
        review=compose_review(record["kind"],record["payload"],record["kind"])
        return PlainTextResponse(
            draft_report(run_id,record["kind"],record["payload"],review),
            media_type="text/markdown",
        )

    @app.get("/api/v1/runs")
    def runs(request:Request):
        user=auth.require(request,"viewer","analyst","auditor")
        return {"runs":store.list_runs(user.tenant)}

    @app.get("/api/v1/runs/{run_id}")
    def run(run_id:str,request:Request):
        user=auth.require(request,"viewer","analyst","auditor")
        try:
            UUID(run_id)
        except ValueError:
            raise HTTPException(404,"not found")
        value=store.get_run(user.tenant,run_id)
        if value is None:
            raise HTTPException(404,"not found")
        return value

    @app.get("/api/v1/audit/verify")
    def audit(request:Request):
        auth.require(request,"auditor")
        return store.verify_audit_chain()

    @app.get("/api/v1/apex/contract")
    def apex_contract(request:Request):
        auth.require(request,"admin")
        return {
            "status":"NOT_CONFIGURED_FOR_LIVE_SYNC",
            "recommended_mode":"PipeMind owned domain ontology + curated/signed outward snapshots",
            "forbidden":["Wong private notes","shared JWT signing keys","equipment commands","unreviewed research claims"],
            "proposed_types":["PipeMindAsset","PipeMindSimulationRun","PipeMindEvidenceClaim","PipeMindAdvisory"],
        }

    if STATIC.exists():
        app.mount("/assets",StaticFiles(directory=str(STATIC/"assets")),name="assets")
        @app.get("/",include_in_schema=False)
        def homepage():
            return FileResponse(STATIC/"index.html")
    return app


app=create_app()
