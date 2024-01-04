from aoc2023 import day10


def parse_step(line: str) -> tuple[str, int]:
    d, m, *_ = line.split()
    return d, int(m)


def parse_path(steps: list[tuple[str, int]]) -> list[tuple[int, int]]:
    i, j = 0, 0
    path = [(i, j)]
    for d, m in steps:
        match d:
            case 'U':
                i -= m
            case 'R':
                j += m
            case 'D':
                i += m
            case 'L':
                j -= m
        path.append((i, j))
    return path


def solve(text: str) -> int:
    steps = [parse_step(line) for line in text.splitlines()]
    path = parse_path(steps)
    return day10.part2.shoelace_inner(path) + day10.part2.border(path)


if __name__ == '__main__':
    pass
