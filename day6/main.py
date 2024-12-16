#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re
import itertools
from typing import Any

sys.path.append("../")
from util import occ_map, get_ints, DIRS, slice_dir

content = open("input").read()
lines = content.splitlines()
groups = content.split('\n\n')

cur_pos = None
cur_dir = 3
mp = set()
for (r, line) in enumerate(lines):
    for (col, c) in  enumerate(line):
        if c == "#":
            mp.add((r, col))
        if c == "^":
            cur_pos = (r,col)

start_pos = cur_pos
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

visited = set()
visited_with_dir = set()

width = len(lines[0])
height = len(lines)
print(f'{width=}')
print(f'{height=}')

possible_loops = set()

def would_loop(visited_with_dir, mp, cur_pos, cur_dir):
    global dirs
    visited_with_dir = set(visited_with_dir)
    cur_pos = list(cur_pos)
    path = list()
    while 0 <= cur_pos[0] < height and 0 <= cur_pos[1] < width:
        
        if (tuple(cur_pos), cur_dir) in visited_with_dir:
            return True

        next_pos = [
            cur_pos[0] + dirs[cur_dir][0],
            cur_pos[1] + dirs[cur_dir][1]
        ]
        if tuple(next_pos) in mp:
            cur_dir = (cur_dir +1 ) % 4
            continue
        if not(0 <= next_pos[0] < height and 0 <= next_pos[1] < width):
            break

        

        visited_with_dir.add((tuple(cur_pos), cur_dir))
        path.append(cur_pos)
        
        cur_pos = next_pos
    return False


while 0 <= cur_pos[0] < height and 0 <= cur_pos[1] < width:

    next_pos = [
        cur_pos[0] + dirs[cur_dir][0],
        cur_pos[1] + dirs[cur_dir][1]
    ]

    if tuple(next_pos) in mp:
        cur_dir = (cur_dir +1 ) % 4
        continue

    visited.add(tuple(cur_pos))


    new_mp = set(mp)
    new_mp.add(tuple(next_pos))


    if not(0 <= next_pos[0] < height and 0 <= next_pos[1] < width):
        break

    if tuple(next_pos) not in visited and would_loop(visited_with_dir, new_mp, cur_pos, cur_dir):
        possible_loops.add(tuple(next_pos))

    visited_with_dir.add((tuple(cur_pos), cur_dir))
    # print((tuple(cur_pos), cur_dir))
    
    cur_pos = next_pos

#1818
#2108
    
for row in range(height):
    l = ""
    for col in range(width):
        if (row,col) == tuple(start_pos):
            l += "^"
        elif (row, col) in mp:
            l += "#"
        elif (row, col) in possible_loops:
            l += "O"
        elif (row, col) in visited:
            l += "X"
        else:
            l += "."
    print(l)


print(tuple(start_pos) in possible_loops)
print(len(possible_loops.intersection(mp)))
print(len(possible_loops))
# print(possible_loops)
print(len(visited))