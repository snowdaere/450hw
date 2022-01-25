import numpy as np
import matplotlib.pyplot as plt

v0 = 10; g = 9.81
t = np.linspace(0, 2*v0/g, 100)
# y = lambda t: v0*t - 0.5*g*pow(t, 2)
y = lambda t: v0*t - 0.5*g*pow(t, 2)

plt.plot(t, y(t))
plt.show()
