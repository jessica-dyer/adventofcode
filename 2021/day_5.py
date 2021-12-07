with open('day_5_input_test.txt') as f:
    array_of_coordinates = []
    for line in f:
        line = line.strip()
        array_of_coordinates.append(line)

array_of_coord = []
for string in array_of_coordinates:
    parsed_string = string.split('->')
    first_coord = parsed_string[0].split(',')
    second_coord = parsed_string[1].split(',')
    current_array_of_tuples = [(int(first_coord[0]), int(first_coord[1])), (int(second_coord[0]), int(second_coord[1]))]
    array_of_coord.append(current_array_of_tuples)


class Coordinate:
    def __init__(self, coordinates: tuple):
        self.x = coordinates[0]
        self.y = coordinates[1]


class Line:
    def __init__(self, point_a: Coordinate, point_b: Coordinate):
        self.line_type = None
        self.point_a = point_a
        self.point_b = point_b
        if self.point_a.x == self.point_b.x:
            self.line_type = 'vertical'
        elif self.point_a.y == self.point_b.y:
            self.line_type = 'horizontal'
        else:
            self.line_type = 'diagonal'

    def draw(self, canvas):
        if self.line_type == 'horizontal':
            if self.point_a_is_leftmost_coordinate():
                for i in range(self.point_a.x, self.point_b.x + 1):
                    canvas.canvas[self.point_a.y][i] += 1
            else:
                for i in range(self.point_b.x, self.point_a.x + 1):
                    canvas.canvas[self.point_b.y][i] += 1
        if self.line_type == 'vertical':
            if self.point_a_is_leftmost_coordinate():
                for i in range(self.point_a.y, self.point_b.y + 1):
                    canvas.canvas[i][self.point_a.x] += 1
            else:
                for i in range(self.point_b.y, self.point_a.y + 1):
                    canvas.canvas[i][self.point_b.x] += 1
        if self.line_type == 'diagonal':


    # returns a boolean
    def point_a_is_leftmost_coordinate(self):
        if self.line_type == 'horizontal':
            return self.point_a.x < self.point_b.x
        elif self.line_type == 'vertical':
            return self.point_a.y < self.point_b.y



class Canvas:
    def __init__(self, canvas_as_array_of_arrays: list):
        self.canvas = canvas_as_array_of_arrays

    @classmethod
    def build(cls, width, height):
        canvas = []
        for index in range(height):
            x_array = []
            for i in range(width):
                x_array.append(0)
            canvas.append(x_array)
        return Canvas(canvas)

canvas = Canvas.build(15, 15)

for array in array_of_coord:
    coordinate1 = Coordinate(array[0])
    coordinate2 = Coordinate(array[1])
    line = Line(coordinate1, coordinate2)
    line.draw(canvas)