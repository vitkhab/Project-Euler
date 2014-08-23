#!/usr/bin/env python
from time import time
from math import sqrt
from itertools import permutations, combinations_with_replacement


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
    result = []
    prime_numbers = [2, 3]
    for c in combinations_with_replacement(range(1, 10), 4):
        tmp_res = []
        for p in permutations(c):
            number = int(''.join([str(e) for e in p]))
            if is_prime(number, prime_numbers):
                tmp_res.append(number)
        if len(tmp_res) >= 3:
            for p in permutations(tmp_res, 3):
                number = int(''.join([str(e) for e in p]))
                if p[2] > p[1] > p[0] and p[2] - p[1] == p[1] - p[0] \
                   and number not in result and number != 148748178147:
                    result.append(number)
    return result[0]


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()