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


def compact(fs):
    new_fs = []
    i = 0
    while i < len(fs):
        if i < len(fs)-1 and fs[i][0] == fs[i+1][0]:
            new_fs.append([fs[i][0], fs[i][1] + fs[i+1][1]])
            i += 2
        elif fs[i][1] == 0:
            i += 1
        else:
            new_fs.append(fs[i])
            i += 1
    return new_fs

def move(fs: list, mv_id):
    for (i, (id, size)) in reversed(list(enumerate(fs))):
        if id == mv_id:
            for (j, (new_spot, free_space)) in enumerate(fs[:i]):
                if new_spot is None and free_space >= size:
                    e = fs[i]
                    fs[i] = [None, size]

                    fs[j][1] = free_space - size
                    fs.insert(j, e)
                    return True
    return False

def str_fs(fs):
    res = ""
    for (id, size) in fs:
        for _ in range(size):
            if id is None:
                res += '.'
            else:
                res += str(id)
    return res

def brute_force(fs):
    rep = []
    for id, size in fs:
        rep += [id]*size

    start_i = 0
    for j in reversed(range(len(rep))):
        for i in range(start_i, j):
            if rep[i] is None:
                rep[i], rep[j] = rep[j], rep[i]
                start_i = i
                break
    return checksum(rep)
        
def checksum(s):
    sm = 0
    for (i, c) in enumerate(s):
        if c is not None:
            sm += i*c
    return sm

print("hello")

id_to_size = {}
fs = []

for (i, c) in enumerate(lines[0]):
    if i % 2 == 0:
        fs.append([i // 2, int(c)])
        id_to_size[i // 2] = int(c)
    else:
        fs.append([None, int(c)])

res = ""

max_id = max(id or -1 for id, _ in fs)
print(max_id)

for id in reversed(range(0,max_id+1)):
    print(id)
    move(fs, id)
    fs = compact(fs)

rep = []
for id, size in fs:
    rep += [id]*size
print(checksum(rep))

s = brute_force(fs)
print(s)
