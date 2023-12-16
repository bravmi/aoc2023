from . import part1

COUNT = 5


def parse_record(line: str) -> tuple[str, tuple[int, ...]]:
    left, right = line.split()
    pattern = '?'.join([left] * COUNT)
    damaged = tuple(int(x) for x in right.split(',')) * COUNT
    return pattern, damaged


def solve(text: str) -> int:
    records = [parse_record(line) for line in text.splitlines()]
    return sum(part1.arrange(*r) for r in records)


if __name__ == '__main__':
    pass
