import numpy as np
from aocd import get_data
from dataclasses import dataclass

with open('2019/day_8_input.txt', 'r') as data:
    data = np.fromiter(data.read().strip(), int).reshape((-1, 6, 25))

fewest_zeros = data[(data == 0).sum(axis=(1, 2)).argmin()]
print((fewest_zeros == 1).sum() * (fewest_zeros == 2).sum()) # Part 1

row, col = np.mgrid[:6, :25]
decoded = data[(data != 2).argmax(axis=0), row, col]
print(*map(''.join, decoded.astype(str)), sep='\n') # Part 2