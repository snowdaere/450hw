import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import typing
from PIL import Image


def animate_series(fk: typing.Callable, exact: typing.Callable,
                   sumlimits=(0, 10), xlim=(-10, 10), ylim=(-10, 10), n=100):

    # define x values
    domain = np.linspace(*xlim, n)

    # define inclusive sum limits
    sumlimits = (sumlimits[0], sumlimits[1] + 1)

    # define summation function
    def s(y, order):
        a = np.zeros(np.shape(y))
        for j in range(sumlimits[0], order):
            a = np.add(a, fk(y, j))
        return a

    # delete any existing animation frames
    for file in glob.glob("frames/tmp_*.png"):
        os.remove(file)

    # init list of filenames
    filenames = [''] * (sumlimits[1] - sumlimits[0])

    # generate frames of animation
    for frame in range(*sumlimits):
        # initialize plot
        plt.figure()
        plt.xlim(xlim)
        plt.ylim(ylim)

        # plot exact function
        plt.plot(domain, exact(domain))

        # plot summation until that frame
        plt.plot(domain, s(domain, frame))

        # save frame and add to list
        filename = 'frames/tmp_%04d.png' % frame
        plt.savefig(filename)
        plt.close()
        filenames[frame] = filename

        pass

    # generate animation
    frames = [Image.open(image) for image in filenames]
    frame_one = frames[0]
    frame_one.save("taylor.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)
    # code adapted from https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/


exact = lambda y: np.sin(y)
fk = lambda y, j: (-1)**j * (np.power(y, (2*j+1)))/np.math.factorial(2*j+1)

animate_series(fk, exact)
