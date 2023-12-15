import dataclasses


@dataclasses.dataclass
class Record:
    start: int
    unknowns: list[int]
    damaged: list[int]
    _len_unknowns: int = 0
    _len_damaged: int = 0

    @classmethod
    def parse(cls, line: str) -> 'Record':
        left, right = line.split()
        start = sum(1 << i for i, c in enumerate(left[::-1]) if c == '#')
        unknowns = [i for i, c in enumerate(left[::-1]) if c == '?']
        damaged = [int(s) for s in right.split(',')]
        return cls(start, unknowns, damaged)

    def __post_init__(self):
        self._len_unknowns = len(self.unknowns)
        self._len_damaged = len(self.damaged)

    def match(self, state: int) -> bool:
        count = 0
        i = self._len_damaged - 1
        while state:
            if state & 1:
                count += 1
            else:
                if count:
                    if i < 0 or count != self.damaged[i]:
                        return False
                    count = 0
                    i -= 1
            state >>= 1
        if count and count != self.damaged[i]:
            return False
        return i == 0

    def arrange(self) -> int:
        count = 0
        for mask in range(1 << self._len_unknowns):
            state = self.start
            for i, u in enumerate(self.unknowns):
                if mask & (1 << i):
                    state |= 1 << u
            if self.match(state):
                count += 1
        return count

    def __str__(self) -> str:
        return f'{self.start:b} {self.unknowns} {self.damaged}'


def solve(text: str) -> int:
    records = [Record.parse(line) for line in text.splitlines()]
    return sum(r.arrange() for r in records)


if __name__ == '__main__':
    pass
