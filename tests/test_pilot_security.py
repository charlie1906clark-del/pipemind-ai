"""HTTP tenant/role isolation, ingestion provenance and evidence-package invariants."""
from __future__ import annotations
import json
import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from fastapi.testclient import TestClient

from pipemind.api.auth import Identity
from pipemind.evidence import load_evidence


class PilotSecurityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.previous={k:os.environ.get(k) for k in ("PIPEMIND_ENV","PIPEMIND_DEV_TOKEN","PIPEMIND_DB_PATH")}
        os.environ.update({
            "PIPEMIND_ENV":"development",
            "PIPEMIND_DEV_TOKEN":"lab-test-token-secret-very-long",
            "PIPEMIND_DB_PATH":str(Path(self.tmp.name)/"data.sqlite"),
        })
        from pipemind.api.app import create_app
        self.application=create_app()
        self.client=TestClient(self.application)
        # Identity stubs are only inside a test. Production JWT checks remain
        # in IdentityProvider and do not trust X-Tenant-ID or user input.
        def checked_identity(token: str):
            subjects={
                "alice-token":Identity("alice","operator-a",frozenset({"analyst","ingest","viewer","auditor"})),
                "bob-token":Identity("bob","operator-b",frozenset({"analyst","viewer"})),
                "viewer-token":Identity("viewer","operator-a",frozenset({"viewer"})),
            }
            from fastapi import HTTPException
            if token not in subjects:
                raise HTTPException(401, "unrecognised test identity")
            return subjects[token]
        self.application.state.auth.verify=checked_identity

    def tearDown(self):
        self.client.close()
        self.application.state.store.db.close()
        for key,val in self.previous.items():
            if val is None: os.environ.pop(key,None)
            else: os.environ[key]=val
        self.tmp.cleanup()

    def bearer(self,name:str):
        return {"Authorization":f"Bearer {name}-token"}

    def test_customer_run_and_telemetry_do_not_cross_tenant(self):
        alice=self.bearer("alice")
        bob=self.bearer("bob")
        sim=self.client.post("/api/v1/cost/evaluate",headers=alice,json={"heat_load_w":1200})
        self.assertEqual(sim.status_code,200,sim.text)
        identifier=sim.json()["run_id"]
        self.assertEqual(self.client.get("/api/v1/runs/"+identifier,headers=bob).status_code,404)
        self.assertEqual(self.client.get("/api/v1/runs",headers=bob).json()["runs"],[])
        payload={"asset_id":"test-tank","metric":"temperature_k","value":20.0,
                 "unit":"K","source":"operator-import","measured_at":datetime.now(timezone.utc).isoformat()}
        a=self.client.post("/api/v1/twin/ingest",headers=alice,json={"observations":[payload]})
        self.assertEqual(a.status_code,200,a.text)
        self.assertEqual(a.json()["persisted"],1)
        b=self.client.get("/api/v1/twin/observations/test-tank/temperature_k",headers=bob)
        self.assertEqual(b.json()["observations"],[])
        second=self.client.post("/api/v1/twin/ingest",headers=alice,json={"observations":[payload]})
        self.assertEqual(second.json()["persisted"],0)
        self.assertEqual(second.json()["duplicates_previous_batches"],1)
        self.assertTrue(self.client.get("/api/v1/audit/verify",headers=alice).json()["verified"])

    def test_no_header_tenant_override_and_viewer_cannot_ingest(self):
        visitor=self.bearer("viewer")
        r=self.client.post("/api/v1/twin/ingest",
                           headers={**visitor,"X-Tenant-ID":"operator-b"},
                           json={"observations":[]})
        self.assertEqual(r.status_code,422) # schema disallows empty sample batch
        r=self.client.post("/api/v1/twin/forecast",headers=visitor,json={"values":[20]*20})
        self.assertEqual(r.status_code,403)
        status=self.client.get("/api/v1/status",headers={**visitor,"X-Tenant-ID":"operator-b"})
        self.assertEqual(status.json()["tenant"],"operator-a")
        self.assertEqual(self.client.get("/api/v1/apex/contract",headers=visitor).status_code,403)

    def test_gateway_label_never_means_signature(self):
        sample={"asset_id":"tank","metric":"pressure_pa","value":101325,"unit":"Pa",
                "source":"signed-gateway","measured_at":datetime.now(timezone.utc).isoformat()}
        r=self.client.post("/api/v1/twin/ingest",headers=self.bearer("alice"),
                           json={"observations":[sample]})
        self.assertEqual(r.status_code,200,r.text)
        self.assertEqual(r.json()["persisted"],0)
        self.assertIn("UNTRUSTED_SOURCE",r.json()["quality"]["rejected"][0]["flags"])

    def test_evidence_copies_have_identical_ids(self):
        from pipemind.evidence import _DATA
        source=Path(__file__).resolve().parents[1]/"data/evidence/claims.json"
        a=json.loads(source.read_text())
        b=json.loads(_DATA.read_text())
        self.assertEqual(a,b)
        self.assertEqual(len(load_evidence()),len(a["claims"]))
        self.assertTrue(all(c.status=="source_checked" for c in load_evidence()))
