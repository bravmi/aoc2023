LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse_color(s: str) -> tuple[str, int]:
    v, c = s.split()
    return c, int(v)


def parse_round(s: str) -> dict[str, int]:
    return dict(parse_color(c) for c in s.split(', '))


def parse_game(line: str) -> tuple[int, list[dict[str, int]]]:
    h, rest = line.split(': ')
    i = int(h.split()[1])
    return i, [parse_round(r) for r in rest.split('; ')]


def limited(d: dict[str, int]) -> bool:
    return all(d[c] <= LIMITS[c] for c in d)


def solve(text: str) -> int:
    res = 0
    for game in text.splitlines():
        index, rounds = parse_game(game)
        if all(limited(r) for r in rounds):
            res += index
    return res


if __name__ == '__main__':
    pass
