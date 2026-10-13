import os
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

class AppTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.previous={k:os.environ.get(k) for k in ("PIPEMIND_ENV","PIPEMIND_DEV_TOKEN","PIPEMIND_DB_PATH")}
        os.environ["PIPEMIND_ENV"]="development"
        os.environ["PIPEMIND_DEV_TOKEN"]="testing-0123456789abcdefghij"
        os.environ["PIPEMIND_DB_PATH"]=str(Path(self.temp.name)/"db.sqlite")
        from pipemind.api.app import create_app
        self.app=create_app()
        self.client=TestClient(self.app)
        self.token={"Authorization":"Bearer testing-0123456789abcdefghij"}

    def tearDown(self):
        self.client.close()
        for key,v in self.previous.items():
            if v is None: os.environ.pop(key,None)
            else: os.environ[key]=v
        self.temp.cleanup()

    def test_public_health_authenticated_status(self):
        self.assertEqual(self.client.get("/healthz").status_code,200)
        self.assertEqual(self.client.get("/api/v1/status").status_code,401)
        r=self.client.get("/api/v1/status",headers=self.token)
        self.assertEqual(r.status_code,200)
        self.assertFalse(r.json()["actuation_enabled"])

    def test_cost_case_and_audit(self):
        r=self.client.post("/api/v1/cost/evaluate",headers=self.token,json={"heat_load_w":2000})
        self.assertEqual(r.status_code,200,r.text)
        self.assertGreater(r.json()["gross_vapour_equivalent_kg"],0)
        audit=self.client.get("/api/v1/audit/verify",headers=self.token)
        self.assertTrue(audit.json()["verified"])

    def test_unknown_inputs_fail(self):
        r=self.client.post("/api/v1/simulations/tank",headers=self.token,json={"disarm_relief":True})
        self.assertEqual(r.status_code,422)
        self.assertEqual(self.client.delete("/api/v1/runs/anything",headers=self.token).status_code,405)

    def test_research_has_provenance(self):
        r=self.client.post("/api/v1/research/search",headers=self.token,
                           json={"question":"hydrogen cryogenic cable","limit":2})
        self.assertEqual(r.status_code,200)
        self.assertTrue(r.json()["results"])
        self.assertIn("path",r.json()["results"][0])

    def test_ingestion_quality(self):
        from datetime import datetime,timezone
        p={"asset_id":"demo-tank","metric":"temperature_k","value":20.1,"unit":"K",
           "source":"simulated","measured_at":datetime.now(timezone.utc).isoformat()}
        r=self.client.post("/api/v1/twin/ingest",headers=self.token,json={"observations":[p]})
        self.assertEqual(r.status_code,200,r.text)
        self.assertEqual(r.json()["persisted"],1)
        r2=self.client.get("/api/v1/twin/observations/demo-tank/temperature_k",headers=self.token)
        self.assertEqual(len(r2.json()["observations"]),1)

    def test_production_cannot_enable_demo(self):
        from pipemind.api.auth import IdentityProvider
        os.environ["PIPEMIND_ENV"]="production"
        with self.assertRaises(RuntimeError):
            IdentityProvider()

if __name__=="__main__":
    unittest.main()
