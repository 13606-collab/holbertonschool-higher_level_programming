#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11)
y = x ** 3

plt.plot(x, y, color='red', linestyle='-')
plt.xlim(0, 10)
plt.title('Line Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
