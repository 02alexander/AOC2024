#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re
import itertools
from typing import Any
from collections import deque

sys.path.append("../")
from util import occ_map, get_ints, DIRS, slice_dir

content = open("input").read()
lines = content.splitlines()
groups = content.split('\n\n')


W = 71
H = 71

occ = dict()

ints = get_ints(lines)

def find(start, end, occ):
    nxt = deque([(0, start)])
    visited = set()
    while nxt:
        d, cur = nxt.popleft()
        if cur not in occ or occ[cur]:
            continue
        if cur in visited:
            continue
        if cur == end:
            return d
        visited.add(cur)
        for dr in [-1j, 1, -1 ,1j]:
            
            nxt.append((d+1, cur + dr))


for n in range(len(ints)):


    for x, y in ints[:n]:
        occ[x + 1j*y] = True


    for x in range(W):
        for y in range(H):
            if x + 1j*y not in occ:
                occ[x + 1j*y] = False

    d = find((W-1)+(H-1)*1j, 0, occ)
    if d is None:
        print(ints[n-1])
        break