from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    res_arr = []
    for x, y in zip(arr1, arr2):
        res_arr.append((x, y))
    return res_arr


if __name__ == '__main__':
    print(corresponding_pairs([1,2,3,4], ['a','b','c']))