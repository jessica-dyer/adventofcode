import re

from lib.utils import load_input

PROD = 1

TEST_INPUT = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)
PART_TWO_TEST_INPUT = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)

INPUT = load_input(year=2024, day=3) if PROD else TEST_INPUT


def part_1():
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", INPUT))


def part_2():
    pattern = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
    tokens = [m.group(0) for m in pattern.finditer(INPUT)]

    mul_enabled = True
    total = 0

    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        elif token.startswith("mul(") and mul_enabled:
            x, y = map(int, re.findall(r"\d+", token))
            total += x * y

    return total


if __name__ == "__main__":
    print(part_1())
    print(part_2())
