import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 35),
        ('input.txt', 650599855),
    ],
)
def test_part1(filename: str, expected: int):
    with open(pathlib.Path(__file__).parent.absolute() / filename) as f:
        text = f.read()
    assert part1.solve(text) == expected


@pytest.mark.skip
@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', ...),
        ('input.txt', ...),
    ],
)
def test_part2(filename: str, expected: int):
    with open(pathlib.Path(__file__).parent.absolute() / filename) as f:
        text = f.read()
    assert part2.solve(text) == expected
