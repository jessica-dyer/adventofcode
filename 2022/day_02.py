import aoc_helper
import aoc_lube.utils

RAW = aoc_helper.day(2)

points = dict(
    A=0, B=1, C=2, 
    X=0, Y=1, Z=2
)

GAMES = [
    (points[a], points[b])
    for a, _, b in RAW.splitlines()
]

def i_won(a: int, b: int)->bool: 
    if b == 2 and a == 1: 
        return True
    return True if b == 1 and a == 0 else b == 0 and a == 2

def is_draw(a: int, b: int)-> bool: 
    return a == b

def score(a: int, b: int) -> int: 
    if i_won(a, b): 
        return 6 + b + 1
    elif is_draw(a, b): 
        return 3 + b + 1
    return b + 1

def lose(a: int) -> int: 
    pick = a - 1
    return 2 if pick < 0 else pick

def win(a: int) -> int: 
    pick = a + 1
    return 0 if pick > 2 else pick

def draw(a: int) -> int: 
    return a 

def score_two(a: int, b: int) -> int: 
    if b == 0: 
        return lose(a=a) + 1
    elif b == 1: 
        return draw(a=a) + 3 + 1
    else: 
        return win(a=a) + 6 + 1

def part_one():
    return sum(score(a, b) for a, b in GAMES)

def part_two():
    return sum(score_two(a, b) for a, b in GAMES)

print(part_two())
aoc_helper.submit(2, part_one)
aoc_helper.submit(2, part_two)
