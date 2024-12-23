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

def step(secret):
    secret = (secret ^ (secret << 6)) & ((1 << 24) - 1)
    secret = (secret ^ (secret >> 5)) & ((1 << 24) - 1)
    secret = (secret ^ (secret << 11)) & ((1 << 24) - 1)
    return secret

def step_n(secret, n):
    secrets = [secret]
    for _ in range(n):
        secret = step(secret)
        secrets.append(secret)
    return secrets
    

stuff = defaultdict(int)

part1 = 0
for line in lines[:]:
    secrets = step_n(int(line), 2000)
    changes = []
    visited = set()
    for i in range(len(secrets)-1):
        changes.append((secrets[i+1] % 10) - (secrets[i] % 10))

    for i in range(len(changes)-4):
        tpl = tuple(changes[i:i+4])
        if tpl in visited:
            continue
        visited.add(tpl)
        stuff[tpl] += secrets[i+4] % 10

    part1 += secrets[-1]

print(max( (value, key) for key,value in stuff.items() ))


print(part1)

#1914
#1898