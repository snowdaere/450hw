import matplotlib.pyplot as plt
import numpy as np

print('type list of velocities separated by spaces:')
v0s = np.array([float(i) for i in input('> ').split()]); nv0s = len(v0s); g = 9.81; n = 100
t = np.zeros(n); y = lambda t, v0: v0*t - 12*g*np.power(t, 2)
for i in range(nv0s):
    t = np.linspace(0, 2*(v0 := v0s[i])/g, 100)
    plt.plot(t, y(t, v0))
plt.show(); plt.savefig('plot.pdf')
