from itertools import product, starmap
from math import inf

def extract_ints(raw: str):
    """
    Extract integers from a string.
    """
    import re

    return map(int, re.findall(r'(-?\d+)', raw))

# XMIN, XMAX, YMIN, YMAX = extract_ints("target area: x=124..174, y=-123..-86")
XMIN, XMAX, YMIN, YMAX = extract_ints("target area: x=20..30, y=-10..-5")

print(XMIN, XMAX, YMIN, YMAX)

def integrate(dx, dy):
    x = y = 0
    max_y = -inf

    while not (
        y < YMIN and dy <= 0
        or dx >= 0 and x > XMAX
        or dx <= 0 and x < XMIN
        or dx == 0 and not (XMIN <= x <= XMAX)
    ):
        x += dx
        y += dy

        dx -= 1 if dx > 0 else -1 if dx < 0 else 0
        dy -= 1

        max_y = max(y, max_y)

        if XMIN <= x <= XMAX and YMIN <= y <= YMAX:
            return True

    return False

def part_one():
    return YMIN * (YMIN + 1) // 2

print(part_one())