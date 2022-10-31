# plot_rose_curves_instructor.py

import numpy as np
import matplotlib.pyplot as plt


def main():
    plt.figure(__file__)
    ax = plt.axes(projection="polar")

    theta = np.linspace(0, 4 * np.pi, 1000)

    radius_1 = 4 + 4 * np.cos(4 * theta)
    ax.plot(theta, radius_1, color="blue")

    radius_2 = 3 + 3 * np.cos(4 * theta + np.pi)
    ax.plot(theta, radius_2, color="green")

    radius_3 = 5 + 5 * np.cos(3 / 2 * theta)
    ax.plot(theta, radius_3, color="red")

    radius_4 = 7 + 7 * np.cos(5 * theta) * np.sin(11 * theta)
    ax.plot(theta, radius_4, color="black")

    ax.set_aspect("equal")
    ax.axis()

    plt.show()


main()
