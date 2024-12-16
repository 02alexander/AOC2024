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

print("hello world")

# W = 11
# H = 7

W = 101
H = 103

def pos(p, v, n, w, h):
    newp = p + v*n
    newx = round(newp.real) % w
    newy = round(newp.imag) % h
    return newx + 1j*newy

def disp(end_pos, w, h):
    for y in range(0, h):
        for x in range(0, w):
            if end_pos[x + 1j*y] != 0:
                print('#', end="")
            else:
                print(" ", end="")
        print()

def part2(ints):
    ps = []
    for (px, py, vx, vy) in ints:
        ps.append((px + py*1j, vx + vy*1j))

    i = 42
    ps = [(pos(p, v, i, W, H), v) for p,v in ps]

    while True:
        end_pos = defaultdict(int)
        for (p, _) in ps:
            end_pos[p] += 1
        print("\n"*10)
        disp(end_pos, W, H)
        print(i)
        print(i // 103)
        i += 103
        ps = [(pos(p, v, 103, W, H), v) for p,v in ps]
        input()



ints = get_ints(lines)

end_pos = defaultdict(int)
for (px, py, vx, vy) in ints:
    ep = pos(px + py*1j, vx + vy*1j, 100, W, H)
    end_pos[ep] += 1


safetys = []
for (xstart, xend) in [[0, W//2], [W//2+1, W]]:
    for (ystart, yend) in [[0, H//2], [H//2+1, H]]:
        cnt = 0
        for x in range(xstart, xend):
            for y in range(ystart, yend):
                cnt += end_pos[x + 1j*y]
        safetys.append(cnt)
print(safetys)
p = 1
for e in safetys:
    p *= e
print(p)

part2(ints)
#98?
#99?
#42? No

#99 No

#145?

#200?
#351?

