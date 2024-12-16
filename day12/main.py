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

adj = [(1, 0), [0, 1], [-1, 0], [0, -1]]

def fill(mp, cur, visited=set()):
    c = mp[tuple(cur)]
    if cur in visited:
        return
    for d in adj:
        visited.add(cur)
        
        new_p = tuple([a + b for a,b in zip(cur, d)])
        if new_p in mp and mp[new_p] == c:
            fill(mp, new_p, visited)

def split_list(l, f):
    parts = []
    cur_part = []
    for c in l:
        if f(c):
            if len(cur_part) != 0:
                parts.append(cur_part)
            cur_part = []
        else:
            cur_part.append(c)
    return parts

def find_groups(l, f=None):
    if f is None:
        f = lambda a,b: a == b
    l = list(l)
    parts = []
    cur_part = [l[0]]
    for i in range(1, len(l)):
        c = l[i]
        if not f(c, l[i-1]):
            parts.append(cur_part)
            cur_part = [c]
        else:
            cur_part.append(c)
        
    parts.append(cur_part)
    return parts

def col_is_side(mp, part):
    c = mp[part[0]]
    sds = 0
    for dc in [-1, 1]:
        adj_col = [(p[0], p[1] + dc) for p in part]
        if adj_col[0] not in mp:
            sds += 1
            continue
        s = find_groups(adj_col, lambda a,b: (mp[a] == c) == (mp[b] == c) )
        for p in s:
            if mp[p[0]] != c:
                if c == 3:
                    print('ADJ GROUP')
                sds += 1
        if c == 3:
            print('')
    return sds


def row_is_side(mp, part):
    c = mp[part[0]]
    sds = 0
    for dr in [-1, 1]:
        adj_row = [(p[0] + dr, p[1]) for p in part]
        if adj_row[0] not in mp:
            sds += 1
            continue
        s = find_groups(adj_row, lambda a,b: (mp[a] == c) == (mp[b] == c) )
        for p in s:
            if mp[p[0]] != c:
                sds += 1
    return sds

def sides(mp, w, h):
    side_count = defaultdict(int)


    for ci in range(w):
        col = [ (ri, ci) for ri in range(0, h)]

        parts = find_groups(col, lambda a,b: mp[a] == mp[b])
        for part in parts:
            res = col_is_side(mp, part)
            c = mp[part[0]]
            side_count[c] += res

    for ri in range(h):
        row = [ (ri, ci) for ci in range(0, w)]

        parts = find_groups(row, lambda a,b: mp[a] == mp[b])
        for part in parts:
            res = row_is_side(mp, part)
            c = mp[part[0]]
            side_count[c] += res
    
    return side_count        


def adjacents(mp, point):
    # s = set()
    cnt = 0
    for d in adj:
        new_p = tuple([a + b for a,b in zip(point, d)])
        if new_p not in mp or mp[new_p] != mp[point]:
            cnt += 1
    return cnt

mp = dict()
for (ri, row) in enumerate(lines):
    for (ci, c) in enumerate(row):
        mp[(ri, ci)] = c

visited = set()

w = len(lines[0])
h = len(lines[1])

sm = 0

area_map = defaultdict(int)
cur_plant_id = 0
id_map = dict()
id_to_c = dict()

for (key, value) in mp.items():
    if key not in visited:
        s = set()
        fill(mp, key, s)
        visited = visited.union(s)

        perim = sum(adjacents(mp, k) for k in s)
        area = len(s)
        boudnary = perim
        c = mp[key]
        area_map[cur_plant_id]  = area
        id_to_c[cur_plant_id] = c
        for p in s:
            id_map[p] = cur_plant_id
        cur_plant_id += 1

nbsides = sides(id_map, w, h)
for key in area_map:
    sides=nbsides[key]
    area=area_map[key]
    sm += sides * area
    print(key, id_to_c[key], sides*area)
    print(f'{area=} {sides=}')

print(sm)
# print(find_groups([1, 1, 2, 1, 2, 2, 3, 3], lambda a, b: a == b))

