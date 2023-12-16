import functools
import re


def parse_record(line: str) -> tuple[str, tuple[int, ...]]:
    left, right = line.split()
    return left, tuple(int(x) for x in right.split(','))


# TODO: optimize that
@functools.cache
def arrange(pattern: str, damaged: tuple[int]) -> int:
    if not pattern and not damaged:
        return 1
    if not pattern and damaged:
        return 0

    if pattern[0] == '.':
        return arrange(pattern[1:], damaged)

    if damaged and re.match(fr'#[#?]{{{damaged[0] - 1}}}([.?]|$)', pattern):
        return arrange(pattern[damaged[0] + 1 :], damaged[1:])
    bonus = 0
    if pattern[0] == '?':
        bonus = arrange(pattern[1:], damaged)
    if damaged and re.match(fr'\?[#?]{{{damaged[0] - 1}}}([.?]|$)', pattern):
        return arrange(pattern[damaged[0] + 1 :], damaged[1:]) + bonus
    return bonus


def solve(text: str) -> int:
    records = [parse_record(line) for line in text.splitlines()]
    return sum(arrange(*r) for r in records)


if __name__ == '__main__':
    pass
