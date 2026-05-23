#!/usr/bin/env python3
"""Module for renaming and converting DataFrame columns."""
import pandas as pd


def rename(df):
    """Rename Timestamp column to Datetime and convert to datetime values.

    Args:
        df: a pd.DataFrame containing a column named Timestamp

    Returns:
        The modified pd.DataFrame with only Datetime and Close columns
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df[["Datetime", "Close"]]
    print(df)
    return df
