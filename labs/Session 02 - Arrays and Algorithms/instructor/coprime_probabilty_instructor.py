# coprime_probability_instructor.py

import numpy as np

np.random.seed(2021)

max_num = 100_000
num_pairs = 10_000

a = np.random.randint(1, max_num, size=num_pairs)
b = np.random.randint(1, max_num, size=num_pairs)

c = np.gcd(a, b)
num_coprime_pairs = np.count_nonzero(c == 1)
p = num_coprime_pairs / num_pairs

print(f"Coprime Probability = {p}")
print(f"Hidden constant     = {np.sqrt(6 / p)}")
