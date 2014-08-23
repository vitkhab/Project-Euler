#!/usr/bin/env python
from time import time
from math import sqrt

def is_natural_number(n):
    return n % 1.0 == 0 and n > 0


def solve_quadratic_equation(a, b, c):
    root1 = (-1.0 * b + sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
    root2 = (-1.0 * b - sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
    return root1, root2


def is_triangle_number(n):
    (r1, r2) = solve_quadratic_equation(1, 1, -2 * n)
    if is_natural_number(r1) or is_natural_number(r2):
        return True
    return False


def is_triangle_word(word):
    return is_triangle_number(sum([ord(letter) - 64 for letter in word]))


def parse_words(filename):
    words = []
    with open(filename) as filehandle:
        for line in filehandle:
            words += [s.strip('"') for s in line.split(',')]
    return words


def find_solution():
    solution = 0
    words = parse_words("words.txt")
    for w in words:
        print w
        if is_triangle_word(w):
            solution += 1
    return solution


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()