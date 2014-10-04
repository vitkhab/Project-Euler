#!/usr/bin/env python
from time import time
from itertools import permutations
from sys import path
path.append('../Common')
from prime import is_prime


def find_solution():
    res = 0
    for n in range(1, 10):
        for i in permutations(range(1, n+1)):
            number = int(''.join([str(a) for a in i]))
            if number > res and is_prime(number):
                res = number
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()