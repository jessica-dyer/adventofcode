with open('day_11_input.txt') as f:
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
        self.simulation_reference = None

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
                if self.master_map[row][column].energy_level > 9:
                    self.simulation_reference.flash_at(row, column)

    def is_valid_position(self, row, column):
        if column < 0 or column >= self.max_number_cols:
            return False
        if row < 0 or row >= self.max_number_rows:
            return False
        return True


class OctopusEnergySimulation:
    def __init__(self, map_object: Map):
        self.octo_energy_map = map_object
        self.flash_counter = 0
        self.octo_energy_map.simulation_reference = self

    def run_simulation_one_step(self):
        for row in range(self.octo_energy_map.max_number_rows):
            for col in range(self.octo_energy_map.max_number_cols):
                self.octo_energy_map.master_map[row][col].has_flashed_this_round = False

        for row in range(self.octo_energy_map.max_number_rows):
            for col in range(self.octo_energy_map.max_number_cols):
                self.octo_energy_map.increment_value_at_coordinates(row, col)

    def did_all_flash(self):
        for row in range(self.octo_energy_map.max_number_rows):
            for col in range(self.octo_energy_map.max_number_cols):
                if self.octo_energy_map.master_map[row][col].has_flashed_this_round is False:
                    return False
        return True

    def flash_at(self, row, col):
        self.octo_energy_map.master_map[row][col].energy_level = 0
        self.octo_energy_map.master_map[row][col].has_flashed_this_round = True
        self.increment_neighbors(row, col)
        self.flash_counter += 1

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
        return f"'{self.energy_level}'*"


octo_sim = OctopusEnergySimulation(Map(dumbo_octopus_array_of_arrays))
for num in range(300):
    octo_sim.run_simulation_one_step()
    if octo_sim.did_all_flash():
        print(num + 1)
        print(octo_sim.flash_counter)
        break
