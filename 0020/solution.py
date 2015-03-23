#!/usr/bin/env python
from time import time


def factorial (n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def find_solution():
    res = 0
    number = factorial(100)
    while number > 10:
        res += number % 10
        number /= 10
    return res + number


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()