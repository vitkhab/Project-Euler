#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import factorize


def make_divisors(factors, n = 1):
    res = []
    res.append(n)
    for i in range(len(factors)):
        res += make_divisors(factors[i + 1:], n * factors[i])
    return set(res)


def number_of_divisors_less(number, limit):
    factors = factorize(number)
    if 2**len(factors) < limit:
        return True
    return len(make_divisors(factors)) < limit


def find_solution():
    i = 1
    res = 0
    while number_of_divisors_less(res, 500):
        res += i
        i += 1
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()