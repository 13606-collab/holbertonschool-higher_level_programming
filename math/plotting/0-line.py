#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10)
y = x
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.show()