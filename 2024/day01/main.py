from lib.utils import load_input

PROD = True

TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""

INPUT = load_input(year=2024, day=1) if PROD else TEST_INPUT


def part1():
    left_numbers, right_numbers = zip(
        *[map(int, line.split()) for line in INPUT.strip().split("\n")]
    )
    sum_of_diff = sum(
        abs(left - right)
        for left, right in zip(sorted(left_numbers), sorted(right_numbers))
    )
    return sum_of_diff


def part2():
    left_numbers, right_numbers = zip(
        *[map(int, line.split()) for line in INPUT.strip().split("\n")]
    )
    total_sum = 0
    for n in left_numbers:
        count_in_right = right_numbers.count(n)
        similarity_score = count_in_right * n
        total_sum += similarity_score
    return total_sum


if __name__ == "__main__":
    print(part1())
    print(part2())
