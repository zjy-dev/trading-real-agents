# CLAUDE.md

This project runs as **subagents + skills**. See **[AGENTS.md](./AGENTS.md)** for
the full orchestration guide: skills (data access), subagent roles, the
end-to-end pipeline, and output-format contracts.

## Quick start
Ask the `orchestrator` subagent to run an analysis, e.g.:

> run full trading analysis for NVDA on 2024-05-10

It drives the pipeline (4 analysts → bull/bear debate → research manager →
trader → risk debate → portfolio manager) and writes all artifacts to
`./analysis/<TICKER>/<TRADE_DATE>/`, ending with `final_decision.md`.

## Subagents
`.claude/agents/`: `orchestrator`, `market-analyst`, `sentiment-analyst`,
`news-analyst`, `fundamentals-analyst`, `bull-researcher`, `bear-researcher`,
`research-manager`, `trader`, `risk-debators`, `portfolio-manager`.

## Skills
`.claude/skills/`: `market-data`, `fundamental-data`, `news-data`,
`social-sentiment`. Scripts reuse `tradingagents/dataflows/` and default to
yfinance (no API key). Run with `uv run` from the repo root.
