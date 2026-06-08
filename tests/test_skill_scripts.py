"""End-to-end smoke tests for the skill scripts under .claude/skills.

Each skill script is invoked exactly as a subagent would (as a subprocess),
so this verifies the scripts run, resolve `import tradingagents`, and emit
non-empty output. Uses yfinance (zero API key). Social sources (StockTwits /
Reddit) degrade gracefully, so they are asserted to run and print *something*
rather than to return live data.
"""

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS = REPO_ROOT / ".claude" / "skills"

TICKER = "NVDA"
TRADE_DATE = "2024-05-10"
START_DATE = "2024-05-01"

# (skill, script, args) — args mirror each script's CLI signature.
SCRIPT_CASES = [
    ("market-data", "get_stock_data.py", [TICKER, START_DATE, TRADE_DATE]),
    ("market-data", "get_indicators.py", [TICKER, "rsi", TRADE_DATE, "30"]),
    ("fundamental-data", "get_fundamentals.py", [TICKER, TRADE_DATE]),
    ("fundamental-data", "get_balance_sheet.py", [TICKER, "quarterly", TRADE_DATE]),
    ("fundamental-data", "get_cashflow.py", [TICKER, "quarterly", TRADE_DATE]),
    ("fundamental-data", "get_income_statement.py", [TICKER, "quarterly", TRADE_DATE]),
    ("news-data", "get_news.py", [TICKER, "2024-05-03", TRADE_DATE]),
    ("news-data", "get_global_news.py", [TRADE_DATE]),
    ("news-data", "get_insider_transactions.py", [TICKER]),
    ("social-sentiment", "get_stocktwits.py", [TICKER, "5"]),
    ("social-sentiment", "get_reddit.py", [TICKER, "2"]),
]


@pytest.mark.integration
@pytest.mark.parametrize(
    "skill, script, args",
    SCRIPT_CASES,
    ids=[f"{skill}/{script}" for skill, script, _ in SCRIPT_CASES],
)
def test_skill_script_runs(skill, script, args):
    path = SKILLS / skill / "scripts" / script
    assert path.exists(), f"missing script: {path}"

    result = subprocess.run(
        [sys.executable, str(path), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )

    assert result.returncode == 0, f"{script} failed: {result.stderr}"
    assert result.stdout.strip(), f"{script} produced no output"


@pytest.mark.integration
def test_script_usage_error_exits_nonzero():
    """Scripts called with wrong arity should exit non-zero, not crash silently."""
    path = SKILLS / "market-data" / "scripts" / "get_stock_data.py"
    result = subprocess.run(
        [sys.executable, str(path), TICKER],  # missing dates
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode != 0
    assert "Usage" in result.stderr
