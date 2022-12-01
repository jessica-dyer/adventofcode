import aoc_helper

RAW = aoc_helper.day(1)

def parse_raw():
    parsed_data = RAW.splitlines()
    dictionary = {}
    elf_number = 0
    total_calories = 0
    for item in parsed_data: 
        if item != '': 
            total_calories += int(item)
        else: 
            dictionary[elf_number] = total_calories
            elf_number += 1
            total_calories = 0
    return dictionary
        

DATA = parse_raw()

def part_one():
    return max(DATA.values())

def part_two():
    list_of_values = sorted(DATA.values())
    return sum(list_of_values[-3:])

aoc_helper.submit(1, part_one)
aoc_helper.submit(1, part_two)