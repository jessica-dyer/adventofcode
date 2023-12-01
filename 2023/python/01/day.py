import argparse
from pathlib import Path
import re

PROD = True

fp = "/Users/jessica.dyer@leveltenenergy.com/Repositories/adventofcode/2023/python/01/input.txt"


def load_input(fp: str | None):
    if fp:
        return Path(fp).read_text()
    return (Path() / "input.txt").read_text()


TEST_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

INPUT = load_input(fp=fp) if PROD else TEST_INPUT


def part_1() -> int:
    input_list = INPUT.splitlines()
    first_and_last_digits_list = [
        int("".join(filter(str.isdigit, s))[0]) * 10
        + int("".join(filter(str.isdigit, s))[-1])
        for s in input_list
    ]
    return sum(first_and_last_digits_list)


def extract_real_digits(s):
    word_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    word_matches = re.findall(r"one|two|three|four|five|six|seven|eight|nine|\\d", s)
    replaced_string = ""
    for word in word_matches:
        if word.isdigit():
            replaced_string += word
        else:
            replaced_string += str(word_to_digit.get(word, 0))
    return int(replaced_string[0] + replaced_string[-1])


def part_2() -> int:
    input_list = INPUT.splitlines()
    t = 0
    n = "one two three four five six seven eight nine".split()
    p = "(?=(" + "|".join(n) + "|\\d))"

    def f(x):
        if x in n:
            return str(n.index(x) + 1)
        return x

    for x in input_list:
        digits = [*map(f, re.findall(p, x))]
        t += int(digits[0] + digits[-1])
    return t


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("part", type=int, choices=(1, 2))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parts = {
        1: part_1,
        2: part_2,
    }

    print(f"Day: {int(Path().parent.name)} Part: {args.part}")
    print(parts[args.part]())


if __name__ == "__main__":
    part_2()
