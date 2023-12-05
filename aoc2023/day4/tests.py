import pathlib

import pytest

from . import part1


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 13),
        ('input.txt', 20117),
    ],
)
def test_part1(filename: str, expected: int):
    with open(pathlib.Path(__file__).parent.absolute() / filename) as f:
        text = f.read()
    assert part1.solve(text) == expected
