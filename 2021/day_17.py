import re

with open('day_17_input_test.txt') as f:
  coordinates = []
  for line in f:
    line = line.split()
    for word in line:
      if word != 'target' and word != 'area:':
        value = re.split('\..|\,|\=', word)
        coordinates.append(value)

for list in coordinates:
  for item in list:
    if item == '':
      list.remove('')
print(coordinates)

class Target:
  def __init__(self, list_of_coordinates: list):
      self.min_x = int(list_of_coordinates[0][1])
      self.max_x = int(list_of_coordinates[0][2])
      self.min_y = int(list_of_coordinates[1][1])
      self.max_y = int(list_of_coordinates[1][2])

  def distance_from_target(self, probe):
    pass

  def is_in_target(self, x_coord: int, y_coord: int):
    within_x = self.min_x <= x_coord <= self.max_x
    within_y = self.min_y <= y_coord <= self.max_y
    return within_x == True and within_y == True

class Probe:
  def __init__(self):
      self.list_of_positions = [(0, 0)]
      self.list_of_velocities = []

  def launch(self, initial_velocity_x, initial_velocity_y):
    count_of_measurements = 0
    while count_of_measurements == 0:
      position = (initial_velocity_x, initial_velocity_y)
      self.list_of_positions.append(position)
      self.list_of_velocities.append((initial_velocity_x, initial_velocity_y))
      count_of_measurements += 1
    for n in range(10):
      previous_coordinates = self.list_of_positions[-1]
      previous_velocity = self.list_of_velocities[-1]
      is_negative = previous_velocity[0] < 0
      current_y_addition = previous_velocity[1]-1
      if is_negative:
        current_x_addition = previous_velocity[0]+1
      else:
        current_x_addition = previous_velocity[0]-1
      current_position = (previous_coordinates[0]+current_x_addition, previous_coordinates[1]+current_y_addition)
      current_velocity = (current_x_addition, current_y_addition)
      self.list_of_positions.append(current_position)
      self.list_of_velocities.append(current_velocity)
    return(self.list_of_positions)

class Simulator:
  def __init__(self) -> None:
      pass

target = Target(coordinates)
probe = Probe()
print(probe.launch(7,2))