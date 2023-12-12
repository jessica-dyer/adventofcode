from aockit import get_input
import numpy as np
from itertools import combinations

PROD_DATA = get_input(2023, 11)
PROD = False
TEST_DATA = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

INPUT_DATA = PROD_DATA if PROD else TEST_DATA

DATA = INPUT_DATA.splitlines()


def parse_raw():
    yield np.array([y for y, line in enumerate(DATA) for char in line if char == "#"])
    yield np.array([x for x in range(len(DATA[0])) for line in DATA if line[x] == "#"])


YS, XS = parse_raw()


def expand(axis, n):
    diffs = np.diff(axis, prepend=0) - 1
    diffs[diffs < 0] = 0
    return axis + np.cumsum(diffs) * n


def expand_universe(n):
    return sum(
        abs(a - b)
        for axis in (expand(YS, n), expand(XS, n))
        for a, b in combinations(axis, 2)
    )


def part1():
    return expand_universe(1)


def part2():
    return expand_universe(999_999)


if __name__ == "__main__":
    print(part1())
    print(part2())
