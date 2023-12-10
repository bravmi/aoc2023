import itertools
import re


def parse_nodes(text: str) -> dict[str, dict[str, str]]:
    nodes = {}
    for line in text.splitlines():
        line = re.sub(r'[=\s(),]+', ' ', line)
        a, b, c = line.split()
        nodes[a] = {'L': b, 'R': c}
    return nodes


def solve(text: str) -> int:
    instructions, rest = text.split('\n\n', 1)
    nodes = parse_nodes(rest)
    node = 'AAA'
    for steps, inst in enumerate(itertools.cycle(instructions)):
        if node == 'ZZZ':
            break
        node = nodes[node][inst]
    return steps


if __name__ == '__main__':
    pass
