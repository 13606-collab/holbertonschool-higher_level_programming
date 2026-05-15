#!/usr/bin/env python3
"""Module for calculating intersection of data and prior probabilities."""
import numpy as np
likelihood = __import__('likelihood').likelihood


def intersection(x, n, P, Pr):
    """Calculate the intersection of obtaining data with prior probabilities.

    Args:
        x (int): number of patients that develop severe side effects
        n (int): total number of patients observed
        P (numpy.ndarray): 1D array of hypothetical probabilities
        Pr (numpy.ndarray): 1D array of prior beliefs for each value in P

    Returns:
        numpy.ndarray: 1D array of intersection values for each probability

    Raises:
        ValueError: if n is not a positive integer
        ValueError: if x is not an integer >= 0
        ValueError: if x > n
        TypeError: if P is not a 1D numpy.ndarray
        TypeError: if Pr is not a numpy.ndarray with the same shape as P
        ValueError: if any value in P or Pr is not in range [0, 1]
        ValueError: if Pr does not sum to 1
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
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(Pr.sum(), 1):
        raise ValueError("Pr must sum to 1")

    return likelihood(x, n, P) * Pr
