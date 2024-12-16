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


print("eisrnt")

antennas = defaultdict(list)

def count(antennas, tp, width, height):
    lst = antennas[tp]
    resonants = set()
    for i in range(1, len(lst)):
        for j in range(0, i):
            diff = [a - b for a,b in zip(lst[i], lst[j])]

            k = 1
            while True:
                m = [k*a + b for a,b in zip(diff, lst[j])]
                if not(0 <= m[0] < height and 0 <= m[1] < width):
                    break
                resonants.add(tuple(m))
                k += 1

            k = 1
            while True:
                n = [-k*a + b for a,b in zip(diff, lst[i])]
                if not(0 <= n[0] < height and 0 <= n[1] < width):
                    break
                resonants.add(tuple(n))
                k += 1
            
            print(m, n)

    return resonants

width = len(lines[0])
height = len(lines)
for (row, line) in enumerate(lines):
    for (col, c) in enumerate(line):
        if c != '.':
            antennas[c].append((row,col))


print(width)
print(height)
resonants = set()
for key in antennas.keys():
    print(key)
    for v in count(antennas, key, width, height):
        if 0 <= v[0] < height and 0 <= v[1] < width:
            resonants.add(v)

print(len(resonants))


# print(max(len(arr) for arr in antennas.values()))
