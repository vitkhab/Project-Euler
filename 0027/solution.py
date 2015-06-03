#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import is_prime


def get_number_of_consecutive_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n


def find_solution():
    res = 0
    count = 0
    for a in xrange(-999, 1000, 1):
        for b in xrange(-999, 1000, 1):
            c = get_number_of_consecutive_primes(a, b)
            if c > count:
                res = a * b
                count = c
    return res, count


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()