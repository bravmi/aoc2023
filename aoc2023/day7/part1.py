from __future__ import annotations

import collections
import dataclasses
import enum
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


class HandType(enum.Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __lt__(self, other: typing.Self) -> bool:
        return self.value < other.value


@dataclasses.dataclass
class Hand:
    cards: str
    bid: int

    @functools.cached_property
    def type(self) -> HandType:
        counter = collections.Counter(self.cards)
        match sorted(counter.values()):
            case [5]:
                return HandType.FIVE_OF_A_KIND
            case [1, 4]:
                return HandType.FOUR_OF_A_KIND
            case [2, 3]:
                return HandType.FULL_HOUSE
            case [1, 1, 3]:
                return HandType.THREE_OF_A_KIND
            case [1, 2, 2]:
                return HandType.TWO_PAIR
            case [1, 1, 1, 2]:
                return HandType.ONE_PAIR
            case _:
                return HandType.HIGH_CARD

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
