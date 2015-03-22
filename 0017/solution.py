#!/usr/bin/env python
from time import time


numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

keys = numbers.keys()
keys.sort(reverse=True)


def number_to_words(number):
    words = ''
    if number == 1:
        return numbers[1]
    for k in keys:
        div = number / k
        if div > 1:
            words += number_to_words(number / k)
            pass
        if div > 0:
            if (k == 100 or k == 1000) and div == 1:
                words += 'one'
            number %= k
            words += numbers[k]
            if k == 100 and number > 0:
                words += 'and'
    return words


def find_solution():
    res = 0
    for n in xrange(1001):
        res += len(number_to_words(n))
    return res


def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))


if __name__ == "__main__":
    main()