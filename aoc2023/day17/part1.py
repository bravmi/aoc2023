import heapq
import typing

Node: typing.TypeAlias = tuple[int, int, str]

DIRECTIONS = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}
SIDEWAYS = {
    'N': ['W', 'E'],
    'E': ['N', 'S'],
    'S': ['W', 'E'],
    'W': ['N', 'S'],
}


def create_graph(grid: list[list[int]], steps: range) -> dict[Node, dict[Node, int]]:
    n, m = len(grid), len(grid[0])
    graph = {}

    def get_edges(i: int, j: int, dir1: str) -> dict[Node, int]:
        edges = {}
        di, dj = DIRECTIONS[dir1]
        acc = 0
        for s in range(1, steps.stop):
            i, j = i + di, j + dj
            if not (0 <= i < n and 0 <= j < m):
                break
            acc += grid[i][j]

            if s not in steps:
                continue
            for dir2 in SIDEWAYS[dir1]:
                edges[i, j, dir2] = acc
        return edges

    for i in range(n):
        for j in range(m):
            for dir1 in DIRECTIONS:
                graph[i, j, dir1] = get_edges(i, j, dir1)
    return graph


def dijkstra(
    graph: dict[Node, dict[Node, int]], sources: list[Node]
) -> dict[Node, int]:
    dist = {}

    queue = [(0, s) for s in sources]
    while queue:
        score, v = heapq.heappop(queue)
        if v in dist:
            continue

        dist[v] = score
        for w in graph[v]:
            if w in dist:
                continue
            score = dist[v] + graph[v][w]
            heapq.heappush(queue, (score, w))

    return dist


def solve(text: str) -> float:
    # TODO: consider using grid dict
    grid = [list(map(int, line)) for line in text.splitlines()]
    n, m = len(grid), len(grid[0])
    graph = create_graph(grid, range(1, 4))

    sources = [(0, 0, d) for d in DIRECTIONS]
    dist = dijkstra(graph, sources)
    targets = [(n - 1, m - 1, d) for d in DIRECTIONS]
    return min(dist.get(t, float('inf')) for t in targets)


if __name__ == "__main__":
    pass
