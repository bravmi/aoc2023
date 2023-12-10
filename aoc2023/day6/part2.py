from . import part1


def parse_number(line: str) -> int:
    return int(''.join(line.split()[1:]))


def parse_races(text: str) -> tuple[int, int]:
    lines = text.splitlines()
    assert len(lines) == 2
    return parse_number(lines[0]), parse_number(lines[1])


def solve(text: str) -> int:
    return part1.win_ways(*parse_races(text))


if __name__ == '__main__':
    pass
