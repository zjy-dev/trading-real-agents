# Trading Real Agents — Subagents + Skills

A multi-agent trading-analysis framework packaged as **subagents + skills** for
agent platforms (Claude Code, Trae, etc.). Specialized subagents — analysts,
researchers, managers, a trader, and a risk-debate team — collaborate to produce
a final trade decision. State flows between agents through files; market data is
fetched by self-contained skill scripts that default to yfinance and need **no
API key**.

This repository contains only the agent layer (`.claude/`) plus the data layer
(`tradingagents/dataflows/`) that the skills reuse. There is no LLM client or
graph-orchestration code — orchestration is driven by the agent platform.

## Layout
```
.claude/
  agents/    11 subagents (orchestrator + analysts + researchers + managers + trader + risk)
  skills/    4 skills (market-data, fundamental-data, news-data, social-sentiment) + scripts
AGENTS.md    orchestration guide (platform-agnostic)
CLAUDE.md    Claude Code entry point
tradingagents/
  dataflows/        data layer reused by the skill scripts
  default_config.py vendor routing + TRADINGAGENTS_* env overrides
tests/       pytest suite (skill-script smoke + data-layer unit tests)
```

## Quick start
This project uses **[uv](https://docs.astral.sh/uv/)** to manage the Python
environment.
1. Sync the environment (creates `.venv`, installs the data layer so
   `import tradingagents` resolves):
   ```
   uv sync
   ```
2. Smoke-test the skill scripts (no API key, defaults to yfinance):
   ```
   uv run pytest tests/
   ```
3. Run a full analysis on your agent platform. In Claude Code, ask the
   `orchestrator` subagent:
   > run full trading analysis for NVDA on 2024-05-10

   Artifacts are written to `./analysis/<TICKER>/<TRADE_DATE>/`, ending with
   `final_decision.md`.

See **[AGENTS.md](./AGENTS.md)** for the full pipeline, subagent roles, skill
usage, and output-format contracts.

## Pipeline (summary)
4 analysts (market / sentiment / news / fundamentals) → bull/bear investment
debate → research manager → trader → aggressive/conservative/neutral risk
debate → portfolio manager (final decision).

## Data vendors
- Default: **yfinance** (zero key, works out of the box).
- Optional: set `ALPHA_VANTAGE_API_KEY` and configure `data_vendors` /
  `tool_vendors` (via `TRADINGAGENTS_*`) to use alpha_vantage; it auto-falls
  back to yfinance on rate-limit.

## Tests
```
uv run pytest tests/
```
`test_skill_scripts.py` runs every skill script as a subprocess (yfinance,
zero key); the remaining tests cover the data layer (config, env overrides,
ticker handling).
