def run_hash(s: str) -> int:
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr


def solve(text: str) -> int:
    steps = text.strip().split(',')
    return sum(map(run_hash, steps))


if __name__ == '__main__':
    pass
