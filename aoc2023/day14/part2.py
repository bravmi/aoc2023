import dataclasses

CYCLES = 1_000_000_000


# TODO: optimize sliding
@dataclasses.dataclass
class Platform:
    _rocks: list[list[str]]

    def slide_north(self) -> None:
        n, m = len(self._rocks), len(self._rocks[0])
        for j in range(m):
            for i in range(n):
                if self._rocks[i][j] == 'O':
                    k = i
                    while k > 0 and self._rocks[k - 1][j] == '.':
                        self._rocks[k][j], self._rocks[k - 1][j] = (
                            self._rocks[k - 1][j],
                            self._rocks[k][j],
                        )
                        k -= 1

    def slide_west(self) -> None:
        n, m = len(self._rocks), len(self._rocks[0])
        for i in range(n):
            for j in range(m):
                if self._rocks[i][j] == 'O':
                    k = j
                    while k > 0 and self._rocks[i][k - 1] == '.':
                        self._rocks[i][k], self._rocks[i][k - 1] = (
                            self._rocks[i][k - 1],
                            self._rocks[i][k],
                        )
                        k -= 1

    def slide_south(self) -> None:
        n, m = len(self._rocks), len(self._rocks[0])
        for j in range(m):
            for i in range(n - 1, -1, -1):
                if self._rocks[i][j] == 'O':
                    k = i
                    while k < n - 1 and self._rocks[k + 1][j] == '.':
                        self._rocks[k][j], self._rocks[k + 1][j] = (
                            self._rocks[k + 1][j],
                            self._rocks[k][j],
                        )
                        k += 1

    def slide_east(self) -> None:
        n, m = len(self._rocks), len(self._rocks[0])
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if self._rocks[i][j] == 'O':
                    k = j
                    while k < m - 1 and self._rocks[i][k + 1] == '.':
                        self._rocks[i][k], self._rocks[i][k + 1] = (
                            self._rocks[i][k + 1],
                            self._rocks[i][k],
                        )
                        k += 1

    def calc_load(self) -> int:
        n, m = len(self._rocks), len(self._rocks[0])
        return sum(
            n - i for i in range(n) for j in range(m) if self._rocks[i][j] == 'O'
        )

    def __hash__(self) -> int:
        return hash(''.join(''.join(l) for l in self._rocks))

    def do_cycles(self) -> int:
        seen = {hash(self): 0}
        loads = {0: self.calc_load()}
        for i in range(CYCLES):
            self.slide_north()
            self.slide_west()
            self.slide_south()
            self.slide_east()
            h = hash(self)
            if h in seen:
                end = i
                start = seen[h]
                j = (CYCLES - start) % (end - start) - 1
                return loads[start + j]
            seen[h] = i
            loads[i] = self.calc_load()
        return loads[i]


def solve(text: str) -> int:
    rocks = [list(l) for l in text.splitlines()]
    platform = Platform(rocks)
    return platform.do_cycles()


if __name__ == '__main__':
    pass
