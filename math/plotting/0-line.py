#!/usr/bin/env python3
"""Create a simple line plot of y = x using Matplotlib."""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = x

plt.plot(x, y, "r-")
plt.xlim(0, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line Plot")
plt.show()
