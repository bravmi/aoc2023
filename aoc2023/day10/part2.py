from . import part1


def shoelace(path: list[tuple[int, int]]) -> int:
    path = path + [path[0]]
    n = len(path)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += path[i][0] * path[j][1]
        area -= path[j][0] * path[i][1]
    # TODO: move out border calc from here?
    border = sum(
        abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) for p1, p2 in zip(path, path[1:])
    )
    return abs(area) // 2 - (border // 2 - 1)


# TODO: consider refactoring here
def dfs(
    graph: dict[tuple[int, int], list[tuple[int, int]]], start: tuple[int, int]
) -> list[tuple[int, int]]:
    stack = [start]
    visited = {}
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited[u] = True
        for v in graph[u]:
            stack.append(v)
    return list(visited.keys())


def solve(text: str) -> int:
    graph = part1.parse_graph(text)
    start = part1.find_start(text)
    assert start is not None
    loop = dfs(graph, start)
    return shoelace(loop)


if __name__ == '__main__':
    pass
