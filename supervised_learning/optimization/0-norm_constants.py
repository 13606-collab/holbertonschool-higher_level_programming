#!/usr/bin/env python3
"""Module that calculates the normalization (standardization) constants
of a matrix.
"""
import numpy as np


def normalization_constants(X):
    """Calculates the normalization (standardization) constants of a
    matrix.

    Args:
        X (numpy.ndarray): array of shape (m, nx) to normalize, where
            m is the number of data points and nx is the number of
            features.

    Returns:
        mean, std: the mean and standard deviation of each feature,
            respectively.
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return mean, std
