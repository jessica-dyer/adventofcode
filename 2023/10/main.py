from aockit import get_input
from typing import NamedTuple
import networkx as nx

PROD_DATA = get_input(2023, 10)
PROD = True
TEST_DATA = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

INPUT_DATA = PROD_DATA if PROD else TEST_DATA

DATA = [list(line) for line in INPUT_DATA.splitlines()]

class Point(NamedTuple):
    y: int
    x: int

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)

DIRS = [N, E, S, W] = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]
Δs = {"|": (N, S), "J": (N, W), "L": (N, E), "7": (S, W), "F": (S, E), "-": (W, E)}

def parse_raw():
    grid = [list(line) for line in INPUT_DATA.splitlines()]
    yield grid

    edges = set()
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            pos = Point(y, x)
            if char in Δs:
                Δ1, Δ2 = Δs[char]
                edges.add((pos, pos + Δ1))
                edges.add((pos, pos + Δ2))
            elif char == "S":
                start = pos
                for Δ in DIRS:
                    edges.add((pos, pos + Δ))

    for pipe, (Δ1, Δ2) in Δs.items():
        if (start + Δ1, start) in edges and (start + Δ2, start) in edges:
            grid[start.y][start.x] = pipe
            break

    H = nx.Graph(((u, v) for u, v in edges if (v, u) in edges))
    for component in nx.connected_components(H):
        if start in component:
            yield component
            return


GRID, PIPES = parse_raw()


def part1():
    return len(PIPES) // 2


def part2():
    ntiles = 0
    for y, line in enumerate(GRID):
        inside = False
        for x, pipe in enumerate(line):
            if (y, x) not in PIPES:
                ntiles += inside
            elif pipe in "|F7":
                inside = not inside
    return ntiles


if __name__ == "__main__":
    print(part1())
    print(part2())
