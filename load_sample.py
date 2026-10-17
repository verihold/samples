"""Load a Verihold candle CSV, report coverage and gaps, and resample it.

Usage: python load_sample.py path/to/file.csv [--tf 5min]
"""
import argparse

import pandas as pd


def load(path):
    df = pd.read_csv(path, comment="#", parse_dates=["time_utc"], index_col="time_utc")
    df.index = df.index.tz_localize("UTC")
    return df.sort_index()


def gaps(df, min_gap="5min"):
    step = df.index.to_series().diff()
    big = step[step > pd.Timedelta(min_gap)]
    return [(t - d, t, d) for t, d in big.items()]


def resample(df, tf):
    return df.resample(tf, label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"}
    ).dropna()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--tf", default="5min", help="pandas offset to resample to, e.g. 5min, 1h, 1D")
    args = ap.parse_args()

    df = load(args.csv)
    print(f"{len(df):,} candles from {df.index[0]} to {df.index[-1]}")
    g = gaps(df)
    print(f"{len(g)} gaps longer than 5 minutes")
    for start, end, d in g[:10]:
        print(f"  {start:%Y-%m-%d %H:%M} -> {end:%Y-%m-%d %H:%M}  ({d})")
    r = resample(df, args.tf)
    print(f"\nResampled to {args.tf}: {len(r):,} candles")
    print(r.tail())


if __name__ == "__main__":
    main()
