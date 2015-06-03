#!/usr/bin/env python
from time import time


def find_cycle(number):
    length = None
    position = None
    number = str(number)
    for n in xrange(len(number)/2, 1, -1):
        if number[-2*n:-n] == number[-n:]:
            (position, length) = find_cycle(number[-n:])
            if not length:
                length = n
            position = len(number) - 2*n
            break
    return position, length


def get_fraction(numerator, denominator, limit=1000):
    fraction = ''
    for i in xrange(2*limit):
        numerator = numerator % denominator * 10
        fraction += str(numerator/denominator)
    return fraction


def find_solution():
    res = 0
    count = 0
    for n in xrange(1001, 2, -1):
        (pos, cycle) = find_cycle(get_fraction(1, n, n))
        if cycle and cycle > count:
            count = cycle
            res = n
        if count > n:
            break
    return res, count


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()