with open('day_6_input.txt') as f:
    array_of_ages_lanternfish = []
    for line in f:
        for item in line:
            if item != ',':
                array_of_ages_lanternfish.append(int(item))

class LanternFish:
    def __init__(self, current_baby_timer):
        self.current_baby_timer = current_baby_timer

    def make_baby(self):
        new_lanternfish = LanternFish(8)
        return new_lanternfish


    def reduce_baby_timer(self):
        if self.current_baby_timer == 0:
            self.current_baby_timer = 6
        else:
            self.current_baby_timer -= 1


array_of_lanternfish = []
for num in array_of_ages_lanternfish:
    current_lanternfish = LanternFish(num)
    array_of_lanternfish.append(current_lanternfish)

for day in range(0, 256):
    new_baby_array = []
    for lanternfish in array_of_lanternfish:
        if lanternfish.current_baby_timer == 0:
            new_lanternfish = lanternfish.make_baby()
            new_baby_array.append(new_lanternfish)
        lanternfish.reduce_baby_timer()
    array_of_lanternfish += new_baby_array

answer = len(array_of_lanternfish)

