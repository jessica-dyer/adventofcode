from math import floor

with open("2019/day_1_input.txt") as f:
  list_of_module_masses = []
  for line in f:
    list_of_module_masses.append(int(line))

class Module:
  def __init__(self, mass):
      self.mass = mass

  def calculate_amount_of_fuel(self, mass):
    if mass <= 0:
      return 0
    else:
      # print("Calculating fuel")
      newly_added_fuel = floor(mass / 3) - 2
      if newly_added_fuel < 0:
        newly_added_fuel = 0
      return newly_added_fuel + self.calculate_amount_of_fuel(newly_added_fuel)

class Spacecraft:
  def __init__(self):
      self.modules = []

  def add_module(self, module: Module):
    return self.modules.append(module)

  def calculate_total_fuel_requirements(self):
    total_fuel = 0
    for module in self.modules:
      total_fuel += module.calculate_amount_of_fuel(module.mass)
    return total_fuel

module = Module(100756)
# print(module.calculate_amount_of_fuel(module.mass))
spacecraft = Spacecraft()
for mass in list_of_module_masses:
  spacecraft.add_module(Module(mass))
print(spacecraft.calculate_total_fuel_requirements())
