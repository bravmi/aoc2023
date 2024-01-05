import dataclasses
import typing

from aoc2023 import day5


@dataclasses.dataclass
class Condition:
    cat: str
    op: str
    rng: day5.Range

    @classmethod
    def parse(cls, s: str) -> typing.Self:
        cat, op, val = s[0], s[1], int(s[2:])
        start, end = 1, 4001
        if op == '>':
            start = val + 1
        elif op == '<':
            end = val
        return cls(cat, op, day5.Range(start, end))

    def check(self, part: 'Part') -> bool:
        part_val = getattr(part, self.cat)
        return part_val in self.rng


@dataclasses.dataclass
class Rule:
    state: str
    cond: Condition | None = None

    @classmethod
    def parse(cls, s: str) -> typing.Self:
        if ':' not in s:
            return cls(s)
        cond, workflow = s.split(':')
        return cls(workflow, Condition.parse(cond))


@dataclasses.dataclass
class Part:
    x: int
    m: int
    a: int
    s: int
    state = 'in'

    @classmethod
    def parse(cls, line: str) -> typing.Self:
        line = line[1:-1]
        values = [int(s.split('=')[1]) for s in line.split(',')]
        return cls(x=values[0], m=values[1], a=values[2], s=values[3])

    def run(self, workflows: dict[str, list[Rule]]) -> None:
        while not self.final():
            for rule in workflows[self.state]:
                if rule.cond is None or rule.cond.check(self):
                    self.state = rule.state
                    break

    def accepted(self) -> bool:
        return self.state == 'A'

    def final(self) -> bool:
        return self.state in ['A', 'R']

    def rating(self) -> int:
        return self.x + self.m + self.a + self.s


def parse_workflow(line: str) -> tuple[str, list[Rule]]:
    name, rest = line.split('{')
    return name, [Rule.parse(s) for s in rest[:-1].split(',')]


def solve(text: str) -> int:
    text1, text2 = text.split('\n\n')
    workflows = dict(parse_workflow(line) for line in text1.splitlines())
    parts = [Part.parse(line) for line in text2.splitlines()]
    for part in parts:
        part.run(workflows)
    return sum(part.rating() for part in parts if part.accepted())


if __name__ == '__main__':
    pass
