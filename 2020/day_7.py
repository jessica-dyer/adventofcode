with open('day_7_input_test.py') as f:
    array_of_rules = []
    for line in f:
        line = line.strip()
        array_of_rules.append(line)

class Bag:
    def __init__(self, parsed_string):
        self.bag_color = parsed_string[0]
        self.rules = parsed_string[1]

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

        return Bag(parsed_string)
bags = []
for rules_as_string in array_of_rules:
    bag = Bag.build_bag(rules_as_string)
    bags.append(bag)

direct_carry = []
for bag in bags:
    if 'shiny gold' in bag.rules:
        direct_carry.append(bag.bag_color)

secondary_carry = []
for color in direct_carry:
    for bag in bags:
        if color in bag.rules:
            secondary_carry.append(bag.bag_color)
# secondary_carry = set(secondary_carry)
#
# print(len(direct_carry) + len(secondary_carry))