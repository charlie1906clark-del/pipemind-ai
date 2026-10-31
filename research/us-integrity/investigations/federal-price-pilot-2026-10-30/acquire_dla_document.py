#!/usr/bin/env python3
"""Replay one exact public award route, at most GET plus normal notice consent.

Full PDF is an analysis input containing contact/address blocks. Keep its output
outside tracked public artifacts; publish only reviewed selected excerpts.
"""
import argparse
import hashlib
import http.cookiejar
import json
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlencode
from urllib.request import build_opener, HTTPCookieProcessor, Request

URL = "https://dibbs2.bsm.dla.mil/Downloads/Awards/09JUL26/SPE4A626PW775.PDF"


class Notice(HTMLParser):
    def __init__(self):
        super().__init__()
        self.action, self.fields, self.agree = None, {}, False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "form" and attrs.get("method", "").lower() == "post":
            self.action = attrs.get("action")
        if tag == "input" and attrs.get("name"):
            self.fields[attrs["name"]] = attrs.get("value", "")
            if attrs["name"] == "butAgree" and attrs.get("value") == "OK":
                self.agree = True


def acquire(output):
    output.mkdir(parents=True, exist_ok=False)
    manifest = {"source_url": URL, "observed_at": datetime.now(timezone.utc).isoformat(), "operations": [], "hidden_form_values_retained": False, "max_operations": 2, "original_pdf_suitable_for_public_commit": False}
    opener = build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def fetch(request, method):
        step = {"method": method}
        manifest["operations"].append(step)
        with opener.open(request, timeout=20) as response:
            body = response.read(5_000_001)
            step.update(status=response.status, content_type=response.headers.get("Content-Type"), final_url=response.url)
        if len(body) > 5_000_000:
            raise ValueError("Response size cap exceeded")
        return body

    try:
        body = fetch(URL, "GET")
        if not body.startswith(b"%PDF-"):
            notice = Notice()
            notice.feed(body.decode("utf-8"))
            if not notice.action or not notice.agree:
                raise ValueError("Expected ordinary public notice absent; stop")
            action = urljoin(URL, notice.action)
            parsed = urlsplit(action)
            if parsed.scheme != "https" or parsed.netloc != "dibbs2.bsm.dla.mil" or parsed.path.lower() != "/dodwarning.aspx":
                raise ValueError("Unexpected notice action; stop")
            notice.fields["butAgree"] = "OK"
            body = fetch(Request(action, data=urlencode(notice.fields).encode()), "POST ordinary public notice consent")
        if not body.startswith(b"%PDF-"):
            raise ValueError("No PDF returned; stop")
        (output / "SPE4A626PW775.pdf").write_bytes(body)
        manifest.update(result="pdf_acquired", original_sha256=hashlib.sha256(body).hexdigest(), original_bytes=len(body))
    except Exception as exc:
        manifest.update(result="failed_no_retry", error=type(exc).__name__ + ": " + str(exc))
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(acquire(args.output), indent=2))
