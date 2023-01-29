__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым,
    иначе - False
    """
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


if __name__ == '__main__':
    print(is_prime(211), True)
    print(is_prime(809), True)
    print(is_prime(701), True)
    print(is_prime(996), False)
    print(is_prime(681787), True)