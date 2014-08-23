#!/usr/bin/env python
from time import time
from math import sqrt
from itertools import permutations


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


def find_solution():
    res = 0
    prime_numbers = [2, 3]
    for n in range(1, 10):
        for i in permutations(range(1, n+1)):
            number = int(''.join([str(a) for a in i]))
            if number > res and is_prime(number, prime_numbers):
                res = number
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()