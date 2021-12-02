with open('submarine_input_1.txt') as f:
    lines = f.readlines()


class Submarine:
    def __init__(self):
        self.currentHorizontalPosition = 0
        self.currentDepth = 0

    def move(self, input_str):
        current_instructions = self.parse_instructions(input_str)
        current_direction = current_instructions[0]
        current_amount = current_instructions[1]
        if current_direction == 'forward':
            self.currentHorizontalPosition = self.currentHorizontalPosition + current_amount
        elif current_direction == 'down':
            self.currentDepth = self.currentDepth + current_amount
        elif current_direction == 'up':
            self.currentDepth = self.currentDepth - current_amount

    def parse_instructions(self, input_str):
        split_str = input_str.split(' ')
        direction = split_str[0]
        amount = int(split_str[1])
        return_value = (direction, amount)
        return return_value


sub = Submarine()

for line in lines:
    sub.move(line)

answer = sub.currentDepth * sub.currentHorizontalPosition
