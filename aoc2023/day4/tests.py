import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 13),
        ('input.txt', 20117),
    ],
)
def test_part1(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text) == expected


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 30),
        ('input.txt', 13768818),
    ],
)
def test_part2(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text) == expected
