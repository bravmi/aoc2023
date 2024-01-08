import collections
import math

from . import part1

MAX_TIMES = 10000


def push_button(
    graph: dict[str, list[str]], modules: dict[str, part1.Module], final: str
) -> int:
    finals1 = [v for v in graph if final in graph[v]]
    assert len(finals1) == 1
    assert isinstance(modules[finals1[0]], part1.Conjunction)
    finals2 = [v for v in graph if finals1[0] in graph[v]]
    cycles = {v: 0 for v in finals2}

    for times in range(1, MAX_TIMES + 1):
        queue = collections.deque([('broadcaster', False)])
        while queue:
            v, sig1 = queue.popleft()
            if v not in graph:
                continue
            if sig1 and cycles.get(v) == 0:
                cycles[v] = times
                if all(cycles.values()):
                    return math.lcm(*cycles.values())

            for w in graph[v]:
                if w not in modules:
                    continue
                sig2 = modules[w].send(v, sig1)
                if sig2 is not None:
                    queue.append((w, sig2))
    return 0


def solve(text: str) -> int:
    lines = text.splitlines()
    graph = part1.parse_graph(lines)
    modules = part1.parse_modules(lines, graph)
    return push_button(graph, modules, final='rx')


if __name__ == '__main__':
    pass
