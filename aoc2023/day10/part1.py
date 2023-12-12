import collections

EAST = {
    '|': '',
    '-': '-J7S',
    'L': '-J7S',
    'J': '',
    '7': '',
    'F': '-J7S',
    '.': '',
    'S': '-J7S',
}

SOUTH = {
    '|': '|LJS',
    '-': '',
    'L': '',
    'J': '',
    '7': '|LJS',
    'F': '|LJS',
    '.': '',
    'S': '|LJS',
}


def parse_graph(text: str) -> dict[tuple[int, int], list[tuple[int, int]]]:
    graph = collections.defaultdict(list)
    lines = text.splitlines()
    n, m = len(lines), len(lines[0])
    for i in range(n):
        for j in range(m):
            if lines[i][j] == '.':
                continue
            if j < m - 1:
                if lines[i][j + 1] in EAST[lines[i][j]]:
                    graph[i, j].append((i, j + 1))
                    graph[i, j + 1].append((i, j))
            if i < n - 1:
                if lines[i + 1][j] in SOUTH[lines[i][j]]:
                    graph[i, j].append((i + 1, j))
                    graph[i + 1, j].append((i, j))
    return graph


# TODO: consider refactoring here
def dfs(
    graph: dict[tuple[int, int], list[tuple[int, int]]], start: tuple[int, int]
) -> int:
    stack = [start]
    visited = set()
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            stack.append(v)
    return len(visited)


def find_start(text: str) -> tuple[int, int] | None:
    lines = text.splitlines()
    n, m = len(lines), len(lines[0])
    for i in range(n):
        for j in range(m):
            if lines[i][j] == 'S':
                return i, j
    return None


def solve(text: str) -> int:
    graph = parse_graph(text)
    start = find_start(text)
    assert start is not None
    return dfs(graph, start) // 2


if __name__ == '__main__':
    pass
