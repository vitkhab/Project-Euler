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


def find_solution():
    res = []
    for number in xrange(2, 10000):
        factors = factorize(number)
        d1 = (sum(make_divisors(factors)) - number)
        factors = factorize(d1)
        d2 = (sum(make_divisors(factors)) - d1)
        if d2 == number and d1 != number:
            res.append(number)
    return sum(res)


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()