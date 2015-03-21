#!/usr/bin/env python
from time import time


def collatz_sequence_length_stateful(number):
    count = 0
    limit = number
    while number >= limit:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        count += 1
    return (number, count)


def find_solution():
    length_collection = {1: 1}
    for i in xrange(2, 10**6):
        (number, count) = collatz_sequence_length_stateful(i)
        length_collection[i] = length_collection[number] + count
    index = max(length_collection, key=length_collection.get)
    return "{} {}".format(index, length_collection[index])


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))


if __name__ == "__main__":
    main()