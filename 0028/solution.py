#!/usr/bin/env python
from time import time
from basic_approach import basic_approach, basic_cached_approach, approaches as basic_approaches
from series_approach import series_approach, approaches as series_approaches


approaches = {}
for approach in basic_approaches:
    approaches[approach] = basic_approaches[approach]
for approach in series_approaches:
    approaches[approach] = series_approaches[approach]
approaches["optimal"] = ["series_approach", "series_test"]


def find_solution(approach="optimal", size=1001):
    if approach not in approaches:
        raise ValueError("Approach '{}' is not specified".format(approach))

    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(approaches[approach][0])

    if not method:
        raise Exception("Method '{}' not implemented".format(approaches[approach][0]))

    return method(size)

def main():
    start = time()
    print "Answer: {}".format(find_solution())
    print "Time: {}".format((time() - start))

if __name__ == "__main__":
    main()
