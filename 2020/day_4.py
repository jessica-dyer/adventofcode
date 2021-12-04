from abc import *

with open('day_4_input.txt') as f:
    passport_data_strings_array = []
    passport_pieces_accumulator = ''
    for line in f:
        line = line.strip()
        if line == '':
            passport_pieces_accumulator = passport_pieces_accumulator.strip()
            passport_data_strings_array.append(passport_pieces_accumulator)
            passport_pieces_accumulator = ''
        else:
            passport_pieces_accumulator += line.strip() + ' '
    passport_pieces_accumulator = passport_pieces_accumulator.strip()
    passport_data_strings_array.append(passport_pieces_accumulator)


## turn each array into a dictionary
def create_passport_dictionary(passport_data_as_string):
    key_value_pairs = passport_data_as_string.split(' ')
    current_dictionary = {}
    for key_value in key_value_pairs:
        key_and_value = key_value.split(':')
        current_dictionary[key_and_value[0]] = key_and_value[1]
    return current_dictionary


def create_passport_from_dictionary(dictionary: dict):
    passport_fields = []
    for key in dictionary:
        value_string = dictionary[key]
        if key == 'byr':
            passport_fields.append(BirthYearField(key, value_string))
        elif key == 'iyr':
            passport_fields.append(IssueYearField(key, value_string))
        elif key == 'eyr':
            passport_fields.append(ExpirationYearField(key, value_string))
        elif key == 'hgt':
            passport_fields.append(HeightField(key, value_string))
        elif key == 'hcl':
            passport_fields.append(HairColorField(key, value_string))
        elif key == 'ecl':
            passport_fields.append(EyeColorField(key, value_string))
        elif key == 'pid':
            passport_fields.append(PassportIdField(key, value_string))
    return Passport(passport_fields)


def create_passports(string_array):
    array_of_dictionaries = []
    for item in string_array:
        dict = create_passport_dictionary(item)
        array_of_dictionaries.append(dict)
    passports = []
    for dictionary in array_of_dictionaries:
        passports.append(create_passport_from_dictionary(dictionary))
    return passports


class Passport:
    def __init__(self, array_of_passport_fields: list):
        self.fields = array_of_passport_fields

    def all_fields_values_are_valid(self):
        for field in self.fields:
            if not field.is_valid():
                return False
        return True

    # returns an array of strings that represent field keys
    def all_field_keys(self):
        return list(map(lambda x: x.key_string, self.fields))

    # returns a boolean
    def all_field_keys_exist(self):
        keys_for_valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        keys_for_current_pass = self.all_field_keys()
        for key in keys_for_valid:
            if key == 'cid':
                continue
            elif key not in keys_for_current_pass:
                return False
        return True

    def completely_valid(self):
        return self.all_field_keys_exist() and self.all_fields_values_are_valid()


class PassportField(ABC):
    def __init__(self, key_string, value_string):
        self.key_string = key_string
        self.value_string = value_string

    # returns boolean
    @abstractmethod
    def is_valid(self):
        pass


class YearField(PassportField):
    def __init__(self, key_string, value_string, min_year, max_year):
        super().__init__(key_string, value_string)
        self.min_year = min_year
        self.max_year = max_year

    def is_valid(self):
        year_as_int = int(self.value_string)
        return self.min_year <= year_as_int <= self.max_year


class BirthYearField(YearField):
    def __init__(self, key_string, value_string):
        super().__init__(key_string, value_string, 1920, 2002)


class IssueYearField(YearField):
    def __init__(self, key_string, value_string):
        super().__init__(key_string, value_string, 2010, 2020)


class ExpirationYearField(YearField):
    def __init__(self, key_string, value_string):
        super().__init__(key_string, value_string, 2020, 2030)


class HeightField(PassportField):
    def is_valid(self):
        string_length = len(self.value_string)
        if string_length < 3:
            return False
        units = self.value_string[string_length - 2: string_length]
        try:
            amplitude = int(self.value_string[0:string_length - 2])
        except:
            print("That's not a number!")
            return False
        if units == 'cm':
            return 150 <= amplitude <= 193
        elif units == 'in':
            return 59 <= amplitude <= 76
        else:
            return False


class HairColorField(PassportField):
    def is_valid(self):
        # TODO: Little Wiggles, write me!
        return False


class EyeColorField(PassportField):
    def is_valid(self):
        # TODO: Little Wiggles, write me!
        return False


class PassportIdField(PassportField):
    def is_valid(self):
        # TODO: Little Wiggles, write me!
        return False


class CountryIdField(PassportField):
    def is_valid(self):
        # TODO: Little Wiggles, write me!
        return False


passports = create_passports(passport_data_strings_array)
# def isValidPassport(passport_dictionary: dict):
#     keys_for_valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
#     keys_for_current_pass = list(passport_dictionary.keys())
#     for key in keys_for_valid:
#         if key == 'cid':
#             continue
#         elif key not in keys_for_current_pass:
#             return False
#     # if passport_dictionary['byr'] = not >= 1920 & not <= 2002:
#     #     return False
#
#     return True


# array_of_booleans = []
# for item in passport_data:
#     bool = isValidPassport(item)
#     array_of_booleans.append(bool)
#
# answer = sum(array_of_booleans)
