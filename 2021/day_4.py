import functools

with open('day_4_input.txt') as f:
    array_of_bingo_data = []
    bingo_board_accumulator = ''
    for line in f:
        line = line.strip()
        if line == '':
            bingo_board_accumulator = bingo_board_accumulator.strip()
            array_of_bingo_data.append(bingo_board_accumulator)
            bingo_board_accumulator = ''
        else:
            bingo_board_accumulator += line.strip() + ' '
    bingo_board_accumulator = bingo_board_accumulator.strip()
    array_of_bingo_data.append(bingo_board_accumulator)

random_numbers = array_of_bingo_data.pop(0)
random_numbers = random_numbers.split(',')
random_numbers = list(map(int, random_numbers))


class BingoBoard:
    def __init__(self, board_as_array_of_arrays: list):
        self.board = board_as_array_of_arrays
        self.moves_to_win = 0
        self.board_completed = False
        self.winning_number = None
        self.score = 0

    # this returns a new bingo board instance
    # board_data is currently a space separated string
    @classmethod
    def build_bingo_board_from_data_as_string(cls, board_data_as_string):
        board_data_as_string = list(board_data_as_string.split(' '))
        board_data_as_string = list(filter(lambda x: x != '', board_data_as_string))
        board_data_as_string = list(map(int, board_data_as_string))

        # Generate bingo board 5x5
        board = []
        current_array = []
        for item in board_data_as_string:
            if len(current_array) < 5:
                current_array.append(item)
            elif len(current_array) == 5:
                board.append(current_array)
                current_array = [item]
        board.append(current_array)

        return BingoBoard(board)

    def mark_number(self, random_number: int):
        if self.board_completed:
            return
        for array in self.board:
            if random_number in array:
                index = array.index(random_number)
                array[index] = 'X'
        self.moves_to_win += 1
        self.winning_number = random_number
        #     self.has_won()

    def has_won(self):
        if self.moves_to_win < 5:
            return False
        for array in self.board:
            if array.count('X') == 5:
                self.board_completed = True
                return True
        for index in range(5):
            x_accumulator = []
            for array in self.board:
                if array[index] == 'X':
                    x_accumulator.append('X')
                    if len(x_accumulator) == 5:
                        self.board_completed = True
                        return True
            x_accumulator = []
        return False

    def score_card(self):
        if not self.board_completed:
            pass
        else:
            total_sum = 0
            for array in self.board:
                current_array = list(filter(lambda x: x != 'X', array))
                if len(current_array) != 0:
                    current_sum = functools.reduce(lambda a, b: a + b, current_array)
                    total_sum += current_sum
            self.score = total_sum * self.winning_number


game_accumulator = []
moves_to_win = []
for num in range(len(array_of_bingo_data)):
    current_bingo_data = array_of_bingo_data[num]
    bingo_board = BingoBoard.build_bingo_board_from_data_as_string(current_bingo_data)
    if not bingo_board.board_completed:
        for item in random_numbers:
            bingo_board.mark_number(item)
            bingo_board.has_won()
            bingo_board.score_card()
            if bingo_board.board_completed:
                game_accumulator.append(bingo_board)
                moves_to_win.append(bingo_board.moves_to_win)
                break

winning_game_index = moves_to_win.index(min(moves_to_win))
answer = game_accumulator[winning_game_index].score

# Part 2
losing_game_index = moves_to_win.index(max(moves_to_win))
answer_part_2 = game_accumulator[losing_game_index].score
