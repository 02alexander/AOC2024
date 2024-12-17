#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re
import itertools
from typing import Any
from heapq import heapify, heappop, heappush

sys.path.append("../")
from util import occ_map, get_ints, DIRS, slice_dir

content = open("mm").read()
lines = content.splitlines()
groups = content.split('\n\n')

def solve(mp, start, end):
    step = 0
    q = [(0, step, start, 1j)]
    heapify(q)
    print(q)
    visited = set()
    while len(q) != 0:
        d, _, cur, dr = heappop(q)
        if cur not in mp:
            continue
        if cur == end:
            return d
        if (cur, dr) in visited:
            continue
        visited.add((cur, dr))

        heappush(q, (d + 1, step, cur + dr, dr))
        heappush(q, (d + 1000, step+1, cur, dr*1j))
        heappush(q, (d + 1000, step+2, cur, -dr*1j))
        step += 3


def part1():

    mp = set()
    start_pos = None
    end_pos = None
    for (ri, line) in enumerate(lines):
        for (ci, c) in enumerate(line):
            if c == 'S':
                start_pos = ri + 1j*ci
            elif c == 'E':
                end_pos = ri + 1j*ci
            
            if c != '#':
                mp.add(ri + 1j*ci)

    return solve(mp ,start_pos, end_pos)
    
def print_path(mp, pth):

    print(pth)
    pth = set(pth)
    for (ri, line) in enumerate(lines):
        for (ci, c) in enumerate(line):
            if (ri +1j*ci) not in mp:
                print('###', end='')
            elif (ri + 1j*ci) in pth:
                print(' O ', end='')
            else:
                print('   ', end='')
        print()

def solve2(mp, start, end):
    step = 0
    q = [(0, step, start, 1j, [])]
    heapify(q)
    visited = defaultdict(int)
    end_stops = []
    best_d = None
    while len(q) != 0:
        d, _, cur, dr, pth = heappop(q)
        if best_d is not None and d > best_d:
            continue
        if cur == end:
            best_d = d
            end_stops.append(pth)
        if cur not in mp:
            continue
        if (cur, dr) in visited and d > visited[(cur, dr)]:
            continue
        visited[(cur, dr)] = d

        heappush(q, (d + 1, step, cur + dr, dr, list(pth + [cur])))
        heappush(q, (d + 1000, step+1, cur, dr*1j, list(pth)))
        heappush(q, (d + 1000, step+2, cur, -dr*1j, list(pth)))
        step += 3
    tot = set()
    tot.add(end)
    for pth in end_stops:
        tot = tot.union(set(pth))
    return len(tot)
    

def part2():

    mp = set()
    start_pos = None
    end_pos = None
    for (ri, line) in enumerate(lines):
        for (ci, c) in enumerate(line):
            if c == 'S':
                start_pos = ri + 1j*ci
            elif c == 'E':
                end_pos = ri + 1j*ci
            if c != '#':
                mp.add(ri + 1j*ci)

    return solve2(mp ,start_pos, end_pos)
    

# print(part1())
print(part2())
