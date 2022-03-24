import re
def contstructInput(inputFileName: str):
  splits = re.compile("([a-zA-Z]+)([0-9]+)")
  with open(inputFileName) as f:
    listOfInstructions = []
    for line in f:
      current_line = []
      line = line.strip()
      line = line.split(",")
      for item in line:
        if item != '':
          result = splits.match(item).groups()
        current_line.append(result)
      listOfInstructions.append(current_line)
  return listOfInstructions

allInstructions = contstructInput("2019/day_3_input.txt")

class Coordinates:
  def __init__(self, x, y):
      self.x = x
      self.y = y

  def __str__(self) -> str:
      return self.x, self.y

class CircuitBoard:
  def __init__(self, listOfWires) -> None:
      self.wires = listOfWires
      self.board = []

  def findMaxBoardDims(self):
    max_x = 0
    max_y = 0
    for wire in self.wires:
      wire_max_x = 0
      wire_max_y = 0
      for pair in wire.instructions:
        current_direction = pair[0]
        current_amount = int(pair[1])
        if current_direction == 'R':
          wire_max_x += current_amount
        elif current_direction == 'L':
          wire_max_x -= current_amount
        elif current_direction == "U":
          wire_max_y += current_amount
        elif current_direction == "D":
          wire_max_y -= current_amount
      if wire_max_x > max_x:
        max_x = wire_max_x
      if wire_max_y > max_y:
        max_y = wire_max_y
    return (max_x, max_y)

  def generateBoard(self):
    max_dimensions = self.findMaxBoardDims()
    board = []
    for y in range(max_dimensions[1]):
      one_row = []
      for x in range(max_dimensions[0]):
        coordinate = Coordinates(x, y)
        one_row.append(coordinate)
      board.append(one_row)
    self.board = board
    return


  def calculateManhattanDisctanceAtCross():
    pass

  def getCoordinatesOfClosestIntersection():
    pass

class Wire:
  def __init__(self, wireInstructions: list):
      self.instructions = wireInstructions

  def drawPath():
    pass

  def isCrossed():
    pass


listOfWires = []
for instruction in allInstructions:
  newWire = Wire(instruction)
  listOfWires.append(newWire)

circuitBoard = CircuitBoard(listOfWires)
print(circuitBoard.wires)

print(listOfWires)
print(circuitBoard.generateBoard())
circuitBoard.board