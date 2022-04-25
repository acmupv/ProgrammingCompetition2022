# Author: Rodrigo Llanes Lacomba

from typing import Set, Callable, Tuple, List
from collections import defaultdict
from itertools import groupby
from copy import deepcopy
from sys import stdin


def memoize(f: Callable[[int, Set[str]], int]) -> Callable[[int, Set[str]], Tuple[int, List[str]]]:
    mem = {}

    def wrapper(space: int, aval: Set[str]):
        k = (space, tuple(aval))
        if k not in mem:
            mem[k] = f(space, aval)
        return mem[k]

    return wrapper


def main() -> None:
    inp = [line.strip() for line in stdin.readlines()]
    size, plants, pairs = [list(y) for x, y in groupby(inp, lambda z: z == '') if not x]

    size = int(size[0])
    quality = {k: int(v) for k, v in map(str.split, plants)}
    plants = set(quality.keys())
    incompatible = defaultdict(set)
    for a, b in map(str.split, pairs):
        incompatible[a].add(b)
        incompatible[b].add(a)

    @memoize
    def solve(space: int, aval: Set[str]) -> Tuple[int, List[str]]:
        if space == 0:
            return 0, []

        best, receipt = 0, []
        for plant in aval:
            qua, path = solve(space-1, aval - {plant}.union(incompatible[plant]))
            if qua + quality[plant] > best:
                best, receipt = qua + quality[plant], [plant] + path

        return best, receipt

    q, r = solve(size, plants)
    print(q)
    print()
    print('\n'.join(sorted(r)))


if __name__ == '__main__':
    main()
