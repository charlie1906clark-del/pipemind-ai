# Request-byte-limit correction

## Vulnerability
The original research API limited incoming bodies using only the HTTP
`Content-Length` header. A chunked/streamed POST without the header could
bypass this limit. FastAPI and the decoder might then consume unbounded data.

## Remedy
An outer pure-ASGI middleware counts received `http.request` body bytes
and rejects requests over 256,000 bytes with HTTP 413 *before* any endpoint
can execute, regardless of transfer framing. Duplicate Content-Length or
mismatch with actual received bytes also reject. The request buffer is
bounded. Integration tests cover normal requests, chunked bodies, declared
oversize and declared/actual mismatch.

The rejection is fail-closed but the middleware does not enforce network
connection count, bandwidth/slowloris limits, IP/subject rate limits,
reverse-proxy HTTP request smuggling validation or unauthenticated DDoS
capacity. Production must use strict ingress/body/time limits and an
independent security review. No claims of penetration-test completion.
