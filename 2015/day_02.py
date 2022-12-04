import aoc_helper

BOXES = tuple(
    list(sorted(aoc_helper.utils.extract_ints(box)))
    for box in aoc_helper.day(d=2).split("\n")
)


def part_one():
    return sum(3 * l * w + 2 * w * h + 2 * l * h for l, w, h in BOXES)


def part_two():
    return sum(2 * (l + w) + l * w * h for l, w, h in BOXES)


aoc_helper.submit(2, part_one)
aoc_helper.submit(2, part_two)
