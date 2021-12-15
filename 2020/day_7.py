with open('day_7_input_test.py') as f:
    array_of_rules = []
    for line in f:
        line = line.strip()
        array_of_rules.append(line)


class BagRule:
    def __init__(self, parsed_string):
        self.bag_color = parsed_string[0]
        self.can_contain = parsed_string[1]

    @classmethod
    def build_bag(cls, rules_as_string):
        parsed_string = []
        words = rules_as_string.split()
        parsed_string.append(words[0] + " " + words[1])
        rules = {}
        for index in range(len(words)):
            if words[index].isnumeric():
                value = int(words[index])
                color = words[index + 1] + " " + words[index + 2]
                rules[color] = value
            parsed_string.append(rules)

        return BagRule(parsed_string)


bag_rules = []
for rules_as_string in array_of_rules:
    bag = BagRule.build_bag(rules_as_string)
    bag_rules.append(bag)


# function that takes one color
# returns a list of colors that can contain it
def array_of_bag_colors_that_hold_bag_color(single_bag_color):
    colors_that_can_contain = []
    for rules in bag_rules:
        if single_bag_color in rules.can_contain:
            colors_that_can_contain.append(rules.bag_color)
    return list(set(colors_that_can_contain))


# takes: array of colors
# returns: array of colors
def all_bag_colors_that_can_hold_any_of_these(array_of_colors):
    current_colors = []
    for color in array_of_colors:
        for rule in bag_rules:
            if color in rule.can_contain:
                current_colors.append(rule.bag_color)
    current_colors = list(set(current_colors))
    return current_colors


# takes: array of colors
# returns: array of colors
def reduce_to_new_colors(array_of_colors):
    for layer in wrap_layers:
        for color in array_of_colors:
            if color in layer:
                array_of_colors = filter(lambda x: x != color, array_of_colors)
    return list(array_of_colors)


# array of arrays each inner array is the list of colors that could hold the previous colors
wrap_layers = [array_of_bag_colors_that_hold_bag_color('shiny gold')]

for n in range(len(bag_rules)):
    current_colors = all_bag_colors_that_can_hold_any_of_these(wrap_layers[n])
    # current_colors = reduce_to_new_colors(current_colors)
    if len(current_colors) != 0:
        wrap_layers.append(current_colors)
    else:
        break

final_bag_colors = []
for array in wrap_layers:
    for color in array:
        if color not in final_bag_colors:
            final_bag_colors.append(color)


# PART 2
# start by looping through all bag rules and checking original bag_color. If bag color == 'shiny gold', return
# dictionary of rules that should be contained.
# add to counter the number of bags in each times the number of bags containing
# loop through again until the final bags which carry nothing

# Takes: the string 'shiny gold'
# Returns: dictionary with what bags are inside shiny gold bags
def search_for_original_bag_color(color):
    array_of_bag_rules = []
    for rule in bag_rules:
        if rule.bag_color == color:
            array_of_bag_rules.append(rule)
    return array_of_bag_rules


def search_for_remaining_bag_colors(array_of_bag_rules: BagRule):
    # do the math for the current number of bags available here from bag rules
    # 1 dark olive, 2 vibrant plum

    counter = {}

    array_of_new_bag_rules = []
    # Find how many bags each of the above bags must contain
    for rule in array_of_bag_rules:
        for key in rule.can_contain:
            if key not in counter:
                counter[key] = rule.can_contain[key]
                array_of_new_bag_rules += search_for_original_bag_color(key)
    print(counter)
    if len(array_of_bag_rules) == 0:
        return counter
    return search_for_remaining_bag_colors(array_of_new_bag_rules)


foo = search_for_original_bag_color('shiny gold')
boo = search_for_remaining_bag_colors(foo)








