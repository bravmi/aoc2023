import itertools
import sys


def parse_grid(text: str) -> list[list[str]]:
    return [list(line) for line in text.strip().splitlines()]


# TODO: optimize that
def max_energized(grid: list[list[str]]) -> int:
    n, m = len(grid), len(grid[0])
    tiles = [['.'] * m for _ in range(n)]
    seen = set()

    def dfs(i: int, j: int, di: int, dj: int) -> None:
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        if (i, j, di, dj) in seen:
            return

        tiles[i][j] = '#'
        seen.add((i, j, di, dj))
        if grid[i][j] == '.':
            dfs(i + di, j + dj, di, dj)
        elif grid[i][j] == '/':
            di, dj = -dj, -di
            dfs(i + di, j + dj, di, dj)
        elif grid[i][j] == '\\':
            di, dj = dj, di
            dfs(i + di, j + dj, di, dj)
        elif grid[i][j] == '-':
            if dj == 0:
                dfs(i, j + 1, 0, 1)
                dfs(i, j - 1, 0, -1)
            else:
                dfs(i + di, j + dj, di, dj)
        elif grid[i][j] == '|':
            if di == 0:
                dfs(i + 1, j, 1, 0)
                dfs(i - 1, j, -1, 0)
            else:
                dfs(i + di, j + dj, di, dj)

    energized = 0
    for i, j, di, dj in itertools.chain(
        ((0, j, 1, 0) for j in range(m)),
        ((n - 1, j, -1, 0) for j in range(m)),
        ((i, 0, 0, 1) for i in range(n)),
        ((i, m - 1, 0, -1) for i in range(n)),
    ):
        dfs(i, j, di, dj)
        energized = max(sum(row.count('#') for row in tiles), energized)
        tiles = [['.'] * m for _ in range(n)]
        seen.clear()
    return energized


def solve(text: str) -> int:
    sys.setrecursionlimit(10000)
    grid = parse_grid(text)
    return max_energized(grid)


if __name__ == '__main__':
    pass
