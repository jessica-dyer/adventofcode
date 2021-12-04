with open('day_4_input.txt') as f:
    array_of_dictionary_data = []
    passport_pieces_accumulator = ''
    for line in f:
        line = line.strip()
        if line == '':
            passport_pieces_accumulator = passport_pieces_accumulator.strip()
            array_of_dictionary_data.append(passport_pieces_accumulator)
            passport_pieces_accumulator = ''
        else:
            passport_pieces_accumulator += line.strip() + ' '
    passport_pieces_accumulator = passport_pieces_accumulator.strip()
    array_of_dictionary_data.append(passport_pieces_accumulator)


## turn each array into a dictionary
def create_passport_dictionary(string_array):
    array_of_dictionaries = []
    for item in string_array:
        key_value_pairs = item.split(' ')
        current_dictionary = {}
        for key_value in key_value_pairs:
            key_and_value = key_value.split(':')
            current_dictionary[key_and_value[0]] = key_and_value[1]
        array_of_dictionaries.append(current_dictionary)
    return array_of_dictionaries


passport_data = create_passport_dictionary(array_of_dictionary_data)




def isValidPassport(passport_dictionary: dict):
    keys_for_valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    keys_for_current_pass = list(passport_dictionary.keys())
    for key in keys_for_valid:
        if key == 'cid':
            continue
        elif key not in keys_for_current_pass:
            return False
    return True


array_of_booleans = []
for item in passport_data:
    bool = isValidPassport(item)
    array_of_booleans.append(bool)

answer = sum(array_of_booleans)
