import pathlib

from aoc2023 import day9

from . import part1

PARENT = pathlib.Path(__file__).parent.absolute()
OUTPUT = PARENT / 'output.txt'

TERMS = 3


def precompute(steps: int) -> None:
    garden = part1.parse_garden(PARENT.joinpath('input.txt').read_text())
    data = '\n'.join(str(c) for c in part1.plot_counts(garden, steps))
    OUTPUT.write_text(data)


def plot_count(garden: list[list[str]], steps: int) -> int:
    n, m = len(garden), len(garden[0])
    assert n == m

    q, r = divmod(steps, n)
    plots = [1] + [int(x) for x in OUTPUT.read_text().splitlines()]
    hist = plots[r::n][:TERMS]
    if q < TERMS:
        return hist[q]

    assert len(hist) >= TERMS
    for _ in range(TERMS, q + 1):
        hist = hist[-2:] + [day9.prediction(hist)]
    return hist[-1]


def solve(text: str, steps: int) -> int:
    garden = part1.parse_garden(text)
    return plot_count(garden, steps)


if __name__ == '__main__':
    precompute(500)
