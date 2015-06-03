#!/usr/bin/env python
approaches = {
    "basic": ["basic_approach", "basic_test"],
    "basic_cached": ["basic_cached_approach", "basic_test"]
}

sequence_cache = {}


def get_radius_sequence_number(x, y, size):
    """
    :param x: position of number in row
    :param y: position of number in column
    :param size: diameter of spiral
    :return: sequence number of circle on which number is positioned starting from the center
    Return example:
    3 3 3 3 3 3 3
    3 2 2 2 2 2 3
    3 2 1 1 1 2 3
    3 2 1 0 1 2 3
    3 2 1 1 1 2 3
    3 2 2 2 2 2 3
    3 3 3 3 3 3 3
    """
    if size % 2 == 0:
        raise ValueError("Size is even")
    if not (0 <= x < size and 0 <= y < size):
        raise ValueError("Coordinates x={} y={} are outside of range 0..{}".format(x, y, size - 1))
    n = max(abs(size/2 - x), abs(size/2 - y))
    return n


def get_position_on_radius(x, y, size, seq=None):
    """
    :param x: position of number in row
    :param y: position of number in column
    :param size: diameter of spiral
    :param seq: sequence number of circle on which number is positioned starting from the center
    :return: sequence number of chosen number on circle
    Return example:
    18 19 20 21 22 23 24
    17 12 13 14 15 16  1
    16 11  7  8  9  1  2
    15 10  5  0  1  2  3
    14  9  4  3  2  3  4
    13  8  7  6  5  4  5
    12 11 10  9  8  7  6
    """
    if seq is None:
        seq = get_radius_sequence_number(x, y, size)
    if seq == 0:
        return 0

    pos = None
    if y == size/2 - seq:
        pos = 3 * 2 * seq + (x - size/2 + seq)
    if x == size/2 - seq:
        pos = 2 * 2 * seq + (size/2 + seq - y)
    if y == size/2 + seq:
        pos = 1 * 2 * seq + (size/2 + seq - x)
    if x == size/2 + seq and y != size/2 - seq:
        pos = 0 * 2 * seq + (y - size/2 + seq)
    return pos


def get_previous_sequence_last_number(seq, size=None, cached=True):
    """
    :param seq: sequence number of circle on which number is positioned starting from the center
    :param size: diameter of spiral
    :param cached: boolean value to define if cache is used
    :return: number of elements in all previous circle starting from the center
    Return example:
    25 25 25 25 25 25 25
    25  9  9  9  9  9 25
    25  9  1  1  1  9 25
    29  9  1  0  1  9 25
    25  9  1  1  1  9 25
    25  9  9  9  9  9 25
    25 25 25 25 25 25 25
    """
    if size is not None and seq > size/2:
        raise ValueError("Seq={} is greater than radius of the spiral".format(seq))
    if seq < 0:
        raise ValueError("Seq={} is negative".format(seq))
    if seq == 0:
        return 0
    if seq == 1:
        return 1
    if cached:
        if seq not in sequence_cache:
            sequence_cache[seq] = get_previous_sequence_last_number(seq - 1)
        return 8*(seq - 1) + sequence_cache[seq]
    else:
        return 8*(seq - 1) + get_previous_sequence_last_number(seq - 1)


def get_number(x, y, size, cached=True):
    """
    :param x: position of number in row
    :param y: position of number in column
    :param size: diameter of spiral
    :return: number positioned on the specified coordinates of spiral
    Return example:
    43 44 45 46 47 48 49
    42 21 22 23 24 25 26
    41 20  7  8  9 10 27
    40 19  6  1  2 11 28
    39 18  5  4  3 12 29
    38 17 16 15 14 13 30
    37 36 35 34 33 32 31
    """
    seq = get_radius_sequence_number(x, y, size)
    pos = get_position_on_radius(x, y, size, seq)
    if pos == 0:
        return 1
    return pos + get_previous_sequence_last_number(seq, size, cached)


def basic_approach(size):
    res = -1  # Because number 1 in the center of spiral is counted twice
    for x in xrange(size):
        res += get_number(x, x, size, False)
        res += get_number(x, size - x - 1, size, False)
    return res


def basic_cached_approach(size):
    res = -1  # Because number 1 in the center of spiral is counted twice
    for x in xrange(size):
        res += get_number(x, x, size)
        res += get_number(x, size - x - 1, size)
    return res


def basic_test():
    assert get_number(2, 2, 5) == 1
    assert get_number(4, 1, 5) == 10
    assert get_number(1, 4, 5) == 16
    assert get_number(0, 0, 5) == 21
    assert get_number(6, 0, 7) == 49
    assert get_previous_sequence_last_number(1, 5) == 1
    assert get_previous_sequence_last_number(3, 7) == 25
    assert get_position_on_radius(1, 1, 5, 0) == 0
    assert get_position_on_radius(2, 2, 5) == 0
    assert get_position_on_radius(4, 4, 5) == 4
    assert get_position_on_radius(0, 4, 5) == 8
    assert get_position_on_radius(0, 0, 5) == 12
    assert get_position_on_radius(4, 0, 5) == 16
    assert get_radius_sequence_number(0, 1, 5) == 2
    assert get_radius_sequence_number(3, 3, 7) == 0
    assert get_radius_sequence_number(1, 3, 9) == 3
    assert get_radius_sequence_number(0, 3, 11) == 5

    try:
        get_previous_sequence_last_number(3, 5)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        get_previous_sequence_last_number(-1, 5)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        get_radius_sequence_number(0, 3, 10)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        get_radius_sequence_number(0, 11, 11)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        get_radius_sequence_number(-1, 10, 11)
    except ValueError:
        pass
    else:
        raise AssertionError


if __name__ == "__main__":
    basic_test()
    print("Tests were successful")
