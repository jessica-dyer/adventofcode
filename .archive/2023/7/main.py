from aockit import get_input

PROD_DATA = get_input(2023, 7)
PROD = False
TEST_DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
INPUT_DATA = PROD_DATA if PROD else TEST_DATA

HANDS = [
    (line[:5].translate(str.maketrans("TJQKA", "abcde")), int(line[5:]))
    for line in INPUT_DATA.splitlines()
]


def score(hand):
    return sum(hand.count(c) for c in hand)


def score_wild(hand):
    return max(score(hand.replace("b", c)) for c in "123456789acde")


def part1():
    scored = ((score(hand), hand, bid) for hand, bid in HANDS)
    return sum(i * bid for i, (*_, bid) in enumerate(sorted(scored), start=1))


def part2():
    scored = ((score_wild(hand), hand.replace("b", "0"), bid) for hand, bid in HANDS)
    return sum(i * bid for i, (*_, bid) in enumerate(sorted(scored), start=1))


if __name__ == "__main__":
    print(part1())
    print(part2())
