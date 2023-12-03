def solve(text: str) -> int:
    res = 0
    for line in text.splitlines():
        digits = [c for c in line if c.isdigit()]
        res += int(digits[0]) * 10 + int(digits[-1])
    return res


if __name__ == '__main__':
    pass
