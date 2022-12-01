import re
from heapq import nlargest

import aoc_helper

RAW = aoc_helper.day(1)

def extract_ints(raw: str):
    return map(int, re.findall(r'(-?\d+)', raw))
        
CALORIES = [sum(extract_ints(elf)) for elf in RAW.split("\n\n")]

def part_one():
    return max(CALORIES)

def part_two():
    return nlargest(3, CALORIES)

aoc_helper.submit(1, part_one)
aoc_helper.submit(1, part_two)