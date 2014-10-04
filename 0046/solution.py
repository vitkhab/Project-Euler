#!/usr/bin/env python
from time import time
from math import sqrt
from sys import path
path.append('../Common')
from prime import is_prime


def is_solution(n):
    if not is_prime(n):
        for i in range(int(sqrt(n))):
            if is_prime(n - 2 * (i**2)):
                return False
        return True
    return False


def find_solution():
    res = 9
    while not is_solution(res):
        res += 2
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()