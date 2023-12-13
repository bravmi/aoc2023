import itertools

from . import part1


# TODO: consider using numpy here
def shortest_distance(
    g1: tuple[int, int],
    g2: tuple[int, int],
    empty_rows: set[int] | None = None,
    empty_columns: set[int] | None = None,
    expansion: int = 1,
) -> int:
    if empty_rows is None:
        empty_rows = set()
    if empty_columns is None:
        empty_columns = set()
    i1, j1 = g1
    i2, j2 = g2
    dist = abs(i2 - i1) + abs(j2 - j1)
    min_i, max_i = min(i1, i2), max(i1, i2)
    min_j, max_j = min(j1, j2), max(j1, j2)
    dist += sum(expansion - 1 for i in empty_rows if min_i < i < max_i)
    dist += sum(expansion - 1 for j in empty_columns if min_j < j < max_j)
    return dist


def solve(text: str, expansion: int) -> int:
    image = [list(line) for line in text.splitlines()]
    galaxies = part1.find_galaxies(image)
    empty_rows = {i for i, row in enumerate(image) if all(c == '.' for c in row)}
    empty_columns = {
        j for j in range(len(image[0])) if all(row[j] == '.' for row in image)
    }
    return sum(
        shortest_distance(
            g1,
            g2,
            empty_rows=empty_rows,
            empty_columns=empty_columns,
            expansion=expansion,
        )
        for g1, g2 in itertools.combinations(galaxies, 2)
    )


if __name__ == '__main__':
    pass
