with open('day_9_input_test.txt') as f:
    array_of_heights = []
    for line in f:
        current_array_of_heights = []
        line = line.strip()
        for item in line:
            item = int(item)
            current_array_of_heights.append(item)
        array_of_heights.append(current_array_of_heights)


class HeightMap:
    def __init__(self, array_of_array_of_heights):
        self.map = array_of_array_of_heights

    def space_is_lowpoint(self):
        for line in range(1, len(self.map)):
            previous_line = self.map[line - 1]
            current_line = self.map[line]
            if line == len(self.map) -\
                    1:
                next_line = None
            else:
                next_line = self.map[line + 1]


            print(current_line)


map = HeightMap(array_of_heights)
map.space_is_lowpoint()