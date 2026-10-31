# Public transaction-link tracing

This standard-library adapter follows a finite set of declared public procurement sources. It records how each document URL was reached, the exact identifier that made a link relevant, excluded links, access outcomes and response-body hashes. It does not extract or authenticate prices, people, ownership, buyer decisions or wrongdoing. An HTML consent page can return 200 without being the expected award; acquisition status alone does not establish document identity.

The existing research identified a genuine need for persistent link provenance: a contract summary is not an order line, a source-reported recipient is not necessarily a beneficial owner, and an inaccessible source is not evidence of concealment. This adapter provides the acquisition history for subsequent specialist review.

## Run

From repository root:

```bash
python research/us-integrity/price-agents/tracing/trace_links.py research/us-integrity/price-agents/tracing/examples/live-public-source-plan.json --output /tmp/trace-plan-check.json
python research/us-integrity/price-agents/tracing/trace_links.py research/us-integrity/price-agents/tracing/examples/live-public-source-plan.json --output /tmp/new-public-trace.json --execute
python research/us-integrity/price-agents/tracing/demo_trace.py --output /tmp/new-synthetic-trace.json
python -m unittest discover -s research/us-integrity/price-agents/tracing -p 'test_*.py'
```

Without `--execute`, only plan validation occurs. Each output path must be new. No background worker, scheduler, browser session, model call, purchase, complaint or contact is created.

## Input contract

The checked-in [plan](examples/live-public-source-plan.json) is an executable schema example. Required fields are `schema_version`, `case_id`, exact `allowed_hosts` and a nonempty `seeds` list. Each seed has an explicit URL, kind and optional exact identifiers. Kinds are `award`, `order`, `solicitation`, `item`, `specification`, `seller_catalog`, `company_filing` and `source_documentation`. Personal-profile searching is not a supported kind.

`allowed_query_keys` lists permitted keys separately for each host; the default permits none. Authentication/session keys and action parameters remain prohibited even if listed. There are no wildcard host permissions, generated source URLs or automatic company-name searches.

Limits bound logical request attempts, acquired-document count, link depth, redirects, body bytes per response, total received body bytes, DNS/transport time, retries and extracted links per HTML page. Protocol headers remain subject to the standard-library limits and absolute transport deadline. Every robots request, redirect hop, failed connection, HTTP error and retry consumes the logical request budget. The timeout separately bounds DNS resolution and the complete transport operation; worst-case per logical attempt is approximately twice `timeout_seconds`, plus process overhead.

## Link selection

The crawler parses HTML links and embedded attachment URLs as data. It never runs JavaScript, follows source instructions, submits a form or honors a page's `<base>` element. It prioritizes exact declared identifiers. Relevant PDF/text/JSON/XML/CSV attachments from the same document directory can be followed when their anchor identifies an award, order, specification, price schedule, amendment or filing. Generic navigation and unrelated links are recorded as excluded.

Exact item identifiers are matched before anchor redaction, so a numeric NSN can identify a link without retaining other phone-like numbers. Selected anchor text is shortened and contact-like content removed. Invalid target URLs are not retained because they can contain credentials or personal contact values. Every followed link still requires documentary review; an exact string in a link is not authenticated entity identity.

## Network controls

- Only HTTPS on port 443 and exact approved hostnames is allowed. Credentials, unsafe path forms, nested percent encoding, unapproved query keys, account/action routes and IP-literal hosts are rejected.
- Every DNS answer must be globally routable and cannot be multicast, reserved, unspecified or a transition-form IPv6 address. A mixed public/private answer fails closed.
- The actual TLS connection uses one validated IP directly while retaining the approved hostname for SNI and certificate/hostname verification. The peer address is checked. No second hostname lookup occurs during connection.
- Each redirect is independently URL-validated and re-resolved; loops, unapproved targets and exhausted redirect budgets stop acquisition.
- Direct sockets ignore environment HTTP proxies, browser cookies and account credentials. This deliberately does not silently fall back through a proxy whose resolution/peer cannot be checked by this implementation.
- DNS runs in a timeout-limited subprocess. Transport runs in another subprocess with an absolute wall-clock deadline, covering slow TLS/header/body delivery as well as ordinary socket timeout conditions.
- Received response bodies are capped even without a trustworthy Content-Length. Partial, encoded or unsupported content is hashed with explicit scope but is not parsed as a full document. Archive/executable content is not processed.
- Robots checks are budgeted. Supported plain-text rules are applied; 404 permits normal reads, while unavailable/denied/HTML policies defer the host. Complex wildcard rules unsupported by the standard-library parser are deferred for review. Crawl-delay and request-rate requirements cause deferral when a later run is required.
- HTTP 429 is never retried in the same run. A valid Retry-After is retained as an earliest later time, and remaining host work is deferred. HTTP 503 with Retry-After follows the same rule. A later operator must honor that state; a fresh file is not permission to ignore it. Other transient retries are bounded and default to zero.

The adapter is conservative: it can defer a legitimate source. This is an explicit access/format gap, not proof of wrongdoing or proof that the data is private. A reviewed connector acquisition can supply evidence separately, but must not be represented as a successful run of this direct transport.

## Output and source integrity

`attempts` distinguishes logical reservations, network attempts and confirmed HTTP requests. Attempt IDs are scoped to one immutable manifest, not globally unique runtime task IDs. A connection failure does not count as a confirmed sent HTTP request. Each attempt has dates, parent and relationship, status, selected content metadata, byte count and hash scope. No complete page/PDF body is retained. `link_decisions` preserves follow/exclude/defer reasons. `outstanding` records budget-exhausted work; failed and deferred work also remains in its event/decision records. `frontier_complete` is false when acquisition failed, was blocked/deferred/truncated, or left outstanding work. It never means complete nationwide or transaction coverage.

Response-body hashes identify bytes received in memory, not files saved to this repository. For durable runtime ingestion, hash the **retained manifest file itself**, use its repository-relative path, and label its scope as selected acquisition metadata. Never submit a transient wire hash as the digest of a retained manifest. Source authenticity and record interpretation require separate review.

The adapter has its own finite budget. It does not reserve attempts in the new runtime database and cannot claim enforcement of that database's budget. A coordinator may import the completed audited run honestly or add an explicit reservation bridge later. Merely importing the manifest must not invent a successful document acquisition when this run failed.

## Executed proof and limitations

[The live run](runs/live-public-source-proof-final.json) used the three documented official source URLs in the plan. It consumed three logical attempts and reached **zero HTTP requests and zero acquired documents**: direct system DNS failed before the robots requests could reach their hosts. [A separate DNS diagnostic](runs/dns-diagnostic.json) returned `gaierror` errno -3. The environment limitation was retained, rather than changing the private-address/pinned-connection controls. The final code was rerun once after review. Both runs are retained: six logical acquisition attempts in total, plus one separate DNS diagnostic, and no HTTP requests. This result demonstrates failure containment and honest coverage; it does not demonstrate successful live document extraction.

[The offline demonstration](runs/synthetic-link-trace-final.json), produced by `demo_trace.py`, simulates successful link traversal, duplicate suppression and irrelevant/unsafe-link exclusion. It is explicitly synthetic, uses fabricated transport responses and cannot enter actual procurement evidence or money totals. The unit suite independently tests URL/redirect boundaries, mixed DNS, exact-ID priority, numeric anchors, repeated attempts, rate limits, robots behavior, partial content, source instructions-as-data, pinned TLS, absolute deadlines and output overwrite prevention.

## Implementation sources

The implementation uses the official Python documentation consulted on 30 October 2026: [http.client](https://docs.python.org/3/library/http.client.html), [ssl](https://docs.python.org/3/library/ssl.html) and [urllib.parse](https://docs.python.org/3/library/urllib.parse.html). URL parsing is treated as parsing rather than security validation. This module uses APIs available in the repository's Python 3.11+ baseline and does not rely on newly documented 3.15-only arguments.
