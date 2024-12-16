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

ints = get_ints(lines)

print(max(len(row) for row in ints))

count = 0
for row in ints:
    tot = row[0]
    rest = row[1:]
    for ops in itertools.product(('+', '||', '*'), repeat=len(rest)-1):
        res = int(rest[0])
        for (op, val) in zip(ops, rest[1:]):
            if op == "+":
                res = res + val
            elif op == "*":
                res = res * val
            elif op == '||':
                res = int(str(res) + str(val))
        
        c = res
        if c == tot:
            print(tot, ops)
            count += tot
            break
print(count)