import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 374),
        ('input.txt', 9627977),
    ],
)
def test_part1(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text) == expected


@pytest.mark.parametrize(
    'filename, expansion, expected',
    [
        ('example.txt', 2, 374),
        ('example.txt', 10, 1030),
        ('example.txt', 100, 8410),
        ('input.txt', 1_000_000, 644248339497),
    ],
)
def test_part2(filename: str, expansion: int, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text, expansion) == expected
