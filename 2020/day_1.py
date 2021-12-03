with open('day_1_input.txt') as f:
    lines = f.readlines()
    nums = map(int, lines)
    nums = list(nums)

test_values = [1721, 979, 366, 299, 675, 1456]


def sumToValue(array):
    for num in array:
        current_number = num
        for value in array:
            second_number = value
            for n in array:
                third_number = n
                if current_number + second_number + third_number == 2020:
                    return current_number, second_number, third_number


sumToValue(nums)
