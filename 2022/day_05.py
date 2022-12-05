import aoc_helper

RAW = aoc_helper.day(5).splitlines()
board, moves = aoc_helper.day(5).split("\n\n")
MOVES = [tuple((aoc_helper.utils.extract_ints(move))) for move in moves.split("\n")]


def create_matrix(board: str) -> list:
    board = board.splitlines()
    # fix the first row, missing leading spaces
    board[0] = (" " * 4) + board[0]
    bottom = board[-1]
    num_of_stacks = max(int(x) for x in bottom.split())
    STACKS = [[] for _ in range(num_of_stacks)]

    for line in board[::-1]:
        for i, crate in enumerate(line[1::4]):
            if crate.isupper():
                STACKS[i].append(crate)
    return STACKS


def move_boxes_one_at_a_time(moves: list, matrix: list) -> list:
    for item in moves:
        qty, frm, to = item
        for _ in range(qty):
            letter = matrix[frm - 1][-1]
            matrix[frm - 1].pop()
            matrix[to - 1].append(str(letter))
    return matrix


def move_all_boxes_at_one_time(moves: list, matrix: list) -> list:
    for item in moves:
        qty, frm, to = item
        temp = matrix[frm - 1][-qty:]
        del matrix[frm - 1][-qty:]
        matrix[to - 1] = matrix[to - 1] + temp
    return matrix


def part_one():
    matrix = create_matrix(board=board)
    matrix_boxes_moved = move_boxes_one_at_a_time(moves=MOVES, matrix=matrix)
    return "".join(i[-1] for i in matrix_boxes_moved)


def part_two():
    matrix = create_matrix(board=board)
    matrix_boxes_moved = move_all_boxes_at_one_time(moves=MOVES, matrix=matrix)
    return "".join(i[-1] for i in matrix_boxes_moved)


aoc_helper.submit(5, part_one)
aoc_helper.submit(5, part_two)
