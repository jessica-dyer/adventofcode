with open('day_10_input.txt') as f:
    navigation_data = []
    for line in f:
        line = line.strip()
        navigation_data.append(line)

symbols = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item_to_push):
        self.stack.append(item_to_push)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]


# stack = Stack()
# score = 0
# for line in navigation_data:
#     stack = Stack()
#     for item in line:
#         if item in symbols:
#             stack.push(symbols[item])
#         elif item == stack.peek():
#             stack.pop()
#         else:
#             score += scores[item]
#             break
# print(score)

# Part 2
part_2_score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

stack = Stack()
score_array = []
for line in navigation_data:
    stack = Stack()
    for item in line:
        if item in symbols:
            stack.push(symbols[item])
        elif item == stack.peek():
            stack.pop()
        else:
            break
    else:
        score = 0
        for item in stack.stack[::-1]:
            score *= 5
            score += part_2_score[item]
        score_array += [score]
score_array.sort()
print(score_array[len(score_array) // 2])
