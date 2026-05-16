#!/usr/bin/env python3
"""Module for Multivariate Normal distribution."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize MultiNormal distribution.

        Args:
            data: numpy.ndarray of shape (d, n) containing the data set

        Raises:
            TypeError: if data is not a 2D numpy.ndarray
            ValueError: if n is less than 2
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)   # shape (d, 1)

        X_centered = data - self.mean                       # shape (d, n)
        self.cov = (X_centered @ X_centered.T) / (n - 1)  # shape (d, d)

    def pdf(self, x):
        """Calculate the PDF at a data point.

        Args:
            x: numpy.ndarray of shape (d, 1) containing the data point

        Returns:
            float: the value of the PDF at x

        Raises:
            TypeError: if x is not a numpy.ndarray
            ValueError: if x does not have shape (d, 1)
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        diff = x - self.mean
        cov_inv = np.linalg.inv(self.cov)
        cov_det = np.linalg.det(self.cov)

        # Multivariate Normal PDF düsturu
        coeff = 1 / (((2 * np.pi) ** (d / 2)) * (cov_det ** 0.5))
        exponent = -0.5 * (diff.T @ cov_inv @ diff)

        return float(coeff * np.exp(exponent))
