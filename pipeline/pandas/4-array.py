#!/usr/bin/env python3
"""Module for converting DataFrame columns to numpy array."""


def array(df):
    """Select last 10 rows of High and Close columns and convert to numpy array.

    Args:
        df: a pd.DataFrame containing columns named High and Close

    Returns:
        The numpy.ndarray of the selected values
    """
    return df[["High", "Close"]].tail(10).to_numpy()
