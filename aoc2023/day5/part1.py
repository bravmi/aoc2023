import dataclasses
import typing


@dataclasses.dataclass
class Range:
    dst: int
    src: int
    len: int

    @classmethod
    def parse(cls, s: str) -> typing.Self:
        return cls(*map(int, s.split()))

    def get(self, num: int) -> int | None:
        if self.src <= num < self.src + self.len:
            return self.dst + (num - self.src)
        return None


def parse_ranges(text: str) -> list[Range]:
    _, *rest = text.splitlines()
    return [Range.parse(s) for s in rest]


def convert(num: int, ranges: list[Range]) -> int:
    for r in ranges:
        dst = r.get(num)
        if dst is not None:
            return dst
    return num


def solve(text: str) -> int:
    section, *rest = text.split('\n\n')
    nums = [int(s) for s in section.split()[1:]]
    for section in rest:
        ranges = parse_ranges(section)
        nums = [convert(n, ranges) for n in nums]
    return min(nums)


if __name__ == '__main__':
    pass
