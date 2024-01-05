from aoc2023 import day10

from . import part1


def parse_step(line: str) -> tuple[str, int]:
    *_, code = line.split()
    code = code[1:-1]
    d = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[code[-1]]
    return d, int(code[1:-1], 16)


def solve(text: str) -> int:
    steps = [parse_step(line) for line in text.splitlines()]
    path = part1.parse_path(steps)
    return day10.part2.inner_shoelace(path) + day10.part2.border(path)


if __name__ == '__main__':
    pass
