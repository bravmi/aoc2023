import copy
import dataclasses
import typing

from aoc2023 import day5

from . import part1


@dataclasses.dataclass
class PartRange:
    x: day5.Range = dataclasses.field(default_factory=lambda: day5.Range(1, 4001))
    m: day5.Range = dataclasses.field(default_factory=lambda: day5.Range(1, 4001))
    a: day5.Range = dataclasses.field(default_factory=lambda: day5.Range(1, 4001))
    s: day5.Range = dataclasses.field(default_factory=lambda: day5.Range(1, 4001))
    state = 'in'

    def combinations(self) -> int:
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)

    def accepted(self) -> bool:
        return self.state == 'A'

    def final(self) -> bool:
        return self.state in ['A', 'R']

    def sub(self, cond: part1.Condition) -> typing.Self:
        # TODO: refactor that
        cat = cond.cat
        cat_rng = getattr(self, cat)
        setattr(self, cat, (cat_rng - cond.rng)[0])
        pr = copy.copy(self)
        setattr(pr, cat, cat_rng & cond.rng)
        return pr

    def run(self, workflows: dict[str, list[part1.Rule]]) -> list[typing.Self]:
        final = []
        stack = [self]
        while stack:
            pr1 = stack.pop()
            for rule in workflows[pr1.state]:
                pr2 = pr1 if rule.cond is None else pr1.sub(rule.cond)
                pr2.state = rule.state
                if pr2.final():
                    final.append(pr2)
                else:
                    stack.append(pr2)
        return final

    def __repr__(self) -> str:
        return 'PartRange(x={}, m={}, a={}, s={}, state={})'.format(
            self.x, self.m, self.a, self.s, self.state
        )


def parse_workflow(line: str) -> tuple[str, list[part1.Rule]]:
    name, rest = line.split('{')
    return name, [part1.Rule.parse(s) for s in rest[:-1].split(',')]


def solve(text: str) -> int:
    text1, _ = text.split('\n\n')
    workflows = dict(part1.parse_workflow(line) for line in text1.splitlines())
    pr = PartRange()
    part_ranges = pr.run(workflows)
    return sum(part.combinations() for part in part_ranges if part.accepted())


if __name__ == '__main__':
    pass
