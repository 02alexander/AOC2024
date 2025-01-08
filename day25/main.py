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

locks = []
keys = []

for group in groups:
    lines = group.splitlines()
    if lines[0] == "."*5:
        lock = []
        for col in range(5):
            cnt = 0
            for r in range(7):
                if lines[r][col] == "#":
                    cnt += 1
            lock.append(cnt)
        locks.append(lock)
    else:
        print(lines)
        key = []
        for col in range(5):
            cnt = 0
            for r in range(7):
                if lines[r][col] == "#":
                    cnt += 1
            key.append(cnt)
        keys.append(key)


matches = 0
for key in keys:
    for lock in locks:
        # print(key, lock)
        # print(list(a + b  for a,b in zip(key,lock)))
        if all(a + b <= 7 for a,b in zip(key,lock)):
            # print(key, lock)
            matches += 1

print(matches)
