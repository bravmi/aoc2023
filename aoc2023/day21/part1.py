DIRECTIONS = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}


def plot_counts(garden: list[list[str]], steps: int) -> list[int]:
    n, m = len(garden), len(garden[0])
    start = next((i, j) for i in range(n) for j in range(m) if garden[i][j] == 'S')

    counts = []
    plots = {start}
    for _ in range(steps):
        plots = {
            (i + di, j + dj)
            for (i, j) in plots
            for di, dj in DIRECTIONS.values()
            if garden[(i + di) % n][(j + dj) % m] != '#'
        }
        counts.append(len(plots))

    return counts


def parse_garden(text: str) -> list[list[str]]:
    return [list(line) for line in text.splitlines()]


def solve(text: str, steps: int) -> int:
    garden = [list(line) for line in text.splitlines()]
    counts = plot_counts(garden, steps)
    return counts[-1]


if __name__ == '__main__':
    pass
