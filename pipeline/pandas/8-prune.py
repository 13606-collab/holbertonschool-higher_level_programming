#!/usr/bin/env python3
"""Module for pruning a pd.DataFrame."""


def prune(df):
    """Remove entries where Close has NaN values.

    Args:
        df: a pd.DataFrame

    Returns:
        The modified pd.DataFrame
    """
    return df.dropna(subset=["Close"])
