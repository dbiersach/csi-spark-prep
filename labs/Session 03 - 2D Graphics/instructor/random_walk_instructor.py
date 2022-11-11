# random_walk_instructor.py

import numpy as np
import matplotlib.pyplot as plt


def main():
    plt.figure(__file__)
    ax = plt.axes()

    np.random.seed(2016)

    num_steps = 10000

    theta = np.random.random(num_steps) * 2 * np.pi
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        x[i] = x[i - 1] + np.cos(theta[i])
        y[i] = y[i - 1] + np.sin(theta[i])

    ax.plot(x, y)

    ax.set_title("Uniform Random Walk")

    plt.show()


main()
