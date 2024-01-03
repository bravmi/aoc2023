from . import part1


def solve(text: str) -> float:
    grid = [list(map(int, line)) for line in text.splitlines()]
    n, m = len(grid), len(grid[0])
    graph = part1.create_graph(grid, range(4, 11))

    sources = [(0, 0, d) for d in part1.DIRECTIONS]
    dist = part1.dijkstra(graph, sources)
    targets = [(n - 1, m - 1, d) for d in part1.DIRECTIONS]
    return min(dist.get(t, float('inf')) for t in targets)


if __name__ == "__main__":
    pass
