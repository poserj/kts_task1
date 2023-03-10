from typing import Optional
import re


__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    r = re.findall(r'\w+', text)
    return min(r, key=len), max(r, key=len)


if __name__ == '__main__':
    print(find_shortest_longest_word('hello there, general kenobi'))