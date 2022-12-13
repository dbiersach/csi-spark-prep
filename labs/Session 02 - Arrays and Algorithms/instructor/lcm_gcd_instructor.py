# lcm_gcd_instructor.py

import numpy as np


def main():
    num1 = 447618
    num2 = 2011835

    lcm = (num1 * num2) / np.gcd(num1, num2)

    print(f"The LCM of {num1:,.0f} and {num2:,} is {lcm:,.0f}")


main()
