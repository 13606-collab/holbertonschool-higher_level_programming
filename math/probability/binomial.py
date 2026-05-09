#!/usr/bin/env python3
"""Module for Binomial distribution"""


class Binomial:
    """Represents a Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes Binomial distribution

        Args:
            data (list): list of data to estimate the distribution
            n (int): number of Bernoulli trials
            p (float): probability of a success

        Raises:
            TypeError: if data is not a list
            ValueError: if data does not contain at least two data points
            ValueError: if n is not a positive value
            ValueError: if p is not a valid probability
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Step 1: Calculate mean and variance
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            # Step 2: Calculate p first
            # variance = n*p*(1-p), mean = n*p
            # => p = 1 - variance/mean
            p = 1 - (variance / mean)

            # Step 3: Calculate n (rounded, not cast!)
            # mean = n*p => n = mean/p
            n = round(mean / p)

            # Step 4: Recalculate p with rounded n
            p = mean / n

            self.n = n
            self.p = float(p)

        else:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
