
def contstructInput(inputFileName: str):
  with open(inputFileName) as f:
    listOfStrings = []
    for line in f:
      line = line.strip()
      line = line.split(",")
      listOfStrings.append(line)
  return listOfStrings

allInstructions = contstructInput("2019/day_3_input.txt")

class CircuitBoard:
  def __init__(self, listOfWires) -> None:
      pass

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