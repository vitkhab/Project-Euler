#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import is_prime, prime_numbers


def prime_factors(n):
    res = []
    global prime_numbers
    if is_prime(n):
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