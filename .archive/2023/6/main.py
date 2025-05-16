from aockit import get_input
from aoc_helper.utils import extract_ints

PROD_DATA = get_input(2023, 6)
PROD = True
TEST_DATA = """Time: 7  15   30
Distance: 9  40  200"""
INPUT_DATA = PROD_DATA if PROD else TEST_DATA


def get_number_of_ways_to_win(total_time: int, record_distance: int) -> int:
    number_beating_record_distance: int = 0
    for button_time in range(0, total_time):
        remaining_time = total_time - button_time
        distance = remaining_time * button_time
        if distance > record_distance:
            number_beating_record_distance += 1
    return number_beating_record_distance


DATA = list(zip(*[extract_ints(d.strip()) for d in INPUT_DATA.splitlines()]))


def part1():
    n = 1
    for d in DATA:
        n *= get_number_of_ways_to_win(d[0], d[1])
    return n


def part2():
    DATA = [extract_ints(d.replace(" ", "")) for d in INPUT_DATA.splitlines()]
    result = get_number_of_ways_to_win(
        total_time=DATA[0][0], record_distance=DATA[1][0]
    )
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
