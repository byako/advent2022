"""
Solution for task 2
"""

import os

INPUT_FILE_NAME = 'input2_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

WIN = 9
scores = {
  "X" : 1,
  "Y" : 2,
  "Z" : 3
}
scores2 = {
  "X" : 0,
  "Y" : 3,
  "Z" : 6
}
win = {
 "A" : "Y",  # rock vs paper
 "B" : "Z",  # paper vs scussors
 "C" : "X",  # scissors vs rock
}
draw = {
 "A" : "X",
 "B" : "Y",
 "C" : "Z",
}
lose = {
 "A" : "Z",
 "B" : "X",
 "C" : "Y"
}

windrawlose = {
 "X" : lose,
 "Y" : draw,
 "Z"  : win
}

total = 0
total2 = 0
for idx, value in enumerate(INPUTS_RAW):
    parts = value.strip().split(' ')
    amount = scores[parts[1]]
    if parts[1] == win[parts[0]]:
        amount += 6
    elif parts[1] == draw[parts[0]]:
        amount += 3
    total += amount
    # part 2
    amount2 = scores2[parts[1]]
    amount2 += scores[windrawlose[parts[1]][parts[0]]]
    total2 += amount2

print(total)
print(total2)
