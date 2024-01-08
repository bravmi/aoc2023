import abc
import collections
import dataclasses
import math


# TODO: refactor that out
@dataclasses.dataclass
class Module(abc.ABC):
    name: str

    @abc.abstractmethod
    def send(self, name: str, signal: bool) -> bool | None:
        pass


@dataclasses.dataclass
class Conjunction(Module):
    _inputs: dict[str, bool] = dataclasses.field(default_factory=dict)

    def send(self, name: str, signal: bool) -> bool:
        self._inputs[name] = signal
        return set(self._inputs.values()) != {True}


@dataclasses.dataclass
class FlipFlop(Module):
    _state: bool = False

    def send(self, name: str, signal: bool) -> bool | None:
        if signal:
            return None
        if not self._state:
            self._state = True
            return True
        else:
            self._state = False
            return False


@dataclasses.dataclass
class Broadcaster(Module):
    def send(self, name: str, signal: bool) -> bool:
        return signal


def parse_vertex(line: str) -> tuple[str, list[str]]:
    name, right = line.split(' -> ')
    if name[0] in '%&':
        name = name[1:]
    return name, right.split(', ')


def parse_graph(lines: list[str]) -> dict[str, list[str]]:
    return dict(parse_vertex(line) for line in lines)


def parse_module(line: str) -> Module:
    left, _ = line.split(' -> ')
    prefix, name = left[0], left[1:]
    match prefix:
        case '%':
            return FlipFlop(name)
        case '&':
            return Conjunction(name)
    return Broadcaster(left)


def push_button(
    graph: dict[str, list[str]], modules: dict[str, Module], times: int
) -> int:
    counter: dict[bool, int] = collections.Counter()
    for _ in range(times):
        counter[False] += 1
        queue: collections.deque[tuple[str, bool]] = collections.deque(
            [('broadcaster', False)]
        )
        while queue:
            v, sig1 = queue.popleft()
            if v not in graph:
                continue

            for w in graph[v]:
                counter[sig1] += 1
                if w not in modules:
                    continue
                sig2 = modules[w].send(v, sig1)
                if sig2 is not None:
                    queue.append((w, sig2))
    return math.prod(counter.values())


def parse_modules(lines: list[str], graph: dict[str, list[str]]) -> dict[str, Module]:
    modules = {}
    for line in lines:
        module = parse_module(line)
        modules[module.name] = module
    for v in graph:
        for w in graph[v]:
            if w in modules and isinstance(modules[w], Conjunction):
                modules[w].send(v, False)
    return modules


def solve(text: str) -> int:
    lines = text.splitlines()
    graph = parse_graph(lines)
    modules = parse_modules(lines, graph)
    return push_button(graph, modules, times=1000)


if __name__ == '__main__':
    pass
