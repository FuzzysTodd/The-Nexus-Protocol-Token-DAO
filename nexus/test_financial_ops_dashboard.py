"""Tests for the financial ops dashboard real-time refresh UI."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def test_financial_ops_dashboard_has_live_refresh_controls():
    html = (REPO_ROOT / "financial-ops-dashboard.html").read_text()
    assert 'id="refresh-report"' in html
    assert 'id="live-status"' in html
    assert 'id="last-checked"' in html
    assert 'aria-live="polite"' in html


def test_financial_ops_dashboard_polls_for_updates():
    html = (REPO_ROOT / "financial-ops-dashboard.html").read_text()
    assert "const REFRESH_INTERVAL_MS = 15000;" in html
    assert "window.setInterval(loadReport, REFRESH_INTERVAL_MS);" in html
    assert "fetch(REPORT_URL, { cache: 'no-store' })" in html


def test_financial_ops_dashboard_replaces_previous_rendered_items():
    html = (REPO_ROOT / "financial-ops-dashboard.html").read_text()
    for reset_line in [
        "botList.innerHTML = '';",
        "findingList.innerHTML = '';",
        "signalList.innerHTML = '';",
        "logList.innerHTML = '';",
        "actionList.innerHTML = '';",
    ]:
        assert reset_line in html
