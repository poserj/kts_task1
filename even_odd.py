__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    sum_even = 0 #четный
    sum_odd = 0
    for num, val in enumerate(arr):
        if (num + 1) % 2 == 0:
            sum_even += val
        else:
            sum_odd += val
    return sum_even / sum_odd


if __name__ == '__main__':
    print(even_odd([1,2,3,4,5]))