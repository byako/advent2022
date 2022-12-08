"""
Solution for day 8
"""

import os

INPUT_FILE_NAME = 'input8_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

land = []  # row x column
for raw_line in INPUTS_RAW:
    line = raw_line[:-1]
    land.append([int(item) for item in line[:]])

max_x = len(land[0]) - 1
max_y = len(land) - 1
counter = 2 * len(land[0]) + 2 * (len(land) - 2)
print("edges: %d" % counter)
print("max x / max y: %d / %d" % (max_x, max_y))

cur_x = 1
cur_y = 1

def take_next(cur_x, cur_y):
    # take next element
    if cur_x == max_x - 1:
        cur_x = 1
        cur_y += 1
    else:
        cur_x += 1

    return cur_x, cur_y

# left-right
while cur_x <= (max_x-1) and (cur_y <= max_y-1):
    visible = True
    for xi in range(0, cur_x):
        if land[cur_y][xi] >= land[cur_y][cur_x]:
            visible = False
            break
    if visible:
        counter += 1
        cur_x, cur_y = take_next(cur_x, cur_y)
        continue

    visible = True
    for xi in reversed(range(cur_x+1, max_x+1)):
        if land[cur_y][xi] >= land[cur_y][cur_x]:
            visible = False
            break
    if visible:
        counter += 1
        cur_x, cur_y = take_next(cur_x, cur_y)
        continue

    visible = True
    for yi in range(0, cur_y):
        if land[yi][cur_x] >= land[cur_y][cur_x]:
            visible = False
            break
    if visible:
        counter += 1
        cur_x, cur_y = take_next(cur_x, cur_y)
        continue

    visible = True
    for yi in reversed(range(cur_y+1, max_y+1)):
        if land[yi][cur_x] >= land[cur_y][cur_x]:
            visible = False
            break
    if visible:
        counter += 1
    cur_x, cur_y = take_next(cur_x, cur_y)

print("visible trees: %d" % counter)

# part two
cur_x = 1
cur_y = 1
most_scenic = 0
# left-right
while cur_x <= (max_x-1) and (cur_y <= max_y-1):
    left = 0
    right = 0
    top = 0
    bottom = 0

    reached_edge = True
    wall = land[cur_y][cur_x-1]
    for xi in reversed(range(0, cur_x)):
        if land[cur_y][xi] >= land[cur_y][cur_x]:
            left = cur_x - xi
            reached_edge = False
            break
    if reached_edge:
        left = cur_x

    reached_edge = True
    for xi in range(cur_x+1, max_x):
        if land[cur_y][xi] >= land[cur_y][cur_x]:
            reached_edge = False
            right = xi - cur_x
            break
    if reached_edge:
        right = max_x - cur_x

    reached_edge = True
    for yi in reversed(range(0, cur_y)):
        if land[yi][cur_x] >= land[cur_y][cur_x]:
            top = cur_y - yi
            reached_edge = False
            break
    if reached_edge:
        top = cur_y

    reached_edge = True
    for yi in range(cur_y+1, max_y):
        if land[yi][cur_x] >= land[cur_y][cur_x]:
            bottom = yi - cur_y
            reached_edge = False
            break
    if reached_edge:
        bottom = max_y - cur_y

    #print("%d / %d (%d): %d / %d / %d / %d" % (cur_x, cur_y, land[cur_y][cur_x], left, top, right, bottom))

    scenic_score = left * top * right * bottom
    if  scenic_score > most_scenic:
        most_scenic = scenic_score

    cur_x, cur_y = take_next(cur_x, cur_y)

print("most_scenic %d" % most_scenic)
