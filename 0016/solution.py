#!/usr/bin/env python
from time import time


def find_solution():
    res = 0
    n = 2**1000
    while n > 0:
        res += n % 10
        n /= 10
    return res


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))


if __name__ == "__main__":
    main()