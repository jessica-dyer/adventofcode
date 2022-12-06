import aoc_helper
from aoc_helper.utils import sliding_window

RAW = list(aoc_helper.day(6))
GROUPS_OF_FOUR = list(sliding_window(RAW, length=4))
GROUPS_OF_FOURTEEN = list(sliding_window(RAW, length=14))

def is_set(item) -> bool: 
    return len(set(item)) == len(item)

def part_one():
    for index, item in enumerate(GROUPS_OF_FOUR): 
        if is_set(item): 
            return index + 4


def part_two():
    for index, item in enumerate(GROUPS_OF_FOURTEEN): 
        if is_set(item): 
            return index + 14

aoc_helper.submit(6, part_one)
aoc_helper.submit(6, part_two)
