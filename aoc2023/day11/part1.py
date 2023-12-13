import itertools


def expand(image: list[list[str]]) -> list[list[str]]:
    n, m = len(image), len(image[0])
    for j in range(m - 1, -1, -1):
        if all(image[i][j] == '.' for i in range(n)):
            for i in range(n):
                image[i].insert(j, '.')
            m += 1
    for i in range(n - 1, -1, -1):
        if all(image[i][j] == '.' for j in range(m)):
            image.insert(i, ['.'] * m)
    return image


def find_galaxies(image: list[list[str]]) -> list[tuple[int, int]]:
    n, m = len(image), len(image[0])
    return [(i, j) for i in range(n) for j in range(m) if image[i][j] == '#']


def shortest_distance(g1: tuple[int, int], g2: tuple[int, int]) -> int:
    i1, j1 = g1
    i2, j2 = g2
    return abs(i2 - i1) + abs(j2 - j1)


def solve(text: str) -> int:
    image = [list(line) for line in text.splitlines()]
    image = expand(image)
    galaxies = find_galaxies(image)
    return sum(
        shortest_distance(g1, g2) for g1, g2 in itertools.combinations(galaxies, 2)
    )


if __name__ == '__main__':
    pass
