# euler_identity_instructor.py

import math
import numpy as np


def main():
    z = complex(0, np.pi)
    ez = 1

    for p in range(1, 20):
        ez += np.power(z, p) / math.factorial(p)

    print(f"e^({z:.8f}) = {ez:.8f}")


main()
