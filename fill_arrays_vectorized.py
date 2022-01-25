import numpy as np

h = lambda x: (1/(2*np.pi)) * np.exp(-0.5 * np.power(x, 2))
x = np.linspace(-4, 4, 41)
y = h(x)
