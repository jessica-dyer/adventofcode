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


class Traveller:
    def __init__(self, map_of_land: LandMap):
        self.horizontal_position = 0
        self.vertical_position = 0
        self.map_object = LandMap(map_of_land)
        self.horizontal_position_is_max = False

    def isOnTree(self):
        return self.map_object.map_of_land[self.vertical_position][self.horizontal_position] == '#'

    def move(self, right: int, down: int):
        max_horizontal_index = len(self.map_object.map_of_land[0])-1
        for num in range(right):
            if self.horizontal_position == max_horizontal_index:
                self.horizontal_position = -1
            self.horizontal_position += 1
        self.vertical_position += down

    def reset(self, horizontal_position, vertical_position):
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position


mountainWoman = Traveller(map_of_land)
boolean_array = []
while mountainWoman.vertical_position < len(mountainWoman.map_object.map_of_land)-1:
    mountainWoman.move(1, 2)
    bool = mountainWoman.isOnTree()
    boolean_array.append(bool)

answer = sum(boolean_array) # 80*162*77*83*37