#!/usr/bin/env python3
"""Fetch OHLCV stock price data. Thin wrapper over tradingagents.dataflows."""
import os
import sys

# Bootstrap: ensure the repo root is importable regardless of cwd.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.interface import route_to_vendor


def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: get_stock_data.py SYMBOL START_DATE END_DATE", file=sys.stderr)
        sys.exit(2)
    symbol, start_date, end_date = sys.argv[1], sys.argv[2], sys.argv[3]
    print(route_to_vendor("get_stock_data", symbol, start_date, end_date))


if __name__ == "__main__":
    main()
