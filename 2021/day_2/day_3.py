from statistics import mode
from collections import Counter

with open('day_3_input.txt') as f:
    new_array = []
    for readline in f:
        line_strip = readline.strip()
        new_array.append(line_strip)

diagnostic_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                    "01010"]


# Takes: a string of bits i.e. '00100', '11110'
# Returns: most common bit or least common bit in the corresponding index of all numbers in the diagnostic report

def return_bit_by_position(array_of_bytes, index, min_max):
    final_array = []
    i = index
    for byte in array_of_bytes:
        bits = list(byte)
        bits = list(map(int, bits))
        final_array.append(bits[i])
    if min_max == 'max':
        return mode(final_array)
    else:
        count = Counter(final_array)
        values = [key for key, value in count.items() if value == min(count.values())]
        return values[0]


def binary_to_decimal(array_of_bits):
    base_2_array = []
    total = 0
    for i in range(len(array_of_bits)):
        current_base_2 = 2 ** i
        base_2_array.append(current_base_2)
    base_2_array.reverse()
    index: int
    for index in range(len(array_of_bits)):
        if array_of_bits[index] == 1:
            total = total + base_2_array[index]
    return total

length = len(list(new_array[0]))
gamma_array = []
for index in range(length):
    current_bit = return_bit_by_position(new_array, index, 'max')
    gamma_array.append(current_bit)
gamma = binary_to_decimal(gamma_array)

epsilon_array = []
for index in range(length):
    current_bit = return_bit_by_position(new_array, index, 'min')
    epsilon_array.append(current_bit)
epsilon = binary_to_decimal(epsilon_array)

answer = gamma*epsilon
