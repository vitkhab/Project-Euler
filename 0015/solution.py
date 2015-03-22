#!/usr/bin/env python
from time import time

cache = {}


def recursion(num, step):
    res = 0
    if step == 1:
        return 1 + num
    while num >= 0:
        if num not in cache:
            cache[num] = {}
        if step - 1 not in cache[num]:
            cache[num][step - 1] = recursion(num, step - 1)
        res += cache[num][step - 1]
        num -= 1
    return res


def find_solution():
    n = 20
    return "{}".format(2*recursion(n, n - 1))


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()