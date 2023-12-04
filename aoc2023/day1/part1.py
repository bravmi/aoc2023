def calibration(line: str) -> int:
    digits = [c for c in line if c.isdigit()]
    return int(digits[0]) * 10 + int(digits[-1])


def solve(text: str) -> int:
    return sum(calibration(line) for line in text.splitlines())


if __name__ == '__main__':
    pass
