#!/usr/bin/env python
from time import time
from math import sqrt


def hexagonal(n):
    return n * (2 * n - 1)


def is_natural_number(n):
    return n % 1.0 == 0 and n > 0


def solve_quadratic_equation(a, b, c):
    root1 = (-1.0 * b + sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
    root2 = (-1.0 * b - sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
    return root1, root2


def is_triangle(n):
    (r1, r2) = solve_quadratic_equation(1, 1, -2 * n)
    if is_natural_number(r1) or is_natural_number(r2):
        return True
    return False


def is_pentagonal(n):
    (r1, r2) = solve_quadratic_equation(3, -1, -2 * n)
    if is_natural_number(r1) or is_natural_number(r2):
        return True
    return False


def is_solution(n):
    if is_pentagonal(n) and is_triangle(n):
        return True
    return False


def find_solution():
    n = 144
    solution = 3

    while not is_solution(solution):
        n += 1
        solution = hexagonal(n)
    return solution


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()