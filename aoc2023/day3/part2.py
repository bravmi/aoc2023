import collections
import math

from . import part1


def find_region_gears(
    board: dict[tuple[int, int], str],
    regions: dict[tuple[int, int], int],
) -> dict[tuple[int, int], list[tuple[int, int]]]:
    gears = collections.defaultdict(list)
    for start, n in regions.items():
        for p in part1.adjacent(start, n):
            if board[p] == '*':
                gears[p].append(start)
    return gears


def solve(text: str) -> int:
    board = part1.parse_board(text)
    regions = part1.find_number_regions(board)
    gears = find_region_gears(board, regions)
    res = 0
    for starts in gears.values():
        if len(starts) != 1:
            res += math.prod(part1.part_number(board, s, regions[s]) for s in starts)
    return res


if __name__ == '__main__':
    pass
