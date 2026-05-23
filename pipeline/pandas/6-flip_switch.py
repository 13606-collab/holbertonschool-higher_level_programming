#!/usr/bin/env python3
"""Module for flipping and switching a pd.DataFrame."""


def flip_switch(df):
    """Sort data in reverse chronological order and transpose.

    Args:
        df: a pd.DataFrame

    Returns:
        The transformed pd.DataFrame
    """
    return df.sort_index(ascending=False).T
