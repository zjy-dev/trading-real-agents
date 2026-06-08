#!/usr/bin/env python3
"""Fetch global/macro news. Thin wrapper over tradingagents.dataflows."""
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.interface import route_to_vendor


def main() -> None:
    if not 2 <= len(sys.argv) <= 4:
        print("Usage: get_global_news.py CURR_DATE [LOOK_BACK_DAYS] [LIMIT]", file=sys.stderr)
        sys.exit(2)
    curr_date = sys.argv[1]
    look_back_days = int(sys.argv[2]) if len(sys.argv) >= 3 else None
    limit = int(sys.argv[3]) if len(sys.argv) == 4 else None
    print(route_to_vendor("get_global_news", curr_date, look_back_days, limit))


if __name__ == "__main__":
    main()
