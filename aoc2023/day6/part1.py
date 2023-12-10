import math


def parse_numbers(line: str) -> list[int]:
    return list(map(int, line.split()[1:]))


def parse_races(text: str) -> list[tuple[int, int]]:
    lines = text.splitlines()
    assert len(lines) == 2
    return list(zip(parse_numbers(lines[0]), parse_numbers(lines[1])))


def winning_ways(time: int, dist: int) -> int:
    return sum(t * (time - t) > dist for t in range(time))


def solve(text: str) -> int:
    return math.prod(winning_ways(t, d) for t, d in parse_races(text))


if __name__ == '__main__':
    pass
