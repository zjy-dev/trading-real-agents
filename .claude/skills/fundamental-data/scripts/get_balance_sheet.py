#!/usr/bin/env python3
"""Fetch balance sheet data. Thin wrapper over tradingagents.dataflows."""
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.interface import route_to_vendor


def main() -> None:
    if not 2 <= len(sys.argv) <= 4:
        print("Usage: get_balance_sheet.py TICKER [FREQ] [CURR_DATE]", file=sys.stderr)
        sys.exit(2)
    ticker = sys.argv[1]
    freq = sys.argv[2] if len(sys.argv) >= 3 else "quarterly"
    curr_date = sys.argv[3] if len(sys.argv) == 4 else None
    print(route_to_vendor("get_balance_sheet", ticker, freq, curr_date))


if __name__ == "__main__":
    main()
