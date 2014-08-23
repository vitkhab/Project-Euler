#!/usr/bin/env python
from time import time


def find_solution():
    steps = [3, 2, 1, 3, 1, 2, 3]
    i = 0
    num = 0
    res = 0
    while num < 1000:
        res += num
        num += steps[i % len(steps)]
        i += 1
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()