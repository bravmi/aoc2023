from aoc2023.day10 import part2


def parse_step(line: str) -> tuple[str, int]:
    d, m, *_ = line.split()
    return d, int(m)


def parse_path(text: str) -> list[tuple[int, int]]:
    i, j = 0, 0
    path = [(i, j)]
    for line in text.splitlines():
        d, m = parse_step(line)
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
    path = parse_path(text)
    return part2.shoelace(path) + part2.border(path)


if __name__ == '__main__':
    pass
