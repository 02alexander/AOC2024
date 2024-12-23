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

def cached_cnt(patterns, i, wanted, possible_cache=dict):
    if i >= len(wanted):
        return True
    if i in possible_cache:
        return possible_cache[i]
    
    cnt = 0
    for pat in patterns:
        if wanted[i:].startswith(pat):
            res = cached_cnt(patterns, i + len(pat), wanted, possible_cache)
            possible_cache[i + len(pat)] = res
            cnt += res
    return cnt

patterns = [p.strip() for p in groups[0].split(',')]

cnt = 0
cnt2 = 0
for line in groups[1].splitlines():
    res = cached_cnt(patterns, 0, line, dict())
    if res != 0:
        cnt += 1
    cnt2 += res

print(cnt)
print(cnt2)


