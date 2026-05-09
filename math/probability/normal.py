#!/usr/bin/env python3
"""Module for Normal distribution"""


class Normal:
    """Represents a Normal distribution"""

    pi = 3.1415926536
    e = 2.7182818285

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes Normal distribution

        Args:
            data (list): list of data to estimate the distribution
            mean (float): mean of the distribution
            stddev (float): standard deviation of the distribution

        Raises:
            TypeError: if data is not a list
            ValueError: if data does not contain at least two data points
            ValueError: if stddev is not a positive value
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

        else:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)

    def z_score(self, x):
        """Calculates the z-score of a given x-value

        Args:
            x (float): x-value

        Returns:
            float: z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score

        Args:
            z (float): z-score

        Returns:
            float: x-value of z
        """
        return self.mean + (z * self.stddev)

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value

        Args:
            x (float): x-value

        Returns:
            float: PDF value for x
        """
        coefficient = 1 / (self.stddev * (2 * self.pi) ** 0.5)
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)

        return coefficient * (self.e ** exponent)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value

        Args:
            x (float): x-value

        Returns:
            float: CDF value for x
        """
        # Normalize x to z for erf calculation
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        # erf approximation from image 1 Taylor series
        erf = (2 / (self.pi ** 0.5)) * (
            z
            - (z ** 3) / 3
            + (z ** 5) / 10
            - (z ** 7) / 42
            + (z ** 9) / 216
        )

        return (1 + erf) / 2
