from aockit import get_input
from aoc_helper import extract_ints
import numpy as np

PROD_DATA = get_input(2023, 4)
PROD = True
TEST_DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
INPUT_DATA = PROD_DATA if PROD else TEST_DATA


def parse_raw():
    """
    For finding the matches across two lists
    use a set.
    """
    for line in INPUT_DATA.splitlines():
        ints = list(extract_ints(line))
        yield len(set(ints[1:11]) & set(ints[11:]))


MATCHES = np.fromiter(parse_raw(), int)


def part1():
    return (2 ** (MATCHES[MATCHES > 0] - 1)).sum()


def calculate_score(int_data: list[list]) -> int:
    """
    Naive solution before doing more accurate data
    parsing.
    """
    num_matches: int = 0
    for my_num in int_data[1]:
        if my_num in int_data[0][1:]:
            num_matches += 1
    if num_matches == 0:
        return 0
    return 1 if num_matches == 1 else 2 ** (num_matches - 1)


def part2():
    copies = np.ones_like(MATCHES)
    for i, matches in enumerate(MATCHES):
        copies[i + 1 : i + 1 + matches] += copies[i]
    return copies.sum()


if __name__ == "__main__":
    print(part1())
    print(part2())
