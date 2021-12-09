with open('day_8_input.txt') as f:
    segment_displays = []
    for line in f:
        line = line.strip()
        segment_displays.append(line)

output_values = []
for item in segment_displays:
    split_item = item.split(' | ')
    output_values.append(split_item[1])

counter = 0
for item in output_values:
    current_words = item.split(' ')
    for word in current_words:
        if len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7:
            counter += 1

# PART 2


class SevenSegmentDisplay:
    def __init__(self, board_as_array_of_arrays):
        self.display = board_as_array_of_arrays

    @classmethod
    def build_display(cls, array_of_seven_letters: list):
        display = []

        for num in range()

        return SevenSegmentDisplay()



