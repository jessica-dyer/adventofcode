with open('day_11_input_test.txt') as f:
    dumbo_octopus_array_of_arrays = []
    for line in f:
        line = line.strip()
        current_line = []
        for num in line:
            current_line.append(int(num))
        dumbo_octopus_array_of_arrays.append(current_line)


class Map:
    def __init__(self, array_of_arrays):
        self.master_map = array_of_arrays
        self.max_number_rows = len(self.master_map)
        self.max_number_cols = len(self.master_map[0])  # assuming all rows have the same length

        for row in range(self.max_number_rows):
            for column in range(self.max_number_cols):
                self.master_map[row][column] = Octopus(self.master_map[row][column])

    # It's okay to pass x and y coordinates out of bounds, in that case, None is returned.
    def return_value_at_coordinates(self, row, column):
        if self.is_valid_position(row, column):
            return self.master_map[row][column].energy_level
        else:
            return None

    def increment_value_at_coordinates(self, row, column):
        if self.is_valid_position(row, column):
            if self.master_map[row][column].has_flashed_this_round is False:
                self.master_map[row][column].energy_level += 1

    def is_valid_position(self, row, column):
        if column < 0 or column >= self.max_number_cols:
            return False
        if row < 0 or row >= self.max_number_rows:
            return False
        return True

class OctopusEnergySimulation:
    def __init__(self, map_object: Map):
        self.octo_energy_map = map_object

    def run_simulation(self):
        for row in range(self.octo_energy_map.max_number_rows):
            for col in range(self.octo_energy_map.max_number_cols):
                current_value = self.octo_energy_map.return_value_at_coordinates(row, col)
                if current_value == 9:
                    self.increment_neighbors(row, col)
                    self.octo_energy_map.master_map[row][col] = 0
                    self.octo_energy_map.master_map[row][col].has_flashed_this_round = True
                self.octo_energy_map.master_map[row][col].energy_level += 1

        for row in range(self.octo_energy_map.max_number_rows):
            for col in range(self.octo_energy_map.max_number_cols):
                self.octo_energy_map.master_map[row][col].has_flashed_this_round = False

    def increment_neighbors(self, row, column):
        # above
        self.octo_energy_map.increment_value_at_coordinates(row - 1, column)
        self.octo_energy_map.increment_value_at_coordinates(row - 1, column - 1)
        self.octo_energy_map.increment_value_at_coordinates(row - 1, column + 1)

        # left and right
        self.octo_energy_map.increment_value_at_coordinates(row, column - 1)
        self.octo_energy_map.increment_value_at_coordinates(row, column + 1)

        # below
        self.octo_energy_map.increment_value_at_coordinates(row + 1, column)
        self.octo_energy_map.increment_value_at_coordinates(row + 1, column - 1)
        self.octo_energy_map.increment_value_at_coordinates(row + 1, column + 1)

class Octopus:
    def __init__(self, energy_level):
        self.energy_level = energy_level
        self.has_flashed_this_round = False

    def __repr__(self):
        return f"'{self.energy_level}'"



octo_sim = OctopusEnergySimulation(Map(dumbo_octopus_array_of_arrays))
octo_sim.run_simulation()

# def check_neighbors():


# #     first loop over all octopi and reset flash ability
# # second loop over all octopi and take a step_forward
#
#
# class Octopus:
#     def __init__(self, energy_level, map):
#         self.energy_level = energy_level
#         self.has_flashed_this_step = False
#         self.map = map
#
#     def increment_energy_level(self):
#         if not self.has_flashed_this_step:
#             self.energy_level += 1
#         if self.energy_level > 9:
#             self.flash()
#
#     def flash(self):
#         self.has_flashed_this_step = True
#         # for all adjacent octopi call increment_energy_level
#         self.energy_level = 0
#
#
#     def reset_flash_ability(self):
#         self.has_flashed_this_step = False
#
#     def step_forward(self):
#         self.increment_energy_level()
