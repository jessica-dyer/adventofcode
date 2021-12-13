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

# array of arrays each inner array is the list of colors that could hold the previous colors
wrap_layers = []
# start with the color you want to bring with you: 'shiny gold'
# loop over all bag rules and determine which can contain 'shiny gold' return bag_color if can contain
# end up with an array of new colors
# take that array and reduce it to only new colors
# if there are no new colors in that array, break out
# add that as a new layer to wrap layers


# function that takes one color
# returns a list of colors that can contain it
def array_of_bag_colors_that_hold_bag_color(single_bag_color):
#      TODO: use the bag_rules array in here
    pass

# takes: array of colors
# returns: array of colors
def all_bag_colors_that_can_hold_any_of_these(array_of_colors):
#     TODO: use a loop and call array_of_bag_colors_that_hold_bag_color()
    pass

# takes: array of colors
# returns: array of colors
def reduce_to_new_colors(array_of_colors):
# for each color given, check if that color is anywhere in our previous history of wrap layers
# return an array that only contains that are not
    pass



















# def return_array_of_bags_that_hold_bag(array_of_colors):
#     current_bags = array_of_colors
#     for color in current_bags:
#         if color in bag.rules:
#             current_bags.append(bag.bag_color)
#     current_bags = list(set(current_bags))
#     return current_bags

