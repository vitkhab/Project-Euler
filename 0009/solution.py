#!/usr/bin/env python
from time import time


def is_pythagorean(a, b, c):
	if a**2 + b**2 == c**2:
		return True
	return False


def find_solution():
    for c in range(1000):
    	for b in range(c):
    		for a in range(b):
    			if a + b + c == 1000 and is_pythagorean(a, b, c):
    				return a * b * c
    return None


def main():
    start = time()
    print "Answer: %d" % find_solution()
    print "Time: %f" % (time() - start)


if __name__ == "__main__":
    main()