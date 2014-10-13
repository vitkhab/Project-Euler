#!/usr/bin/env python
from time import time
from sys import path
path.append('../Common')
from prime import gen_missing_prime, prime_numbers

def find_solution():
    gen_missing_prime(2 * 10**6)
    return sum(prime_numbers[:-1])


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()