"""
Solution for task 1_1
"""

import os

INPUT_FILE_NAME = 'input1_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

elves = []

amount = 0
for idx, value in enumerate(INPUTS_RAW):
    input_line = value.strip()
    if len(input_line) == 0:
        elves.append(amount)
        amount = 0
    else:
        new_amount = int(input_line)
        amount += new_amount

print(sorted(elves)[-1])

# part two
print(sum(sorted(elves)[-3:]))
