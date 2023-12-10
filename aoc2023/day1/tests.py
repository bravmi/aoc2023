import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example1.txt', 142),
        ('input.txt', 55017),
    ],
)
def test_part1(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text) == expected


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example2.txt', 281),
        ('input.txt', 53539),
    ],
)
def test_part2(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text) == expected
