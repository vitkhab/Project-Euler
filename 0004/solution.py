#!/usr/bin/env python
from time import time


def is_solution(n):
    string = str(n)
    for x in range(len(string)/2):
        if string[x] != string[-1 - x]:
            return False
    return True


def find_solution():
    res = 0
    for a in range(999, 1, -1):
        if a * a < res:
            break
        for b in range(a, 1, - 1):
            if a * b < res:
                break
            if is_solution(a*b) and a*b > res:
                res = a*b
    return res


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()