# Author: Rodrigo Llanes Lacomba


from itertools import groupby
from typing import List
from sys import stdin


def run(field: List[List[chr]], x: int, y: int, seeds: int, ins: List[str]) -> int:
    out = 0
    for i in ins:
        if i[0] == 'mv':
            x += int(i[1])
            y += int(i[2])
        elif i[0] == 'pk':
            if field[y][x] == 'O':
                field[y][x] = '#'
                out += 1
        elif i[0] == 'sd':
            if field[y][x] == '#' and seeds > 0:
                field[y][x] = 'o'
                seeds -= 1
        elif i[0] == 'wt':
            if field[y][x] == 'o':
                field[y][x] = 'O'
    return out


def main() -> None:
    inp = [line.strip() for line in stdin.readlines()]
    field, stats, ins = [list(y) for x, y in groupby(inp, lambda z: z == '') if not x]

    field = [list(line) for line in field]
    x, y = map(int, stats[0].split())
    seeds = int(stats[1])
    ins = [i.split() for i in ins]

    print(run(field, x, y, seeds, ins))


if __name__ == '__main__':
    main()
