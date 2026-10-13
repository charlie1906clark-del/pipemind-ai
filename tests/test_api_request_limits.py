"""Exercise the actual ASGI boundary rather than trusting Content-Length."""
from __future__ import annotations

import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from pipemind.api.request_limits import RequestBodyLimitMiddleware


class RequestBodyLimitsTests(unittest.TestCase):
    def setUp(self):
        app = FastAPI()
        app.add_middleware(RequestBodyLimitMiddleware, max_bytes=128)
        self.writes = []

        @app.post("/ingest")
        async def ingest():
            self.writes.append("would-write")
            return {"accepted": True}

        self.client = TestClient(app)

    def tearDown(self):
        self.client.close()

    def test_content_length_rejected_before_endpoint(self):
        response = self.client.post("/ingest", content=b"x" * 129)
        self.assertEqual(response.status_code, 413)
        self.assertEqual(self.writes, [])

    def test_actual_chunked_stream_rejected(self):
        def body():
            yield b"x" * 80
            yield b"y" * 80

        response = self.client.post(
            "/ingest",
            content=body(),
            headers={"Transfer-Encoding": "chunked"},
        )
        self.assertEqual(response.status_code, 413)
        self.assertEqual(self.writes, [])

    def test_short_body_reaches_endpoint(self):
        response = self.client.post("/ingest", content=b'{"ok":true}')
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(self.writes, ["would-write"])

    def test_inconsistent_content_length_rejected(self):
        # ASGI scope crafted to ensure mismatch detection, independent of
        # httpx normalisation of outgoing Content-Length.
        app = self.client.app
        import asyncio
        sent = []
        scope = {
            "type": "http", "http_version": "1.1", "method": "POST",
            "scheme": "http", "path": "/ingest", "raw_path": b"/ingest",
            "query_string": b"", "server": ("testserver", 80),
            "client": ("127.0.0.1", 12345),
            "headers": [(b"content-length", b"50")],
        }
        initial = True

        async def receive():
            nonlocal initial
            if initial:
                initial = False
                return {"type": "http.request", "body": b"too short", "more_body": False}
            return {"type": "http.disconnect"}

        async def send(message):
            sent.append(message)

        asyncio.run(app(scope, receive, send))
        self.assertTrue(any(m.get("status") == 413 for m in sent))
        self.assertEqual(self.writes, [])
