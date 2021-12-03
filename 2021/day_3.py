from statistics import mode
from collections import Counter

with open('day_3_input.txt') as f:
    new_array = []
    for readline in f:
        line_strip = readline.strip()
        new_array.append(line_strip)

diagnostic_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                    "01010"]


def returnArrayOfIntegers(strings_of_bytes):
    array_of_integers = []
    for byte in strings_of_bytes:
        current_bits = list(byte)
        current_bits = list(map(int, current_bits))
        array_of_integers.append(current_bits)
    return array_of_integers


arrayOfBytes = returnArrayOfIntegers(new_array)


# Takes: a string of bits i.e. '00100', '11110'
# Returns: most common bit or least common bit in the corresponding index of all strings in the diagnostic report
def return_bit_by_position(array_of_bytes, index, min_max):
    array_of_bits_in_same_position = []
    i = index
    for byte in array_of_bytes:
        array_of_bits_in_same_position.append(byte[i])
    if min_max == 'max':
        ones = sum(array_of_bits_in_same_position)
        zeros = len(array_of_bits_in_same_position) - ones
        are_equal = ones == zeros
        if are_equal:
            return 1
        return mode(array_of_bits_in_same_position)
    else:
        count = Counter(array_of_bits_in_same_position)
        values = [key for key, value in count.items() if value == min(count.values())]
        if len(values) > 1:
            return 0
        return values[0]


# Takes: an array of integer bits i.e. [0, 0, 1, 0, 0]
# Returns: a decimal representation of binary base 2 array
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


# Loop over everything in arrayOfBytes to determine gamma and epsilon
length = len(list(arrayOfBytes[0]))
gamma_array = []
for index in range(length):
    current_bit = return_bit_by_position(arrayOfBytes, index, 'max')
    gamma_array.append(current_bit)
gamma = binary_to_decimal(gamma_array)

epsilon_array = []
for index in range(length):
    current_bit = return_bit_by_position(arrayOfBytes, index, 'min')
    epsilon_array.append(current_bit)
epsilon = binary_to_decimal(epsilon_array)

answer_part1 = gamma * epsilon


###### PART 2 ######
# O2 generator rating
# Calculate the most common bit in position 1
# Keep bytes that start with that number
# Calculate the most common bit in position 2
# Keep bytes that have that number in position 2
# etc...until you have one value left and that is your oxygen generator rating

def filterForOxygenCo2Rating(array_of_bytes, min_max):
    length = len(array_of_bytes[0])
    filtered_array = array_of_bytes
    for index in range(length):
        common_bit_at_index = return_bit_by_position(filtered_array, index, min_max)
        filtered_array = list(filter(lambda x: x[index] == common_bit_at_index, filtered_array))
    decimal = binary_to_decimal(list(filtered_array[0]))
    return decimal


oxygen = filterForOxygenCo2Rating(arrayOfBytes, 'max')
co2_scrubber = filterForOxygenCo2Rating(arrayOfBytes, 'min')

answer_part2 = oxygen * co2_scrubber
