"""
Solution for task 5_1 and 5_2

part 5_1 and part 5_2 only differ by reversal of toadd on line 30
"""

import os

INPUT_FILE_NAME = 'input5_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

stacks = []  # [][] in fact
commands = []

is_command = False
for raw_line in INPUTS_RAW:
    line = raw_line[:-1]
    # until blank line
    if len(line) == 0:
        is_command = True
        # reverse stacks
        for idx, stack in enumerate(stacks):
            stack.remove(str(idx+1))
            stack.reverse()
        continue
    if is_command:
        cparts = line.split(' ')
        fromidx = int(cparts[3]) - 1
        toidx = int(cparts[5]) - 1
        howmany = int(cparts[1])
        toadd = stacks[fromidx][-howmany:]
        toadd  #.reverse()
        stacks[toidx].extend(toadd)
        stacks[fromidx] = stacks[fromidx][0:-howmany]
    else:  # populate stacks
        for idx in range(0, int((len(line) + 1) / 4)):
            if len(stacks) < idx+1:
                stacks.append([])
            crate = line[idx*4:idx*4+4].strip()
            if len(crate) != 0:
                stacks[idx].append(crate)

for crate in stacks:
    print(crate[-1:])
