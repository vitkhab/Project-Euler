#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from fibonacci import get_fibonacci_list_by_limit


def find_solution():
    fibonacci_numbers = get_fibonacci_list_by_limit(4 * 10**6)
    return sum([x for x in fibonacci_numbers if x % 2 == 0])


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()