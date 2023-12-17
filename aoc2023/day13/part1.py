def mirror(lines1: list[str], lines2: list[str]) -> bool:
    return all(l1 == l2 for l1, l2 in zip(reversed(lines1), lines2))


def reflexion(lines: list[str]) -> int:
    for i in range(len(lines) - 1):
        if mirror(lines[: i + 1], lines[i + 1 :]):
            return i + 1
    return 0


# TODO: optimize that
def summarize(lines: list[str]) -> int:
    transposed = [''.join(l) for l in zip(*lines)]
    return reflexion(transposed) + 100 * reflexion(lines)


def solve(text: str) -> int:
    return sum(summarize(pattern.split()) for pattern in text.split('\n\n'))


if __name__ == '__main__':
    pass
