import asyncio
import hashlib
import hmac
import json
import unittest

import httpx
from pipemind.integrations.apex import (
    ApexBridgeError, curated_snapshot, deliver_curated_snapshot, signed_headers
)


class ApexBridgeTests(unittest.TestCase):
    def test_explicit_review_required(self):
        with self.assertRaises(ApexBridgeError):
            curated_snapshot(["PM-H2-EOS-001"],"reviewer01")
        packet=curated_snapshot(["PM-H2-EOS-001"],"reviewer01",allow_publish=True)
        self.assertEqual(len(packet["records"]),1)
        self.assertEqual(packet["records"][0]["markings"],["PIPEMIND_REVIEWED_PUBLIC"])
        self.assertNotIn("private_note",json.dumps(packet).lower())

    def test_signature_matches_apex_protocol(self):
        body=b'{"records":[]}'
        headers=signed_headers("x"*40,body,"delivery.123",timestamp=123456789)
        expected=hmac.new(b"x"*40,b"123456789."+body,hashlib.sha256).hexdigest()
        self.assertEqual(headers["X-Apex-Signature"],"v1="+expected)

    def test_signed_delivery_rejects_unapproved_fields(self):
        packet=curated_snapshot(["PM-H2-EOS-001"],"reviewer01",allow_publish=True)
        packet["records"][0]["secret"]="confidential"
        async def run():
            await deliver_curated_snapshot(
                apex_origin="https://apex.example.test",pipeline="pipemind.reviewed-public-evidence",
                secret="x"*40,snapshot=packet,delivery_id="delivery.234"
            )
        with self.assertRaises(ApexBridgeError):
            asyncio.run(run())

    def test_signed_mock_delivery_to_dedicated_pipeline(self):
        packet=curated_snapshot(["PM-H2-EOS-001"],"reviewer01",allow_publish=True)
        requests=[]
        def handler(request):
            requests.append(request)
            return httpx.Response(202,json={"run_id":"r1"})
        async def run():
            return await deliver_curated_snapshot(
                apex_origin="https://apex.example.test",pipeline="pipemind.reviewed-public-evidence",
                secret="x"*40,snapshot=packet,delivery_id="delivery.345",
                transport=httpx.MockTransport(handler)
            )
        result=asyncio.run(run())
        self.assertTrue(result["accepted"])
        self.assertEqual(requests[0].url.path,"/api/v1/ingest/webhooks/pipemind.reviewed-public-evidence")
        self.assertIn("X-Apex-Signature",requests[0].headers)
        self.assertNotIn("Authorization",requests[0].headers)
