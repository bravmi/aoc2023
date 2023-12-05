import dataclasses
import typing

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclasses.dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other: typing.Self) -> bool:
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    @classmethod
    def parse(cls, s: str) -> typing.Self:
        return cls(**dict(parse_color(c) for c in s.split(', ')))


def parse_color(s: str) -> tuple[str, int]:
    v, c = s.split()
    return c, int(v)


def parse_game(line: str) -> list[Round]:
    _, rest = line.split(': ')
    return [Round.parse(s) for s in rest.split('; ')]


def solve(text: str) -> int:
    max_round = Round(MAX_RED, MAX_GREEN, MAX_BLUE)
    res = 0
    for i, line in enumerate(text.splitlines(), 1):
        if all(r <= max_round for r in parse_game(line)):
            res += i
    return res


if __name__ == '__main__':
    pass
