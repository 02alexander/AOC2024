#!/usr/bin/env python3

import sys
from collections import deque
sys.path.append("../")
from util import get_ints

content = open("input").read()
groups = content.split('\n\n')

start_regs = get_ints(groups[0].splitlines())
regs = {
    'A': start_regs[0][0],
    'B': start_regs[1][0],
    'C': start_regs[2][0],
}

prog = get_ints(groups[1].splitlines())[0]

def run_prog(regs, prog):
    i = 0
    output = []
    while i < len(prog):
        op = prog[i]
        i += 1

        literal_op = prog[i]
        i += 1
        if literal_op > 3:
            combo = regs[chr(ord('A')  + literal_op - 4)]
        else:
            combo = literal_op

        if op == 0:
            regs['A'] = regs['A'] >> combo
        elif op == 1:
            regs['B'] = regs['B'] ^ literal_op
        elif op == 2:
            regs['B'] = combo % 8
        elif op == 3:
            if regs['A'] != 0:
                i = literal_op
        elif op == 4:
            regs['B'] = regs['C'] ^ regs['B']
        elif op == 5:
            output.append(combo % 8)
        elif op == 6:
            regs['B'] = regs['A'] >> combo
        elif op == 7:
            regs['C'] = regs['A'] >> combo
    return output

def run_with_a(regs, prog, a):
    nr = dict(regs)
    nr['A'] = a
    return run_prog(nr, prog)

def brute(regs, prog, wanted_out):
    nxt = deque([])
    for a in range(2**9):
        nxt.append((9, a))
    while nxt:
        shift, cur_a = nxt.popleft()
        out = run_with_a(regs, prog, cur_a)
        if out == wanted_out:
            return cur_a
        lookdist = len(out) - 2
        if shift > 4*len(wanted_out):
            continue
        if len(out) > len(wanted_out):
            continue
        if out[:lookdist] != wanted_out[:lookdist]:
            continue
        for a in range(2**3):
            nxt.append((shift + 3, cur_a + (a << shift)))

print(brute(regs, prog, prog))
print(run_prog(regs, prog))

lines = content.splitlines()
#271659095409441
#37222273957364