import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, steps, expected',
    [
        ('example.txt', 6, 16),
        ('input.txt', 64, 3600),
    ],
)
def test_part1(filename: str, steps: int, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text, steps) == expected


@pytest.mark.parametrize(
    'filename, steps, expected',
    [
        ('input.txt', 6, 44),
        ('input.txt', 10, 106),
        ('input.txt', 50, 2160),
        ('input.txt', 100, 8741),
        ('input.txt', 500, 214365),
        ('input.txt', 26501365, 599763113936220),
    ],
)
def test_part2(filename: str, steps: int, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text, steps) == expected
