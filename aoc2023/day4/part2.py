import collections

from . import part1


def solve(text: str) -> int:
    card_copies: dict[int, int] = collections.defaultdict(int)
    for i, line in enumerate(text.splitlines(), 1):
        card_copies[i] += 1
        winning, present = part1.parse_card(line)
        appear = len(set(present) & set(winning))
        for j in range(i + 1, i + appear + 1):
            card_copies[j] += card_copies[i]
    return sum(card_copies.values())


if __name__ == '__main__':
    pass
