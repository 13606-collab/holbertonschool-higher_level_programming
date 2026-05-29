#!/usr/bin/env python3
"""Module for concatenating two pd.DataFrames."""
import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Index both DataFrames and concatenate selected rows from df2 to df1.

    Args:
        df1: a pd.DataFrame (coinbase)
        df2: a pd.DataFrame (bitstamp)

    Returns:
        The concatenated pd.DataFrame
    """
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
