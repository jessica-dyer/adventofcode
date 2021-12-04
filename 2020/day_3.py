with open('day_3_input.txt') as f:
    map_of_land = []
    for readline in f:
        line_strip = readline.strip()
        map_of_land.append(line_strip)
test_map = ['..##.......', '#...#...#..', ".#....#..#.", "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#",
            ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]


class LandMap:
    def __init__(self, map_of_land):
        self.map_of_land = []

        for topo in map_of_land:
            temp_topo = (list(topo))
            self.map_of_land.append(temp_topo)

    def isTreeAt(self, vertical_position, horizontal_position):
        return self.map_of_land[vertical_position][horizontal_position] == '#'

    def maxHorizontalLength(self):
        return len(self.map_of_land[0]) ## Making an assumption that all same length;

    def maxHeight(self):
        return len(self.map_of_land)


class Traveller:
    def __init__(self, map_of_land: 'array of strings'):
        self.horizontal_position = 0
        self.vertical_position = 0
        self.map_object = LandMap(map_of_land)

    def isOnTree(self):
        return self.map_object.isTreeAt(self.vertical_position, self.horizontal_position)

    def move(self, right: int, down: int):
        horizontal_length = self.map_object.maxHorizontalLength()
        self.horizontal_position = (self.horizontal_position + right) % horizontal_length
        temp_vertical_position = self.vertical_position + down
        if temp_vertical_position < self.map_object.maxHeight():
            self.vertical_position += down
        else:
            print('Stopped because bottom of the map was reached.')

    def reset(self, horizontal_position, vertical_position):
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position


mountainWoman = Traveller(map_of_land)
boolean_array = []
while mountainWoman.vertical_position < len(mountainWoman.map_object.map_of_land)-1:
    mountainWoman.move(1, 2)
    bool = mountainWoman.isOnTree()
    boolean_array.append(bool)

answer = sum(boolean_array) # 80*162*77*83*37 (1,2)=37 trees