from lib.utils import load_input

PROD = False

TEST_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

if __name__ == "__main__":
    _ = load_input(year=2024, day=5)

    if PROD:
        INPUT = load_input(year=2024, day=5)
    else:
        INPUT = TEST_INPUT
