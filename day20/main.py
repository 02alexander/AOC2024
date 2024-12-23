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


from collections import deque

def dist_from_start(occ, start, result):
    q = deque([(0, start)])

    while q:
        d, pos = q.popleft()
        if pos in occ:
            continue
        if pos in result:
            continue
        result[pos] = d

        for dr in [1, -1, 1j, -1j]:
            q.append((d + 1, pos + dr))
        
start = None
end = None
mp = dict()
for (ri, line) in enumerate(lines):
    for (ci, c) in enumerate(line):
        if c == '#':
            mp[ri + 1j*ci] = c
        elif c == 'S':
            start = ri + 1j*ci
        elif c == 'E':
            end = ri + 1j*ci

result = dict()
dist_from_start(mp, start, result)

tot_dist = result[end]

cheats = []
k = 0

all_ds = []
N = 20
for dx in range(-N, N+1):
    M = N - abs(dx)
    for dy in range(-M, M+1):
        dpos = dx + 1j*dy
        all_ds.append(dpos)

cnt = 0
for pos in result.keys():
    for dpos in all_ds:
        dist = round(abs(dpos.imag)) + round(abs(dpos.real))
        if dpos == end:
            cheats.append((result[pos + dpos] - result[pos] - dist))
            k += 1
            break
        if dpos + pos in result:

            cheats.append((result[pos + dpos] - result[pos] - dist))
            k += 1

cheats.sort()
cnt = 0
for cheat in cheats:
    if cheat >= 100:
        cnt += 1

print(result[end])
