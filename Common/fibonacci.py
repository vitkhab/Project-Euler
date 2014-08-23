def get_fibonacci_number(n):
    """Finds Nth fibonacci number"""
    if n < 0:
        return None

    a = [[1, 1],
         [1, 0]]
    r = [0, 1]

    while n:
        if n % 2 != 0:
            r = [r[0] * a[0][0] + r[1] * a[1][0], r[0] * a[0][1] + r[1] * a[1][1]]
        a = [[a[0][0] * a[0][0] + a[0][1] * a[1][0], a[0][0] * a[0][1] + a[0][1] * a[1][1]],
             [a[1][0] * a[0][0] + a[1][1] * a[1][0], a[1][0] * a[0][1] + a[1][1] * a[1][1]]]

        n /= 2
    return r[0]


def get_fibonacci_list(n, limit = None):
    """Generates list consisted of N fibonacci numbers"""
    if n < 0:
        return None
    if n == 0:
        return []
    if n == 1:
        return [0]
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers


def get_fibonacci_list_by_limit(limit):
    """Generates list consisting of fibonacci numbers less than limit"""
    if limit < 0:
        return None
    if limit == 0:
        return []
    if limit == 1:
        return [0]
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < limit:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[:-1]