#!/usr/bin/env python
from time import time
from math import sqrt


def is_prime_preseed(n, prime_numbers):
    for i in prime_numbers:
        if n % i == 0:
            return False
        if n < i**2 - 1:
            return True
    return True


def gen_missing_prime(n, prime_numbers):
    for i in range(prime_numbers[-1], n + 1, 2):
        if is_prime_preseed(i, prime_numbers):
            prime_numbers.append(i)


def is_prime(n, prime_numbers):
    if n < 2:
        return False
    if n > prime_numbers[-1]**2:
        gen_missing_prime(int(sqrt(n)), prime_numbers)
    return is_prime_preseed(n, prime_numbers)


def prime_factors(n):
    res = []
    prime_numbers = [2, 3]
    if is_prime(n, prime_numbers):
        return [n]
    for i in prime_numbers:
        if n == 1:
            break
        if n % i == 0:
            res.append(i)
            n /= i
    return res


def find_solution():
    return max(prime_factors(600851475143))


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()