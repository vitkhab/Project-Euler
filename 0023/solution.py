#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import factorize


def make_divisors(factors, n=1):
    res = list()
    res.append(n)
    for i in range(len(factors)):
        res += make_divisors(factors[i + 1:], n * factors[i])
    return set(res)


def find_solution():
    abundant_numbers = []
    res = 1
    for i in xrange(2, 28124):
        found = False
        if sum(make_divisors(factorize(i))) > 2*i:
            abundant_numbers.append(i)
        for number in abundant_numbers:
            if i - number in abundant_numbers:
                found = True
                break
            if 2*number > i:
                break
        if not found:
            res += i
    return res


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()