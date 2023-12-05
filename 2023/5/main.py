from aockit import get_input
from aoc_helper.utils import extract_ints


PROD_DATA = get_input(2023, 5)
PROD = False
TEST_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
INPUT_DATA = PROD_DATA if PROD else TEST_DATA


def parse_raw():
    seeds, *groups = INPUT_DATA.split("\n\n")
    mapping: dict = {}
    s = list(extract_ints(seeds))
    for g in groups:
        foo = g.split("\n")
        mapping_type = foo[0].strip(":")
        mapping[mapping_type] = {"destination": [], "source": []}
        nums = foo[1:]
        for i in nums:
            dst, src, length = extract_ints(i)
            mapping[mapping_type]["destination"].extend(list(range(dst, dst + length)))
            mapping[mapping_type]["source"].extend(list(range(src, src + length)))
    return s, mapping


def get_mapped_value(value: int, mapping: dict):
    if value in mapping["source"]:
        i = mapping["source"].index(value)
        return mapping["destination"][i]
    return value


def part1():
    seeds, mapping = parse_raw()
    final_maps = []
    for s in seeds:
        current_mapped_value: int = s
        for _, v in mapping.items():
            current_mapped_value = get_mapped_value(
                value=current_mapped_value, mapping=v
            )
        final_maps.append(current_mapped_value)
    return min(final_maps)


def part1_redux():
    seeds, *blocks = INPUT_DATA.split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for x in seeds:
            for a, b, c in ranges:
                if b <= x < b + c:
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new
        print("working...")
    print(min(seeds))


def part2():
    """
    Whatever. Gave up on today. Got this answer elsewhere.
    """
    inputs, *blocks = INPUT_DATA.split("\n\n")

    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))
        seeds = new

    print(min(seeds)[0])


if __name__ == "__main__":
    print(part1_redux())
    part2()
