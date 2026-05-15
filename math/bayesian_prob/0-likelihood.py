#!/usr/bin/env python3
"""Module for calculating binomial likelihood of observed data."""
import numpy as np


def likelihood(x, n, P):
    """Calculate likelihood of data given hypothetical probabilities.

    Args:
        x (int): number of patients that develop severe side effects
        n (int): total number of patients observed
        P (numpy.ndarray): 1D array of hypothetical probabilities

    Returns:
        numpy.ndarray: 1D array of likelihoods for each probability in P

    Raises:
        ValueError: if n is not a positive integer
        ValueError: if x is not an integer >= 0
        ValueError: if x > n
        TypeError: if P is not a 1D numpy.ndarray
        ValueError: if any value in P is not in range [0, 1]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Binomial coefficient C(n, x)
    def factorial(k):
        """Return factorial of k."""
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result

    coeff = factorial(n) / (factorial(x) * factorial(n - x))
    return coeff * (P ** x) * ((1 - P) ** (n - x))
