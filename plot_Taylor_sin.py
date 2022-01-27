import numpy as np
import matplotlib.pyplot as plt


def s(y, n: int):
    a = np.zeros(np.shape(y))
    for j in range(n+1):
        a = np.add(a, (-1)**j * (np.power(y, (2*j+1)))/np.math.factorial(2*j+1))
    return a


x = np.linspace(0, 4*np.pi)
plt.plot(x, np.sin(x))
for i in [1, 2, 3, 4, 6, 12]:

    plt.plot(x, s(x, i))



plt.ylim((-2, 2))
plt.show()
