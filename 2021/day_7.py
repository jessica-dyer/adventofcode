with open('day_7_input_test.txt') as f:
    array_of_crab_positions = []
    for line in f:
        array_of_crab_positions.append(line)

array_of_crab_positions = array_of_crab_positions[0].split(',')
array_of_crab_positions = list(map(int, array_of_crab_positions))

cumulative_moves_for_each_index = []
max_crab_position = max(array_of_crab_positions)

for num in range(max_crab_position + 1):
    current_cummulative_moves = 0
    for position in array_of_crab_positions:
        fuel_used = 0
        distance = abs(num-position) + 1
        for n in range(distance):
            fuel_used += n
        current_cummulative_moves += fuel_used
    cumulative_moves_for_each_index.append(current_cummulative_moves)
    if num % 2 == 2:
        print('Working.')

answer = cumulative_moves_for_each_index.index(min(cumulative_moves_for_each_index))