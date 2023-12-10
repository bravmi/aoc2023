from __future__ import annotations

import collections
import dataclasses
import functools
import typing

CARD_LABELS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


@dataclasses.dataclass
class Hand:
    cards: str
    bid: int

    @functools.cached_property
    def type(self) -> list[int]:
        counter = collections.Counter(self.cards)
        return sorted(counter.values(), reverse=True)

    def __lt__(self, other: typing.Self) -> bool:
        if self.type == other.type:
            return tuple(CARD_LABELS[c1] for c1 in self.cards) < tuple(
                CARD_LABELS[c2] for c2 in other.cards
            )
        return self.type < other.type

    @classmethod
    def parse(cls, line: str) -> Hand:
        cards, bid = line.split()
        return Hand(cards, int(bid))


def solve(text: str) -> int:
    hands = [Hand.parse(line) for line in text.splitlines()]
    hands.sort()
    return sum(hand.bid * rank for rank, hand in enumerate(hands, start=1))


if __name__ == '__main__':
    pass
