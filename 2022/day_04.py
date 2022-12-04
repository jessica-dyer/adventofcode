import aoc_helper
from aoc_helper.utils import extract_ints

RAW = aoc_helper.day(4).split("\n")
PAIRS = [tuple(extract_ints(str(pairs.split("-")))) for pairs in RAW]


def part_one():
    return sum(a <= x and b >= y or x <= a and y >= b for a, b, x, y in PAIRS)


def part_two():
    return sum(
        bool(set(range(a, b + 1)) & set(range(x, y + 1))) for a, b, x, y in PAIRS
    )


aoc_helper.submit(4, part_one)
aoc_helper.submit(4, part_two)
