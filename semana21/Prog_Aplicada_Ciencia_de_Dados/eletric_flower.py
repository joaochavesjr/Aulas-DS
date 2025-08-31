# Script utilizando numpy para ilustrar 
# algumas das possibilidades da biblioteca

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")
t = np.linspace(0, 2 * np.pi,1500)
r = 1 + 0.3 * np.cos(12 * t)
x, y = r * np.cos(t), r * np.sin(t)
plt.scatter(x, y, c=t, cmap="rainbow", s=4)
plt.axis("equal")
plt.show()
