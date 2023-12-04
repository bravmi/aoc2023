import collections


def parse_board(text: str) -> dict[tuple[int, int], str]:
    board = collections.defaultdict(lambda: '.')
    for i, line in enumerate(text.splitlines()):
        for j, c in enumerate(line):
            board[i, j] = c
    return board


def find_number_regions(
    board: dict[tuple[int, int], str]
) -> dict[tuple[int, int], int]:
    regions: dict[tuple[int, int], int] = collections.defaultdict(int)
    current = None
    for (i, j), c in sorted(board.items()):
        if not c.isdigit():
            current = None
            continue
        if current is None or i != current[0]:
            current = i, j
        regions[current] += 1
    return regions


def adjacent(p: tuple[int, int], n: int) -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(p[0] - 1, p[0] + 2)
        for j in range(p[1] - 1, p[1] + n + 1)
        if not (i == p[0] and p[1] <= j < p[1] + n)
    ]


def part_number(board: dict[tuple[int, int], str], p: tuple[int, int], n: int) -> int:
    digits = [board[p[0], j] for j in range(p[1], p[1] + n)]
    return int(''.join(digits))


def solve(text: str) -> int:
    board = parse_board(text)
    regions = find_number_regions(board)
    res = 0
    for start, n in regions.items():
        if any(board[p] != '.' for p in adjacent(start, n)):
            res += part_number(board, start, n)
    return res


if __name__ == '__main__':
    pass
