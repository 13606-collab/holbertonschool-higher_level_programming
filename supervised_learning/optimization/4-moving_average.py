#!/usr/bin/env python3
"""Module that calculates the weighted moving average of a data set."""


def moving_average(data, beta):
    """Calculates the weighted moving average of a data set.

    The moving average calculation uses bias correction.

    Args:
        data (list): the list of data to calculate the moving average
            of.
        beta (float): the weight used for the moving average.

    Returns:
        list: a list containing the moving averages of data.
    """
    moving_averages = []
    v = 0

    for i, value in enumerate(data):
        v = beta * v + (1 - beta) * value
        bias_corrected = v / (1 - beta ** (i + 1))
        moving_averages.append(bias_corrected)

    return moving_averages
