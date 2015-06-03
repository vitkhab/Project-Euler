#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from fibonacci import get_fibonacci_list_by_limit


def find_solution():
    return len(get_fibonacci_list_by_limit(10**999))


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()