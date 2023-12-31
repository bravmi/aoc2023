import math


def parse_number(line: str) -> int:
    return int(''.join(line.split()[1:]))


def parse_races(text: str) -> tuple[int, int]:
    lines = text.splitlines()
    assert len(lines) == 2
    return parse_number(lines[0]), parse_number(lines[1])


# TODO: consider the case when t1 or t2 are integers
def winning_ways(time: int, dist: int) -> int:
    a, b, c = 1, -time, dist
    D = b**2 - 4 * a * c
    t1 = -b / 2 - (D**0.5) / 2
    t2 = -b / 2 + (D**0.5) / 2
    return math.floor(t2) - math.ceil(t1) + 1


def solve(text: str) -> int:
    return winning_ways(*parse_races(text))


if __name__ == '__main__':
    pass
