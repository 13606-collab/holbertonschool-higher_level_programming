#!/usr/bin/env python3
"""Module for plotting y as a line graph."""
import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph():
    """Plot y as a solid red line with x-axis ranging from 0 to 10."""
    y = np.arange(0, 11) ** 3
    x = np.arange(0, 11)
    plt.plot(x, y, 'r-')
    plt.xlim(0, 10)
    plt.show()


if __name__ == "__main__":
    plot_line_graph()
