from . import part1


def border(path: list[tuple[int, int]]) -> int:
    return sum(
        abs(i2 - i1) + abs(j2 - j1) for (i1, j1), (i2, j2) in zip(path, path[1:])
    )


def inner_shoelace(path: list[tuple[int, int]]) -> int:
    # TODO: go over shoelace algo
    area = sum(i1 * j2 - i2 * j1 for (i1, j1), (i2, j2) in zip(path, path[1:]))
    return abs(area) // 2 - (border(path) // 2 - 1)


def dfs(
    graph: dict[tuple[int, int], list[tuple[int, int]]], start: tuple[int, int]
) -> list[tuple[int, int]]:
    stack = [start]
    explored = {}
    while stack:
        v = stack.pop()
        if v in explored:
            continue
        explored[v] = True
        for w in graph[v]:
            stack.append(w)
    return list(explored.keys())


def solve(text: str) -> int:
    graph = part1.parse_graph(text)
    start = part1.find_start(text)
    assert start is not None
    path = dfs(graph, start)
    return inner_shoelace(path + [path[0]])


if __name__ == '__main__':
    pass
