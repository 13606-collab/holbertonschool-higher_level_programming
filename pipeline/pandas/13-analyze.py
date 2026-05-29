#!/usr/bin/env python3
"""Module for analyzing a pd.DataFrame."""


def analyze(df):
    """Compute descriptive statistics for all columns except Timestamp.

    Args:
        df: a pd.DataFrame

    Returns:
        A new pd.DataFrame containing descriptive statistics
    """
    return df.drop(columns=["Timestamp"]).describe()
