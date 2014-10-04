from math import sqrt


prime_numbers = [2, 3]


def is_prime_preseed(n):
    global prime_numbers
    for i in prime_numbers:
        if n == i:
            return True
        elif n % i == 0:
            return False
        elif n < i**2 - 1:
            return True
    return True


def gen_next_prime():
    global prime_numbers
    number = prime_numbers[-1] + 2
    while not is_prime(number):
        number += 2
    prime_numbers.append(number)


def gen_missing_prime(n):
    global prime_numbers
    while  prime_numbers[-1] < n:
        gen_next_prime()


def is_prime(n):
    global prime_numbers
    if n < 2:
        return False
    while n > prime_numbers[-1]**2:
        gen_next_prime()
    return is_prime_preseed(n)


def get_prime(num):
    global prime_numbers
    while len(prime_numbers) < num:
        gen_next_prime()
    return prime_numbers[num - 1]


def test_module():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(20747) == True
    assert is_prime(20737) == False
    assert is_prime(104729) == True
    assert is_prime(104719) == False

    assert get_prime(1) == 2
    assert get_prime(3) == 5
    assert get_prime(10000) == 104729