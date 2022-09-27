# basel_series_instructor.py

import numpy as np

num_terms = 10_000

a = np.arange(1, num_terms)

sigma = np.sum(1 / a)

print(f"Sum of first {num_terms:,} terms = {sigma}")

print(f"Magic number = {np.sqrt(sigma * 6)}")
