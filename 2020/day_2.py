with open('day_2_input.txt') as f:
    new_array = []
    for readline in f:
        line_strip = readline.strip()
        new_array.append(line_strip)


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


def runAll(arrayOfStrings):
    boolean_array = []
    for item in arrayOfStrings:
        password_dictionary = parser(item)
        boolean = isValidPassword(password_dictionary)
        boolean_array.append(boolean)
    return boolean_array

answer = runAll(new_array)
