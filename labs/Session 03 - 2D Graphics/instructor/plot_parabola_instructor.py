# plot_parabola_instructor.py

import numpy as np
import matplotlib.pyplot as plt


def main():
    plt.figure(__file__)
    ax = plt.axes()

    x = np.linspace(-4, 5, 100)
    y = np.power(x, 2) + 1
    ax.plot(x, y)

    # Give the graph a title and axis labels
    ax.set_title(r"$y = x^2+1\;(-4\leq x \leq5)$")  # LaTeX format
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Center the graph on appropriate range
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 30)

    # Turn on the grid, and add decorations
    ax.grid()
    ax.axhline(1, color="gray", linestyle="--")
    ax.plot(0, 1, color="red", marker="o")

    plt.show()


main()
