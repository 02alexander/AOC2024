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

page_ordering = get_ints(groups[0].splitlines())

ordering = defaultdict(set)
for (a,b) in page_ordering:
    ordering[a].add(b)

def after(ordering, c, numbs):
    numbs = set(numbs)
    return len(set(ordering[c]).intersection(numbs))

def is_ordered(ordering, numbs):
    for i in reversed(range(len(numbs))):
        e = numbs[i]
        if len(set(numbs[:i]).intersection(ordering[e])) > 0:
            return False
    return True

def order(ordering, numbs):
    while True:
        done = True

        for (i, c) in enumerate(numbs):
            must_after = ordering[c]
            break_outer = False
            for k in range(0,i):
                if numbs[k] in must_after:
                    numbs[i], numbs[k] = numbs[k], numbs[i]
                    done = False
                    break_outer = True
                    break

            if break_outer:
                break
        
        if done:
            break


sm = 0
for line in groups[1].splitlines():
    numbs = list(map(int,line.split(',')))
    if not is_ordered(ordering, numbs):

        order(ordering, numbs)
        print(is_ordered(ordering, numbs))
        print(numbs)
        print(numbs[len(numbs)//2])
        sm += numbs[len(numbs)//2]
        #5213

print(sm)
