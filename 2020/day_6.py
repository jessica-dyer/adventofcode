# with open('day_6_input.txt') as f:
#     array_of_answers = []
#     string_accumulator = ''
#     for line in f:
#         line = line.strip()
#         if line == '':
#             array_of_answers.append(string_accumulator)
#             string_accumulator = ''
#         else:
#             string_accumulator += line.strip()
#     array_of_answers.append(string_accumulator)
#
# total_yes = 0
# for item in array_of_answers:
#     unique_items = len(set(item))
#     total_yes += unique_items

with open('day_6_input_test.txt') as f:
    array_of_answers = []
    answers_from_all_people_in_group = []
    string_accumulator = ''
    for line in f:
        line = line.strip()
        if line == '':
            string_accumulator = string_accumulator[:-1]
            answers_from_all_people_in_group.append(string_accumulator)
            array_of_answers.append(answers_from_all_people_in_group)
            string_accumulator = ''
            answers_from_all_people_in_group = []

        else:
            string_accumulator += line.strip() + ","
    string_accumulator = string_accumulator[:-1]
    answers_from_all_people_in_group.append(string_accumulator)
    array_of_answers.append(answers_from_all_people_in_group)

