import itertools
import string

WORD_TO_NUMBER = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def left_digit(line: str) -> int:
    items = [
        (line.find(word), word)
        for word in itertools.chain(WORD_TO_NUMBER.keys(), string.digits)
    ]
    items = [(i, word) for i, word in items if i >= 0]
    if items:
        _, word = min(items)
        return int(WORD_TO_NUMBER.get(word, word))
    return 0


def right_digit(line: str) -> int:
    items = [
        (line.rfind(word), word)
        for word in itertools.chain(WORD_TO_NUMBER.keys(), string.digits)
    ]
    items = [(i, word) for i, word in items if i >= 0]
    if items:
        _, word = max(items)
        return int(WORD_TO_NUMBER.get(word, word))
    return 0


def solve(text: str) -> int:
    res = 0
    for line in text.splitlines():
        res += left_digit(line) * 10 + right_digit(line)
    return res


if __name__ == '__main__':
    pass
