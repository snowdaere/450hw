import numpy as np

x0 = float(-4); deltax = 8; n = 41
dx = deltax / (n - 1)
x = [float(i) * dx + x0 for i in range(0, n)]
h = lambda x: (1/(2*np.pi)) * np.exp(-0.5 * np.power(x, 2))

y = [0.0] * n
for i in range(n):
    y[i] = h(x[i])
