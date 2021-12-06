with open('day_6_input.txt') as f:
    array_of_ages_lanternfish = []
    for line in f:
        for item in line:
            if item != ',':
                array_of_ages_lanternfish.append(int(item))


# Less computationally intensive approach:

def create_fish_bins(list_of_int: list):
    fish_bins = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in list_of_int:
        fish_bins[num] += 1
    return fish_bins


lanternfish_bin = create_fish_bins(array_of_ages_lanternfish)


def pass_a_day(bins_of_fish_at_baby_counter: list):
    at_zero = bins_of_fish_at_baby_counter[0]
    new_babies = at_zero
    for index in range(1, len(bins_of_fish_at_baby_counter)):
        bins_of_fish_at_baby_counter[index - 1] = bins_of_fish_at_baby_counter[index]
        if index == 8:
            bins_of_fish_at_baby_counter[8] = 0
    bins_of_fish_at_baby_counter[6] += at_zero
    bins_of_fish_at_baby_counter[8] += new_babies

    return bins_of_fish_at_baby_counter


for day in range(256):
    pass_a_day(lanternfish_bin)

answer = sum(lanternfish_bin)

# class LanternFish:
#     def __init__(self, current_baby_timer):
#         self.current_baby_timer = current_baby_timer
#
#     def make_baby(self):
#         new_lanternfish = LanternFish(8)
#         return new_lanternfish
#
#
#     def reduce_baby_timer(self):
#         if self.current_baby_timer == 0:
#             self.current_baby_timer = 6
#         else:
#             self.current_baby_timer -= 1
#
#
# array_of_lanternfish = []
# for num in array_of_ages_lanternfish:
#     current_lanternfish = LanternFish(num)
#     array_of_lanternfish.append(current_lanternfish)
#
# for day in range(0, 80):
#     new_baby_array = []
#     for lanternfish in array_of_lanternfish:
#         if lanternfish.current_baby_timer == 0:
#             new_lanternfish = lanternfish.make_baby()
#             new_baby_array.append(new_lanternfish)
#         lanternfish.reduce_baby_timer()
#     array_of_lanternfish += new_baby_array
#
# answer = len(array_of_lanternfish)
