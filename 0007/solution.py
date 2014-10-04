#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import get_prime

def find_solution():
    return get_prime(10001)


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()