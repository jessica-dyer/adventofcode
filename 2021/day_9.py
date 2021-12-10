from enum import Enum

with open('day_9_input.txt') as f:
    array_of_heights = []
    for line in f:
        current_array_of_heights = []
        line = line.strip()
        for item in line:
            item = int(item)
            current_array_of_heights.append(item)
        array_of_heights.append(current_array_of_heights)

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


class HeightMapApp:
    def __init__(self, array_of_array_of_heights):
        self.height_map = HeightMap(array_of_array_of_heights)

    def space_is_lowpoint(self, x_coord, y_coord):
        adjacent_values = []
        current_value = self.height_map.return_value_at_coordinates(x_coord, y_coord)
        # Check up, down, left, right
        adjacent_values.append(self.height_map.return_value_at_coordinates(x_coord, y_coord - 1))
        adjacent_values.append(self.height_map.return_value_at_coordinates(x_coord, y_coord + 1))
        adjacent_values.append(self.height_map.return_value_at_coordinates(x_coord - 1, y_coord))
        adjacent_values.append(self.height_map.return_value_at_coordinates(x_coord + 1, y_coord))
        adjacent_values = list(filter(lambda x: x is not None, adjacent_values))
        for num in adjacent_values:
            if num < current_value:
                return False
        return True

    def calculate_risk_level(self, x_coord, y_coord):
        if self.space_is_lowpoint(x_coord, y_coord):
            return self.height_map.return_value_at_coordinates(x_coord, y_coord) + 1


class MapPoint(Enum):
    NINE = 9
    BASIN_PART = "B"
    COUNTED = "C"
    UNKNOWN = 0


class BasinAreaMap:
    def __init__(self, height_map_objct):
        self.height_map = height_map_objct
        self.column_count = self.height_map.max_columns
        self.row_count = self.height_map.max_index_rows
        self.basin_map = [self.create_empty_row() for x in range(self.row_count)]
        self.build_basin_map()

    def create_empty_row(self):
        return [MapPoint.UNKNOWN for x in range(self.column_count)]

    def build_basin_map(self):
        for row in range(self.row_count):
            for column in range(self.column_count):
                if self.height_map.return_value_at_coordinates(column, row) == 9:
                    self.basin_map[row][column] = MapPoint.NINE
                else:
                    self.basin_map[row][column] = MapPoint.BASIN_PART

    # Returns an array of ints
    def get_list_of_basin_areas(self):
        list_of_basin_areas = []
        for row in range(self.row_count):
            for column in range(self.column_count):
                if self.basin_map[row][column] == MapPoint.BASIN_PART:
                    area_of_basin = self.count_of_basin_parts(row, column)
                    list_of_basin_areas.append(area_of_basin)
        return list_of_basin_areas

    # Returns an integer that is the count of all contiguous basin parts
    # THIS IS A DESTRUCTIVE FUNCTION
    def count_of_basin_parts(self, row, column):
        if row < 0 or row >= self.row_count:
            return 0
        if column < 0 or column >= self.column_count:
            return 0
        if self.basin_map[row][column] != MapPoint.BASIN_PART:
            return 0
        # Now we know we're at a basin part
        counter = 0
        counter += 1
        self.basin_map[row][column] = MapPoint.COUNTED
        counter += self.count_of_basin_parts(row + 1, column)
        counter += self.count_of_basin_parts(row - 1, column)
        counter += self.count_of_basin_parts(row, column + 1)
        counter += self.count_of_basin_parts(row, column - 1)
        return counter


poo = HeightMap(array_of_heights)
foo = BasinAreaMap(poo)
# sum_of_risk_level = 0
# map = HeightMapApp(array_of_heights)
# for num in range(map.max_index_rows):
#     for n in range(map.max_columns):
#         if map.space_is_lowpoint(n, num):
#             sum_of_risk_level += map.calculate_risk_level(n, num)
