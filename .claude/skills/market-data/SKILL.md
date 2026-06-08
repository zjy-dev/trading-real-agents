---
name: market-data
description: >
  Fetch OHLCV stock price data and technical indicators for a ticker. Use
  when a subagent needs raw price history or indicator values
  (close_50_sma, close_200_sma, close_10_ema, macd, macds, macdh, rsi,
  boll, boll_ub, boll_lb, atr, vwma). Vendor defaults to yfinance (no API
  key); set ALPHA_VANTAGE_API_KEY to optionally enable alpha_vantage.
---

# Market Data Skill

Provides OHLCV price data and technical indicators. Scripts are thin wrappers
over `tradingagents.dataflows` and print a formatted string to stdout.

## Scripts

### get_stock_data.py
```
python .claude/skills/market-data/scripts/get_stock_data.py SYMBOL START_DATE END_DATE
```
- `SYMBOL`: e.g. `AAPL`, `NVDA`, `0700.HK`
- `START_DATE` / `END_DATE`: `yyyy-mm-dd`

Returns a formatted OHLCV table. Call this **first** before requesting indicators.

### get_indicators.py
```
python .claude/skills/market-data/scripts/get_indicators.py SYMBOL INDICATOR CURR_DATE [LOOK_BACK_DAYS]
```
- `INDICATOR`: single name or comma-separated list (`rsi`, `macd`, `close_50_sma`, ...)
- `CURR_DATE`: `yyyy-mm-dd`
- `LOOK_BACK_DAYS`: optional integer, default `30`

Supported indicators: `close_50_sma`, `close_200_sma`, `close_10_ema`, `macd`,
`macds`, `macdh`, `rsi`, `boll`, `boll_ub`, `boll_lb`, `atr`, `vwma`.

## Vendor / keys
- Default vendor: **yfinance** (zero key, works out of the box).
- Optional: `export ALPHA_VANTAGE_API_KEY=...` and set `data_vendors` /
  `tool_vendors` (via `TRADINGAGENTS_*`) to route to alpha_vantage; on
  rate-limit it auto-falls back to yfinance.
