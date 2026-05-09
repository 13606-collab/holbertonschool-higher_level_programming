#!/usr/bin/env python3
"""Module for Poisson distribution"""


class Poisson:
    """Represents a Poisson distribution"""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initializes Poisson distribution

        Args:
            data (list): list of data to estimate the distribution
            lambtha (float):
            expected number of occurrences in a given time frame

        Raises:
            TypeError: if data is not a list
            ValueError: if data does not contain at least two data points
            ValueError: if lambtha is not a positive value
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes

        Args:
            k (int): number of successes

        Returns:
            float: PMF value for k, or 0 if k is out of range
        """
        k = int(k)

        if k < 0:
            return 0

        # Calculate e^(-λ)
        e_pow = self.e ** (-self.lambtha)

        # Calculate λ^k
        lambda_pow = self.lambtha ** k

        # Calculate k! (factorial)
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        return (lambda_pow * e_pow) / factorial
