#!/usr/bin/env python3
"""Module for calculating continuous posterior probability using Beta dist."""
from scipy import special


def posterior(x, n, p1, p2):
    """Calculate posterior probability that p is within range [p1, p2].

    Assumes a uniform prior. Uses the Beta distribution as the posterior:
    Beta(x + 1, n - x + 1).

    Args:
        x (int): number of patients that develop severe side effects
        n (int): total number of patients observed
        p1 (float): lower bound of the range
        p2 (float): upper bound of the range

    Returns:
        float: posterior probability that p is within [p1, p2]

    Raises:
        ValueError: if n is not a positive integer
        ValueError: if x is not an integer >= 0
        ValueError: if x > n
        ValueError: if p1 or p2 is not a float in range [0, 1]
        ValueError: if p2 <= p1
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or p1 < 0 or p1 > 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or p2 < 0 or p2 > 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    a = x + 1
    b = n - x + 1
    return special.betainc(a, b, p2) - special.betainc(a, b, p1)
