import numpy as np
import matplotlib.pyplot as plt


class Data:
    def __init__(self, filename):
        self.data = np.loadtxt(filename, delimiter = ',')
        self.x, self.y = self.data[:, 0], self.data[:, 1]
        file = open(filename, 'r').readlines()
        self.title = file[0][2:]
        cut = lambda string, mark: string[string.index(mark)+2:]
        self.xlab, self.ylab = cut(file[1], ': '), cut(file[2], ': ')

    def plot(self, fit=False, degree=[0]):
        plt.scatter(self.x, self.y)
        if type(degree) != list: degree = [degree]
        if fit:
            for degr in degree:
                plt.plot(x := np.linspace(min(self.x), max(self.x), 100),
                         np.poly1d(np.polyfit(self.x, self.y, deg=degr))(x), c='red')
        plt.title(self.title)
        plt.ylabel(self.ylab)
        plt.xlabel(self.xlab)
        plt.show()


print('Type filename:')
Data(input('> ')).plot(True, [1, 2])
