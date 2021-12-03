with open('day_2_input.txt') as f:
    new_array = []
    for readline in f:
        line_strip = readline.strip()
        new_array.append(line_strip)

test_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']


def parser(string):
    password_dictionary = {'min': 0,
                           'max': 0,
                           'letter': '',
                           'password': ''}
    new_array = string.split(': ')
    password_dictionary['password'] = new_array[1]
    rules = new_array[0].split(' ')
    password_dictionary['letter'] = rules[1]
    nums = rules[0].split('-')
    password_dictionary['min'] = int(nums[0])
    password_dictionary['max'] = int(nums[1])
    return password_dictionary


def isValidPassword(password_dictionary):
    password_char_count = {}
    current_password = list(password_dictionary['password'])
    current_letter = password_dictionary['letter']
    for letter in current_password:
        if letter in password_char_count:
            password_char_count[letter] += 1
        else:
            password_char_count[letter] = 1
    if current_letter not in password_char_count:
        return False

    return password_dictionary['min'] <= password_char_count[current_letter] <= password_dictionary['max']


def isValidPasswordPosition(password_dictionary):
    index_one = password_dictionary['min'] - 1
    index_two = password_dictionary['max'] - 1
    current_letter = password_dictionary['letter']
    current_password = password_dictionary['password']

    index_one_is_valid = current_password[index_one] == current_letter
    index_two_is_valid = current_password[index_two] == current_letter

    one_is_valid = (index_one_is_valid and not index_two_is_valid) or (not index_one_is_valid and index_two_is_valid)

    if one_is_valid:
        return True

    return False


def runAll(array_of_strings):
    boolean_array = []
    for item in array_of_strings:
        password_dictionary = parser(item)
        boolean = isValidPassword(password_dictionary)
        boolean_array.append(boolean)
    return boolean_array


# answer = runAll(new_array)

def runAllPosition(array_of_strings):
    boolean_array = []
    for item in array_of_strings:
        password_dictionary = parser(item)
        boolean = isValidPasswordPosition(password_dictionary)
        boolean_array.append(boolean)
    return boolean_array


answer = runAllPosition(new_array)
