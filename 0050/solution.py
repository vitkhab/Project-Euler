#!/usr/bin/env python
from time import time
from math import sqrt
from sys import path
path.append('../Common')
from prime import is_prime, gen_missing_prime, prime_numbers


def find_solution():
    limit = 10**6
    global prime_numbers
    gen_missing_prime(limit/2)
    result = [0, 0]
    for start in range(len(prime_numbers)):
        number = [0, 0]
        if len(prime_numbers) - start < result[1]:
            break
        for i in range(start, len(prime_numbers)):
            number[0] += prime_numbers[i]
            number[1] += 1
            if number[0] > limit:
                break
            if is_prime(number[0]) and number[1] > result[1]:
                result = [] + number
    return result[0]


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()