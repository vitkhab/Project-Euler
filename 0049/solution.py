#!/usr/bin/env python
from time import time
from itertools import permutations, combinations_with_replacement
from sys import path
path.append('../Common')
from prime import is_prime


def find_solution():
    result = []
    for c in combinations_with_replacement(range(1, 10), 4):
        tmp_res = []
        for p in permutations(c):
            number = int(''.join([str(e) for e in p]))
            if is_prime(number):
                tmp_res.append(number)
        if len(tmp_res) >= 3:
            for p in permutations(tmp_res, 3):
                number = int(''.join([str(e) for e in p]))
                if p[2] > p[1] > p[0] and p[2] - p[1] == p[1] - p[0] \
                   and number not in result and number != 148748178147:
                    result.append(number)
    return result[0]


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()