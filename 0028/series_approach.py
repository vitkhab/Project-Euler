#!/usr/bin/env python
approaches = {"series": ["series_approach", "series_test"]}

def series_approach(size):
    if size % 2 == 0:
        raise ValueError("Size={} is even".format(size))
    if size < 1:
        raise ValueError("Size={} less than 1".format(size))

    n = 1
    res = 1

    for x in xrange(1, size/2 + 1):
        res += (n + 2 * x) + (n + 4 * x) + (n + 6 * x) + (n + 8 * x)
        n += 8 * x

    return res


def series_test():
    assert series_approach(1) == 1
    assert series_approach(3) == 25
    assert series_approach(5) == 101

    try:
        series_approach(4)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        series_approach(0)
    except ValueError:
        pass
    else:
        raise AssertionError


if __name__ == "__main__":
    series_test()
    print("Tests were successful")
