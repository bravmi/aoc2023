def parse_card(line: str) -> tuple[list[str], list[str]]:
    _, line = line.split(':')
    left, right = line.split('|')
    return left.split(), right.split()


def points(line: str) -> int:
    winning, present = parse_card(line)
    appear = len(set(present) & set(winning))
    return 2 ** (appear - 1) if appear else 0


def solve(text: str) -> int:
    return sum(points(line) for line in text.splitlines())


if __name__ == '__main__':
    pass
