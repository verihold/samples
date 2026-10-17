# Verihold samples

Tools for working with [Verihold](https://verihold.dev/?ref=github) Pocket Option OTC candle files.

Pocket Option's OTC pairs are broker-generated quotes, so exchange data (Binance, TradingView feeds) shows different prices at the same timestamps. Public Pocket Option API wrappers only return a short recent window of OTC history. Verihold has recorded the OTC feed continuously since July 4, 2026.

## Get the free sample

Join the early-access list on [verihold.dev](https://verihold.dev/?ref=github) and you'll get a 7-day BTCUSD OTC CSV by email. Compare it candle by candle with your Pocket Option chart.

## File format

```
# Verihold - Pocket Option OTC candles (broker-generated quotes), times in UTC
# Licensed to buyer V-XXXXXXXXXX, order N, generated YYYY-MM-DD HH:MM UTC
# Personal-use license: no resale or redistribution. https://verihold.dev/#license
time_utc,open,high,low,close
```

| Column | Meaning |
|---|---|
| `time_utc` | Candle open time, UTC, `YYYY-MM-DD HH:MM:SS` |
| `open`, `high`, `low`, `close` | Prices as Pocket Option displayed them |

There is no volume column: Pocket Option OTC quotes don't carry trade volume. Lines starting with `#` are the license header. Gaps can occur when the platform was down or a pair was closed.

## Load it

```bash
pip install pandas
python load_sample.py verihold_BTCUSDotc_1m_....csv
```

`load_sample.py` loads a file, prints coverage and gaps, and shows how to resample 1-minute candles to any timeframe.

```python
import pandas as pd
df = pd.read_csv("file.csv", comment="#", parse_dates=["time_utc"], index_col="time_utc")
```

## Full data

Pair Pack (1 pair, last 30 days, 11 timeframes) $19 · Monthly Updates $15/mo · Full Archive on request. Pay in USDT, BTC or ETH. See [verihold.dev/#pricing](https://verihold.dev/?ref=github#pricing).

Not affiliated with Pocket Option. Market data, not financial advice.
