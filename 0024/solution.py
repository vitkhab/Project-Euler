#!/usr/bin/env python
from time import time
from itertools import permutations


def find_solution():
    return ''.join(list(permutations('0123456789', 10))[10**6 - 1])


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()