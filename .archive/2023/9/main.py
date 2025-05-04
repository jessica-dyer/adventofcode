from aockit import get_input
from aoc_helper import extract_ints
import numpy as np

PROD_DATA = get_input(2023, 9)
PROD = False
TEST_DATA = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

INPUT_DATA = PROD_DATA if PROD else TEST_DATA

DATA = [extract_ints(line) for line in INPUT_DATA.splitlines()]


def get_oasis_reading(reading) -> int:
    return sum(np.diff(reading, n=i)[-1] for i in range(len(reading)))


def part1():
    return sum(get_oasis_reading(reading) for reading in DATA)


def part2():
    return sum(get_oasis_reading(reading[::-1]) for reading in DATA)


if __name__ == "__main__":
    print(part1())
    print(part2())
