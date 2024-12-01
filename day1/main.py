#!/usr/bin/env python3

import sys
import os
from collections import defaultdict

content = open("input").read()
groups = content.split('\n\n')
lines = content.splitlines()

l = []
r = []

for line in lines:
    a, b = map(int, line.split())
    l.append(a)
    r.append(b)

sm = 0
l = sorted(l)
r = sorted(r)
for i in range(len(l)):
    sm += abs(l[i] - r[i])
print(f'part 1: {sm}')

sm = 0
for i in range(len(l)):
    a = l[i]
    sm += a*r.count(a)

print(f'part 2: {sm}')
