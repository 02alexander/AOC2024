
import sys
import os
import numpy as np
from collections import defaultdict
import itertools
from typing import Any
import re

DIRS = list(itertools.product([1, 0, -1], [1, 0, -1]))
DIRS.remove((0,0))

def slice_dir(lines: list[list[Any]], startcol: int, startrow: int, slice_len: int, direction: tuple[int, int]) -> list[Any]:
    result: list[list[Any]] = []
    for k in range(slice_len):
        col = startcol + direction[0]*k
        row = startrow + direction[1]*k
        if not(0 <= col < len(lines[0]) and 0 <= row < len(lines)):
            break
        result.append(lines[row][col])
    return result


def occ_map(lst: list) -> defaultdict[Any, int]:
    res: defaultdict[Any, int] = defaultdict(int)
    for e in lst:
        res[e] += 1
    return res

def get_ints(lines: list[str]) -> list[list[int]]:
    res = []
    for line in lines:
        res.append(list(int(m.group()) for m in re.finditer('-?\d+', line)))
    return res
    