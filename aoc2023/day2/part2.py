from . import part1


def power(rounds: list[part1.Round]) -> int:
    return (
        max(r.red for r in rounds)
        * max(r.green for r in rounds)
        * max(r.blue for r in rounds)
    )


def solve(text: str) -> int:
    return sum(power(part1.parse_game(game)) for game in text.splitlines())


if __name__ == '__main__':
    pass
