with open('day_9_input.txt') as f:
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
        self.map = array_of_array_of_heights
        self.max_index_rows = len(self.map)
        self.max_columns = len(self.map[0])

    def space_is_lowpoint(self, x_coord, y_coord):
        is_top_row = y_coord == 0
        is_bottom_row = y_coord == len(self.map) - 1
        is_first_x = x_coord == 0
        is_last_x = x_coord == len(self.map[y_coord]) - 1

        if not is_top_row and not is_bottom_row and not is_first_x and not is_last_x:
            if self.check_space_above(x_coord, y_coord) and self.check_space_right(x_coord,
                                                                                   y_coord) and self.check_space_left(
                    x_coord, y_coord) and self.check_space_below(x_coord, y_coord):
                return True
            return False

        elif is_top_row and is_first_x:
            if self.check_space_below(x_coord, y_coord) and self.check_space_right(x_coord, y_coord):
                return True
            return False

        elif is_top_row and is_last_x:
            if self.check_space_below(x_coord, y_coord) and self.check_space_left(x_coord, y_coord):
                return True
            return False

        elif is_bottom_row and is_first_x:
            if self.check_space_above(x_coord, y_coord) and self.check_space_right(x_coord, y_coord):
                return True
            return False

        elif is_bottom_row and is_last_x:
            if self.check_space_above(x_coord, y_coord) and self.check_space_left(x_coord, y_coord):
                return True
            return False

        elif is_top_row:
            if self.check_space_right(x_coord, y_coord) and self.check_space_left(x_coord,
                                                                                  y_coord) and self.check_space_below(
                    x_coord, y_coord):
                return True
            return False

        elif is_bottom_row:
            if self.check_space_right(x_coord, y_coord) and self.check_space_left(x_coord,
                                                                                  y_coord) and self.check_space_above(
                    x_coord, y_coord):
                return True
            return False

        elif is_first_x:
            if self.check_space_right(x_coord, y_coord) and self.check_space_below(x_coord,
                                                                                   y_coord) and self.check_space_above(
                    x_coord, y_coord):
                return True
            return False

        elif is_last_x:
            if self.check_space_left(x_coord, y_coord) and self.check_space_below(x_coord,
                                                                                  y_coord) and self.check_space_above(
                    x_coord, y_coord):
                return True
            return False

    def check_space_above(self, x_coord, y_coord):
        return self.map[y_coord][x_coord] < self.map[y_coord - 1][x_coord]

    def check_space_left(self, x_coord, y_coord):
        return self.map[y_coord][x_coord] < self.map[y_coord][x_coord - 1]

    def check_space_right(self, x_coord, y_coord):
        return self.map[y_coord][x_coord] < self.map[y_coord][x_coord + 1]

    def check_space_below(self, x_coord, y_coord):
        return self.map[y_coord][x_coord] < self.map[y_coord + 1][x_coord]

    def calculate_risk_level(self, x_coord, y_coord):
        if self.space_is_lowpoint(x_coord, y_coord):
            return self.map[y_coord][x_coord] + 1


sum_of_risk_level = 0
map = HeightMap(array_of_heights)
for num in range(map.max_index_rows):
    for n in range(map.max_columns):
        if map.space_is_lowpoint(n, num):
            sum_of_risk_level += map.calculate_risk_level(n, num)
