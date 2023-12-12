from . import part1


# TODO: check int vs float here
def shoelace(path: list[tuple[int, int]]) -> int:
    path = path + [path[0]]
    n = len(path)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += path[i][0] * path[j][1]
        area -= path[j][0] * path[i][1]
    border = sum(
        abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) for p1, p2 in zip(path, path[1:])
    )
    return abs(area) // 2 - (border // 2 - 1)


# TODO: consider refactoring here
def dfs(
    graph: dict[tuple[int, int], list[tuple[int, int]]], s: tuple[int, int]
) -> list[tuple[int, int]]:
    stack = [s]
    loop = []
    visited = set()
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        loop.append(u)
        for v in graph[u]:
            stack.append(v)
    return loop


def solve(text: str) -> int:
    graph = part1.parse_graph(text)
    s = part1.find_start(text)
    loop = dfs(graph, s)
    return shoelace(loop)


if __name__ == '__main__':
    pass
