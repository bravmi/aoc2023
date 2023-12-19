import collections
import dataclasses

from . import part1


@dataclasses.dataclass
class Box:
    lenses: list[tuple[str, int]] = dataclasses.field(default_factory=list)

    def add(self, label: str, length: int) -> None:
        lens = label, length
        for i, (l, _) in enumerate(self.lenses):
            if l == label:
                self.lenses[i] = lens
                return
        self.lenses.append(lens)

    def remove(self, label: str) -> None:
        for i, (l, _) in enumerate(self.lenses):
            if l == label:
                del self.lenses[i]
                return


def focusing_power(boxes: dict[int, Box]) -> int:
    result = 0
    for num, box in boxes.items():
        for i, (_, length) in enumerate(box.lenses, 1):
            result += (1 + num) * i * length
    return result


# TODO: refactor parsing
def solve(text: str) -> int:
    steps = text.strip().split(',')
    boxes: dict[int, Box] = collections.defaultdict(Box)
    for step in steps:
        parts = step.split('=')
        if len(parts) == 2:
            label, length = parts[0], int(parts[1])
            h = part1.run_hash(label)
            boxes[h].add(label, length)
            continue
        parts = step.split('-')
        if len(parts) == 2:
            label, _ = parts
            h = part1.run_hash(label)
            boxes[h].remove(label)
            continue
    return focusing_power(boxes)


if __name__ == '__main__':
    pass
