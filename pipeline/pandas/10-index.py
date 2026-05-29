#!/usr/bin/env python3
"""Module for setting the index of a pd.DataFrame."""


def index(df):
    """Set the Timestamp column as the index of the DataFrame.

    Args:
        df: a pd.DataFrame

    Returns:
        The modified pd.DataFrame
    """
    return df.set_index("Timestamp")
