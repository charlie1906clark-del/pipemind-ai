"""Real Chromium desktop/mobile smoke against the actual running PipeMind API.

Only synthetic data; no external deployment or industrial endpoints.
Usage: python tests/browser_smoke.py --screenshots /tmp/pipemind-shots
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

from playwright.sync_api import Page, sync_playwright, expect

BASE = os.environ.get("PIPEMIND_TEST_URL", "http://127.0.0.1:18888")
TOKEN = os.environ.get("PIPEMIND_TEST_TOKEN", "")


def visit(page: Page, view: str) -> None:
    page.locator(f'.sidebar [data-view="{view}"]').click()
    expect(page.locator(f"#view-{view}")).to_be_visible()


def run_scenario(page: Page, label: str, shots: Path) -> None:
    errors: list[str] = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(BASE, wait_until="networkidle", timeout=25_000)
    expect(page.locator("#login-overlay")).to_be_visible()
    expect(page.locator("#view-overview")).to_be_visible()
    page.locator("#token-field").fill(TOKEN)
    page.locator("#login-form button").click()
    expect(page.locator("#login-overlay")).to_be_hidden(timeout=12_000)
    expect(page.locator("#tenant-label")).to_have_text("demo")
    page.screenshot(path=str(shots / f"{label}-overview.png"), full_page=True)

    # The browser silently suppresses invalid forms before any API request.
    for form in ("#tank-form", "#cable-form", "#cost-form"):
        if not page.locator(form).evaluate("(f) => f.checkValidity()"):
            detail = page.locator(form).evaluate(
                "(f) => [...f.elements].filter(e => e.willValidate && !e.validity.valid)"
                ".map(e => ({name:e.name,value:e.value,reason:e.validationMessage}))"
            )
            raise AssertionError(f"{label}: invalid default input(s) in {form}: {detail}")

    visit(page,"tank")
    page.locator('#tank-form button[type="submit"]').click()
    expect(page.locator("#tank-end-pressure")).not_to_have_text("—", timeout=30_000)
    expect(page.locator("#tank-result-id")).to_contain_text("Run ")
    page.screenshot(path=str(shots / f"{label}-tank.png"), full_page=True)

    visit(page,"cable")
    page.locator('#cable-form button[type="submit"]').click()
    expect(page.locator("#cable-end-temp")).not_to_have_text("—", timeout=30_000)
    page.screenshot(path=str(shots / f"{label}-cable.png"), full_page=True)

    visit(page,"economics")
    page.locator('#cost-form button[type="submit"]').click()
    expect(page.locator("#cost-total")).to_contain_text("£", timeout=12_000)

    visit(page,"research")
    page.locator('#research-form button').click()
    expect(page.locator(".research-hit").first).to_be_visible(timeout=15_000)

    visit(page,"validation")
    page.locator("#load-validation-cases").click()
    expect(page.locator(".reference-card")).to_have_count(5, timeout=15_000)
    page.locator(".reference-card button").first.click()
    expect(page.locator("#validation-prepared")).to_contain_text("NOT", timeout=15_000)

    visit(page,"telemetry")
    expect(page.locator("#replay-demo")).to_be_visible()
    # Each viewport tests its own synthetic asset. Running both in the same
    # test database must not cause a misleading extra-history expectation.
    page.locator('#replay-form input[name="asset_id"]').fill(f"browser-{label}-tank")
    page.locator("#replay-demo").click()
    expect(page.locator("#replay-count")).to_contain_text("36 accepted samples", timeout=15_000)
    page.screenshot(path=str(shots / f"{label}-replay.png"), full_page=True)

    visit(page,"corridors")
    page.locator("#corridor-demo").click()
    expect(page.locator("#corridor-result")).to_contain_text(
        "SYNTHETIC_ROUTING_SCREENING", timeout=12_000
    )

    visit(page,"reports")
    page.locator("#refresh-runs").click()
    expect(page.locator(".run-button").first).to_be_visible(timeout=12_000)
    page.locator(".run-button:not([disabled])").first.click()
    expect(page.locator("#report-findings")).to_contain_text(
        "ADVISORY_DRAFT_REQUIRES_HUMAN_REVIEW", timeout=12_000
    )
    with page.expect_download(timeout=12_000) as downloaded:
        page.locator("#download-report").click()
    if not downloaded.value.suggested_filename.endswith(".md"):
        raise AssertionError(f"{label}: report did not download as Markdown")

    visit(page,"security")
    page.locator("#verify-audit").click()
    expect(page.locator("#audit-response")).to_contain_text("Chain verified", timeout=12_000)
    page.screenshot(path=str(shots / f"{label}-security.png"), full_page=True)

    page.goto(BASE, wait_until="domcontentloaded")
    width_ok = page.evaluate(
        "document.documentElement.scrollWidth <= document.documentElement.clientWidth + 2"
    )
    if not width_ok:
        raise AssertionError(f"{label}: viewport horizontal overflow")
    if errors:
        raise AssertionError(f"{label}: browser runtime errors: {errors}")
    print(f"PASS {label}: auth, tank, cable, costs, research, five references, replay, reports, tenant audit, responsiveness")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--screenshots", required=True)
    args = parser.parse_args()
    if len(TOKEN) < 24:
        raise SystemExit("Set PIPEMIND_TEST_TOKEN >= 24 characters")
    shots = Path(args.screenshots)
    shots.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for label, dimensions in [
                ("desktop", {"width": 1440, "height": 900}),
                ("mobile", {"width": 390, "height": 844}),
            ]:
                context = browser.new_context(
                    viewport=dimensions,
                    is_mobile=(label == "mobile"),
                    device_scale_factor=1,
                )
                try:
                    page = context.new_page()
                    run_scenario(page, label, shots)
                finally:
                    context.close()
        finally:
            browser.close()


if __name__ == "__main__":
    main()
