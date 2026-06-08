---
name: social-sentiment
description: >
  Fetch retail/social sentiment for a ticker from StockTwits (with
  Bullish/Bearish tallies) and Reddit finance subreddits (wallstreetbets,
  stocks, investing). Use when a subagent needs crowd mood, message volume,
  or social buzz. Public endpoints, no API key required; degrades gracefully
  to a placeholder string if a source is unreachable.
---

# Social Sentiment Skill

Provides social media sentiment data. Scripts print a formatted plaintext
block to stdout, suitable for direct inclusion in a report.

## Scripts

### get_stocktwits.py
```
python3 ${CLAUDE_SKILL_DIR}/scripts/get_stocktwits.py TICKER [LIMIT]
```
Recent StockTwits messages plus a Bullish/Bearish tally. `LIMIT` default `30`.

### get_reddit.py
```
python3 ${CLAUDE_SKILL_DIR}/scripts/get_reddit.py TICKER [LIMIT_PER_SUB]
```
Recent posts mentioning the ticker across wallstreetbets / stocks / investing.
`LIMIT_PER_SUB` default `5`.

## Keys
None required. Both use public endpoints and return a placeholder string
rather than raising if the source is down or rate-limited.
