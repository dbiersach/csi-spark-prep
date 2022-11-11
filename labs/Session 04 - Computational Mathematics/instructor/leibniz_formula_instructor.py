# leibniz_formula_instructor.py

import numpy as np


def main():
    n = 1_000_000

    a = np.empty(n)
    a[::2] = 1
    a[1::2] = -1

    b = np.arange(1, 2 * n + 1, 2)

    print(a[:10])
    print(b[:10])

    print(4 * np.sum(a / b))


main()
