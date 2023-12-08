from aockit import get_input
from math import lcm

PROD_DATA = get_input(2023, 8)
PROD = True
TEST_DATA = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

INPUT_DATA = PROD_DATA if PROD else TEST_DATA

INTSTRUCTIONS = INPUT_DATA.splitlines().pop(0)
DATA = {
    k: {"L": v.split(", ")[0][1:], "R": v.split(", ")[1][:-1]}
    for k, v in (item.split(" = ") for item in INPUT_DATA.splitlines()[2:])
}


def find_number_of_steps(start: str):
    index = 0
    while True:
        current_instruction = INTSTRUCTIONS[index % len(INTSTRUCTIONS)]
        return_value = DATA[start].get(current_instruction)

        if return_value and return_value.endswith("Z"):
            return index + 1
        elif return_value is not None:
            start = return_value
        index += 1


def part1():
    start = "AAA"
    end = "ZZZ"
    index = 0

    while True:
        current_instruction = INTSTRUCTIONS[index % len(INTSTRUCTIONS)]
        return_value = DATA[start].get(current_instruction)

        if return_value == end:
            return index + 1
        elif return_value is not None:
            start = return_value
        index += 1


def part2():
    start_values = []
    for k in DATA:
        if k.endswith("A"):
            start_values.append(k)
    list_num_of_steps = []
    for s in start_values:
        num_of_steps = find_number_of_steps(start=s)
        list_num_of_steps.append(num_of_steps)
    return lcm(*list_num_of_steps)


if __name__ == "__main__":
    print(part1())
    print(part2())
