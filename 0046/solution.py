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


def is_solution(n, prime_numbers):
    if not is_prime(n, prime_numbers):
        for i in range(int(sqrt(n))):
            if is_prime(n - 2 * (i**2), prime_numbers):
                return False
        return True
    return False


def find_solution():
    res = 9
    prime_numbers = [2, 3]
    while not is_solution(res, prime_numbers):
        res += 2
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()