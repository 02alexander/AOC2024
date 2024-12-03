
import sys
import os
import numpy as np
from collections import defaultdict
from typing import Any
import re


def occ_map(lst: list) -> defaultdict[Any, int]:
    res = defaultdict(int)
    for e in lst:
        res[e] += 1
    return res

def get_ints(lines: list[str]) -> list[list[int]]:
    res = []
    for line in lines:
        res.append(list(int(m.group()) for m in re.finditer('-?\d+', line)))
    return res
    