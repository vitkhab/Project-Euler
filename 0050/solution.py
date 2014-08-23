#!/usr/bin/env python
from time import time
from math import sqrt


def is_prime_preseed(n, prime_numbers):
    for i in prime_numbers:
        if n % i == 0:
            return False
        if n < i**2 - 1:
            return True
    return True


def gen_missing_prime(n, prime_numbers):
    for i in range(prime_numbers[-1], n + 1, 2):
        if is_prime_preseed(i, prime_numbers):
            prime_numbers.append(i)


def is_prime(n, prime_numbers):
    if n < 2:
        return False
    if n > prime_numbers[-1]**2:
        gen_missing_prime(int(sqrt(n)), prime_numbers)
    return is_prime_preseed(n, prime_numbers)


def find_solution():
    limit = 10**6
    prime_numbers = [2, 3]
    gen_missing_prime(limit/2, prime_numbers)
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
            if is_prime(number[0], prime_numbers) and number[1] > result[1]:
                result = [] + number
    return result[0]


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()