#!/usr/bin/env python
from time import time
from math import sqrt


def pentagonal(n):
    return n * (3 * n - 1) / 2


def is_natural_number(n):
    return n % 1.0 == 0 and n > 0


def solve_quadratic_equation(a, b, c):
    root1 = (-1.0 * b + sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
    root2 = (-1.0 * b - sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
    return root1, root2


def is_pentagonal(n):
    (r1, r2) = solve_quadratic_equation(3, -1, -2 * n)
    if is_natural_number(r1) or is_natural_number(r2):
        return True
    return False


def is_solution(n1, n2):
    if is_pentagonal(n2 - n1) and is_pentagonal(n2 + n1):
        return True
    return False


def find_solution():
    n = 2
    solution = None
    pentagonal_numbers = [pentagonal(2), pentagonal(1)]

    while pentagonal_numbers[0] - pentagonal_numbers[1] > solution:
        n += 1
        new_pentagonal_number = pentagonal(n)
        for i in pentagonal_numbers:
            if solution is not None and new_pentagonal_number - i > solution:
                break
            if is_solution(i, new_pentagonal_number):
                solution = new_pentagonal_number - i
        pentagonal_numbers.insert(0, new_pentagonal_number)
    return solution


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()