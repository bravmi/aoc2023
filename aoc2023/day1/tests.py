import pytest

from .part1 import solve


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('example.txt', 142),
        ('input.txt', 55017),
    ],
)
def test_part1(filename: str, expected: int):
    with open(filename) as f:
        text = f.read()
    assert solve(text) == expected
