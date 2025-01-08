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


mp = defaultdict(list)
glob_mp = defaultdict(list)
for line in lines:
    src, dst = line.split('-')
    mp[src].append(dst)
    mp[dst].append(src)

    glob_mp[src].append(dst)
    glob_mp[dst].append(src)

mp = dict(mp)

@cache
def is_connected(subgraph):
    # print(subgraph)
    l = list(subgraph)
    for i in range(1, len(l)):
        for k in range(i):
            if l[i] not in mp[l[k]]:
                return False
    return True


cnt = 0
sts = set()
for key, nbs in mp.items():
    for i in range(len(nbs)):
        for k in range(i):
            if nbs[i] in mp[nbs[k]]:
                sts.add(tuple(sorted((key, nbs[i], nbs[k]))))

cnt = 0
for s in sorted(sts):
    for n in s:
        if n[0] == 't':
            cnt += 1
            break

mx = 0
part2 = 0
for key, nbs in mp.items():
    # print(key, nbs)
    for i in range(mx, len(nbs)+1):
        for subgraph in set(itertools.combinations(nbs, i)):
            l = list(subgraph)
            if is_connected(tuple(l + [key])):
                if i > mx:
                    s = tuple(l + [key])
                    print(s)
                    print(','.join(sorted(s)))
                    mx = i
    # print()
print(f'part2: {mx+1}')

# print(max(len(v) for v in mp.values()))
# print(len(lines))
# print(len(sts))
print(cnt)

#13
