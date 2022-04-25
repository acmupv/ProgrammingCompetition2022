# Author: Rodrigo Llanes Lacomba

from typing import List, Iterator
from copy import deepcopy
from sys import stdin


def neighbors(row: int, col: int, field: List[List[chr]]) -> Iterator[chr]:
    for i in range(row - 1, row + 2):
        if 0 <= i < len(field):
            for j in range(col - 1, col + 2):
                if 0 <= j < len(field[i]) and (i != row or j != col):
                    yield field[i][j]


def print_field(field: List[List[chr]]) -> None:
    for row in field:
        print(''.join(row))


def step(last: List[List[chr]]) -> List[List[chr]]:
    field = deepcopy(last)
    for i, row in enumerate(last):
        for j, cell in enumerate(row):
            if cell == '#':
                if sum(x == 'O' for x in neighbors(i, j, last)) >= 1:
                    field[i][j] = 'o'
            elif cell == 'o':
                if sum(x == 'O' for x in neighbors(i, j, last)) >= 3:
                    field[i][j] = '#'
                else:
                    field[i][j] = 'O'
            elif cell == 'O':
                if sum(x != '#' for x in neighbors(i, j, last)) >= 6:
                    field[i][j] = '#'
    return field


def biodiversity(field: List[List[chr]]) -> int:
    return sum(1 if cell == 'o' else 2 for row in field for cell in row if cell != '#')


def main() -> None:
    field = [list(line.strip()) for line in stdin.readlines()]
    history = [field]
    while True:
        field = step(field)
        if field in history:
            i = history.index(field)
            loop = history[i:]
            print_field(max(loop, key=lambda f: biodiversity(f)))
            break
        history.append(field)


if __name__ == '__main__':
    main()
