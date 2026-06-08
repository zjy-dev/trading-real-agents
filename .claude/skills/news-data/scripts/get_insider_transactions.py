#!/usr/bin/env python3
"""Fetch insider transactions. Thin wrapper over tradingagents.dataflows."""
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.interface import route_to_vendor


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: get_insider_transactions.py TICKER", file=sys.stderr)
        sys.exit(2)
    ticker = sys.argv[1]
    print(route_to_vendor("get_insider_transactions", ticker))


if __name__ == "__main__":
    main()
