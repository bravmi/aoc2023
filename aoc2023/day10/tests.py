import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example1.txt', 4),
        ('example2.txt', 8),
        ('input.txt', 6786),
    ],
)
def test_part1(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text) == expected


# TODO: check test files naming here
@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example3.txt', 4),
        ('example4.txt', 4),
        ('example5.txt', 8),
        ('example6.txt', 10),
        ('input.txt', 495),
    ],
)
def test_part2(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text) == expected
