def construct_input():
  with open("2019/day_2_input.txt") as f:
    for line in f:
      new_line = line.split(",")
    input = []
    for num in new_line:
      input.append(int(num))
  return input

class IntcodeProgram:
  def __init__(self, input: list):
      self.input = input


class IntcodeComputer:
  def __init__(self, input: IntcodeProgram, noun, verb):
      self.intcode_program = input
      self.custom_noun = noun
      self.custom_verb = verb
      self.intcode_program.input[1] = self.custom_noun
      self.intcode_program.input[2] = self.custom_verb

  def run_intcode_program(self):
      for num in range(0, len(self.intcode_program.input), 4):
        current_instructions = self.intcode_program.input[num:num+4]
        current_opcode = current_instructions[0]
        if current_opcode == 1:
          try:
            addition = self.intcode_program.input[current_instructions[1]] + self.intcode_program.input[current_instructions[2]]
            return_index = current_instructions[3]
            self.intcode_program.input[return_index] = addition
          except IndexError:
            return
        elif current_opcode == 2:
          try:
            product = self.intcode_program.input[current_instructions[1]] * self.intcode_program.input[current_instructions[2]]
            return_index = current_instructions[3]
            self.intcode_program.input[return_index] = product
          except IndexError:
            return
        elif current_opcode == 99:
          return self.intcode_program

def simulator():
  input = construct_input()
  program_results = []
  counter = 1
  for noun in range(1, len(input)):
    for verb in range(1, len(input)):
      print("Running simulation: ", counter)
      counter += 1
      input = construct_input()
      intcode_program = IntcodeProgram(input)
      intcode_computer = IntcodeComputer(intcode_program, noun, verb)
      intcode_computer.run_intcode_program()
      program_results.append(intcode_computer.intcode_program.input[0])
      if intcode_computer.intcode_program.input[0] == 19690720:
        print("Winner! noun: ", intcode_computer.custom_noun, "verb: ", intcode_computer.custom_verb)
        print(100 * intcode_computer.custom_noun + intcode_computer.custom_verb)
        return

# print(19690720 in program_results)
# print(program_results.index(19690720))
simulator()


