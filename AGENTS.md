# TradingAgents — Agent Orchestration Guide

A multi-agent trading-analysis framework, implemented as **subagents + skills**
for agent platforms (Claude Code, Trae, etc.). Specialized subagents (analysts,
researchers, managers, trader, risk debate) collaborate to produce a final
trade decision. State is passed between agents via files; data is fetched by
self-contained skill scripts that default to yfinance (no API key required).

## Layout
- `.claude/agents/*.md` — subagent definitions (role, prompt, I/O contract).
- `.claude/skills/<skill>/` — `SKILL.md` + `scripts/*.py` data-fetch wrappers.
- `tradingagents/dataflows/` — the data layer the skill scripts reuse.

## Skills (data access)
All scripts print a formatted string to stdout. Run via `python3` from the repo
root (vendor defaults to yfinance, zero key; optional `ALPHA_VANTAGE_API_KEY`
enables alpha_vantage with auto-fallback):

- **market-data**: `get_stock_data.py SYMBOL START END`, `get_indicators.py SYMBOL IND CURR_DATE [LOOKBACK]`
- **fundamental-data**: `get_fundamentals.py TICKER CURR_DATE`, `get_balance_sheet.py`, `get_cashflow.py`, `get_income_statement.py` (`TICKER [FREQ] [CURR_DATE]`)
- **news-data**: `get_news.py TICKER START END`, `get_global_news.py CURR_DATE [LOOKBACK] [LIMIT]`, `get_insider_transactions.py TICKER`
- **social-sentiment**: `get_stocktwits.py TICKER [LIMIT]`, `get_reddit.py TICKER [LIMIT_PER_SUB]`

## How to run a full analysis
Ask the `orchestrator` subagent: *"run full trading analysis for NVDA on 2024-05-10"*.
On platforms without subagent dispatch, follow the pipeline below directly.

## Pipeline
Inputs: `TICKER`, `TRADE_DATE` (`yyyy-mm-dd`), `MAX_DEBATE_ROUNDS=1`,
`MAX_RISK_ROUNDS=1`, `ASSET_TYPE=stock|crypto`.
Working directory: `./analysis/<TICKER>/<TRADE_DATE>/`. State files replace the
original shared graph state.

1. **Analysts (independent, parallelizable)** — `market-analyst`,
   `sentiment-analyst`, `news-analyst`, `fundamentals-analyst` →
   `market_report.md` / `sentiment_report.md` / `news_report.md` /
   `fundamentals_report.md`.
2. **Investment debate** — for `MAX_DEBATE_ROUNDS` rounds, `bull-researcher`
   then `bear-researcher`, appending to `debate_history.md`.
3. **research-manager** — reads debate + reports → `investment_plan.md`
   (contains `**Recommendation**`).
4. **trader** — reads `investment_plan.md` → `trader_plan.md` (contains
   `**Action**`, ends with `FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**`).
5. **risk-debators** — reads `trader_plan.md` + reports, runs
   aggressive→conservative→neutral for `MAX_RISK_ROUNDS` rounds →
   `risk_debate.md`.
6. **portfolio-manager (terminal)** — synthesizes everything →
   `final_decision.md` (contains `**Rating**`).

## Output-format contracts (preserve exactly)
- `investment_plan.md`: `**Recommendation**`, `**Rationale**`, `**Strategic Actions**`.
- `trader_plan.md`: `**Action**`, `**Reasoning**`, optional `**Entry Price**` /
  `**Stop Loss**` / `**Position Sizing**`, then `FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**`.
- `final_decision.md`: `**Rating**`, `**Executive Summary**`, `**Investment Thesis**`,
  optional `**Price Target**` / `**Time Horizon**`.
- Ratings use the 5-tier scale: Buy / Overweight / Hold / Underweight / Sell.

## Verify
Smoke-test the data layer with no API key:
```
python3 .claude/skills/market-data/scripts/get_stock_data.py NVDA 2024-05-01 2024-05-10
python3 .claude/skills/news-data/scripts/get_news.py NVDA 2024-05-03 2024-05-10
```
