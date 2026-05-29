#!/usr/bin/env python3
"""Module for hierarchical concatenation of two pd.DataFrames."""
import pandas as pd

index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate bitstamp and coinbase DataFrames with rearranged MultiIndex.

    Args:
        df1: a pd.DataFrame (coinbase)
        df2: a pd.DataFrame (bitstamp)

    Returns:
        The concatenated pd.DataFrame
    """
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1)
    return df.sort_index()
