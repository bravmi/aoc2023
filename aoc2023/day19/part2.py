import copy
import dataclasses
import typing

from aoc2023 import day5

from . import part1


@dataclasses.dataclass
class PartRange:
    x = day5.Range(1, 4001)
    m = day5.Range(1, 4001)
    a = day5.Range(1, 4001)
    s = day5.Range(1, 4001)
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
        curr_rng = getattr(self, cat)
        new_rng = curr_rng & cond.rng
        setattr(self, cat, (curr_rng - cond.rng)[0])
        new_part = copy.copy(self)
        setattr(new_part, cat, new_rng)
        return new_part

    def run(self, workflows: dict[str, list[part1.Rule]]) -> list['PartRange']:
        # TODO: refactor that
        final = []
        stack = [self]
        while stack:
            part = stack.pop()
            for rule in workflows[part.state]:
                if rule.cond is None:
                    part.state = rule.state
                    if part.final():
                        final.append(part)
                    else:
                        stack.append(part)
                    continue

                new_part = part.sub(rule.cond)
                new_part.state = rule.state
                if new_part.final():
                    final.append(new_part)
                else:
                    stack.append(new_part)
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
    part = PartRange()
    parts = part.run(workflows)
    return sum(part.combinations() for part in parts if part.accepted())


if __name__ == '__main__':
    pass
