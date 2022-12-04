"""
Solution for task 4_1 and 4_2
"""

import os

INPUT_FILE_NAME = 'input4_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

amount = 0
amount2 = 0
for value in INPUTS_RAW:
    parts = value.strip().split(',')
    parts_ab = parts[0].split('-')
    parts_cd = parts[1].split('-')
    part_a = int(parts_ab[0])
    part_b = int(parts_ab[1])
    part_c = int(parts_cd[0])
    part_d = int(parts_cd[1])
    if ((part_a <= part_c and part_b >= part_d) or
        (part_c <= part_a and part_d >= part_b)):
        amount += 1
    if ((part_a <= part_d and part_a >= part_c) or
        (part_b <= part_d and part_b >= part_c) or
        (part_a <= part_c and part_b >= part_d)):
        amount2 += 1
print(amount)
print(amount2)
