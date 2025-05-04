from lib.utils import load_input

PROD = 1


TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

INPUT = load_input(year=2024, day=2) if PROD else TEST_INPUT
PARSED_INPUT = [list(map(int, line.split())) for line in INPUT.strip().split("\n")]


def is_valid_sequence(numbers):
    if len(numbers) < 2:
        return True  # Trivially true for lists with fewer than 2 elements

    increasing = decreasing = True

    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])

        # Check the difference condition
        if diff < 1 or diff > 3:
            return False

        # Check if the sequence is increasing or decreasing
        if numbers[i] < numbers[i - 1]:
            increasing = False
        elif numbers[i] > numbers[i - 1]:
            decreasing = False

    # The sequence must either be strictly increasing or strictly decreasing
    return increasing or decreasing


def is_valid_sequence_part_two(numbers):
    is_safe = is_valid_sequence(numbers)
    if is_safe:
        return True

    # Try removing one element and check if the sequence becomes safe
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i + 1 :]
        if is_valid_sequence(modified_numbers):
            return True

    return False


def part1():
    return sum(1 for r in PARSED_INPUT if is_valid_sequence(r))


def part2():
    return sum(1 for r in PARSED_INPUT if is_valid_sequence_part_two(r))


if __name__ == "__main__":
    print(part1())
    print(part2())
