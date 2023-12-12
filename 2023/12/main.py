from aockit import get_input
from functools import cache

PROD_DATA = get_input(2023, 12)
PROD = True
TEST_DATA = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

INPUT_DATA = PROD_DATA if PROD else TEST_DATA

def parse_raw(): 
    for line in INPUT_DATA.splitlines(): 
        springs, groups = line.split()
        yield springs, tuple(map(int, groups.split(",")))

DATA = list(parse_raw())

def total_combinations(springs, groups):
    @cache
    def combinations(i, j, r):
        if j == len(groups):
            return springs.count("#", i) == 0
        if i == len(springs):
            return j == len(groups) - 1 and r == groups[j]

        n = 0
        if springs[i] != ".":
            n += combinations(i + 1, j, r + 1)
        if springs[i] != "#":
            if r == groups[j]:
                n += combinations(i + 1, j + 1, 0)
            elif r == 0:
                n += combinations(i + 1, j, 0)
        return n

    return combinations(0, 0, 0)

def part1():
    return sum(total_combinations(springs, groups) for springs, groups in DATA)

def part2():
    return sum(
        total_combinations("?".join([springs] * 5), groups * 5)
        for springs, groups in DATA
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
