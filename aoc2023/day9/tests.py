import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 114),
        ('input.txt', 1834108701),
    ],
)
def test_part1(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text) == expected


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 2),
        ('input.txt', 993),
    ],
)
def test_part2(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text) == expected
