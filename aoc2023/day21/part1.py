DIRECTIONS = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}


def plots(garden: list[list[str]], steps: int) -> int:
    n, m = len(garden), len(garden[0])
    start = next((i, j) for i in range(n) for j in range(m) if garden[i][j] == 'S')

    reached = {start}
    for _ in range(steps):
        reached = {
            (i + di, j + dj)
            for (i, j) in reached
            for di, dj in DIRECTIONS.values()
            if 0 <= i + di < n and 0 <= j + dj < m and garden[i + di][j + dj] != '#'
        }

    return len(reached)


def solve(text: str, steps: int) -> int:
    garden = [list(line) for line in text.splitlines()]
    return plots(garden, steps)


if __name__ == '__main__':
    pass
