import collections
import functools
import math

from . import part1

MAX_TIMES = 10000


def push_button(graph: dict[str, list[str]], modules: dict[str, part1.Module]) -> int:
    counter = dict.fromkeys({'sg', 'lm', 'dh', 'db'}, 0)
    for times in range(1, MAX_TIMES + 1):
        queue = collections.deque([('broadcaster', False)])
        while queue:
            v, sig1 = queue.popleft()
            if v not in graph:
                continue
            if sig1 and counter.get(v) == 0:
                counter[v] = times
                if all(counter.values()):
                    return functools.reduce(math.lcm, counter.values())

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
    modules = {
        module.name: module for module in (part1.parse_modules(line) for line in lines)
    }
    for v in graph:
        for w in graph[v]:
            if w in modules and isinstance(modules[w], part1.Conjunction):
                modules[w].send(v, False)
    return push_button(graph, modules)


if __name__ == '__main__':
    pass
