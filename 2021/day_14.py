with open('day_14_input_test.txt') as f:
    polymer_template = []
    pair_insertion_rules = {}
    for line in f:
        line = line.strip()
        if line == '':
            continue
        elif len(polymer_template) == 0:
            polymer_template.append(line)
        else:
            line_split = line.split('->')
            pair_insertion_rules[line_split[0].strip()] = line_split[1].strip()


