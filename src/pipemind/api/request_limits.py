"""Bounded ASGI request-body buffering, including chunked transfers.

The previous Content-Length-only limit could be bypassed by HTTP chunking.
The middleware checks actual received bytes *before* any endpoint executes.
This is an API payload guard, not a replacement for upstream rate limiting,
reverse proxy header validation, ingress connection limits, or DDoS protection.
"""
from __future__ import annotations

from collections import deque
from typing import Any, Awaitable, Callable

from starlette.responses import JSONResponse

Scope = dict[str, Any]
Message = dict[str, Any]
Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]


class RequestBodyLimitMiddleware:
    def __init__(self, app: Callable, max_bytes: int = 256_000):
        self.app = app
        self.max_bytes = max_bytes

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        length_values = [
            v for k, v in scope.get("headers", [])
            if k.lower() == b"content-length"
        ]
        if len(length_values) > 1 or (
            length_values and (
                not length_values[0].isdigit()
                or int(length_values[0]) > self.max_bytes
            )
        ):
            await self._reject(scope, receive, send)
            return

        # Body is buffered to enforce the byte cap before FastAPI or any route
        # can mutate the database. Strict upper bound on memory from input body.
        queued: deque[Message] = deque()
        total = 0
        while True:
            message = await receive()
            kind = message.get("type")
            if kind == "http.disconnect":
                return
            if kind != "http.request":
                return  # invalid ASGI input; never reach application logic
            total += len(message.get("body", b""))
            if total > self.max_bytes:
                await self._reject(scope, receive, send)
                return
            queued.append(message)
            if not message.get("more_body", False):
                break

        # If Content-Length lies, fail closed rather than trusting it.
        if length_values and total != int(length_values[0]):
            await self._reject(scope, receive, send)
            return

        async def bounded_receive() -> Message:
            if queued:
                return queued.popleft()
            return await receive()

        await self.app(scope, bounded_receive, send)

    @staticmethod
    async def _reject(scope: Scope, receive: Receive, send: Send) -> None:
        response = JSONResponse(
            {"error": "REQUEST_BODY_LIMIT_EXCEEDED_OR_INVALID"},
            status_code=413,
            headers={
                "Cache-Control": "no-store",
                "X-Content-Type-Options": "nosniff",
                "Referrer-Policy": "no-referrer",
            },
        )
        await response(scope, receive, send)
