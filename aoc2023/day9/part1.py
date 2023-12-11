def parse_history(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def prediction(hist: list[int]) -> int:
    seqs = [hist]
    while not all(x == 0 for x in seqs[-1]):
        diffs = [y - x for x, y in zip(seqs[-1], seqs[-1][1:])]
        seqs.append(diffs)
    seqs[-1].append(0)
    for i in range(len(seqs) - 2, -1, -1):
        seqs[i].append(seqs[i][-1] + seqs[i + 1][-1])
    return seqs[0][-1]


def solve(text: str) -> int:
    histories = [parse_history(line) for line in text.splitlines()]
    return sum(prediction(hist) for hist in histories)


if __name__ == '__main__':
    pass
