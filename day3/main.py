#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict
import re

sys.path.append("../")
from util import occ_map, get_ints

content = open("input").read()
lines = content.splitlines()

part2 = 0
part1 = 0
enabled = True
for line in lines:
    # print(line)
    for m in re.finditer(r'(mul)\((-?\d+),(-?\d+)\)|(do)\(\)|(don\'t)\(\)', line):
        g = m.groups()
        if g[3]:
            enabled = True
        elif g[4]:
            enabled = False
        elif g[0]:
            x, y = map(int, g[1:3])
            part1 += y*x
            part2 += x*y if enabled else 0

print(part1)
print(part2)
