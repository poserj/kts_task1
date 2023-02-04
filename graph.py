from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        search_list = []

        def __dfs(n: Node):
            if n in search_list: return
            search_list.append(n)
            for node in n.outbound:
                __dfs(node)

        __dfs(self._root)
        return search_list

    def bfs(self) -> list[Node]:
        raise NotImplementedError


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    a.point_to(b)
    b.point_to(d)
    a.point_to(c)
    g = Graph(a)
    print(g.dfs())
    assert g.dfs() == [a, b, d, c]
