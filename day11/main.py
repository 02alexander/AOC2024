#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re
import itertools
from typing import Any
from functools import cache

sys.path.append("../")
from util import occ_map, get_ints, DIRS, slice_dir

content = open("input").read()
lines = content.splitlines()
groups = content.split('\n\n')

@cache
def end_evolve(n, iterations):
    if iterations == 0:
        return 1
    if n == 0:
        return end_evolve(1, iterations-1) 
    elif len(str(n)) % 2 == 0:
        s = str(n)
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        return end_evolve(int(s1), iterations-1) + end_evolve(int(s2), iterations-1)
    else:
        return end_evolve(n*2024, iterations-1)

stones = list(map(int, lines[0].split()))
print(stones)

def evolve(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2:]
            # print(f'split {s1} {s2}')
            new_stones.append(int(s1))
            new_stones.append(int(s2))
        else:
            new_stones.append(stone*2024)

    return new_stones

cnt = 0
for stone in stones:
    a = end_evolve(stone, 75)
    cnt += a

cnt = 0
for stone in stones:
    a = end_evolve(stone, 22)
    cnt += a

print(cnt)
