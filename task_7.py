"""
Solution for day 7
"""

import os

INPUTS_RAW = None

INPUT_FILE_NAME = 'input7_0.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

limit = 100000

stack = []  # prev dirs
dirs = {}
curdir = dirs
cursize = 0
found_dir = False

for raw_line in INPUTS_RAW:
    line = raw_line[:-1]
    if line.startswith("$ cd"):  # moving around
        if line.endswith(".."):
            if len(stack):
                curdir = stack.pop(len(stack)-1)
        elif line == "$ cd /":
            curdir = dirs
            stack = []
        else:  # dirname
            dirname = line.split(" ")[-1]
            stack.append(curdir)
            curdir = curdir[dirname]
        found_dir = False
    elif line == "$ ls":  # list command
        continue
    elif line.startswith("dir "):  # dir
        dirname = line[4:]
        found_dir = True
        curdir[dirname] = {}
    else:  # file size
        sizefile = line.split(" ")
        size = sizefile[0]
        filename = sizefile[1]
        curdir[filename] = int(size)

sizes = []

def walker(walk):
    cursize = 0
    count = 0
    for _, item in walk.items():
        if isinstance(item, dict):
            itemsize, newcount = walker(item)
            cursize += itemsize
            count += newcount
        else:
            cursize += item

    if cursize < limit:
        count += cursize
    sizes.append(cursize)
    return cursize, count

total_size, counter = walker(dirs)

print("counter: %d" % counter)

disk_size = 70000000
total_space_needed = 30000000
space_free = disk_size - total_size
space_needed = total_space_needed - space_free

if space_free > total_space_needed:
    print("space_free: %d" % space_free)
    print("nothing to do")

for size in sorted(sizes):
    if size > space_needed:
        print("size: %s" % size)
        break
