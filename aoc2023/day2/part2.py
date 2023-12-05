from . import part1


def power(rounds: list[part1.Round]) -> int:
    return (
        max(r.red for r in rounds)
        * max(r.green for r in rounds)
        * max(r.blue for r in rounds)
    )


def solve(text: str) -> int:
    res = 0
    for game in text.splitlines():
        res += power(part1.parse_game(game))
    return res


if __name__ == '__main__':
    pass
