import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 8),
        ('input.txt', 3035),
    ],
)
def test_part1(filename: str, expected: int):
    with open(pathlib.Path(__file__).parent.absolute() / filename) as f:
        text = f.read()
    assert part1.solve(text) == expected


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 2286),
        ('input.txt', 66027),
    ],
)
def test_part2(filename: str, expected: int):
    with open(pathlib.Path(__file__).parent.absolute() / filename) as f:
        text = f.read()
    assert part2.solve(text) == expected
