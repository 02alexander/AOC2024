#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re
import itertools
import z3
from typing import Any
import numpy as np

sys.path.append("../")
from util import occ_map, get_ints, DIRS, slice_dir

content = open("input").read()
lines = content.splitlines()
groups = content.split('\n\n')

NUM = 10000000000000
# NUM = 0

def brute(button1, button2, prize):
    solutions = []
    for i in range(100):
        for m in range(100):
            if button1[0]*i + button2[0]*m == prize[0] and button1[1]*i + button2[1]*m == prize[1]:
                solutions.append((i+m, i, m))
    return solutions

def solve(A, B, prize):
    ax = A[0]
    ay = A[1]

    bx = B[0]
    by = B[1]

    px = prize[0]
    py = prize[1]

    c = by - ay*bx/ax
    m = (py - ay*px/ax) / c
    k = (px - m*bx)/ax

    return k, m



part1 = 0
part2 = 0
for group in groups:
    lines = list(group.splitlines())
    # res.append(list(int(m.group()) for m in re.finditer('-?\d+', line)))
    button1 = list(map(int, re.findall('-?\d+', lines[0])))
    button2 = list(map(int, re.findall('-?\d+', lines[1])))
    dst = list(map(int, re.findall('-?\d+', lines[2])))
    dst = (dst[0] + NUM, dst[1] + NUM)

    solution = solve(button1, button2, dst)
    # b = brute(button1, button2, dst)
    if solution:
        k, m = solution
        k = round(k)
        m = round(m)
        # print(solution)
        if button1[0]*k + button2[0]*m == dst[0] and button1[1]*k + button2[1]*m == dst[1]:
            if m <= 100 and k <= 100:
                part1 += k*3 + m
            
            if m < 0 or k < 0:
                print("WARNING", solution)
            else:
                part2 += k*3 + m


print(part1)
print(part2)

