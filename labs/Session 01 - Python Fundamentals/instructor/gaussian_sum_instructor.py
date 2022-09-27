# gaussian_sum_instructor.py

n = 1_000_000

sum = 0

for k in range(n + 1):
    sum = sum + k

print(f"Sum by looping = {sum:,}")

sum = n * (n + 1) // 2

print(f"Gaussian sum   = {sum:,}")
