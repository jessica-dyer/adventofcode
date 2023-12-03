import argparse
from pathlib import Path
from collections import Counter
import re
from math import prod


def load_input():
    script_path = Path(__file__).resolve().parent
    input_path = script_path / "input.txt"
    return input_path.read_text()


PROD = True

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

INPUT = load_input() if PROD else TEST_INPUT


def parse():
    for line in INPUT.splitlines():
        cubes = Counter()
        for n, color in re.findall(r"(\d+) (\w+)", line):
            if int(n) > cubes[color]:
                cubes[color] = int(n)
        yield int(re.search(r"Game (\d+)", line)[1]), cubes


GAMES = list(parse())


def part_1() -> int:
    max_cubes = Counter({"red": 12, "green": 13, "blue": 14})
    return sum(id for id, game in GAMES if game <= max_cubes)


def part_2() -> int:
    return sum(prod(game.values()) for _, game in GAMES)


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
    part_1()
    part_2()
