with open('day_5_input_test.txt') as f:
    array_of_coordinates = []
    for line in f:
        line = line.strip()
        array_of_coordinates.append(line)

array_dictionary_of_coord = []
for string in array_of_coordinates:
    current_dictionary = {}
    parsed_string = string.split('->')
    first_coord = parsed_string[0].split(',')
    second_coord = parsed_string[1].split(',')
    current_dictionary['x1'] = int(first_coord[0])
    current_dictionary['y1'] = int(first_coord[1])
    current_dictionary['x2'] = int(second_coord[0])
    current_dictionary['y2'] = int(second_coord[1])
    array_dictionary_of_coord.append(current_dictionary)

max_x = 0
max_y = 0

for dictionary in array_dictionary_of_coord:
    current_x1 = dictionary['x1']
    current_x2 = dictionary['x2']
    if current_x1 > max_x:
        max_x = current_x1
    if current_x2 > max_x:
        max_x = current_x2

    current_y1 = dictionary['y1']
    current_y2 = dictionary['y2']
    if current_y1 > max_y:
        max_y = current_y1
    if current_y2 > max_y:
        max_y = current_y2


def build_coordinate_system(max_x, max_y):
    plane = []
    for index in range(max_y):
        x_array = []
        for i in range(max_x):
            x_array.append(0)
        plane.append(x_array)
    return plane


plane = build_coordinate_system(15, 15)


def return_key_at_min(dictionary, key1, key2):
    min = dictionary[key1]
    if dictionary[key2] < min:
        return key2
    return key1


def return_key_at_max(dictionary, key1, key2):
    max = dictionary[key1]
    if dictionary[key2] > max:
        return key2
    return key1


def mark_geothermal_vent(dictionary_of_coordinates: dict, plane):
    is_horizontal_line = dictionary_of_coordinates['y1'] == dictionary_of_coordinates['y2']
    is_vertical_line = dictionary_of_coordinates['x1'] == dictionary_of_coordinates['x2']
    if not is_horizontal_line and not is_vertical_line:
        is_diagonal_line = True

    if is_horizontal_line:
        key_at_min = return_key_at_min(dictionary_of_coordinates, 'x1', 'x2')
        key_at_max = return_key_at_max(dictionary_of_coordinates, 'x1', 'x2')
        for i in range(dictionary_of_coordinates[key_at_min], (dictionary_of_coordinates[key_at_max] + 1)):
            plane[dictionary_of_coordinates['y1']][i] += 1
    elif is_vertical_line:
        key_at_min = return_key_at_min(dictionary_of_coordinates, 'y1', 'y2')
        key_at_max = return_key_at_max(dictionary_of_coordinates, 'y1', 'y2')
        for i in range(dictionary_of_coordinates[key_at_min], (dictionary_of_coordinates[key_at_max] + 1)):
            plane[i][dictionary_of_coordinates['x1']] += 1
    # elif is_diagonal_line:
    #     first_x = return_key_at_min(dictionary_of_coordinates, 'x1', 'x2')
    #     if first_x == 'x1':
    #         first_y = 'y1'
    #         second_x = 'x2'
    #         second_y = 'y2'
    #     else:
    #         first_y = 'y2'
    #         second_x = 'x1'
    #         second_y = 'y1'
    #
    #     upslope = dictionary_of_coordinates[first_y] > dictionary_of_coordinates[second_y]
    #     if upslope:
    #         for i in range(dictionary_of_coordinates[first_x], dictionary_of_coordinates[second_x]+1):
    #             for num in range(dictionary_of_coordinates[second_y], dictionary_of_coordinates[first_y]+1):
    #                 plane[num][i] += 1
    return plane


for coordinates in array_dictionary_of_coord:
    mark_geothermal_vent(coordinates, plane)

count = 0
for array in plane:
    for i in array:
        if i > 1:
            count += 1
