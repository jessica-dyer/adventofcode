from functools import total_ordering
import math

"""
Useful functions for AoC. Note deferred imports.

Requirements:
    * networkx
    * numpy
"""

__all__ = (
    "extract_ints",
    "extract_maze",
    "maximum_matching",
    "get_direction_enum",
    "chinese_remainder_theorem",
    "pairwise",
    "sliding_window",
    "DELTAS_4",
    "DELTAS_5",
    "DELTAS_8",
    "DELTAS_9",
)

DELTAS_4 = (0, 1), (0, -1), (1, 0), (-1, 0)
DELTAS_5 = DELTAS_4 + ((0, 0),)
DELTAS_8 = DELTAS_4 + ((1, 1), (-1, -1), (1, -1), (-1, 1))
DELTAS_9 = DELTAS_8 + ((0, 0),)


def chunk(it, n: int):
    """
    Chunk an iterable into non-overlapping fixed sized pieces.
    """
    args = [iter(it)] * n
    return zip(*args, strict=True)


def parts(l, n: int):
    """Splits l into n equal parts. Excess (if it exists) returned as the n+1-th."""
    m = len(l) // n
    for i in range(n):
        yield l[i * m : (i + 1) * m]

    if len(l) % n != 0:
        yield l[m * n :]


def group_by_n(iter: list, n: int) -> list:
    """
    Group items in a list by n numbers with no overlap.
    """
    return [iter[i * n : (i + 1) * n] for i in range((len(iter) + n - 1) // n)]


def extract_ints(raw: str):
    """
    Extract integers from a string.
    """
    import re

    return map(int, re.findall(r"(-?\d+)", raw))


def extract_maze(raw: str, wall="#", largest_component=False):
    """
    Parse an ascii maze into a networkx graph. Return a tuple `(np.array, nx.Graph)`.
    """
    import numpy as np
    import networkx as nx

    lines = raw.splitlines()
    max_width = max(map(len, lines))
    maze = np.array([list(line + " " * (max_width - len(line))) for line in lines])

    G = nx.grid_graph(maze.shape[::-1])

    walls = np.stack(np.where(maze == wall)).T
    G.remove_nodes_from(map(tuple, walls))

    if largest_component:
        G.remove_nodes_from(
            G.nodes - max(nx.connected_components(G), key=lambda g: len(g))
        )

    return maze, G


def maximum_matching(items: dict[list]):
    """
    Return a maximum matching from a dict of lists.
    """
    import networkx as nx

    G = nx.from_dict_of_lists(items)

    for k, v in nx.bipartite.maximum_matching(G, top_nodes=items).items():
        if k in items:  # Filter edges pointing the wrong direction.
            yield k, v


def get_direction_enum():
    """
    Return an enum for Directions with a rotate method.
    """
    from enum import IntEnum

    class Direction(IntEnum):
        EAST = E = 0
        NORTH = N = 1
        WEST = W = 2
        SOUTH = S = 3

        def rotate(self, steps=1, clockwise=False):
            if clockwise:
                return Direction((self - steps) % 4)
            return Direction((self + steps) % 4)

    return Direction


def chinese_remainder_theorem(moduli, residues):
    from math import prod

    N = prod(moduli)

    return (
        sum(
            (div := (N // modulus)) * pow(div, -1, modulus) * residue
            for modulus, residue in zip(moduli, residues)
        )
        % N
    )


def pairwise(iterable, offset=1):
    """
    Return successive pairs from iterable.
    """
    from itertools import islice, tee

    a, b = tee(iterable)

    return zip(a, islice(b, offset, None))


def sliding_window(iterable, length=2):
    """
    Return a sliding window over iterable.
    """
    from itertools import islice, tee

    its = (islice(it, i, None) for i, it in enumerate(tee(iterable, length)))

    return zip(*its)


def oscillate_range(start=None, stop=None, step=None, /):
    """
    Yield values around start.
    """
    match start, stop, step:
        case (int(), None, None):
            start, stop, step = 0, start, 1 if start > 0 else -1
        case (int(), int(), None):
            step = 1 if start < stop else -1
        case (int(), int(), int()) if step != 0:
            pass
        case _:
            ValueError(f"non-integer values or 0 step ({start=}, {stop=}, {step=})")

    stop_n = (stop - start) // step

    if stop_n <= 0:
        return

    yield start

    n = 1
    while n < stop_n:
        yield start + step * n
        yield start - step * n
        n += 1


def int_grid(raw, np=True, separator=""):
    """
    Parse a grid of ints into a 2d list or numpy array (if np==True).
    """
    array = [
        [int(i) for i in (line.split(separator) if separator else line)]
        for line in raw.splitlines()
    ]

    if np:
        import numpy as np

        return np.array(array)

    return array


def dot_print(array):
    """
    Pretty print a binary or boolean array.
    """
    for row in array:
        print("".join(" #"[i] for i in row))


def shiftmod(n, m, shift=1):
    """
    Simlar to n % m except the result lies within [shift, m + shift).

    Example:
        shiftmod(10, 10, shift=1) == 10
        shiftmod(11, 10, shift=1) == 1
        shiftmod(11, 10, shift=2) == 11
        shiftmod(12, 10, shift=2) == 2
    """
    return (n - shift) % m + shift


@total_ordering
class Point:
    """Simple 2-dimensional point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __div__(self, n):
        return Point(self.x / n, self.y / n)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length < other.length

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dist_manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle(self, to=None):
        if to is None:
            return math.atan2(self.y, self.x)
        return math.atan2(self.y - to.y, self.x - to.x)

    def rotate(self, turns):
        """Returns the rotation of the Point around (0, 0) `turn` times clockwise."""
        turns = turns % 4

        if turns == 1:
            return Point(self.y, -self.x)
        elif turns == 2:
            return Point(-self.x, -self.y)
        elif turns == 3:
            return Point(-self.y, self.x)
        else:
            return self

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def neighbours_4(self):
        return [self + p for p in DIRS_4]

    def neighbors_4(self):
        return self.neighbours_4()

    def neighbours(self):
        return self.neighbours_4()

    def neighbors(self):
        return self.neighbours()

    def neighbours_8(self):
        return [self + p for p in DIRS_8]

    def neighbors_8(self):
        return self.neighbours_8()


N = Point(0, 1)
NE = Point(1, 1)
E = Point(1, 0)
SE = Point(1, -1)
S = Point(0, -1)
SW = Point(-1, -1)
W = Point(-1, 0)
NW = Point(-1, 1)

DIRS_4 = DIRS = [
    Point(0, 1),  # north
    Point(1, 0),  # east
    Point(0, -1),  # south
    Point(-1, 0),  # west
]

DIRS_8 = [
    Point(0, 1),  # N
    Point(1, 1),  # NE
    Point(1, 0),  # E
    Point(1, -1),  # SE
    Point(0, -1),  # S
    Point(-1, -1),  # SW
    Point(-1, 0),  # W
    Point(-1, 1),  # NW
]
