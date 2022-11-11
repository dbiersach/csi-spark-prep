# herons_method_instructor.py

import numpy as np


def heron_sqrt(s):
    x = s / 2
    x_next = (x + s / x) / 2
    
    diff = np.abs(x - x_next)
    min_diff = np.nextafter(0, 1)
    
    while diff > min_diff:
        x = x_next
        x_next = (x + s / x) / 2
        diff = np.abs(x - x_next)
    return x


def main():
    v = 987654321.0
    r = heron_sqrt(v)
    
    print(f"The square root of {v:,} is {r:,}")
    print(f"The square of {r:,} is {r**2:,}")


main()
