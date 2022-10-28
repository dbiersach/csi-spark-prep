# perfect_numbers_bonus_instructor.py


def is_perfect_number(n):
    sum_of_factors = 1
    for factor in range(2, n):
        if n % factor == 0:
            sum_of_factors += factor
    if sum_of_factors == n:
        return True
    else:
        return False


def main():
    for n in range(2, 10_000):
        if is_perfect_number(n):
            print(f"{n:,} is a perfect number")
            # sum of the reciprocals of its divisors
            srd = 0.0
            for factor in range(1, n + 1):
                if n % factor == 0:
                    srd += 1 / factor
            print(f"Sum of reciprocals of divisors = {srd}")
            print()


main()
