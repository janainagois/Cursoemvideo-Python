import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10,100 )
y = (2**3-3*2**2+6*2-4) / (2**2-4*2**2 +8*2 -5)

y_min= min(y)
y_max= max(y)

y_inter = np.linspace(y_min, y_max , 100)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(np.zeros_like(y_inter), y_inter, 'r--', label='Intervalo de y')

ax.set_xlabel('x')
ax.set_ylabel('y')

plt.grid(True)
plt.show()