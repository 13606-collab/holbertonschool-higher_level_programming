#!/usr/bin/env python3
"""Module for sorting a pd.DataFrame by High price."""


def high(df):
    """Sort the DataFrame by High price in descending order.

    Args:
        df: a pd.DataFrame

    Returns:
        The sorted pd.DataFrame
    """
    return df.sort_values(by="High", ascending=False)
