#!/usr/bin/env python3
"""Fetch Reddit posts. Thin wrapper over tradingagents.dataflows."""
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tradingagents.dataflows.reddit import fetch_reddit_posts


def main() -> None:
    if not 2 <= len(sys.argv) <= 3:
        print("Usage: get_reddit.py TICKER [LIMIT_PER_SUB]", file=sys.stderr)
        sys.exit(2)
    ticker = sys.argv[1]
    limit_per_sub = int(sys.argv[2]) if len(sys.argv) == 3 else 5
    print(fetch_reddit_posts(ticker, limit_per_sub=limit_per_sub))


if __name__ == "__main__":
    main()
