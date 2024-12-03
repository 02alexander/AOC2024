#!/usr/bin/env python3

import sys
import os
import numpy as np
from collections import defaultdict

sys.path.append("../")
from util import occ_map, get_ints

content = open("input").read()
groups = content.split('\n\n')
lines = content.splitlines()

def is_safe(toks):
    sf = True
    dec = None
    for i in range(len(toks)-1):
        d = toks[i+1] - toks[i]

        if abs(d) == 0:
            sf = False
            break            
        
        if dec is None:
            dec = -1
            dec = int(d/abs(d))

        
        if not(d/abs(d) * dec > 0 and (1 <= abs(d) <= 3)):
            sf = False
            break
    return sf

sm = 0
for line in lines:
    toks = list(map(int, line.split()))
    sf = False
    for i in range(len(toks)):
        new_l = toks[0:i] + toks[i+1:]
        if is_safe(new_l):
            sf = True
            break
    if sf or is_safe(toks):
        sm += 1

print(sm)