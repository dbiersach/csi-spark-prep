# logarithm_series_instructor.py

import numpy as np


def main():
    n = 10_000
    s = 0

    for k in range(1, n + 1):
        s = s + 1 / (2**k * k)

    print(np.exp(s))


main()
