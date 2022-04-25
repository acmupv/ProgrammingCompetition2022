# Author: Rodrigo Llanes Lacomba


from __future__ import annotations


from typing import List, Iterator, Tuple, Dict, Optional
from copy import deepcopy
from sys import stdin


class Node:
    def __init__(self, coord: Tuple[int, int], tile: chr) -> None:
        self.coord: Tuple[int, int] = coord
        self.tile: chr = tile
        self.neighbors: Dict[Node, int] = {}

    def is_ground(self) -> bool:
        return self.tile == ' '

    def is_pumpkin(self) -> bool:
        return self.tile == 'o'

    def is_exit(self) -> bool:
        return self.tile == 'S'

    def is_wall(self) -> bool:
        return self.tile == '#'

    def is_caterpillar(self) -> bool:
        return self.tile.isdigit()

    def add_neighbour(self, other: Node, distance: Optional[int] = 0):
        if other not in self.neighbors or self.neighbors[other] > distance:
            self.neighbors[other] = distance
            other.neighbors[self] = distance

    def dissolve(self):
        w = 0 if not self.is_caterpillar() else int(self.tile)
        for n0, d0 in self.neighbors.items():
            del n0.neighbors[self]
            for n1, d1 in self.neighbors.items():
                if n1 != n0:
                    n0.add_neighbour(n1, d0 + w + d1)


def neighbors(row: int, col: int, field: List[List[chr]], graph: Dict[chr, Node]) -> Iterator[Node]:
    for i, j in [(row - 1, col), (row, col - 1)]:
        if 0 <= i < len(field) and 0 <= j < len(field[i]):
            if field[i][j] != '#':
                yield graph[i, j]


def build_graph(field: List[List[chr]]) -> Node:
    graph = {}
    s = None
    for i, row in enumerate(field):
        for j, tile in enumerate(row):
            if tile != '#':
                graph[i, j] = Node((i, j), tile)
                if graph[i, j].is_exit():
                    s = graph[i, j]
                for node in neighbors(i, j, field, graph):
                    graph[i, j].add_neighbour(node)

    for node in graph.values():
        if node.is_caterpillar() or node.is_ground():
            node.dissolve()

    return s


def rec_solve(current: Node) -> int:
    if len(current.neighbors) == 1:
        return sum(current.neighbors.values())  # Basically the only element

    best = float('inf')
    for other, distance in current.neighbors.items():
        if other.is_pumpkin():
            new = deepcopy(current)
            new_curr = [n for n in new.neighbors.keys() if n.coord == other.coord][0]
            new.dissolve()
            best = min(best, distance + rec_solve(new_curr))

    return best


def solve(current: Node) -> int:
    best = float('inf')
    for other, distance in current.neighbors.items():
        best = min(best, distance + rec_solve(other))
    return best if best != float('inf') else 0


def main() -> None:
    field = [list(line.strip()) for line in stdin.readlines()]
    graph = build_graph(field)
    print(solve(graph))


if __name__ == '__main__':
    main()
