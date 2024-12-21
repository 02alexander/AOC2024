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



@cache
def find_key(keypad_id, target_key):
    keypad = keypads[keypad_id]
    target_pos = None
    for pos, value in keypad.items():
        if value == target_key:
            target_pos = pos
    return target_pos
    

@cache
def all_paths(cur_key, target_key, keypad_id):
    keypad = keypads[keypad_id]
    cur_pos = find_key(keypad_id, cur_key)
    target_pos = find_key(keypad_id, target_key)
    if cur_pos == target_pos:
        return 'A'

    finished_paths = []
    paths = [[cur_pos]]
    while len(paths) > 0:
        cur_path = paths.pop()
        for d in [1, -1, 1j, -1j]:
            cur_pos = cur_path[-1]
            newp = cur_path[-1] + d
            if newp in keypad:
                if abs(newp.imag - target_pos.imag) + abs(newp.real-target_pos.real) < abs(cur_pos.imag - target_pos.imag) + abs(cur_pos.real-target_pos.real):
                    newpath = list(cur_path)
                    newpath.append(newp)
                    if newp == target_pos:
                        finished_paths.append(newpath)
                    else:
                        paths.append(newpath)
    return [
        ''.join(str(dr_to_key[dr]) for dr in get_dirs(path)) + 'A' for path in finished_paths
    ]

def get_dirs(path):
    d = []
    for i in range(len(path)-1):
        d.append(path[i+1] - path[i])
    return d

def paths_through(keypad, sequence, last_c='A'):
    paths = []
    for path in all_paths('A', sequence[0], keypad):
        if len(sequence) > 1:
            for other_path in paths_through(keypad, sequence[1:]):
                paths.append( path + other_path)
        else:
            paths.append(path)
    return paths

@cache
def shortest(keypad_start_idx, start, end):
    dists = []
    # print(keypad_start_idx, len(keypads_indices))
    for path in all_paths(start, end, keypads_indices[keypad_start_idx]):
        if keypad_start_idx+1 >= len(keypads_indices):
            dists.append(len(path))
        else:
            tot_dist = 0
            for i in range(len(path)):
                prev = 'A'
                if i > 0:
                    prev = path[i-1]
                tot_dist += shortest(keypad_start_idx+1, prev, path[i])
            dists.append(tot_dist)
    return min(dists)

import time

lines = content.splitlines()
groups = content.split('\n\n')


start_time = time.time()

keypad1_arr = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

keypad1 = dict()

for (ri, row) in enumerate(keypad1_arr):
    for (ci, c) in enumerate(row):
        if c is not None:
            keypad1[ri + 1j*ci] = c

keypad2_arr = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]
keypad2 = dict()

for (ri, row) in enumerate(keypad2_arr):
    for (ci, c) in enumerate(row):
        if c is not None:
            keypad2[ri + 1j*ci] = c


key_to_dr = {
    '<': -1j,
    '>': 1j,
    '^': -1,
    'v': 1,
}

dr_to_key = {
    -1j: '<',
    1j: '>',
    -1: '^',
    1: 'v',
}


keypads = [
    keypad1,
    keypad2,
]
part1 = 0

N = 25
keypads_indices = [0] + N*[1]

for line in lines:
    cnt = 0     
    d = int(re.findall('-?\d+', line)[0])

    for i in range(len(line)):
        prev = 'A'
        if i > 0:
            prev = line[i-1]
        l = shortest(0, prev, line[i])
        cnt += l
    print(d, cnt)
    part1 += d*cnt

print(part1)

end_time = time.time()
print(f'{(end_time-start_time)*1000} ms')


