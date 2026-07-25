#!/usr/bin/env python3
"""Module that shuffles the data points in two matrices the same way."""
import numpy as np


def shuffle_data(X, Y):
    """Shuffles the data points in two matrices the same way.

    Args:
        X (numpy.ndarray): the first array of shape (m, nx) to
            shuffle, where m is the number of data points and nx is
            the number of features in X.
        Y (numpy.ndarray): the second array of shape (m, ny) to
            shuffle, where m is the same number of data points as in
            X and ny is the number of features in Y.

    Returns:
        The shuffled X and Y matrices.
    """
    permutation = np.random.permutation(X.shape[0])
    return X[permutation], Y[permutation]
