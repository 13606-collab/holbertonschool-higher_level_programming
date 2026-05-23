#!/usr/bin/env python3
"""Module for converting numpy arrays to pandas DataFrames."""
import pandas as pd


def from_numpy(array):
    """Create a pd.DataFrame from a np.ndarray with alphabetical column labels.

    Args:
        array: the np.ndarray from which to create the pd.DataFrame

    Returns:
        A newly created pd.DataFrame with capitalized alphabetical columns
    """
    cols = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)