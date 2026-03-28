"""Tests for the Nexus Contract Withdrawal Manager dashboard files."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# withdraw.html
# ---------------------------------------------------------------------------

def test_withdraw_html_exists():
    assert (REPO_ROOT / "withdraw.html").is_file()


def test_withdraw_html_loads_ethers_and_withdraw_script():
    html = (REPO_ROOT / "withdraw.html").read_text()
    assert "ethers" in html and "umd.min.js" in html
    assert '<script src="./withdraw.js"></script>' in html


def test_withdraw_html_has_wallet_connect_button():
    html = (REPO_ROOT / "withdraw.html").read_text()
    assert 'id="connect-btn"' in html
    assert "Connect Wallet" in html


def test_withdraw_html_has_add_contract_form():
    html = (REPO_ROOT / "withdraw.html").read_text()
    assert 'id="add-contract-form"' in html
    assert 'id="input-address"' in html
    assert 'id="input-method"' in html


def test_withdraw_html_has_contract_list_section():
    html = (REPO_ROOT / "withdraw.html").read_text()
    assert 'id="contract-list"' in html
    assert "My Contracts" in html


def test_withdraw_html_has_withdraw_methods_in_select():
    html = (REPO_ROOT / "withdraw.html").read_text()
    for method in [
        "withdraw()", "withdrawAll()", "release(address)", "claimRewards()"
    ]:
        assert method in html


def test_withdraw_html_explains_proxy_pattern():
    html = (REPO_ROOT / "withdraw.html").read_text()
    assert "EIP-1967" in html
    assert "fallback" in html
    assert "implementation" in html


def test_withdraw_html_mentions_local_storage_only():
    html = (REPO_ROOT / "withdraw.html").read_text()
    assert "Local-only storage" in html


# ---------------------------------------------------------------------------
# withdraw.js – proxy ABI
# ---------------------------------------------------------------------------

def test_withdraw_js_exists():
    assert (REPO_ROOT / "withdraw.js").is_file()


def test_withdraw_js_embeds_proxy_abi_events():
    script = (REPO_ROOT / "withdraw.js").read_text()
    for event in ["AdminChanged", "BeaconUpgraded", "Upgraded"]:
        assert event in script


def test_withdraw_js_proxy_abi_has_fallback_and_receive():
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert '"fallback"' in script
    assert '"receive"' in script


def test_withdraw_js_proxy_abi_constructor_fields():
    script = (REPO_ROOT / "withdraw.js").read_text()
    for param in ["_logic", "admin_", "_data"]:
        assert param in script


def test_withdraw_js_proxy_abi_is_valid_json_embedded():
    """Extract PROXY_ABI array literal and verify it parses as JSON."""
    script = (REPO_ROOT / "withdraw.js").read_text()
    start = script.index("const PROXY_ABI = [")
    # Grab from the opening bracket
    start = script.index("[", start)
    # Walk to the matching closing bracket
    depth = 0
    end = start
    for i, ch in enumerate(script[start:], start):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                end = i
                break
    raw = script[start:end + 1]
    parsed = json.loads(raw)
    assert isinstance(parsed, list)
    assert len(parsed) >= 5  # constructor + 3 events + fallback + receive


# ---------------------------------------------------------------------------
# withdraw.js – withdraw methods
# ---------------------------------------------------------------------------

def test_withdraw_js_has_withdraw_method_selectors():
    script = (REPO_ROOT / "withdraw.js").read_text()
    # Standard 4-byte selectors
    assert "0x3ccfd60b" in script   # withdraw()
    assert "0x853828b6" in script   # withdrawAll()
    assert "0x19165587" in script   # release(address)


def test_withdraw_js_encodes_release_with_connected_wallet_address():
    script = (REPO_ROOT / "withdraw.js").read_text()
    release_branch = 'if (method === "release(address)")'
    custom_branch = 'else if (method === "custom" && customSelector)'
    assert release_branch in script
    assert custom_branch in script
    assert script.index(release_branch) < script.index(custom_branch)
    assert 'encodeFunctionData("release", [signerAddress])' in script


def test_withdraw_js_defines_storage_key():
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert "nexus_withdraw_contracts" in script


def test_withdraw_js_exports_nexus_withdraw_namespace():
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert "NexusWithdraw" in script
    assert "connectWallet" in script
    assert "withdrawFromContract" in script


def test_withdraw_js_escape_html_helper_present():
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert "escapeHtml" in script


def test_withdraw_js_uses_escaped_balance_ids_for_render_and_lookup():
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert 'id="bal-${escapeHtml(c.address)}"' in script
    assert 'document.getElementById("bal-" + escapeHtml(c.address))' in script


def test_withdraw_js_handles_custom_selector():
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert (
        "customSelector" in script
        or "custom-selector" in script
        or "custom_selector" in script
    )


def test_withdraw_js_no_private_key_literals():
    """Ensure no hard-coded private key placeholder was left in the script."""
    script = (REPO_ROOT / "withdraw.js").read_text()
    assert "YOUR_PRIVATE_KEY" not in script
    assert "PRIVATE_KEY" not in script
