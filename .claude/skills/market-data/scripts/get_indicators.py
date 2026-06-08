#!/usr/bin/env python3
"""Fetch one or more technical indicators. Thin wrapper over tradingagents.dataflows.

Accepts a single indicator or a comma-separated list (mirrors the original
get_indicators tool behavior).
"""
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.interface import route_to_vendor


def main() -> None:
    if len(sys.argv) not in (4, 5):
        print(
            "Usage: get_indicators.py SYMBOL INDICATOR CURR_DATE [LOOK_BACK_DAYS]",
            file=sys.stderr,
        )
        sys.exit(2)
    symbol, indicator, curr_date = sys.argv[1], sys.argv[2], sys.argv[3]
    look_back_days = int(sys.argv[4]) if len(sys.argv) == 5 else 30

    indicators = [i.strip().lower() for i in indicator.split(",") if i.strip()]
    results = []
    for ind in indicators:
        try:
            results.append(
                route_to_vendor("get_indicators", symbol, ind, curr_date, look_back_days)
            )
        except ValueError as exc:
            results.append(str(exc))
    print("\n\n".join(results))


if __name__ == "__main__":
    main()
