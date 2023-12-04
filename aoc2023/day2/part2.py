import math

from . import part1

COLORS = ['red', 'green', 'blue']


def power(rounds: list[dict[str, int]]) -> int:
    cubes = {c: max(r.get(c, 0) for r in rounds) for c in COLORS}
    return math.prod(cubes.values())


def solve(text: str) -> int:
    res = 0
    for game in text.splitlines():
        _, rounds = part1.parse_game(game)
        res += power(rounds)
    return res


if __name__ == '__main__':
    pass
