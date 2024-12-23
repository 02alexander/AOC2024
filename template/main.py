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



