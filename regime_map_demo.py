"""
regime_map_demo.py
------------------
Lightweight market regime classifier.

This demo classifies market conditions based on:
- trend strength (directional movement)
- volatility (price variability)

It produces a simple "regime" label such as:
- TRENDING_BULL
- TRENDING_BEAR
- CHOPPY_HIGH_VOL
- CHOPPY_LOW_VOL
"""

import pandas as pd


def compute_trend_strength(df: pd.DataFrame, window: int = 10) -> pd.Series:
    """Rolling directional movement using close-to-close changes."""
    returns = df["close"].pct_change()
    return returns.rolling(window).mean()


def compute_volatility(df: pd.DataFrame, window: int = 10) -> pd.Series:
    """Rolling standard deviation of returns."""
    returns = df["close"].pct_change()
    return returns.rolling(window).std()


def classify_regime(trend: float, vol: float, trend_thresh: float, vol_thresh: float) -> str:
    """Map numeric trend + vol into a discrete regime string."""
    if pd.isna(trend) or pd.isna(vol):
        return "UNKNOWN"

    if abs(trend) >= trend_thresh:
        if trend > 0:
            return "TRENDING_BULL" if vol <= vol_thresh else "TRENDING_BULL_HIGH_VOL"
        else:
            return "TRENDING_BEAR" if vol <= vol_thresh else "TRENDING_BEAR_HIGH_VOL"
    else:
        return "CHOPPY_HIGH_VOL" if vol > vol_thresh else "CHOPPY_LOW_VOL"


def compute_regime_map(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add trend_strength, volatility and regime columns to the DataFrame.
    """
    df = df.copy()

    df["trend_strength"] = compute_trend_strength(df, window=10)
    df["volatility"] = compute_volatility(df, window=10)

    # Use simple quantile-based thresholds for demo purposes
    trend_thresh = df["trend_strength"].abs().quantile(0.7)
    vol_thresh = df["volatility"].quantile(0.7)

    df["regime"] = df.apply(
        lambda row: classify_regime(
            trend=row["trend_strength"],
            vol=row["volatility"],
            trend_thresh=trend_thresh,
            vol_thresh=vol_thresh,
        ),
        axis=1,
    )

    return df
