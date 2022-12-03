import aoc_helper
import string

RAW = aoc_helper.day(3)

RUCKSACKS = list(RAW.splitlines())

split_rucksacks = [
    (sack[: len(sack) // 2], sack[len(sack) // 2 :]) for sack in RUCKSACKS
]
unique_letters = [
    "".join(set(compartment_one) & set(compartment_two))
    for compartment_one, compartment_two in split_rucksacks
]

uppercase_letters = dict(zip(string.ascii_uppercase, range(27, 53)))
letters = dict(zip(string.ascii_lowercase, range(1, 27))) | uppercase_letters


def group_by_n(iter: list, n: int) -> list:
    return [iter[i * n : (i + 1) * n] for i in range((len(iter) + n - 1) // n)]


groups_of_three = group_by_n(iter=RUCKSACKS, n=3)
security_for_elves = [
    "".join(set(first) & set(second) & set(third))
    for first, second, third in groups_of_three
]


def part_one():
    return sum(letters.get(letter) for letter in unique_letters)


def part_two():
    return sum(letters.get(letter) for letter in security_for_elves)


aoc_helper.submit(3, part_one)
aoc_helper.submit(3, part_two)
