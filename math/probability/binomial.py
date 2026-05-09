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

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p = 1 - (variance / mean)
            n = round(mean / p)
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

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes

        Args:
            k (int): number of successes

        Returns:
            float: PMF value for k, or 0 if k is out of range
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        def factorial(num):
            """Calculates factorial of a number"""
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

        n_fact = factorial(self.n)
        k_fact = factorial(k) * factorial(self.n - k)
        coefficient = n_fact / k_fact

        return coefficient * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes

        Args:
            k (int): number of successes

        Returns:
            float: CDF value for k, or 0 if k is out of range
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        # Hint: use pmf method — sum PMF from 0 to k
        return sum(self.pmf(i) for i in range(k + 1))
