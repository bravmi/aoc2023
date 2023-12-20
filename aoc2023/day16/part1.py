import sys


def parse_grid(text: str) -> list[list[str]]:
    return [list(line) for line in text.strip().splitlines()]


# TODO: refactor that
def energize(grid: list[list[str]]) -> list[list[str]]:
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

    dfs(0, 0, 0, 1)
    return tiles


def solve(text: str) -> int:
    sys.setrecursionlimit(10000)
    grid = parse_grid(text)
    return sum(row.count('#') for row in energize(grid))


if __name__ == '__main__':
    pass
