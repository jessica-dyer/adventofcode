import aoc_helper

RAW = aoc_helper.day(2)
POINTS_FOR_DRAW = 3
POINTS_FOR_WIN = 6

points = dict(
    A=0, B=1, C=2, 
    X=0, Y=1, Z=2
)

GAMES = [
    (points[a], points[b])
    for a, _, b in RAW.splitlines()
]

def score(a: int, b: int) -> int: 
    score = 0
    if a == b:
        score += POINTS_FOR_DRAW
    elif (b - a) % 3 == 1:
        score += POINTS_FOR_WIN
    score += b + 1
    return score

def score_two(a: int, b: int) -> int:
    score = 0
    if b == 0:
        score += (a - 1) % 3 + 1
    elif b == 1:
        score += POINTS_FOR_DRAW + a + 1
    else:
        score += POINTS_FOR_WIN + (a + 1) % 3 + 1
    return score

def part_one() -> int:
    return sum(score(a, b) for a, b in GAMES)

def part_two() -> int:
    return sum(score_two(a, b) for a, b in GAMES)

aoc_helper.submit(2, part_one)
aoc_helper.submit(2, part_two)
