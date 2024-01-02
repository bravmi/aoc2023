import collections
import heapq
import math


def a_star(
    grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]
) -> float:
    n, m = len(grid), len(grid[0])
    heuristic: dict[tuple[int, int], float] = collections.defaultdict(
        lambda: float('inf')
    )
    heuristic[end] = 0
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                heuristic[i, j] = min(
                    heuristic[i, j], heuristic[i + di, j + dj] + grid[i][j]
                )

    def same_line(path: list[tuple[int, int]], i: int, j: int, length: int = 4) -> bool:
        if len(path) < length:
            return False
        for k in range(-2, -length - 1, -1):
            if path[k][0] != i:
                break
        else:
            return True
        for k in range(-2, -length - 1, -1):
            if path[k][1] != j:
                break
        else:
            return True
        return False

    def get_neighbors(
        node: tuple[int, int], path: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        # TODO: do we even need node here?
        i, j = node
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        return [
            (i + di, j + dj)
            for di, dj in directions
            if 0 <= i + di < n
            and 0 <= j + dj < m
            and not same_line(path, i + di, j + dj)
            and not (i + di, j + dj) in path
        ]

    frontier: list[tuple[float, int, list[tuple[int, int]]]] = [(0, 0, [start])]
    start_cost = grid[0][0]
    cost_so_far: dict[tuple[tuple[int, int], ...], int] = {
        tuple(
            [start],
        ): start_cost
    }
    while frontier:
        _, cost, path = heapq.heappop(frontier)
        curr = path[-1]
        cost += grid[curr[0]][curr[1]]
        if curr == end:
            return cost - grid[0][0]

        key = tuple(path[-4:])
        if cost > cost_so_far.get(key, math.inf):
            continue
        cost_so_far[key] = cost

        for node in get_neighbors(curr, path):
            priority = cost + heuristic[*node]
            heapq.heappush(frontier, (priority, cost, path + [node]))
    return math.inf


def solve(text: str) -> float:
    grid = [list(map(int, line)) for line in text.splitlines()]
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    return a_star(grid, start, end)


if __name__ == "__main__":
    pass
