import argparse
from pathlib import Path

PROD = False

def load_input():
    return (Path() / "input.txt").read_text()

TEST_INPUT = """
"""

INPUT = load_input() if PROD else TEST_INPUT


def part_1() -> str:
    raise NotImplementedError

def part_2() -> str:
    raise NotImplementedError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int, choices=(1,2))
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
    main()
