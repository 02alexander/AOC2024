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

mp_lines = groups[0].splitlines()

def attempt_push(mp, pos, dr):
    ps = []
    for i in range(10000):
        newp = pos + dr*i
        ps.append(mp[newp])
        if newp in mp and (mp[newp] == '.' or mp[newp] == '#'):
            break
    
    if ps[-1] == '.':
        for i in reversed(range(1, len(ps))):
            mp[pos + dr*i] = mp[pos+ dr*(i-1)]
        mp[pos] = '.'
        return True
    return False

def attempt_push_lst(mp, pos, dr, end_at):
    ps = []
    for i in range(10000):
        newp = pos + dr*i
        ps.append(mp[newp])
        if newp in mp and (mp[newp] in end_at):
        # if newp in mp and (mp[newp] == '.' or mp[newp] == '#'):
            break
    return ps
    
def get_n_pushable(mp, pos, dr):
    if mp[pos + dr] == '.':
        return 1
    elif mp[pos + dr] == '#':
        return 0
    elif mp[pos + dr] == '[':
        return min(get_n_pushable(mp, pos + dr, dr), get_n_pushable(mp, pos + 1j + dr, dr))
    elif mp[pos + dr] == ']':
        return min(get_n_pushable(mp, pos + dr, dr), get_n_pushable(mp, pos - 1j + dr, dr))

def push_n(mp, pos, dr):
    if dr.imag == 0 and mp[pos] == '[':
        success = push_n(mp, pos + dr, dr) and push_n(mp, pos + dr + 1j, dr)
        mp[pos + dr] = mp[pos]
        mp[pos] = '.'
        mp[pos + dr + 1j] = mp[pos + 1j]
        mp[pos + 1j] = '.'
        return success
    elif dr.imag == 0 and mp[pos] == ']':
        success = push_n(mp, pos + dr, dr) and push_n(mp, pos + dr - 1j, dr)
        mp[pos + dr] = mp[pos]
        mp[pos] = '.'
        mp[pos + dr - 1j] = mp[pos - 1j]
        mp[pos - 1j] = '.'
        return success
    elif mp[pos] == '.':
        return True
    elif mp[pos] == '#':
        return False
    else: # [] ver, @
        success = push_n(mp, pos + dr, dr)
        # print(pos)
        mp[pos + dr]  = mp[pos]
        mp[pos] = '.'
        return success
        


def attempt_push2(mp, pos, dr):
    new_mp = dict(mp)
    if push_n(new_mp, pos, dr):
        return (new_mp, True)
    return (mp, False)
            

def disp_map(mp):
    for ri in range(len(mp_lines)):
        for ci in range(len(mp_lines[0]*2)):
            if (ri+1j*ci) in mp:
                print(mp[ri + ci*1j], end="")
        print("")

def part2():
    start_pos = None
    mp = dict()
    for (ri, row) in enumerate(mp_lines):
        for (ci, c) in enumerate(row):
            if c == '@':
                start_pos = ri + 2j*ci
                mp[ri + 1j*2*ci] = c
                mp[ri + 1j*(2*ci+1)] = '.'
            if c == '#':
                mp[ri + 1j*2*ci] = '#'
                mp[ri + 1j*(2*ci+1)] = '#'
            if c == 'O':
                mp[ri + 1j*2*ci] = '['
                mp[ri + 1j*(2*ci+1)] = ']'
            if c == '.':
                mp[ri + 1j*2*ci] = '.'
                mp[ri + 1j*(2*ci+1)] = '.'
    movements = groups[1].replace('\n', '')
    c_to_dir = {
        '<': -1j,
        '^': -1,
        'v': 1,
        '>': 1j,
    }
    for (i, mv) in enumerate(movements):
        dr = c_to_dir[mv]
        (mp, succ) = attempt_push2(mp, start_pos, dr)
        if succ:
            start_pos += dr

    sm = 0
    for (ri, row) in enumerate(mp_lines):
        for ci in range(len(row)*2):
            if mp[ri + 1j*ci] == '[':
                sm += ri *100 + ci
    return sm
    

def part1():
    start_pos = None
    mp = dict()
    for (ri, row) in enumerate(mp_lines):
        for (ci, c) in enumerate(row):
            if c == '@':
                start_pos = ri + 1j*ci
            mp[ri + 1j*ci] = c

    movements = groups[1].replace('\n', '')

    c_to_dir = {
        '<': -1j,
        '^': -1,
        'v': 1,
        '>': 1j,
    }

    for mv in movements:
        dr = c_to_dir[mv]
        if attempt_push(mp, start_pos, dr):
            start_pos += dr

    sm = 0
    for (ri, row) in enumerate(mp_lines):
        for (ci, c) in enumerate(row):
            if mp[ri + 1j*ci] == 'O':
                sm += ri *100 + ci
    return sm

print(part1())
print(part2())