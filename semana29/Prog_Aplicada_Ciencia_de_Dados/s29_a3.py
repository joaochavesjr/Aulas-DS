# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1, label='Seno', color='b', linewidth=2, linestyle='-')
ax.plot(x, y2, label='Cosseno', color='r',linewidth=2, linestyle='--')

ax.set_title('Funções Trigonométricas', fontsize=16)
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)

ax.grid(True, which='both', linestyle='--', linewidth=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(loc='upper right', fontsize=12)
plt.show()
