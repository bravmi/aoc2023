from . import part1


# TODO: get rid of inserts
def prediction(hist: list[int]) -> int:
    seqs = [hist]
    while not all(x == 0 for x in seqs[-1]):
        diffs = [y - x for x, y in zip(seqs[-1], seqs[-1][1:])]
        seqs.append(diffs)
    seqs[-1].insert(0, 0)
    for i in range(len(seqs) - 2, -1, -1):
        seqs[i].insert(0, seqs[i][0] - seqs[i + 1][0])
    return seqs[0][0]


def solve(text: str) -> int:
    histories = [part1.parse_history(line) for line in text.splitlines()]
    return sum(prediction(hist) for hist in histories)


if __name__ == '__main__':
    pass
