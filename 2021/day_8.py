from itertools import *
with open('day_8_input_test.txt') as f:
    segment_displays = []
    for line in f:
        line = line.strip()
        segment_displays.append(line)

# output_values = []
# for item in segment_displays:
#     split_item = item.split(' | ')
#     output_values.append(split_item[1])
#
# counter = 0
# for item in output_values:
#     current_words = item.split(' ')
#     for word in current_words:
#         if len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7:
#             counter += 1

# PART 2
t = 0
for k in segment_displays:
    a, b = k.split(" | ")
    do = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    req = set(do)
    for x in permutations("abcdefg"):
        m = {i: j for i, j in zip(x, "abcdefg")}
        r = {"".join(sorted(map(m.get, q))) for q in a.split()}
        if r == req:
            b = ["".join(sorted(map(m.get, q))) for q in b.split()]
            b = "".join(str(do.index(q)) for q in b)
            t += int(b)

print(t)




