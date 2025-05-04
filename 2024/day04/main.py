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

INPUT = load_input(year=2024, day=4) if PROD else TEST_INPUT


def is_valid_coordinate(y: int, x: int, length_of_y: int, length_of_x: int) -> bool:
    return 0 <= y < length_of_y and 0 <= x < length_of_x


def is_diagonal_mas(board, y, x, d1, d2):
    try:
        y1, x1 = y + d1[0], x + d1[1]
        y2, x2 = y + d2[0], x + d2[1]
        c1 = board[y1][x1]
        c2 = board[y2][x2]
        return (c1 == "M" and c2 == "S") or (c1 == "S" and c2 == "M")
    except IndexError:
        return False


def is_word_match(board, y, x, word, direction):
    # Check if the word "XMAS" can be matched starting from (y, x) in the given direction
    for i in range(len(word)):
        ny, nx = y + i * direction[0], x + i * direction[1]
        valid_coord = is_valid_coordinate(ny, nx, len(board), len(board[0]))
        if valid_coord:
            current_letter = board[ny][nx]
            desired_letter = word[i]
            if (
                not is_valid_coordinate(ny, nx, len(board), len(board[0]))
                or current_letter != desired_letter
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
    board = [[c for c in line] for line in INPUT.strip().split()]
    rows, cols = len(board), len(board[0])

    count = 0
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            if board[y][x] != "A":
                continue

            try:
                tl = board[y - 1][x - 1]
                tr = board[y - 1][x + 1]
                bl = board[y + 1][x - 1]
                br = board[y + 1][x + 1]

                d1 = [tl, br]
                d2 = [tr, bl]

                if sorted(d1) == ["M", "S"] and sorted(d2) == ["M", "S"]:
                    count += 1
            except IndexError:
                continue

    return count


if __name__ == "__main__":
    print(part_1())
    print(part_2())
