import re
from typing import List
from xmlrpc.client import Boolean

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



class CircuitBoard:
  def __init__(self, listOfWires) -> None:
      self.wires = listOfWires

  def coordinateContainsWire(self, x, y, wire)-> Boolean:
    for segment in wire.wire_segments:
      if segment.isHorizontalSegment:
        if segment.startCoordinate.x <= x <= segment.endCoordinate.x and segment.startCoordinate.y == y:
          return True
      else:
        if segment.startCoordinate.y <= y <= segment.endCoordinate.y and segment.startCoordinate.x == x:
          return True
    return False

  def getMaxBoardCoordinates(self):
    max_x = 0
    max_y = 0
    for wire in self.wires:
      currentWireMaxCoords = wire.getMaxCoords()
      if currentWireMaxCoords.x > max_x:
        max_x = currentWireMaxCoords.x
      if currentWireMaxCoords.y > max_y:
        max_y = currentWireMaxCoords.y
    return Coordinate(max_x, max_y)

  def getCoordinatesOfIntersections(self) -> List:
    coordinatesOfIntersections = []
    max_coords = self.getMaxBoardCoordinates()
    for x in range(max_coords.x):
      for y in range(max_coords.y):
        intersection = None
        bools = []
        for wire in self.wires:
          if self.coordinateContainsWire(x, y, wire):
            bools.append(True)
          else:
            bools.append(False)
            break
        if all(bools):
          intersection = Coordinate(x, y)
          coordinatesOfIntersections.append(intersection)
    return coordinatesOfIntersections


  def calculateLowestManhattanDisctanceAtIntersection(self):
    listOfIntersections = circuitBoard.getCoordinatesOfIntersections()
    manhattanDistances = []
    for intersection in listOfIntersections:
      sum = intersection.x + intersection.y
      if sum != 0:
        manhattanDistances.append(sum)
    return min(manhattanDistances)

class Wire:
  def __init__(self, dataAsListOfPairedStrings: list, wire_segments: list):
      self.instructions = dataAsListOfPairedStrings
      self.wire_segments = wire_segments

  @classmethod
  def buildWireSegmentsFromDataAsString(cls, dataAsListOfPairedStrings):
    currentWireSegments = [WireSegment(Coordinate(0, 0), Coordinate(0, 0))]
    for pair in dataAsListOfPairedStrings:
        currentDirection = pair[0]
        currentMagnitude = int(pair[1])
        previousEndCoord = currentWireSegments[-1].endCoordinate
        newStartCoord = previousEndCoord
        if currentDirection == 'R':
          newEndCoord = Coordinate((newStartCoord.x + currentMagnitude), newStartCoord.y)
        if currentDirection == 'L':
          newEndCoord = Coordinate((newStartCoord.x - currentMagnitude), newStartCoord.y)
        if currentDirection == 'U':
          newEndCoord = Coordinate(newStartCoord.x, (newStartCoord.y  + currentMagnitude))
        if currentDirection == 'D':
          newEndCoord = Coordinate(newStartCoord.x, (newStartCoord.y  - currentMagnitude))
        currentWireSegment = WireSegment(newStartCoord, newEndCoord)
        currentWireSegment.isHorizontalSegment = currentWireSegment.isHorizontal()
        currentWireSegments.append(currentWireSegment)
    for segment in currentWireSegments:
      segment.normalizeCoordinates()
    return Wire(dataAsListOfPairedStrings, currentWireSegments)

  def getMaxCoords(self):
    max_x = 0
    max_y = 0
    for segment in self.wire_segments:
      if segment.startCoordinate.x >= max_x:
        max_x = segment.startCoordinate.x
      if segment.endCoordinate.x >= max_x:
        max_x = segment.endCoordinate.x
      if segment.startCoordinate.y >= max_y:
        max_y = segment.startCoordinate.y
      if segment.endCoordinate.y >= max_y:
        max_y = segment.endCoordinate.y
    return Coordinate(max_x, max_y)


class Coordinate:
  def __init__(self, x, y):
      self.x = x
      self.y = y

class WireSegment:
  def __init__(self, startCoordinate: Coordinate, endCoordinate: Coordinate):
    self.startCoordinate = startCoordinate
    self.endCoordinate = endCoordinate
    self.isHorizontalSegment = None

  def isHorizontal(self):
    return self.startCoordinate.y == self.endCoordinate.y

  def normalizeCoordinates(self):
    if self.isHorizontalSegment and self.startCoordinate.x > self.endCoordinate.x:
      temp = self.endCoordinate
      self.endCoordinate = self.startCoordinate
      self.startCoordinate = temp
    elif not self.isHorizontalSegment and self.startCoordinate.y > self.endCoordinate.y:
      temp = self.endCoordinate
      self.endCoordinate = self.startCoordinate
      self.startCoordinate = temp
    return

listOfWires = []
circuitBoard = CircuitBoard(listOfWires)
foo = circuitBoard.getCoordinatesOfIntersections()
print(foo)