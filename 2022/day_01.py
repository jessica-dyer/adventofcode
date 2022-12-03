from heapq import nlargest
import aoc_lube
from aoc_lube.utils import extract_ints
import aoc_helper

CALORIES = [
    sum(extract_ints(elf)) for elf in aoc_lube.fetch(year=2022, day=1).split("\n\n")
]


def part_one():
    return max(CALORIES)


def part_two():
    return nlargest(3, CALORIES)


aoc_helper.submit(day=1, solution=part_one)
aoc_helper.submit(day=1, solution=part_two)
