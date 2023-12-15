import dataclasses
import typing


@dataclasses.dataclass
class Record:
    pattern: str
    damaged: list[int]

    @classmethod
    def parse(cls, line: str) -> typing.Self:
        left, right = line.split()
        return cls(left, [int(x) for x in right.split(',')])

    def arrange(self) -> int:
        groups = [[0]]
        for c in self.pattern:
            match c:
                case '#':
                    for g in groups:
                        g[-1] += 1
                case '.':
                    for g in groups:
                        g.append(0)
                case '?':
                    for g in groups.copy():
                        groups.append(g + [0])
                        g[-1] += 1
        groups = [[d for d in g if d] for g in groups]
        return groups.count(self.damaged)


def solve(text: str) -> int:
    records = [Record.parse(line) for line in text.splitlines()]
    return sum(r.arrange() for r in records)


if __name__ == '__main__':
    pass
