#!/usr/bin/env python3
"""Fetch StockTwits messages. Thin wrapper over tradingagents.dataflows."""
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.stocktwits import fetch_stocktwits_messages


def main() -> None:
    if not 2 <= len(sys.argv) <= 3:
        print("Usage: get_stocktwits.py TICKER [LIMIT]", file=sys.stderr)
        sys.exit(2)
    ticker = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) == 3 else 30
    print(fetch_stocktwits_messages(ticker, limit=limit))


if __name__ == "__main__":
    main()
