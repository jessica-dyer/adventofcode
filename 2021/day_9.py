with open('day_9_input_test.txt') as f:
    array_of_heights = []
    for line in f:
        current_array_of_heights = []
        line = line.strip()
        for item in line:
            item = int(item)
            current_array_of_heights.append(item)
        array_of_heights.append(current_array_of_heights)


# noinspection PyStatementEffect,PyUnreachableCode
class HeightMap:
    def __init__(self, array_of_array_of_heights):
        self.master_map = array_of_array_of_heights
        self.max_index_rows = len(self.master_map)
        self.max_columns = len(self.master_map[0])

    # It's okay to pass x and y coordinates out of bounds, in that case, None is returned.
    def return_value_at_coordinates(self, x_coord, y_coord):
        if x_coord < 0 or x_coord >= self.max_columns:
            return None
        if y_coord < 0 or y_coord >= self.max_index_rows:
            return None
        return self.master_map[y_coord][x_coord]

    def space_is_lowpoint(self, x_coord, y_coord):
        adjacent_values = []
        current_value = self.return_value_at_coordinates(x_coord, y_coord)
        # Check up, down, left, right
        adjacent_values.append(self.return_value_at_coordinates(x_coord, y_coord - 1))
        adjacent_values.append(self.return_value_at_coordinates(x_coord, y_coord + 1))
        adjacent_values.append(self.return_value_at_coordinates(x_coord - 1, y_coord))
        adjacent_values.append(self.return_value_at_coordinates(x_coord + 1, y_coord))
        adjacent_values = list(filter(lambda x: x is not None, adjacent_values))
        for num in adjacent_values:
            if num < current_value:
                return False
        return True

    def calculate_risk_level(self, x_coord, y_coord):
        if self.space_is_lowpoint(x_coord, y_coord):
            return self.master_map[y_coord][x_coord] + 1






sum_of_risk_level = 0
map = HeightMap(array_of_heights)
for num in range(map.max_index_rows):
    for n in range(map.max_columns):
        if map.space_is_lowpoint(n, num):
            sum_of_risk_level += map.calculate_risk_level(n, num)
