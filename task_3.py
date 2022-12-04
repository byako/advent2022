"""
Solution for task 3_1 and 3_2
"""

import os

INPUT_FILE_NAME = 'input3_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

weights = {}
for i in range(26):
    weights[(chr(ord('a')+i))] = i + 1
    weights[(chr(ord('A')+i))] = i + 27

amount = 0
for idx, value in enumerate(INPUTS_RAW):
    input_line = value.strip()
    slice_idx = int(len(input_line) / 2)
    seta = set(input_line[:slice_idx])
    setb = set(input_line[slice_idx:])
    result = seta.intersection(setb)
    if len(result) == 0:
        continue
    amount += weights[list(result)[0]]

print(amount)

amount2 = 0
for idx in range(0, len(INPUTS_RAW), 3):
    seta = set(INPUTS_RAW[idx].strip())
    result = seta.intersection(
        set(INPUTS_RAW[idx+1].strip()),
        set(INPUTS_RAW[idx+2].strip())
    )
    amount2 += weights[list(result)[0]]
print(amount2)
