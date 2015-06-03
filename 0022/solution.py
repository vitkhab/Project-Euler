#!/usr/bin/env python
from time import time


def get_alphabetical_value(name):
    alphabetical_value = 0
    for letter in name:
        alphabetical_value += ord(letter)-64
    return alphabetical_value


def find_solution():
    names = []
    with open('names.txt', 'r') as input_file:
        for line in input_file:
            for name in line.split(','):
                names.append(name.strip('"'))
    names.sort()

    return sum(map(
        lambda name, index: get_alphabetical_value(name) * (index + 1),
        names,
        xrange(len(names))
    ))


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()