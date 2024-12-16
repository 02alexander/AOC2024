#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re
import itertools

sys.path.append("../")
from util import occ_map, get_ints, DIRS

content = open("input").read()
lines = content.splitlines()



def findxmas(lines, d, startx, starty):
    s = "XMAS"
    for k in range(len(s)):
        x = d[0]*k + startx
        y = d[1]*k + starty
        if not(0 <= x < len(lines[0]) and 0 <= y < len(lines)):
            return False

        if lines[y][x] != s[k]:
            return False
    return True

def find_x_mas(lines, startx, starty):
    dirs = [[1, 1], [1, -1]]
    s = 'MAS'

    al = []
    for d in dirs:
        found = False

        for rev in [1, -1]:
            err = False
            for k in range(-1, 2):
                x = d[0]*k + startx
                y = d[1]*k + starty 
                if not(0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                    err = True
                    break
                c = s[rev*k+1]
                if lines[y][x] != c:
                    err = True
                    break
            if not err:
                found = True
                break
        al.append(found)

    return all(al)

count = 0

for d in DIRS:
    for startx in range(len(lines[0])):
        for starty in range(len(lines)):
            if findxmas(lines, np.array(d),startx, starty):
                count += 1
print(count)

count =0 
for startx in range(len(lines[0])):
    for starty in range(len(lines)):
        if find_x_mas(lines, startx, starty):
            count += 1
print(count)

