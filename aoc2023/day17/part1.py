import heapq
import typing

Node: typing.TypeAlias = tuple[int, int, str, int]

DIRECTIONS = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
BACKWARD = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}


def create_graph(grid: list[list[int]], move: range) -> dict[Node, dict[Node, int]]:
    n, m = len(grid), len(grid[0])
    graph = {}

    def get_edges(i1: int, j1: int, dir1: str, steps: int) -> dict[Node, int]:
        edges = {}
        for dir2, (di, dj) in DIRECTIONS.items():
            if dir2 == BACKWARD[dir1]:
                continue
            i2, j2 = i1 + di, j1 + dj
            if 0 <= i2 < n and 0 <= j2 < m:
                if dir1 == dir2:
                    if steps < move.stop - 1:
                        edges[i2, j2, dir2, steps + 1] = grid[i2][j2]
                else:
                    edges[i2, j2, dir2, move[0]] = grid[i2][j2]
        return edges

    for i in range(n):
        for j in range(m):
            for dir1 in ['N', 'E', 'S', 'W']:
                for steps in move:
                    graph[i, j, dir1, steps] = get_edges(i, j, dir1, steps)
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
    grid = [list(map(int, line)) for line in text.splitlines()]
    n, m = len(grid), len(grid[0])
    move = range(1, 4)
    graph = create_graph(grid, move)

    sources = [(0, 0, d, move[0]) for d in ['N', 'E', 'S', 'W']]
    dist = dijkstra(graph, sources)
    targets = [(n - 1, m - 1, d, s) for d in ['N', 'E', 'S', 'W'] for s in move]
    return min(dist.get(t, float('inf')) for t in targets)


if __name__ == "__main__":
    pass
