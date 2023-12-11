from __future__ import annotations

import dataclasses

from . import part1


@dataclasses.dataclass
class Range:
    start: int
    end: int

    def __and__(self, other: Range) -> Range:
        return Range(max(self.start, other.start), min(self.end, other.end))

    def __bool__(self) -> bool:
        return self.start < self.end

    def __sub__(self, other: Range) -> list[Range]:
        if other.start <= self.start < self.end <= other.end:
            return []
        if self.start <= other.start <= self.end <= other.end:
            return [Range(self.start, other.start)]
        if other.start <= self.start <= other.end <= self.end:
            return [Range(other.end, self.end)]
        if self.start <= other.start < other.end <= self.end:
            return [Range(self.start, other.start), Range(other.end, self.end)]
        return [self]


def parse_seeds(line: str) -> list[Range]:
    nums = [int(s) for s in line.split()[1:]]
    return [Range(n, n + l) for n, l in zip(nums[::2], nums[1::2])]


# TODO: clean up this range mess
def convert(rng: Range, maps: list[part1.Map]) -> list[Range]:
    result = []
    for map in maps:
        src_rng = rng & Range(map.src, map.src + map.len)
        if src_rng:
            dst_start = map.dst + (src_rng.start - map.src)
            dst_rng = Range(dst_start, dst_start + src_rng.end - src_rng.start)
            result.append(dst_rng)
            for r in rng - src_rng:
                result.extend(convert(r, maps))
            break
    else:
        result.append(rng)
    return result


def solve(text: str) -> int:
    section, *rest = text.split('\n\n')
    ranges = parse_seeds(section)
    print(ranges)
    for section in rest:
        maps = part1.parse_maps(section)
        maps.sort(key=lambda m: m.src)
        ranges = sum([convert(r, maps) for r in ranges], [])
    return min(r.start for r in ranges)


if __name__ == '__main__':
    pass
