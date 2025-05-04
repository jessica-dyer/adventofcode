from lib.utils import load_input

PROD = True

TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
DIRECTIONS = [
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # down
    (-1, 0),  # up
    (1, 1),  # down-right diagonal
    (-1, -1),  # up-left diagonal
    (1, -1),  # down-left diagonal
    (-1, 1),  # up-right diagonal
]

PART_2_DIRECTIONS = [(1, 1), (1, -1)]
INPUT = load_input(year=2024, day=4) if PROD else TEST_INPUT


def is_valid_coordinate(y: int, x: int, length_of_y: int, length_of_x: int) -> bool:
    return 0 <= y < length_of_y and 0 <= x < length_of_x


def is_word_match(board, y, x, word, direction):
    # Check if the word "XMAS" can be matched starting from (y, x) in the given direction
    for i in range(len(word)):
        ny, nx = y + i * direction[0], x + i * direction[1]
        if (
            not is_valid_coordinate(ny, nx, len(board), len(board[0]))
            or board[ny][nx] != word[i]
        ):
            return False
    return True


def part_1():
    board = [[c for c in line] for line in INPUT.strip().split()]
    total = 0

    # Loop through each cell in the grid
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == "X":  # Start searching only from 'X' cells
                # Check in all 8 possible directions
                for direction in DIRECTIONS:
                    if is_word_match(board, y, x, "XMAS", direction):
                        total += 1
    return total


def part_2():
    ...


if __name__ == "__main__":
    print(part_1())
