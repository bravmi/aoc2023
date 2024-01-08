import itertools
import math

from . import part1


def node_steps(node: str, instructions: str, nodes: dict[str, dict[str, str]]) -> int:
    for steps, inst in enumerate(itertools.cycle(instructions)):
        if node[-1] == 'Z':
            break
        node = nodes[node][inst]
    return steps


def solve(text: str) -> int:
    instructions, rest = text.split('\n\n', 1)
    nodes = part1.parse_nodes(rest)
    steps = [node_steps(node, instructions, nodes) for node in nodes if node[-1] == 'A']
    return math.lcm(*steps)


if __name__ == '__main__':
    pass
