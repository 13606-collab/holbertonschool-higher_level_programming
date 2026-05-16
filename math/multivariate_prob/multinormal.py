#!/usr/bin/env python3
"""Module for Multivariate Normal distribution."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize MultiNormal distribution.

        Args:
            data: numpy.ndarray of shape (d, n) containing the data set
                d is the number of dimensions
                n is the number of data points

        Raises:
            TypeError: if data is not a 2D numpy.ndarray
            ValueError: if n is less than 2
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        X_centered = data - self.mean
        self.cov = (X_centered @ X_centered.T) / (n - 1)
