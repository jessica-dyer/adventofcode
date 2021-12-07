with open('day_5_input.txt') as f:
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
            if self.is_upslope() and self.point_a_is_leftmost_coordinate():
                x = self.point_a.x
                y = self.point_a.y
                length = self.point_b.x - self.point_a.x
                for n in range(length + 1):
                    canvas.canvas[y - n][x + n] += 1
            elif self.is_upslope() and not self.point_a_is_leftmost_coordinate():
                x = self.point_b.x
                y = self.point_b.y
                length = self.point_a.x - self.point_b.x
                for n in range(length + 1):
                    canvas.canvas[y - n][x + n] += 1
            elif not self.is_upslope() and self.point_a_is_leftmost_coordinate():
                x = self.point_a.x
                y = self.point_a.y
                length = self.point_b.x - self.point_a.x
                for n in range(length + 1):
                    canvas.canvas[y + n][x + n] += 1
            elif not self.is_upslope() and not self.point_a_is_leftmost_coordinate():
                x = self.point_b.x
                y = self.point_b.y
                length = self.point_a.x - self.point_b.x
                for n in range(length + 1):
                    canvas.canvas[y + n][x + n] += 1

    # returns a boolean
    def point_a_is_leftmost_coordinate(self):
        if self.line_type == 'horizontal' or self.line_type == 'diagonal':
            return self.point_a.x < self.point_b.x
        elif self.line_type == 'vertical':
            return self.point_a.y < self.point_b.y

    def is_upslope(self):
        if self.point_a_is_leftmost_coordinate():
            return self.point_a.y > self.point_b.y
        else:
            return self.point_b.y > self.point_a.y


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


canvas = Canvas.build(1000, 1000)

for array in array_of_coord:
    coordinate1 = Coordinate(array[0])
    coordinate2 = Coordinate(array[1])
    line = Line(coordinate1, coordinate2)
    line.draw(canvas)

answer = 0
for array in canvas.canvas:
    for num in array:
        if num > 1:
            answer += 1
