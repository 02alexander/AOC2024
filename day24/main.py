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


def dependencies(v, codes):
    visited = set()
    nxt = [v]
    while nxt:
        cur_var = nxt.pop()
        if cur_var in visited:
            continue
        visited.add(cur_var)
        a, op, b, _, = out_to_in[cur_var]
        if a in out_to_in:
            nxt.append(a)
        if b in out_to_in:
            nxt.append(b)
    return visited

def affected_by(v, codes):
    visited = set()
    nxt = [v]
    while nxt:
        cur_var = nxt.pop()
        if cur_var in visited:
            continue
        visited.add(cur_var)
        for a, _, b, _, out in code:
            if cur_var in [a,b]:
                nxt.append(out)
        
    return visited


print("hello wolrd")

vars = dict()
for line in groups[0].splitlines():
    name, start = line.split(':')
    vars[name] = int(start)
print(vars)

ls = groups[1].splitlines()
code = []
for line in ls:
    a, op, b, _, out = line.split()
    code.append([a, op, b, _, out])

done = False
while not done:
    done = True
    for a, op, b, _, out in code:
        if out not in vars:
            done = False
        if a in vars and b in vars:
            if op == "AND":
                vars[out] = vars[a] & vars[b]
            if op == "OR":
                vars[out] = vars[a] | vars[b]
            if op == "XOR":
                vars[out] = vars[a] ^ vars[b]

zs = list((name, val) for name, val in vars.items() if name[0] == 'z')

inx = ""
for _, d in sorted(list((name, val) for name, val in vars.items() if name[0] == 'x'), reverse=True):
    inx += str(d)


iny = ""
for _, d in sorted(list((name, val) for name, val in vars.items() if name[0] == 'y'), reverse=True):
    iny += str(d)


result = ""
for _, d in sorted(zs, reverse=True):
    result += str(d)

xored = []
for a, op, b, _, out in code:
    x, y = sorted([a,b])
    if op == "XOR" and x[0] == "x" and y[0] == "y":
        xored.append(out)

# print(inx, sum(1 for c in inx if c == "1"))
# print(iny, sum(1 for c in iny if c == "1"))
# print(result, sum(1 for c in iny if c == "1"))
wanted = f'{int(inx,2)+int(iny,2):b}'
# print(wanted, sum(1 for c in wanted if c == "1"))

out_to_in = dict()
for i, (a, op, b, _, out) in enumerate(code):
    out_to_in[out] = (a, op, b, i)

in_to_out = defaultdict(list)
for i, (a, op, b, _, out) in enumerate(code):
    in_to_out[(a,op,b)] = (op, out, i)
    in_to_out[(b,op,a)] = (op, out, i)

def swap(code, a,b):
    new_code = list(code)
    idxa = out_to_in[a][3]
    idxb = out_to_in[b][3]
    new_code[idxa][4], new_code[idxb][4] = new_code[idxb][4], new_code[idxa][4]
    

    new_out_to_in = dict()
    for i, (a, op, b, _, out) in enumerate(new_code):
        new_out_to_in[out] = (a, op, b, i)

    new_in_to_out = defaultdict(list)
    for i, (a, op, b, _, out) in enumerate(new_code):
        new_in_to_out[(a,op,b)] = (op, out, i)
        new_in_to_out[(b,op,a)] = (op, out, i)
    return new_code, new_out_to_in, new_in_to_out


code, out_to_in, in_to_out = swap(code, "z05","jst")
code, out_to_in, in_to_out = swap(code, "mcm","gdf")
code, out_to_in, in_to_out = swap(code, "z15","dnt")
code, out_to_in, in_to_out = swap(code, "gwc","z30")

swapped = [
    "z05","jst",
    "mcm","gdf",
    "z15","dnt",
    "gwc","z30",
]

print(in_to_out)

def to_graphviz(code):
    res = "digraph {\n"
    nodes = set()
    op_at = dict()
    edges = list()
    for a, op, b, _, out in code:
        nodes.add(a)
        nodes.add(b)
        nodes.add(out)
        op_at[out] = op

        edges.append((a, out))
        edges.append((b, out))
    
    for node in nodes:
        if node[0] == "x":
            pass
            # n = int(node[1:])
            # res += f'{node} [pos="{2*n},{n*2+1}!"]\n'
        elif node[0] == "y":
            pass
            # n = int(node[1:])
            # res += f'{node} [pos="{2*n},{n*2}!"]\n'
        elif node[0] == "z":
            pass
            n = int(node[1:])
            # res += f'{node} [pos="80,{n*2}!"]\n'
            op = op_at[node]
            res += f'{node} [label="{node} {op}"]\n'
        else:
            op = op_at[node]
            res += f'{node} [label="{node} {op}"]\n'
        
    for (a, b) in edges:
        res += f"{a}->{b}\n"
    res += "}\n"
    return res

def check(in_to_out):

    carries = []
    souts = []
    for i in range(45):
        print(i)
        if i == 0:
            sout = in_to_out[("x00", "XOR", "y00")][1]
            cout = in_to_out[("x00", "AND", "y00")][1]
            souts.append(sout)
            carries.append(cout)
            print(sout, cout)
        else:
            d = in_to_out[(f"x{i:0>2}", "XOR", f"y{i:0>2}")][1]
            print(d, carries[-1])
            sout = in_to_out[(carries[-1], "XOR", d)][1]
            e = in_to_out[(d, "AND", carries[-1])][1]
            f = in_to_out[(f"x{i:0>2}", "AND", f"y{i:0>2}")][1]
            carry = in_to_out[(e, "OR", f)][1]

            print(d,e,f)
            print(carry, sout)
            carries.append(carry)
            souts.append(sout)
        # print()
    return True

try:
    check(in_to_out)
except Exception as e:
    print("aroseitnoiaensas")
    print("arsoetnarosiet", e)

# print(list(a for a in dependencies("gdf", code)))

graph = to_graphviz(code)
a = open("circuit.gv", "w")
a.write(graph)

print(int(result,2))

print(','.join(sorted(swapped)))
