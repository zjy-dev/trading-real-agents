---
name: news-data
description: >
  Fetch news for a ticker (company news), global/macro news, and insider
  transactions. Use when a subagent needs recent headlines, world affairs
  context, or insider buying/selling activity. Vendor defaults to yfinance
  (no API key); set ALPHA_VANTAGE_API_KEY to optionally enable alpha_vantage.
---

# News Data Skill

Provides news and insider data. Scripts are thin wrappers over
`tradingagents.dataflows` and print a formatted string to stdout.

## Scripts

### get_news.py
```
python .claude/skills/news-data/scripts/get_news.py TICKER START_DATE END_DATE
```
Company-specific news between two `yyyy-mm-dd` dates.

### get_global_news.py
```
python .claude/skills/news-data/scripts/get_global_news.py CURR_DATE [LOOK_BACK_DAYS] [LIMIT]
```
Global/macro news. `LOOK_BACK_DAYS` and `LIMIT` are optional; omit to inherit
config defaults (`global_news_lookback_days`, `global_news_article_limit`).

### get_insider_transactions.py
```
python .claude/skills/news-data/scripts/get_insider_transactions.py TICKER
```
Insider transaction report.

## Vendor / keys
- Default vendor: **yfinance** (zero key).
- Optional alpha_vantage via `ALPHA_VANTAGE_API_KEY` + `data_vendors`/`tool_vendors`;
  auto-falls back to yfinance on rate-limit.
