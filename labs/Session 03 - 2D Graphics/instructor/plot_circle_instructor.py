# plot_circle_instructor.py

import numpy as np
import matplotlib.pyplot as plt


def main():
    plt.figure(__file__)
    ax = plt.axes()

    radius = 250
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    ax.plot(x, y)

    ax.set_title(f"$x^2 + y^2 = {radius}$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.set_aspect("equal")

    plt.show()


main()
