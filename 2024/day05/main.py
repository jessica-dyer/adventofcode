from lib.utils import load_input

PROD = True

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


def is_valid(update: list[int], rules: tuple[int, int]) -> int:
    # For each (a, b) rule, if both a and b are present in the update, then the index of a must be less than the index of b.
    index_map = {page: i for i, page in enumerate(update)}
    for a, b in rules:
        if a in index_map and b in index_map:
            if index_map[a] > index_map[b]:
                return None
    middle_num = len(update) // 2
    return update[middle_num]


def order(update: list[int], rules: tuple[int, int]) -> list[int]:
    changed = True
    while changed:
        changed = False
        index_map = {page: i for i, page in enumerate(update)}
        for a, b in rules:
            if a in index_map and b in index_map:
                if index_map[a] > index_map[b]:
                    # swap and flag that we made a change
                    update[index_map[a]], update[index_map[b]] = (
                        update[index_map[b]],
                        update[index_map[a]],
                    )
                    changed = True
                    break  # start over from the beginning of the rules
    return update


def part_one():
    total = 0
    rules_and_arrays = INPUT.strip().split("\n\n")
    rules = [
        tuple(map(int, rule.split("|")))
        for rule in rules_and_arrays[0].strip().split("\n")
    ]
    arrays_to_check = [
        list(map(int, r.split(","))) for r in rules_and_arrays[1].strip().splitlines()
    ]
    for array in arrays_to_check:
        if is_valid(array, rules):
            total += is_valid(array, rules)
    return total


def part_two():
    total = 0
    rules_and_arrays = INPUT.strip().split("\n\n")
    rules = [
        tuple(map(int, rule.split("|")))
        for rule in rules_and_arrays[0].strip().split("\n")
    ]
    arrays_to_check = [
        list(map(int, r.split(","))) for r in rules_and_arrays[1].strip().splitlines()
    ]
    for array in arrays_to_check:
        if not is_valid(array, rules):
            ordered_list = order(array, rules)
            middle_num = len(ordered_list) // 2
            total += ordered_list[middle_num]
    return total


if __name__ == "__main__":
    _ = load_input(year=2024, day=5)
    if PROD:
        INPUT = load_input(year=2024, day=5)
    else:
        INPUT = TEST_INPUT
    print(part_one())
    print(part_two())
