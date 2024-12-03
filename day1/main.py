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

arr = np.array(get_ints(lines))

l = list(arr[:,0])
r = list(arr[:,1])

print(sum(abs(a - b) for a,b in zip(sorted(l), sorted(r))))

print(sum(a*list(r).count(a) for a,b in zip(sorted(l), sorted(r))))
