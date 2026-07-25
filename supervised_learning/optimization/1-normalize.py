#!/usr/bin/env python3
"""Module that normalizes (standardizes) a matrix."""
import numpy as np


def normalize(X, m, s):
    """Normalizes (standardizes) a matrix.

    Args:
        X (numpy.ndarray): array of shape (d, nx) to normalize, where
            d is the number of data points and nx is the number of
            features.
        m (numpy.ndarray): array of shape (nx,) that contains the
            mean of all features of X.
        s (numpy.ndarray): array of shape (nx,) that contains the
            standard deviation of all features of X.

    Returns:
        numpy.ndarray: the normalized X matrix.
    """
    return (X - m) / s
