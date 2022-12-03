import aoc_helper
import aoc_lube.utils

RAW = aoc_helper.day(2)
POINTS_FOR_DRAW = 3
POINTS_FOR_WIN = 6
ROCK = 1
PAPER = 2
SCISSORS = 3

points = dict(
    A=ROCK, B=PAPER, C=SCISSORS, 
    X=ROCK, Y=PAPER, Z=SCISSORS
)

GAMES = [
    (points[a], points[b])
    for a, _, b in RAW.splitlines()
]

def i_won(a: int, b: int)->bool: 
    if b == SCISSORS and a == PAPER: 
        return True
    return True if b == PAPER and a == ROCK else b == ROCK and a == SCISSORS

def is_draw(a: int, b: int)-> bool: 
    return a == b

def score(a: int, b: int) -> int: 
    if i_won(a, b): 
        return POINTS_FOR_WIN + b
    elif is_draw(a, b): 
        return POINTS_FOR_DRAW + b
    return b

def return_losing_int(a: int) -> int: 
    pick = a - 1
    return SCISSORS if pick < ROCK else pick

def return_winning_int(a: int) -> int: 
    pick = a + 1
    return ROCK if pick > SCISSORS else pick

def return_int_for_draw(a: int) -> int: 
    return a 

def score_two(a: int, b: int) -> int: 
    if b == ROCK: 
        return return_losing_int(a=a)
    elif b == PAPER: 
        return return_int_for_draw(a=a) + POINTS_FOR_DRAW
    else: 
        return return_winning_int(a=a) + POINTS_FOR_WIN

def part_one() -> int:
    return sum(score(a, b) for a, b in GAMES)

def part_two() -> int:
    return sum(score_two(a, b) for a, b in GAMES)

aoc_helper.submit(2, part_one)
aoc_helper.submit(2, part_two)
