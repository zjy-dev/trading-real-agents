"""Thin smoke-test entry point for the subagents + skills setup.

The trading analysis itself now runs as subagents + skills driven by an agent
platform (Claude Code / Trae) — see AGENTS.md. This script only exercises the
data layer that the skills reuse, so you can confirm the foundation works
without any LLM or API key (defaults to yfinance).

Usage:
    python3 main.py [TICKER] [TRADE_DATE]
"""

import sys

from tradingagents.dataflows.interface import route_to_vendor


def main() -> None:
    ticker = sys.argv[1] if len(sys.argv) > 1 else "NVDA"
    trade_date = sys.argv[2] if len(sys.argv) > 2 else "2024-05-10"

    checks = [
        ("get_stock_data", (ticker, "2024-05-01", trade_date)),
        ("get_indicators", (ticker, "rsi", trade_date, 30)),
        ("get_fundamentals", (ticker, trade_date)),
        ("get_news", (ticker, "2024-05-03", trade_date)),
        ("get_global_news", (trade_date, None, None)),
    ]

    failures = 0
    for method, args in checks:
        try:
            result = route_to_vendor(method, *args)
            ok = bool(result and str(result).strip())
            print(f"[{'OK' if ok else 'EMPTY'}] {method} -> {len(str(result))} chars")
            failures += 0 if ok else 1
        except Exception as exc:  # noqa: BLE001 - smoke test surfaces any failure
            print(f"[FAIL] {method}: {type(exc).__name__}: {exc}")
            failures += 1

    if failures:
        print(f"\n{failures} check(s) failed.")
        sys.exit(1)
    print("\nAll data-layer checks passed.")


if __name__ == "__main__":
    main()
