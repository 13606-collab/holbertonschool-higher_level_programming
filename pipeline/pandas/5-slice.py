#!/usr/bin/env python3
"""Module for slicing a pd.DataFrame."""


def slice(df):
    """Extract specific columns and select every 60th row.

    Args:
        df: a pd.DataFrame

    Returns:
        The sliced pd.DataFrame
    """
    df = df[["High", "Low", "Close", "Volume_(BTC)"]]
    return df.iloc[::60]
