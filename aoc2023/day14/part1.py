def slide_north(platform: list[list[str]]) -> list[list[str]]:
    n, m = len(platform), len(platform[0])
    for j in range(m):
        for i in range(n):
            if platform[i][j] == 'O':
                k = i
                while k > 0 and platform[k - 1][j] == '.':
                    platform[k][j], platform[k - 1][j] = (
                        platform[k - 1][j],
                        platform[k][j],
                    )
                    k -= 1
    return platform


def calc_load(platform: list[list[str]]) -> int:
    n, m = len(platform), len(platform[0])
    return sum(n - i for i in range(n) for j in range(m) if platform[i][j] == 'O')


def solve(text: str) -> int:
    platform = [list(l) for l in text.splitlines()]
    return calc_load(slide_north(platform))


if __name__ == '__main__':
    pass
