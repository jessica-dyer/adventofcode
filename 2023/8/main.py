from aockit import get_input
from math import lcm
from itertools import cycle

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

INSTRUCTIONS = INPUT_DATA.splitlines().pop(0)
NETWORK = {
    k: {"L": v.split(", ")[0][1:], "R": v.split(", ")[1][:-1]}
    for k, v in (item.split(" = ") for item in INPUT_DATA.splitlines()[2:])
}


def traverse(start, end_condition):
    """Alternative solution, shorter."""
    current = start
    for i, dir in enumerate(cycle(INSTRUCTIONS)):
        current = NETWORK[current][dir]
        if end_condition(current):
            return i + 1


def find_number_of_steps(start: str):
    index = 0
    while True:
        current_instruction = INSTRUCTIONS[index % len(INSTRUCTIONS)]
        return_value = NETWORK[start].get(current_instruction)

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
        current_instruction = INSTRUCTIONS[index % len(INSTRUCTIONS)]
        return_value = NETWORK[start].get(current_instruction)

        if return_value == end:
            return index + 1
        elif return_value is not None:
            start = return_value
        index += 1


def part1_redux():
    return traverse("AAA", lambda node: node == "ZZZ")


def part2():
    start_values = []
    for k in NETWORK:
        if k.endswith("A"):
            start_values.append(k)
    list_num_of_steps = []
    for s in start_values:
        num_of_steps = find_number_of_steps(start=s)
        list_num_of_steps.append(num_of_steps)
    return lcm(*list_num_of_steps)


def part2_redux():
    dist = (
        traverse(node, lambda node: node.endswith("Z"))
        for node in NETWORK
        if node.endswith("A")
    )
    return lcm(*dist)


if __name__ == "__main__":
    print(part1())
    print(part1_redux())
    print(part2())
    print(part2_redux())
