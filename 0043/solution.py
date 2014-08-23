#!/usr/bin/env python
from time import time
from itertools import permutations


def has_divisibility_property(number):
    if ((number / 10**9 == 0
         or (number / 10**6 % 10**3) % 2 != 0
         or (number / 10**5 % 10**3) % 3 != 0
         or (number / 10**4 % 10**3) % 5 != 0
         or (number / 10**3 % 10**3) % 7 != 0
         or (number / 10**2 % 10**3) % 11 != 0
         or (number / 10**1 % 10**3) % 13 != 0
         or (number / 10**0 % 10**3) % 17 != 0)):
        return 0
    return number


def find_solution():
    solution = 0
    for i in permutations(range(10)):
        solution += has_divisibility_property(int('%d%d%d%d%d%d%d%d%d%d' % i))
    return solution


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()