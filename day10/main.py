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


def count(mp, visited, start):
    dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
    visited.add(start)

    for d in dirs:
        new_p = tuple([a + b for a,b in zip(start, d)])
        if new_p in visited:
            continue
        if new_p in mp and mp[new_p] == mp[start] + 1: 
            count(mp, visited, new_p)

def distinct(mp, visited, start):

    if mp[start] == 9:
        return 1
    
    sm = 0
    dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
    visited.add(start)
    for d in dirs:
        new_p = tuple([a + b for a,b in zip(start, d)])
        if new_p in visited:
            continue
        if new_p in mp and mp[new_p] == mp[start] + 1: 
            new_visited = set(visited)
            sm += distinct(mp, new_visited, new_p)
    return sm

mp = {}
for (ri, row) in enumerate(lines):
    for (ci, c) in enumerate(row):
        if c != '.':
            if c == '0':
                print(ri, ci)
            mp[(ri, ci)] = int(c)


tot_score = 0
tot_rating = 0

for key, val in mp.items():
    if val == 0:
        a = key
        visited = set()
        count(mp, visited, key)
        cnt = 0
        for key in visited:
            if mp[key] == 9:
                cnt += 1
        v = set()
        sm = distinct(mp, v, a)
        tot_rating += sm
        tot_score += cnt
        


print(tot_score)
print(tot_rating)
