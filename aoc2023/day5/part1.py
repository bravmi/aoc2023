import dataclasses
import typing


@dataclasses.dataclass
class Map:
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


def parse_maps(text: str) -> list[Map]:
    _, *rest = text.splitlines()
    return [Map.parse(s) for s in rest]


def convert(num: int, maps: list[Map]) -> int:
    for map in maps:
        dst = map.get(num)
        if dst is not None:
            return dst
    return num


def solve(text: str) -> int:
    section, *rest = text.split('\n\n')
    nums = [int(s) for s in section.split()[1:]]
    for section in rest:
        maps = parse_maps(section)
        nums = [convert(n, maps) for n in nums]
    return min(nums)


if __name__ == '__main__':
    pass
