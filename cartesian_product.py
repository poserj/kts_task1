from typing import Any
from itertools import product

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    res = []
    for i in product(arr1, arr2):
        res.append(i)
    return res


if __name__ == '__main__':
    print(cartesian_product([1, 2], [3, 4]))