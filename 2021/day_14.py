with open('day_14_input.txt') as f:
    polymer_template = []
    pair_insertion_rules = {}
    for line in f:
        line = line.strip()
        if line == '':
            continue
        elif len(polymer_template) == 0:
            polymer_template.append(line)
        else:
            x, y = line.split(' -> ')
            pair_insertion_rules[x] = y


def find_letter_to_add(current_letters_to_examine):
    if current_letters_to_examine in pair_insertion_rules:
        return pair_insertion_rules[current_letters_to_examine]

def run_step(polymer_template: str):
    final_string = ''
    for index in range(1, len(polymer_template)):
        previous_letter = polymer_template[index - 1]
        current_letter = polymer_template[index]
        letter_to_insert = find_letter_to_add(previous_letter + current_letter)
        final_string += previous_letter + letter_to_insert
    final_string += current_letter
    return final_string

def count_characters(string_of_letters) -> object:
    count_dict = {}
    for letter in string_of_letters:
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1
    return count_dict

return_letters = polymer_template[0]
for step in range(10):
    return_letters = run_step(return_letters)

count_dict = count_characters(return_letters)

def find_difference_max_min_in_dict():
    first_value = count_dict[list(count_dict.keys())[0]]
    max_value = first_value
    min_value = first_value

    for key in count_dict:
        if count_dict[key] > max_value:
            max_value = count_dict[key]
        if count_dict[key] < min_value:
            min_value = count_dict[key]
    return max_value - min_value

print(find_difference_max_min_in_dict())

# PART 2 NEEDS TO BE LESS COMPUTATIONALLY EXPENSIVE, NEED TO LOOP 40 TIMES. CAN WE USE BINS?

with open('day_14_input.txt') as f:
    s = ''
    k = {}
    for line in f:
        line = line.strip()
        if line == '':
            continue
        elif len(s) == 0:
            s += line
        else:
            x, y = line.split(' -> ')
            k[x] = y

pc = {}
for x, y in zip(s, s[1:]):
    if x + y not in pc: pc[x + y] = 0
    pc[x + y] += 1


for _ in range(40):
    npc = {}
    for p in pc:
        q = k[p]
        if p[0] + q not in npc: npc[p[0] + q] = 0
        npc[p[0] + q] += pc[p]
        if q + p[1] not in npc: npc[q + p[1]] = 0
        npc[q + p[1]] += pc[p]
    pc = npc

hc = {}
tc = {}

for p in pc:
    if p[0] not in hc: hc[p[0]] = 0
    if p[1] not in tc: tc[p[1]] = 0
    hc[p[0]] += pc[p]
    tc[p[1]] += pc[p]

c = {x: max(hc.get(x, 0), tc.get(x, 0)) for x in set(hc) | set(tc)}

print(max(c.values()) - min(c.values()))