---
name: fundamental-data
description: >
  Fetch company fundamentals for a ticker: comprehensive fundamentals
  summary, balance sheet, cash flow statement, and income statement. Use
  when a subagent needs financial statements, valuation inputs, margins,
  liquidity, or capital structure data. Vendor defaults to yfinance (no API
  key); set ALPHA_VANTAGE_API_KEY to optionally enable alpha_vantage.
---

# Fundamental Data Skill

Provides company financial data. Scripts are thin wrappers over
`tradingagents.dataflows` and print a formatted report to stdout.

## Scripts

### get_fundamentals.py
```
python3 ${CLAUDE_SKILL_DIR}/scripts/get_fundamentals.py TICKER CURR_DATE
```
Comprehensive fundamentals report. `CURR_DATE` is `yyyy-mm-dd`.

### get_balance_sheet.py
```
python3 ${CLAUDE_SKILL_DIR}/scripts/get_balance_sheet.py TICKER [FREQ] [CURR_DATE]
```

### get_cashflow.py
```
python3 ${CLAUDE_SKILL_DIR}/scripts/get_cashflow.py TICKER [FREQ] [CURR_DATE]
```

### get_income_statement.py
```
python3 ${CLAUDE_SKILL_DIR}/scripts/get_income_statement.py TICKER [FREQ] [CURR_DATE]
```
- `FREQ`: `annual` or `quarterly` (default `quarterly`)
- `CURR_DATE`: optional `yyyy-mm-dd`

## Vendor / keys
- Default vendor: **yfinance** (zero key).
- Optional alpha_vantage via `ALPHA_VANTAGE_API_KEY` + `data_vendors`/`tool_vendors`;
  auto-falls back to yfinance on rate-limit.
