with open('day_7_input.txt') as f:
    array_of_crab_positions = []
    for line in f:
        array_of_crab_positions.append(line)

array_of_crab_positions = array_of_crab_positions[0].split(',')
array_of_crab_positions = list(map(int, array_of_crab_positions))

cumulative_moves_for_each_index = []
max_crab_position = max(array_of_crab_positions)

fuel_lookup_table = []
for n in range(max_crab_position + 10):
    fuel_used = 0
    for num in range(n + 1):
        fuel_used += num
    fuel_lookup_table.append(fuel_used)

fuel_lookup_table_2 = []
first_number = 1
for n in range(max_crab_position + 10):
    if n == 0:
        fuel_used = 0
        fuel_lookup_table_2.append(fuel_used)
    else:
        fuel_used = int((n/2)*(first_number + n))
        fuel_lookup_table_2.append(fuel_used)

for num in range(max_crab_position + 1):
    current_cummulative_moves = 0
    for position in array_of_crab_positions:
        fuel_used = 0
        distance = abs(num-position)
        fuel_used = fuel_lookup_table[distance]
        current_cummulative_moves += fuel_used
    cumulative_moves_for_each_index.append(current_cummulative_moves)

answer = cumulative_moves_for_each_index.index(min(cumulative_moves_for_each_index))