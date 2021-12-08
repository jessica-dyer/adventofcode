import math

with open('day_5_input.txt') as f:
    array_of_seat_directions = []
    for line in f:
        line = line.strip()
        array_of_seat_directions.append(line)


# Function that detects the midpoint of the array
# Takes: minIndex: int, maxIndex: int
# returns midIndex: int
def findMidIndex(minIndex: int, maxIndex: int):
    mid = minIndex + math.floor((maxIndex - minIndex) / 2)
    return mid


def binarySearch(searchInstructions):
    #     find midpoint index in sorted array
    minIndex = 0
    maxIndex = 128
    midIndex = findMidIndex(minIndex, maxIndex)
    rowInstructions = searchInstructions[0:7]
    seatInstructions = searchInstructions[7:10]
    row = None
    seat = None
    #     Iterate over the sorted array
    for letter in rowInstructions:
        if letter == 'B':
            minIndex = midIndex
            midIndex = findMidIndex(midIndex, maxIndex)

        if letter == 'F':
            maxIndex = midIndex
            midIndex = findMidIndex(minIndex, maxIndex)

        if maxIndex - 1 == midIndex:
            row = midIndex
    minIndex = 0
    maxIndex = 8
    midIndex = findMidIndex(minIndex, maxIndex)
    for letter in seatInstructions:
        if letter == 'R':
            minIndex = midIndex
            midIndex = findMidIndex(midIndex, maxIndex)
        if letter == 'L':
            maxIndex = midIndex
            midIndex = findMidIndex(minIndex, maxIndex)
        if maxIndex - 1 == midIndex:
            seat = midIndex

    return (row * 8) + seat

highest_seat_id = 0
all_seat_ids = []
for instructions in array_of_seat_directions:
    current_seat_id = binarySearch(instructions)
    all_seat_ids.append(current_seat_id)
    if current_seat_id > highest_seat_id:
        highest_seat_id = current_seat_id

all_seat_ids.sort()
my_seat_id = 0
for index in range(1, len(all_seat_ids)):
    previous_seat_id = all_seat_ids[index - 1]
    current_seat_id = all_seat_ids[index]
    print(previous_seat_id)
    print(current_seat_id)
    if current_seat_id - previous_seat_id == 2:
        my_seat_id = previous_seat_id + 1
        print(previous_seat_id)
        print(current_seat_id)
        break