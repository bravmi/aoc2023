from . import part1


def border(path: list[tuple[int, int]]) -> int:
    return sum(
        abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) for p1, p2 in zip(path, path[1:])
    )


def shoelace(path: list[tuple[int, int]]) -> int:
    area = sum(i1 * j2 - i2 * j1 for (i1, j1), (i2, j2) in zip(path, path[1:]))
    return abs(area) // 2 - (border(path) // 2 - 1)


def dfs(
    graph: dict[tuple[int, int], list[tuple[int, int]]], start: tuple[int, int]
) -> list[tuple[int, int]]:
    stack = [start]
    explored = {}
    while stack:
        u = stack.pop()
        if u in explored:
            continue
        explored[u] = True
        for v in graph[u]:
            stack.append(v)
    return list(explored.keys())


def solve(text: str) -> int:
    graph = part1.parse_graph(text)
    start = part1.find_start(text)
    assert start is not None
    path = dfs(graph, start)
    return shoelace(path + [path[0]])


if __name__ == '__main__':
    pass
