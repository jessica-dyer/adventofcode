from aockit import get_input
from aoc_helper.utils import Grid
from aoc_lube import submit
import re
from math import prod

PROD = False
TEST_DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
DATA = get_input(2023, 3)

INPUT_DATA = DATA if PROD else TEST_DATA

GRID = INPUT_DATA.splitlines()


def part1():
    data = [list(d) for d in INPUT_DATA.splitlines()]
    grid = Grid(data=data)
    length_grid: int = len(grid.data)
    width_grid: int = len(grid.data[0])
    sum: int = 0
    current_digits: str = ""
    machine_part: bool = False
    last_value: str = ""
    for x in range(length_grid):
        for y in range(width_grid):
            current_value = grid.data[x][y]
            if last_value.isdigit() and not current_value.isdigit() and machine_part:
                sum += int(current_digits)
                current_digits = ""
                machine_part = False
            elif (
                last_value.isdigit()
                and not current_value.isdigit()
                and not machine_part
            ):
                current_digits = ""
            if current_value.isdigit():
                current_digits += grid.data[x][y]
                neighbors = grid.neighbours(y, x)
                for _, v in neighbors:
                    if not v.isdigit() and v != ".":
                        machine_part = True
                last_value = current_value
    return sum


def find_symbol(y, match):
    for v in [y - 1, y, y + 1]:
        for u in range(match.start() - 1, match.end() + 1):
            if (
                0 <= v < len(GRID)
                and 0 <= u < len(GRID[0])
                and GRID[v][u] != "."
                and not GRID[v][u].isdigit()
            ):
                return v, u


def part2():
    MATCHES = [list(re.finditer(r"(\d+)", line)) for line in GRID]
    SYMBOLS = {}

    def find_all_symbols():
        for y, line in enumerate(MATCHES):
            for match in line:
                if symbol := find_symbol(y, match):
                    SYMBOLS.setdefault(symbol, []).append(int(match[1]))

    find_all_symbols()
    return sum(
        prod(parts)
        for (y, x), parts in SYMBOLS.items()
        if GRID[y][x] == "*" and len(parts) == 2
    )


if __name__ == "__main__":
    # submit(year=2023, day=3, part=1, solution=part1)
    print(part2())
