import aoc_helper
from functools import cached_property


RAW = aoc_helper.day(7).splitlines()


class Path:
    def __init__(self) -> None:
        self.directories = {}
        self.files = {}

    @cached_property
    def size(self):
        return sum(self.files.values()) + sum(
            child.size for child in self.directories.values()
        )

    def iterate_directories(self):
        yield self

        for child in self.directories.values():
            yield from child.iterate_directories()


def parse_raw_data():
    cwd = system = Path()
    system.directories["/"] = Path()

    for line in RAW:
        match line.split():
            case ["$", "cd", ".."]:
                cwd = cwd.parent
            case ["$", "cd", dir_]:
                cwd = cwd.directories[dir_]
            case ["$", "ls"]:
                pass
            case ["dir", dir_]:
                if dir_ not in cwd.directories:
                    node = Path()
                    cwd.directories[dir_] = node
                    node.parent = cwd
            case [size, file]:
                cwd.files[file] = int(size)
    return system


SYSTEM = parse_raw_data()
SYSTEM.iterate_directories()

def part_one():
    return sum(
        directory.size
        for directory in SYSTEM.iterate_directories()
        if directory.size <= 100000
    )


def part_two():
    needed = SYSTEM.size - 40_000_000
    return min(
        directory.size
        for directory in SYSTEM.iterate_directories()
        if directory.size > needed
    )


# aoc_helper.submit(7, part_one)
# aoc_helper.submit(7, part_two)
