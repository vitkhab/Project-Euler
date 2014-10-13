#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import get_prime


def find_solution():
    return sum(range(101))**2 - sum([x**2 for x in range(101)])


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()