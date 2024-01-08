import pathlib

import pytest

from . import part1, part2


@pytest.mark.parametrize(
    'filename, steps, expected',
    [
        ('example.txt', 6, 16),
        ('input.txt', 64, ...),
    ],
)
def test_part1(filename: str, steps: int, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part1.solve(text, steps) == expected


@pytest.mark.skip
@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', ...),
        ('input.txt', ...),
    ],
)
def test_part2(filename: str, expected: int):
    text = pathlib.Path(__file__).parent.absolute().joinpath(filename).read_text()
    assert part2.solve(text) == expected
