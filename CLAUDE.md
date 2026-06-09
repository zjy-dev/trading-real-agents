# CLAUDE.md

This project runs as **subagents + skills**. See **[AGENTS.md](./AGENTS.md)** for
the full orchestration guide: skills (data access), subagent roles, the
end-to-end pipeline, and output-format contracts.

## Quick start
Just ask the main agent to run an analysis, e.g.:

> run full trading analysis for NVDA on 2024-05-10

The **main agent** orchestrates the pipeline directly (per AGENTS.md), dispatching
each subagent at the top level so every subagent call is visible: 4 analysts →
bull/bear debate → research manager → trader → risk debate → portfolio manager.
All artifacts are written to `./analysis/<TICKER>/<TRADE_DATE>/`, ending with
`final_decision.md`.

## Subagents
`.claude/agents/`: `market-analyst`, `sentiment-analyst`,
`news-analyst`, `fundamentals-analyst`, `bull-researcher`, `bear-researcher`,
`research-manager`, `trader`, `risk-debators`, `portfolio-manager`.

## Skills
`.claude/skills/`: `market-data`, `fundamental-data`, `news-data`,
`social-sentiment`. Scripts reuse `tradingagents/dataflows/` and default to
yfinance (no API key). Run with `uv run` from the repo root.
